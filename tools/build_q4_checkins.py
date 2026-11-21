#!/usr/bin/env python3
"""Build ONE Canvas package with the G4 ELA Quarter 4 check-ins (weeks 25-32) from the repo's week-N-checkin.html.

    python3 tools/build_q4_checkins.py OUTDIR

Writes OUTDIR/g4-ela-q4-checkins.imscc (Canvas export shape: Common Cartridge 1.1 + Canvas quiz meta)
and OUTDIR/g4-ela-q4-checkins-qti.zip (the plain QTI zip shape Canvas's "QTI .zip file" importer takes;
same quizzes, same idents). Each quiz: 14 points, one attempt, unpublished, answers not shown.
Multiple-choice keys are listed in KEYS below (checked by hand Nov 19 2026)."""
import hashlib, html, io, os, sys, zipfile
from xml.sax.saxutils import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_checkin import parse

WEEKS = range(25, 33)
# week -> {question number: index of the right option (0 = A)}
KEYS = {25: {1: 1, 5: 1}, 26: {1: 1, 5: 1}, 27: {1: 1, 5: 1}, 28: {1: 1, 5: 1},
        29: {1: 1, 5: 1}, 30: {1: 0, 5: 1}, 31: {1: 1, 5: 1}, 32: {1: 1, 5: 1}}
# The page versions put almost every right answer at B. In Canvas the right answer is moved to
# these positions (other options keep their order) so the key isn't a pattern. 0 = A.
PLACE = {25: {1: 0, 5: 2}, 26: {1: 2, 5: 0}, 27: {1: 1, 5: 2}, 28: {1: 0, 5: 1},
         29: {1: 2, 5: 0}, 30: {1: 1, 5: 2}, 31: {1: 0, 5: 1}, 32: {1: 2, 5: 0}}
TWO_POINT = 11   # Q11 is worth 2 points every week (14 total)

def num(x): return "%.1f" % x
def meta(l, v): return "<qtimetadatafield><fieldlabel>%s</fieldlabel><fieldentry>%s</fieldentry></qtimetadatafield>" % (l, v)
def ident(*a): return hashlib.md5("|".join(map(str, a)).encode()).hexdigest()

def book_of(title):
    return title.split("Check-In:", 1)[1].strip() if "Check-In:" in title else title

def body_html(q):
    b = "<p><strong>%s</strong> · %s (%d point%s)</p>" % (html.escape(q["section"], quote=False), q["label"], q["points"], "" if q["points"] == 1 else "s")
    for ex in q["pre"]:
        b += "<blockquote><p>%s</p>%s</blockquote>" % (ex["text"], ("<p><em>%s</em></p>" % ex["cite"]) if ex["cite"] else "")
    for p in q["parts"]:
        if p[0] == "model":
            b += '<div style="border-left:4px solid #4A2C6E;padding:6px 12px;margin:8px 0;"><p><strong>%s</strong></p><p><em>%s</em></p></div>' % (p[1], p[2])
        elif p[0] == "excerpt":
            b += "<blockquote><p>%s</p>%s</blockquote>" % (p[1], ("<p><em>%s</em></p>" % p[2]) if p[2] else "")
        elif p[0] == "q-text":
            b += "<p>%s</p>" % p[1]
        elif p[0] == "hint":
            b += '<p><em>Hint: %s</em></p>' % p[1]
        else:
            b += "<p>%s</p>" % p[1]
    return b

