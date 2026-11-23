#!/usr/bin/env python3
"""fix_wk32_recorder.py - Nov 22 2026. Puts an in-page Talk Recorder in G4 ELA 32.4, the same way the G3 science
32.02 Park Slide Studio does it (assets/sparkle/wf-studio.js in optima-3rd-science):
  - the student records their voice card by card (getUserMedia, audio only); recordings stay in memory, never saved or sent
  - "Make my video" plays the four cue cards on a 1280x720 canvas with each recording and downloads an .mp4
    (Chrome/Edge/Safari) or .webm; the student uploads that file to the Canvas assignment
  - if the mic is blocked (Canvas iframe without allow="microphone"), it says so and points to Canvas "Record media"
  - <meta name="canvas-iframe-allow" content="microphone; fullscreen"> marks the page, like the science page
The title slide pulls the portfolio title from Lesson 32.3 (same site, so same browser storage).
    python3 tools/fix_wk32_recorder.py [--apply]
"""
import io, sys
APPLY = '--apply' in sys.argv
P = 'lesson-32-4-project-celebration.html'
h = io.open(P, encoding='utf-8', newline='').read()

def rep(old, new, label):
    global h
    if h.count(old) != 1: sys.exit('expected one match (%d): %s' % (h.count(old), label))
    h = h.replace(old, new)

rep('<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<meta name="canvas-iframe-allow" content="microphone; fullscreen">', 'meta')

CSS = """
/* ═══════════ TALK RECORDER (32.4) ═══════════ */
.tr-list{display:grid;gap:10px;margin:10px 0;}
.tr-row{display:grid;grid-template-columns:200px 1fr;gap:14px;align-items:center;border:2px solid #E2E8F4;border-radius:14px;padding:10px;background:#fff;}
@media(max-width:700px){.tr-row{grid-template-columns:1fr;}}
.tr-thumb{aspect-ratio:16/9;border-radius:10px;background:#0E1C42;color:#fff;padding:10px;font-size:11px;line-height:1.35;overflow:hidden;font-family:Georgia,serif;position:relative;}
.tr-thumb b{display:block;color:#F9A825;font-family:Arial,sans-serif;font-size:10px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px;}
.tr-name{font-weight:800;color:#0E1C42;font-size:15px;}
.tr-sub{font-size:13px;color:#7A88A8;margin:2px 0 8px;}
.tr-btns{display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
.tr-b{font-family:inherit;font-size:14px;font-weight:800;padding:8px 14px;border-radius:999px;border:2px solid #E2E8F4;background:#fff;color:#0E1C42;cursor:pointer;}
.tr-b.rec{background:#C0392B;border-color:#C0392B;color:#fff;}
.tr-b.on{background:#0E1C42;border-color:#0E1C42;color:#fff;}
.tr-b:disabled{opacity:.45;cursor:default;}
.tr-ok{font-size:13px;font-weight:700;color:#1E5E3A;}
.tr-msg{background:#FFF6E0;color:#6B4A00;border-radius:10px;padding:10px 14px;font-size:14px;line-height:1.5;margin:8px 0;}
.tr-total{font-size:14px;font-weight:700;color:#3A4A6B;margin:6px 0 10px;}
.tr-make{font-family:inherit;font-size:16px;font-weight:800;padding:12px 22px;border-radius:999px;border:none;background:#F9A825;color:#0E1C42;cursor:pointer;}
.tr-ov{position:fixed;inset:0;background:rgba(14,28,66,.85);z-index:9999;display:flex;align-items:center;justify-content:center;padding:20px;}
.tr-mk{background:#fff;border-radius:18px;padding:18px;max-width:720px;width:100%;text-align:center;}
.tr-mk canvas{width:100%;height:auto;border-radius:10px;background:#0E1C42;}
.tr-bar{height:8px;background:#E2E8F4;border-radius:99px;overflow:hidden;margin:10px 0;} .tr-bar i{display:block;height:100%;width:0;background:#34B76F;}
"""
rep('/* ═══════════ PRESENTATION (32.4) ═══════════ */\n.pr-cards', CSS + '\n/* ═══════════ PRESENTATION (32.4) ═══════════ */\n.pr-cards', 'css')

rep('<b>📹 Record a video</b>Record your talk (1&ndash;2 minutes) with your portfolio on screen or in your hands. Turn in the video on Canvas.',
    '<b>🎬 Make a video here</b>Record your voice card by card, right on this page. It turns your cue cards into a video you upload to Canvas.', 'path label')

