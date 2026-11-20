"""Final G4 ELA check fixes (Nov 20 2026). Run from the repo root."""
import re, sys, glob

def edit(f, old, new, count=1):
    s = open(f, encoding='utf8').read()
    n = s.count(old)
    if n != count:
        sys.exit(f'{f}: expected {count} match(es), found {n}: {old[:60]!r}')
    open(f, 'w', encoding='utf8', newline='').write(s.replace(old, new))
    print('fixed', f)

# 1. Weeks 1-6: Next / tab buttons landed at the top of the PAGE (header),
#    leaving the new tab below the fold. Land at the top of the new tab,
#    just under the sticky tab bar (same rule as sparkle.js goTabTop).
OLD = "  document.getElementById('pageTop').scrollIntoView({ behavior: 'smooth', block: 'start' });\n}"
NEW = """  /* land at the top of the new tab, just under the sticky tab bar */
  (function () {
    var last = -1;
    function place() {
      var panel = document.getElementById('tab-' + tabId);
      if (!panel) { window.scrollTo(0, 0); return; }
      var off = 8, bar = document.querySelector('.tab-bar');
      if (bar) { var cs = getComputedStyle(bar); off += (parseFloat(cs.top) || 0) + bar.offsetHeight; }
      var y = panel.getBoundingClientRect().top + (window.pageYOffset || 0) - off;
      window.scrollTo(0, Math.max(0, Math.round(y)));
      last = Math.round(window.pageYOffset || 0);
    }
    function again() { if (Math.abs((window.pageYOffset || 0) - last) <= 2) place(); }
    place(); requestAnimationFrame(again); setTimeout(again, 380);
    try {
      if (window.parent && window.parent !== window) {
        window.parent.postMessage(JSON.stringify({ subject: 'lti.scrollToTop' }), '*');
        window.parent.postMessage({ subject: 'lti.scrollToTop' }, '*');
      }
    } catch (e) {}
  })();
}"""
for f in sorted(glob.glob('lesson-[1-6]-[1-4]-*.html')):
    edit(f, OLD, NEW)

# 2. 6.4: the Daily Oral Language card lost its opening tag, which closed the
#    Warm-Up tab early. Poetry Corner, the By Heart poem and the Warm-Up Next
#    button sat outside every tab (showing on all four tabs).
edit('lesson-6-4-share.html',
     "</div>\n\n\n  \n\n    <div class=\"activity-body\">\n      <p>The first sentence is <strong>correct</strong>.",
     "</div>\n\n  <!-- DOL -->\n  <div class=\"activity bl-cyan\">\n    <div class=\"activity-head\"><div class=\"activity-num\" style=\"background:#55C8E8;\">1</div><div><div class=\"activity-title\">✏️ Daily Oral Language</div><div class=\"activity-sub\">Study the model, then fix the sentence.</div></div></div>\n    <div class=\"activity-body\">\n      <p>The first sentence is <strong>correct</strong>.")

edit('lesson-6-4-share.html',
     "no need to write here.</div>\n    </div>\n  \n\n  <div class=\"tab-next-wrap\">\n    <p class=\"tab-transition-voice\">Now that your mind is warmed up",
     "no need to write here.</div>\n    </div>\n  </div>\n\n  <div class=\"tab-next-wrap\">\n    <p class=\"tab-transition-voice\">Now that your mind is warmed up")

# 3. Choice-board day said Week 1 in weeks 2 and 5.
edit('lesson-2-4-frisby-ch12.html', "It's the last day of Week 1.", "It's the last day of Week 2.")
edit('lesson-5-4-assessment.html', "It's the last day of Week 1.", "It's the last day of Week 5.")

# 4. 31.3 copywork is Anne's rose line, but the question was about Peter and Caspian.
edit('lesson-31-3-synthesis-compare.html',
     "<em>Why does Peter say this to Caspian? What does it tell you about Peter&rsquo;s character? What would it feel like to hear these words if you were Caspian?</em>",
     "<em>Why can&rsquo;t Anne believe the book? What does this tell you about how much names matter to her? Do you agree with Anne?</em>")

# 5. No chapter to open in synthesis / project weeks.
edit('lesson-31-3-synthesis-compare.html',
     "you&rsquo;ll need before opening the final chapter.</p>",
     "you&rsquo;ll need for today&rsquo;s theme work.</p>")
edit('lesson-32-3-project-final.html',
     "you&rsquo;ll need before opening the final chapter.</p>",
     "you&rsquo;ll need for today&rsquo;s portfolio work.</p>")

# 6. 29.4's Today's Wonder was a copy of 28.4's. New one fits Ch. 10-12
#    (Lucy follows Aslan when the others can't see him; Caspian refuses
#    Nikabrik's plan to call back the White Witch).
edit('lesson-29-4-pc-discussion.html',
     "This week you watched leaders make choices &mdash; some good, some costly. Today ask yourself: <strong>What makes someone a good leader when the people they lead can&rsquo;t agree?</strong>",
     "This week Lucy followed Aslan when the others could not see him, and Caspian said no to a dark plan to bring back the White Witch. Today ask yourself: <strong>How do you choose the right path when the people around you want something else?</strong>")