def quiz(week):
    d = parse("week-%d-checkin.html" % week)
    book = book_of(d["title"])
    book = {26: "Prince Caspian, Ch. 1–3", 27: "Prince Caspian, Ch. 4–6", 28: "Prince Caspian, Ch. 7–9", 29: "Prince Caspian, Ch. 10–12",
            30: "Prince Caspian Wrap-Up, Ch. 13–15"}.get(week, book)
    title = "Week %d Check-In: %s" % (week, book)
    h = ident("g4ela-checkin", week)
    gid, rid, aid = "g" + h, "r" + h, "a" + h
    qs = d["questions"]
    for q in qs:
        q["points"] = 2 if q["n"] == TWO_POINT else 1
    total = sum(q["points"] for q in qs)
    assert total == 14, (week, total)
    items_canvas, items_cc = [], []
    for q in qs:
        n, t = q["n"], q["type"]
        iid = "i" + ident("g4ela-checkin", week, n)
        body = escape(body_html(q))
        if t == "multiple_choice_question":
            key = KEYS[week][n]
            opts = list(q["options"]); right = opts.pop(key); key = PLACE[week][n]; opts.insert(key, right)
            q["options"] = opts; q["key_letter"] = "ABC"[key]
            ids = [str(1000 + i) for i in range(len(q["options"]))]
            labels = "".join('<response_label ident="%s"><material><mattext texttype="text/html">%s</mattext></material></response_label>'
                             % (i, escape(o)) for i, o in zip(ids, q["options"]))
            pres = '<response_lid ident="response1" rcardinality="Single"><render_choice>%s</render_choice></response_lid>' % labels
            proc = ('<respcondition continue="No"><conditionvar><varequal respident="response1">%s</varequal></conditionvar>'
                    '<setvar action="Set" varname="SCORE">100</setvar></respcondition>' % ids[key])
            md_c = meta("question_type", t) + meta("points_possible", num(q["points"])) + meta("original_answer_ids", ",".join(ids))
            md_cc = meta("cc_profile", "cc.multiple_choice.v0p1") + meta("cc_weighting", q["points"])
        else:
            pres = '<response_str ident="response1" rcardinality="Single"><render_fib><response_label ident="answer1" rshuffle="No"/></render_fib></response_str>'
            proc = '<respcondition continue="No"><conditionvar><other/></conditionvar></respcondition>'
            md_c = meta("question_type", t) + meta("points_possible", num(q["points"]))
            md_cc = meta("cc_profile", "cc.essay.v0p1") + meta("cc_weighting", q["points"])
        tmpl = ('<item ident="%s" title="Question %d"><itemmetadata><qtimetadata>%s</qtimetadata></itemmetadata>'
                '<presentation><material><mattext texttype="text/html">%s</mattext></material>%s</presentation>'
                '<resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>%s</resprocessing></item>')
        items_canvas.append(tmpl % (iid, n, md_c, body, pres, proc))
        items_cc.append(tmpl % (iid, n, md_cc, body, pres, proc))
    def qti(items, extra):
        return ('<?xml version="1.0" encoding="UTF-8"?>\n<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" '
                'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 '
                'http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">\n<assessment ident="%s" title="%s"><qtimetadata>%s</qtimetadata>\n'
                '<section ident="root_section">\n%s\n</section>\n</assessment>\n</questestinterop>\n'
                % (gid, escape(title, {'"': "&quot;"}), meta("cc_maxattempts", "1") + extra, "\n".join(items)))
    desc = escape("<p>%s</p>" % (d["intro"] or "This week's check-in."))
    ameta = ('<?xml version="1.0" encoding="UTF-8"?>\n<quiz identifier="%s" xmlns="http://canvas.instructure.com/xsd/cccv1p0" '
             'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 '
             'https://canvas.instructure.com/xsd/cccv1p0.xsd"><title>%s</title><description>%s</description>'
             '<shuffle_answers>false</shuffle_answers><scoring_policy>keep_highest</scoring_policy><quiz_type>assignment</quiz_type>'
             '<points_possible>%s</points_possible><allowed_attempts>1</allowed_attempts><one_question_at_a_time>false</one_question_at_a_time>'
             '<show_correct_answers>false</show_correct_answers><available>false</available><assignment identifier="%s"><title>%s</title>'
             '<points_possible>%s</points_possible><grading_type>points</grading_type><submission_types>online_quiz</submission_types>'
             '<workflow_state>unpublished</workflow_state></assignment></quiz>\n'
             % (gid, escape(title), desc, num(total), aid, escape(title), num(total)))
    return dict(week=week, title=title, gid=gid, rid=rid, qti_canvas=qti(items_canvas, ""),
                qti_cc=qti(items_cc, meta("qmd_assessmenttype", "Examination")), ameta=ameta, n=len(qs), total=total,
                keys=", ".join("Q%d %s" % (q["n"], q["key_letter"]) for q in qs if q.get("key_letter")))