PANE = """<div class="pr-pane" id="prPane-video">
        <p style="font-size:14px;color:#3A4A6B;">Each cue card becomes a slide. Tap 🎙️ Record, say that card, then tap ■ Stop. Listen back, and redo any card you want. Your recordings stay on this page only; nothing is saved or sent until you upload your video.</p>
        <div class="tr-msg" id="trMsg" hidden></div>
        <div class="tr-list" id="trList"></div>
        <div class="tr-total" id="trTotal"></div>
        <div style="text-align:center;"><button type="button" class="tr-make" onclick="trMovie()">🎬 Make my video</button></div>
        <p style="font-size:13px;color:#7A88A8;text-align:center;margin-top:8px;">The video lands in your Downloads. Upload it to the Canvas assignment with your cue cards. Closing this page erases your recordings, so make the video first.</p>
      </div>"""
i = h.find('<div class="pr-pane" id="prPane-video">'); j = h.find('</div>', i) + len('</div>')
if i < 0: sys.exit('no video pane')
h = h[:i] + PANE + h[j:]

JS = r"""
/* ═══════════ TALK RECORDER (32.4) — modeled on G3 science 32.02 wf-studio.js ═══════════
   Voice recordings live in memory only (never saved, never sent). The only copy ends up inside the downloaded video. */
var TR_CARDS=[{id:'journal-q1',k:'Card 1 · Open',max:40},{id:'journal-q2',k:'Card 2 · Show the change',max:60},{id:'journal-q3',k:'Card 3 · Look forward',max:40},{id:'journal-writing',k:'Card 4 · My last line',max:25}];
var TR_REC={},trNow=null,trIdx=-1,trT=null;
function trPf(s){try{var k='Lesson 32.3 — Year-End Project: Portfolio and Presentation (Sparkle)'.replace(/[^a-zA-Z0-9]+/g,'-').toLowerCase()+'-'+s;return localStorage.getItem(k)||'';}catch(e){return '';}}
function trTitle(){return (trPf('pf-title')||'My Year of Reading').trim();}
function trText(i){var e=document.getElementById(TR_CARDS[i].id);return e?e.value.trim():'';}
function trE(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function trMsg(t){var m=document.getElementById('trMsg');if(m){m.hidden=!t;m.innerHTML=t||'';}}
function trDraw(){
  var L=document.getElementById('trList');if(!L)return;var h='',tot=0;
  TR_CARDS.forEach(function(c,i){var r=TR_REC[i],live=trIdx===i,t=trText(i);if(r)tot+=r.sec;
    h+='<div class="tr-row"><div class="tr-thumb"><b>'+(i===0?trE(trTitle()):c.k.split(' · ')[1])+'</b>'+(t?trE(t.slice(0,140))+(t.length>140?'…':''):'<i style="opacity:.6">Write this card in Part '+(i===3?'B':'A')+' first.</i>')+'</div>'+
      '<div><div class="tr-name">'+c.k+'</div><div class="tr-sub">Up to '+c.max+' seconds'+(live?' · <b id="trSec">0</b>s':'')+'</div><div class="tr-btns">'+
      (live?'<button type="button" class="tr-b rec" onclick="trStop()">■ Stop</button>':'<button type="button" class="tr-b" '+(trNow?'disabled':'')+' onclick="trRec('+i+')">🎙️ '+(r?'Redo':'Record')+'</button>')+
      (r&&!live?'<button type="button" class="tr-b" onclick="trPlay('+i+')">▶ Listen</button><span class="tr-ok">✓ '+r.sec+' sec</span>':'')+'</div></div></div>';});
  L.innerHTML=h;
  var T=document.getElementById('trTotal'),n=Object.keys(TR_REC).length;
  if(T)T.textContent=n?('Recorded '+n+' of 4 cards · '+Math.floor(tot/60)+':'+('0'+tot%60).slice(-2)+(tot<60?' · a little short, aim for 1:00–2:00':tot>120?' · a bit long, aim for 1:00–2:00':' · just right')):'';
}
function trRec(i){
  var blocked='The microphone is blocked here, so this page can’t record. That’s OK: use <b>Record media</b> on the Canvas assignment, or present to a grown-up instead.';
  if(!navigator.mediaDevices||!navigator.mediaDevices.getUserMedia||!window.MediaRecorder){trMsg(blocked);return;}
  navigator.mediaDevices.getUserMedia({audio:true}).then(function(stream){
    var chunks=[],mr;try{mr=new MediaRecorder(stream);}catch(e){stream.getTracks().forEach(function(t){t.stop();});trMsg(blocked);return;}
    var t0=Date.now();trMsg('');
    trT=setInterval(function(){var s=Math.floor((Date.now()-t0)/1000),e=document.getElementById('trSec');if(e)e.textContent=s;if(s>=TR_CARDS[i].max&&mr.state==='recording')mr.stop();},250);
    mr.ondataavailable=function(e){if(e.data&&e.data.size)chunks.push(e.data);};
    mr.onstop=function(){clearInterval(trT);stream.getTracks().forEach(function(t){t.stop();});trNow=null;trIdx=-1;
      var blob=new Blob(chunks,{type:mr.mimeType||'audio/webm'}),old=TR_REC[i];if(old)URL.revokeObjectURL(old.url);
      if(blob.size)TR_REC[i]={blob:blob,url:URL.createObjectURL(blob),sec:Math.max(1,Math.round((Date.now()-t0)/1000))};
      trDraw();gatherAnswers();};
    trNow=mr;trIdx=i;mr.start();trDraw();
  },function(){trMsg(blocked);});
}
function trStop(){if(trNow&&trNow.state==='recording')trNow.stop();}
function trPlay(i){var r=TR_REC[i];if(r)new Audio(r.url).play();}
function trWrap(x,t,X0,Y0,W,maxH,size,font,lh){var s=size,lines;
  for(;;){x.font=font.replace('{s}',s);lines=[];var line='';t.split(/\s+/).forEach(function(w){var tt=line?line+' '+w:w;if(x.measureText(tt).width>W&&line){lines.push(line);line=w;}else line=tt;});if(line)lines.push(line);
    if(lines.length*s*lh<=maxH||s<=18)break;s-=2;}
  lines.forEach(function(l,k){x.fillText(l,X0,Y0+s+k*s*lh);});}
function trPaint(x,i){
  var t=trText(i)||'',colors=['#F9A825','#55C8E8','#34B76F','#F9A825'];
  x.fillStyle='#0E1C42';x.fillRect(0,0,1280,720);x.fillStyle=colors[i];x.fillRect(0,0,1280,10);x.textBaseline='alphabetic';x.textAlign='left';
  if(i===0){x.textAlign='center';x.fillStyle='#F9A825';x.font='bold 22px Arial';x.fillText('4TH GRADE ELA · YEAR-END PORTFOLIO',640,120);
    x.fillStyle='#fff';x.font='bold 60px Georgia';x.fillText(trTitle(),640,200);x.font='54px Arial';x.fillText('🐭  👩‍🦰  ⭐  🚆  🦁',640,290);x.textAlign='left';
    x.fillStyle='#fff';trWrap(x,t,120,330,1040,330,36,'{s}px Georgia',1.35);}
  else if(i===3){x.textAlign='center';x.fillStyle='#F9A825';x.font='bold 24px Arial';x.fillText('MY LAST LINE OF 4TH GRADE ELA',640,180);x.fillStyle='#fff';
    x.font='italic 52px Georgia';var words=t.split(/\s+/),line='',ls=[];words.forEach(function(w){var tt=line?line+' '+w:w;if(x.measureText(tt).width>1060&&line){ls.push(line);line=w;}else line=tt;});if(line)ls.push(line);
    ls.slice(0,5).forEach(function(l,k){x.fillText(l,640,290+k*70);});x.font='44px Arial';x.fillText('🐭  👩‍🦰  ⭐  🚆  🦁',640,660);x.textAlign='left';}
  else{x.fillStyle=colors[i];x.font='bold 26px Arial';x.fillText(TR_CARDS[i].k.toUpperCase(),80,100);x.fillStyle='#fff';x.font='bold 44px Georgia';
    x.fillText(i===1?'Then and now':'Next year',80,165);x.fillStyle='#E8EEF8';trWrap(x,t,80,200,1120,470,38,'{s}px Georgia',1.38);}
}
function trMovie(){
  if(!window.MediaRecorder||!HTMLCanvasElement.prototype.captureStream){trMsg('This browser can’t make videos. Use <b>Record media</b> on the Canvas assignment instead.');return;}
  var types=['video/mp4;codecs=avc1.42E01E,mp4a.40.2','video/mp4;codecs=avc1,mp4a.40.2','video/mp4;codecs=avc1,opus','video/mp4','video/webm;codecs=vp9,opus','video/webm;codecs=vp8,opus','video/webm'],
      type=types.filter(function(t){return MediaRecorder.isTypeSupported&&MediaRecorder.isTypeSupported(t);})[0];
  if(!type){trMsg('This browser can’t make videos. Use <b>Record media</b> on the Canvas assignment instead.');return;}
  if(!Object.keys(TR_REC).length&&!confirmNoVoice())return;
  var o=document.createElement('div');o.className='tr-ov';o.setAttribute('role','dialog');o.setAttribute('aria-label','Making my video');
  o.innerHTML='<div class="tr-mk"><h3 style="margin:0 0 8px;">🎬 Making your video…</h3><canvas width="1280" height="720"></canvas><div class="tr-bar"><i></i></div><p id="trMk" style="margin:4px 0;">Getting ready…</p><p style="font-size:13px;color:#7A88A8;">Keep this page open. Your video is made on this computer.</p><button type="button" class="tr-b" data-x>Cancel</button></div>';
  document.body.appendChild(o);var cv=o.querySelector('canvas'),x=cv.getContext('2d'),bar=o.querySelector('.tr-bar i'),msg=o.querySelector('#trMk'),stop=false,mr=null,tk=null;
  var AudioC=window.AudioContext||window.webkitAudioContext,AC=AudioC?new AudioC():null,dest=AC?AC.createMediaStreamDestination():null;
  o.querySelector('[data-x]').onclick=function(){stop=true;clearInterval(tk);if(mr&&mr.state==='recording')mr.stop();o.remove();try{AC&&AC.close();}catch(e){}};
  Promise.all(TR_CARDS.map(function(c,i){var r=TR_REC[i];return r&&AC?r.blob.arrayBuffer().then(function(b){return AC.decodeAudioData(b);}).catch(function(){return null;}):Promise.resolve(null);})).then(function(bufs){
    if(stop)return;var durs=TR_CARDS.map(function(c,i){return bufs[i]?bufs[i].duration+1.2:6;}),total=durs.reduce(function(a,b){return a+b;},0)+1,starts=[],acc=0;durs.forEach(function(v){starts.push(acc);acc+=v;});
    trPaint(x,0);var stream=cv.captureStream(30);if(dest)dest.stream.getAudioTracks().forEach(function(t){stream.addTrack(t);});
    var chunks=[];mr=new MediaRecorder(stream,{mimeType:type,videoBitsPerSecond:2500000});mr.ondataavailable=function(e){if(e.data&&e.data.size)chunks.push(e.data);};
    mr.onstop=function(){clearInterval(tk);if(stop)return;try{AC&&AC.close();}catch(e){}var ext=/mp4/.test(type)?'mp4':'webm',blob=new Blob(chunks,{type:type.split(';')[0]}),a=document.createElement('a');
      a.href=URL.createObjectURL(blob);a.download='Lesson-32-4-my-portfolio-talk.'+ext;document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},5000);
      o.remove();try{localStorage.setItem(prK('videoMade'),'1');}catch(e){}trMsg('🎬 Your video is in your Downloads. Upload it to the Canvas assignment.');gatherAnswers();};
    if(AC&&AC.state==='suspended')AC.resume();
    mr.start(1000);var t0=performance.now(),cur=-1;
    tk=setInterval(function(){var t=(performance.now()-t0)/1000,i=0;while(i<TR_CARDS.length-1&&t>=starts[i+1])i++;
      if(i!==cur){cur=i;if(bufs[i]&&AC){var src=AC.createBufferSource();src.buffer=bufs[i];src.connect(dest);src.start(AC.currentTime+.4);}msg.textContent='Card '+(i+1)+' of 4'+(bufs[i]?' · with your voice':' · no recording, 6 seconds');}
      trPaint(x,i);bar.style.width=Math.min(100,t/total*100)+'%';if(t>=total&&mr.state==='recording')mr.stop();},100);
  });
}
function confirmNoVoice(){trMsg('You haven’t recorded any cards yet. Record at least one card first, so your teacher can hear you.');return false;}
(function(){
  trDraw();
  TR_CARDS.forEach(function(c){var e=document.getElementById(c.id);if(e)e.addEventListener('input',function(){if(!trNow)trDraw();});});
})();
"""
rep('/* DOWNLOAD PDF */\nfunction downloadJournal(){', JS + '\n/* DOWNLOAD PDF */\nfunction downloadJournal(){', 'js')

# gathered: say whether the video was made + how many cards were recorded
rep("  o+='How I presented: '+(p==='video'?'Video (turned in on Canvas)'",
    "  o+='How I presented: '+(p==='video'?('Video made on this page'+(typeof TR_REC!=='undefined'?' ('+Object.keys(TR_REC).length+' of 4 cards recorded)':'')+(prGet('videoMade','')?', downloaded':', not made yet'))", 'gather')
# todo + checklist wording
rep('I presented, and turned in my video or my grown-up&rsquo;s listener card on Canvas with my cue cards.',
    'I presented: I made my video here and uploaded it, or my grown-up filled in the listener card. I turned in my cue cards too.', 'checklist')

if APPLY:
    io.open(P, 'w', encoding='utf-8', newline='').write(h); print('written', P)
else:
    print('dry run ok')
