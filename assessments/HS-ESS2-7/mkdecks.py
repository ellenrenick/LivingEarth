import sys,json,re,math,html
sys.path.insert(0,'/home/user/LivingEarth/assessments/HS-ESS2-7')
import days
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__();s.lines=[];s.cur='';s.row=None;s.cell=None
    def flush(s):
        t=re.sub(r'\s+',' ',s.cur).strip()
        if t:s.lines.append(t)
        s.cur=''
    def handle_starttag(s,t,a):
        if t in('p','li','div','ol','ul'):s.flush()
        if t=='tr':s.flush();s.row=[]
        if t in('td','th'):s.cell=''
        if t=='br':s.cur+=' '
    def handle_endtag(s,t):
        if t in('p','li','div'):s.flush()
        if t in('td','th') and s.row is not None:
            s.row.append(re.sub(r'\s+',' ',s.cell or '').strip());s.cell=None
        if t=='tr' and s.row is not None:
            r=[x for x in s.row if x!='']
            if r:s.lines.append(' | '.join(s.row).strip(' |'))
            s.row=None
    def handle_data(s,d):
        if s.cell is not None:s.cell+=d
        else:s.cur+=d
def lines(h):
    p=P();p.feed(h);p.flush();return [l for l in p.lines if l]
def est(ls,size):
    cpl={18:60,16:68,14:78}[size]
    return sum(max(1,math.ceil(len(l)/cpl)) for l in ls)
def chunks(ls):
    out=[];cur=[]
    for l in ls:
        t=cur+[l]
        if est(t,14)>14 and cur: out.append(cur);cur=[l]
        else:cur=t
    if cur:out.append(cur)
    return out
def size_for(ls):
    for s,m in((18,10),(16,12),(14,14)):
        if est(ls,s)<=m:return s
    return 14
def build(d):
    n=d['n'];R=[];k=[0]
    def slide(layout,title,body=None,size=None):
        k[0]+=1;i=k[0]
        t=f"sl{i:02d}t";b=f"sl{i:02d}b"
        maps={"TITLE":[("CENTERED_TITLE",t),("SUBTITLE",b)],"TITLE_AND_BODY":[("TITLE",t),("BODY",b)],"MAIN_POINT":[("TITLE",t)]}[layout]
        R.append({"createSlide":{"objectId":f"slide{i:02d}","slideLayoutReference":{"predefinedLayout":layout},"placeholderIdMappings":[{"layoutPlaceholder":{"type":ty,"index":0},"objectId":oid} for ty,oid in maps]}})
        R.append({"insertText":{"objectId":t,"text":title}})
        if body is not None and layout!="MAIN_POINT":
            R.append({"insertText":{"objectId":b,"text":"\n".join(body) if isinstance(body,list) else body}})
            if layout=="TITLE_AND_BODY":
                s=size or size_for(body)
                if s!=18:R.append({"updateTextStyle":{"objectId":b,"textRange":{"type":"ALL"},"style":{"fontSize":{"magnitude":s,"unit":"PT"}},"fields":"fontSize"}})
    s=d['s'];tg=d['targets']
    slide("TITLE",f"Day {n}: {d['title']}",f"Unit 3.1 · Changing Earth, Changing Life · HS-ESS2-7")
    slide("MAIN_POINT",s['focus'])
    slide("TITLE_AND_BODY","The big question",[lines('<p>'+s['driving']+'</p>')[0],"","Focus question: "+s['focus']])
    slide("TITLE_AND_BODY","Learning targets for today",["ESS2-"+x+"  "+days.TARGETS[x] for x in tg])
    ag=[a for a in d['t']['agenda']]
    pl=[f"{a[0]} min: {a[1]}" for a in ag]
    if s.get('reading'):pl.append("Reading: "+s['reading'])
    slide("TITLE_AND_BODY","Today's plan",pl)
    slide("TITLE_AND_BODY","Notebook setup",[lines('<p>'+x+'</p>')[0] for x in s['nb']])
    for title,h in s['parts']:
        title=re.sub(r' \(\d+ min[^)]*\)','',title)
        ls=lines(h)
        cs=chunks(ls) or [[]]
        for j,c in enumerate(cs):
            slide("TITLE_AND_BODY",title if len(cs)==1 else f"{title} ({j+1} of {len(cs)})",c)
    slide("TITLE_AND_BODY","Wrap-up",lines(s['wrap']))
    return R
if __name__=="__main__":
    for d in days.DAYS:
        R=build(d)
        open(f"/tmp/deck31_{d['n']}.json","w").write(json.dumps([{"deleteObject":{"objectId":"p"}}]+R,separators=(",",":")))
        print(d['n'],d['title'],sum(1 for r in R if 'createSlide' in r),len(json.dumps(R,separators=(',',':'))))