def main(outdir):
    Q = [quiz(w) for w in WEEKS]
    mh = "m" + ident("g4ela-q4-checkins")
    # 1) .imscc, Canvas course-export shape
    res = ""
    for q in Q:
        res += ('<resource identifier="%(gid)s" type="imsqti_xmlv1p2/imscc_xmlv1p1/assessment"><file href="%(gid)s/assessment_qti.xml"/>'
                '<dependency identifierref="%(rid)s"/></resource>'
                '<resource identifier="%(rid)s" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="%(gid)s/assessment_meta.xml">'
                '<file href="%(gid)s/assessment_meta.xml"/><file href="non_cc_assessments/%(gid)s.xml.qti"/></resource>') % q
    man = ('<?xml version="1.0" encoding="UTF-8"?>\n<manifest identifier="%s" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" '
           'xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest" '
           'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 '
           'http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd">'
           '<metadata><schema>IMS Common Cartridge</schema><schemaversion>1.1.0</schemaversion>'
           '<lomimscc:lom><lomimscc:general><lomimscc:title><lomimscc:string>4th Grade ELA: Quarter 4 Check-Ins (Weeks 25-32)</lomimscc:string>'
           '</lomimscc:title></lomimscc:general></lomimscc:lom></metadata>'
           '<organizations/><resources>%s</resources></manifest>\n' % (mh, res))
    p1 = os.path.join(outdir, "g4-ela-q4-checkins.imscc")
    with zipfile.ZipFile(p1, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", man)
        for q in Q:
            z.writestr("%s/assessment_qti.xml" % q["gid"], q["qti_cc"])
            z.writestr("%s/assessment_meta.xml" % q["gid"], q["ameta"])
            z.writestr("non_cc_assessments/%s.xml.qti" % q["gid"], q["qti_canvas"])
    # 2) plain QTI zip (same shape as the G3 week zips that imported fine)
    res2 = ""
    for q in Q:
        res2 += ('<resource identifier="%(gid)s" type="imsqti_xmlv1p2"><file href="%(gid)s/%(gid)s.xml"/><dependency identifierref="%(rid)s"/></resource>'
                 '<resource identifier="%(rid)s" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="%(gid)s/assessment_meta.xml">'
                 '<file href="%(gid)s/assessment_meta.xml"/></resource>') % q
    man2 = ('<?xml version="1.0" encoding="UTF-8"?>\n<manifest identifier="%s" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 '
            'http://www.imsglobal.org/xsd/imscp_v1p1.xsd"><metadata><schema>IMS Content</schema><schemaversion>1.1.3</schemaversion></metadata>'
            '<organizations/><resources>%s</resources></manifest>\n' % (mh + "q", res2))
    p2 = os.path.join(outdir, "g4-ela-q4-checkins-qti.zip")
    with zipfile.ZipFile(p2, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", man2)
        for q in Q:
            z.writestr("%s/%s.xml" % (q["gid"], q["gid"]), q["qti_canvas"])
            z.writestr("%s/assessment_meta.xml" % q["gid"], q["ameta"])
    for q in Q: print("  %s: %d questions, %d points, key %s" % (q["title"], q["n"], q["total"], q["keys"]))
    print("wrote", p1, "and", p2)
    from tag_qti import tag   # each question's standards, from the page tags (tools/std_tag.py)
    tag(p1); tag(p2)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
