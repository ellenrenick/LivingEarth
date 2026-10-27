(function(){
const D=window.UNIT, $=(s,r=document)=>r.querySelector(s);
const KEY='review:'+D.code;
let saved={};try{saved=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){}
const save=()=>{try{localStorage.setItem(KEY,JSON.stringify(saved))}catch(e){}};
const shuffle=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const h=(tag,attrs,html)=>{const e=document.createElement(tag);for(const k in attrs||{}){if(k==='class')e.className=attrs[k];else e.setAttribute(k,attrs[k])}if(html!=null)e.innerHTML=html;return e};
let total=0,qid=0;
const meter=h('div',{class:'meter'},'<span id="mtxt"></span><div class="bar"><i id="mbar"></i></div>');
function upd(){const n=Object.keys(saved).filter(k=>saved[k]==='ok').length;$('#mtxt').textContent=n+' of '+total+' correct';$('#mbar').style.width=(total?100*n/total:0)+'%';
  const dm=$('#done');if(dm)dm.classList.toggle('show',n===total&&total>0)}
function feedback(box,ok,why){box.className='fb show '+(ok?'ok':'no');
  box.innerHTML='<b class="s">'+(ok?'Correct.':'Not yet.')+'</b>'+(ok?'':'Look again and try once more. ')+(why?why:'')}
function wrapQ(q,body,tag){const id=D.code+'-q'+(++qid);total++;const box=h('div',{class:'q',id});
  box.appendChild(h('div',{class:'tag'},tag||q.tag||'Practice'));
  if(q.ctx)box.appendChild(h('div',{class:'ctx'},q.ctx));
  box.appendChild(h('div',{class:'stem'},q.q));box.appendChild(body);
  const fb=h('div',{class:'fb',role:'status'});box.appendChild(fb);return {box,fb,id}}
function mc(q,multi){
  const opts=q.opts.map((t,i)=>({t,i,right:multi?q.a.includes(i):q.a===i}));
  const list=h('div',{class:'opts'}),name='n'+(qid+1);
  shuffle(opts).forEach(o=>{const l=h('label',{class:'opt'},'<input type="'+(multi?'checkbox':'radio')+'" name="'+name+'"><span>'+o.t+'</span>');l._o=o;list.appendChild(l)});
  const {box,fb,id}=wrapQ(q,list,multi?'Choose '+q.a.length:null);
  const b=h('button',{class:'go',type:'button'},'Check');box.insertBefore(b,fb);
  b.onclick=()=>{let ok=true;const sel=[...list.children];
    sel.forEach(l=>{const c=l.firstChild.checked;l.classList.remove('right','wrong');
      if(c&&l._o.right)l.classList.add('right');else if(c&&!l._o.right){l.classList.add('wrong');ok=false}else if(!c&&l._o.right)ok=false});
    if(!sel.some(l=>l.firstChild.checked)){fb.className='fb show no';fb.innerHTML='Pick an answer first.';return}
    saved[id]=ok?'ok':'no';save();upd();feedback(fb,ok,ok?q.why:(q.hint||''))
    if(ok)sel.forEach(l=>l.firstChild.disabled=true)};
  if(saved[id]==='ok'){/* progress counted; question stays fresh for re-practice */}
  return box}
function match(q){
  const rights=shuffle(q.pairs.map(p=>p[1]).concat(q.extra||[]));const body=h('div');
  q.pairs.forEach(p=>{const r=h('div',{class:'row'},'<div class="l">'+p[0]+'</div>');
    const s=h('select',{'aria-label':p[0].replace(/<[^>]+>/g,'')},'<option value="">Choose…</option>'+rights.map((t,i)=>'<option value="'+i+'">'+t+'</option>').join(''));
    s._ans=rights.indexOf(p[1]);r.appendChild(s);body.appendChild(r)});
  const {box,fb,id}=wrapQ(q,body,'Match');const b=h('button',{class:'go',type:'button'},'Check');box.insertBefore(b,fb);
  b.onclick=()=>{let ok=true,blank=false;body.querySelectorAll('select').forEach(s=>{s.classList.remove('right','wrong');
    if(s.value===''){blank=true;ok=false;return}if(+s.value===s._ans)s.classList.add('right');else{s.classList.add('wrong');ok=false}});
    if(blank&&ok===false&&!body.querySelector('.wrong')){fb.className='fb show no';fb.innerHTML='Choose an answer for every row.';return}
    saved[id]=ok?'ok':'no';save();upd();feedback(fb,ok,ok?q.why:'Fix the red rows and check again.')};
  return box}
function write(q){
  const body=h('div');
  if(q.frames)body.appendChild(h('ul',{class:'frames'},q.frames.map(f=>'<li>'+f+'</li>').join('')));
  const ta=h('textarea',{id:D.code+'-w'+(++qid),placeholder:'Write your answer here…'});
  try{ta.value=localStorage.getItem(KEY+':'+ta.id)||''}catch(e){}ta.oninput=()=>{try{localStorage.setItem(KEY+':'+ta.id,ta.value)}catch(e){}};
  body.appendChild(ta);qid--;
  body.appendChild(h('div',{class:'tag',style:'margin-top:12px'},'Check your own answer'));
  const chk=h('div',{class:'chk'});q.check.forEach((c,i)=>chk.appendChild(h('label',{},'<input type="checkbox"><span>'+c+'</span>')));body.appendChild(chk);
  const id=D.code+'-q'+(++qid);const box=h('div',{class:'q',id});total++;
  box.appendChild(h('div',{class:'tag'},'Write it'));if(q.ctx)box.appendChild(h('div',{class:'ctx'},q.ctx));
  box.appendChild(h('div',{class:'stem'},q.q));box.appendChild(body);
  const sample=h('div',{class:'sample'},'<b>Sample answer (about a 4)</b><br>'+q.sample);
  const b=h('button',{class:'go alt',type:'button'},'Show a sample answer');b.onclick=()=>{sample.classList.toggle('show')};
  const done=h('button',{class:'go',type:'button'},'I wrote it and checked every box');
  const fb=h('div',{class:'fb',role:'status'});
  done.onclick=()=>{const all=[...chk.querySelectorAll('input')].every(i=>i.checked);
    if(!ta.value.trim()){fb.className='fb show no';fb.textContent='Write your answer first.';return}
    if(!all){fb.className='fb show no';fb.innerHTML='Some boxes are not checked. Add the missing piece to your answer, then check the box. You can look at the sample answer to compare.';return}
    saved[id]='ok';save();upd();fb.className='fb show ok';fb.innerHTML='<b class="s">Nice work.</b>Compare with the sample answer and fix anything you missed.'};
  box.append(done,' ',b,fb,sample);return box}
function sec(id,title,sub){const s=h('section',{id});s.appendChild(h('h2',{},title));if(sub)s.appendChild(h('p',{class:'sub'},sub));return s}

const root=$('#app');
const hd=h('header',{class:'top'},'<div class="eyebrow">'+D.eyebrow+'</div><h1>'+D.title+'</h1><p class="lede">'+D.lede+'</p>');
hd.appendChild(meter);root.appendChild(hd);
const nav=h('nav',{class:'tabs','aria-label':'Sections'});root.appendChild(nav);
const add=(id,t)=>nav.appendChild(h('a',{href:'#'+id},t));

let s=sec('ideas','Key ideas','Read these first. Then try the practice.');add('ideas','Key ideas');
const ul=h('ol',{class:'ideas'});D.ideas.forEach(i=>ul.appendChild(h('li',{},'<div><b>'+i.t+'</b> '+i.d+(i.eq?'<div class="eq">'+i.eq+'</div>':'')+'</div>')));
s.appendChild(ul);root.appendChild(s);

s=sec('words','Vocabulary','Tap a card to see the meaning. Then say it in your own words.');add('words','Vocabulary');
const cards=h('div',{class:'cards'});D.vocab.forEach(v=>{const c=h('button',{class:'card',type:'button','aria-expanded':'false'},'<span class="t">'+v[0]+'</span><span class="hint">Tap to flip</span><span class="d">'+v[1]+'</span>');
  c.onclick=()=>{const o=c.classList.toggle('open');c.setAttribute('aria-expanded',o)};cards.appendChild(c)});
s.appendChild(cards);D.vocabQuiz.forEach(q=>s.appendChild(match(q)));root.appendChild(s);

s=sec('practice','Practice','Each question tells you right away. Missed one? Read the explanation, then try it again.');add('practice','Practice');
D.practice.forEach(q=>s.appendChild(q.type==='multi'?mc(q,true):q.type==='match'?match(q):mc(q,false)));root.appendChild(s);

s=sec('model',D.model.title,D.model.sub);add('model','Models');
const fig=h('figure',{},D.model.figure+'<figcaption>'+D.model.caption+'</figcaption>');s.appendChild(fig);
D.model.qs.forEach(q=>s.appendChild(q.type==='multi'?mc(q,true):q.type==='match'?match(q):mc(q,false)));root.appendChild(s);

s=sec('write','Explain it','Written answers are scored out of 4. Write, check yourself, then compare with the sample.');add('write','Explain it');
const rub=h('div',{class:'scroll'},'<table class="rubric"><tr><th>Score</th><th>What it looks like</th></tr>'+D.rubric.map(r=>'<tr><td>'+r[0]+'</td><td>'+r[1]+'</td></tr>').join('')+'</table>');
s.appendChild(rub);D.write.forEach(q=>s.appendChild(write(q)));root.appendChild(s);

s=sec('ready','Ready check','Check each one only when you can do it without notes.');add('ready','Ready check');
const rl=h('ul',{class:'ready'});D.ready.forEach((t,i)=>{const id=D.code+'-r'+i;const li=h('li',{},'<label><input type="checkbox" id="'+id+'"><span>'+t+'</span></label>');
  const c=li.querySelector('input');c.checked=saved[id]==='1';c.onchange=()=>{saved[id]=c.checked?'1':'';save()};rl.appendChild(li)});
s.appendChild(rl);s.appendChild(h('div',{class:'done-msg',id:'done'},'<b>You answered everything.</b> Take what you got wrong back to your notes, then tell your teacher you are ready to reassess.'));
root.appendChild(s);root.appendChild(h('footer',{},D.footer));
upd();
})();
