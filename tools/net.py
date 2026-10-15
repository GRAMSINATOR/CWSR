import math, random
random.seed(7)
C=280
R=205
nodes=[("Research",225,(0,-28),"middle"),("Practice",315,(0,-28),"middle"),("Policy",45,(0,38),"middle"),("Lived experience",135,(0,38),"middle")]
pos=[]
for name,ang,off,anch in nodes:
    a=math.radians(ang); pos.append((C+R*math.cos(a),C+R*math.sin(a)))
dots=[]
tries=0
while len(dots)<26 and tries<5000:
    tries+=1
    a=random.uniform(0,2*math.pi); r=random.uniform(70,250)
    x,y=C+r*math.cos(a),C+r*math.sin(a)
    if any(math.hypot(x-px,y-py)<34 for px,py in dots+pos+[(C,C)]): continue
    if r>185 and any(math.hypot(x-px,y-py)<60 for px,py in pos): continue
    dots.append((x,y))
f=lambda v:f"{v:.1f}"
out=[]
out.append('<svg viewBox="0 0 560 560" role="img" aria-labelledby="net-title"><title id="net-title">Research, practice, policy and lived experience connected through a shared network</title>')
out.append(f'<circle class="net-ring" cx="{C}" cy="{C}" r="{R}"/><circle class="net-ring" cx="{C}" cy="{C}" r="120"/>')
# dot links: each dot to nearest node and nearest other dot
links=[]
for i,(x,y) in enumerate(dots):
    nn=min(pos,key=lambda p:math.hypot(x-p[0],y-p[1]))
    links.append((x,y,*nn))
    others=sorted([d for j,d in enumerate(dots) if j!=i],key=lambda p:math.hypot(x-p[0],y-p[1]))
    o=others[0]
    if (o[0],o[1],x,y) not in links: links.append((x,y,*o))
for x1,y1,x2,y2 in links:
    out.append(f'<line class="net-link" x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"/>')
# strong spokes and perimeter curves
paths=[]
for i,(x,y) in enumerate(pos):
    d=f"M{f(x)} {f(y)} L{C} {C}"
    out.append(f'<path id="sp{i}" class="net-link net-link--strong" d="{d}"/>')
    nx,ny=pos[(i+1)%4]
    d2=f"M{f(x)} {f(y)} Q{C} {C} {f(nx)} {f(ny)}"
    out.append(f'<path id="cv{i}" class="net-link" d="{d2}"/>')
for i,(x,y) in enumerate(dots):
    cls="net-dot" if i%3 else "net-dot net-dot--soft"
    out.append(f'<circle class="{cls}" cx="{f(x)}" cy="{f(y)}" r="{3.2 if i%3 else 4.5}"/>')
# pulses
for i in range(4):
    dur=3.2+i*0.7
    out.append(f'<circle class="net-pulse" r="4"><animateMotion dur="{dur}s" repeatCount="indefinite" begin="-{i*0.6+0.4}s" keyPoints="{"0;1" if i%2==0 else "1;0"}" keyTimes="0;1" calcMode="linear"><mpath href="#sp{i}"/></animateMotion></circle>')
    out.append(f'<circle class="net-pulse" r="3" opacity=".7"><animateMotion dur="{5+i}s" repeatCount="indefinite" begin="-{i*1.1+0.5}s"><mpath href="#cv{i}"/></animateMotion></circle>')
# centre
out.append(f'<circle class="net-centre" cx="{C}" cy="{C}" r="54"/><circle cx="{C}" cy="{C}" r="54" fill="none" stroke="var(--gold)" stroke-width="1.4" stroke-dasharray="3 5"><animateTransform attributeName="transform" type="rotate" from="0 {C} {C}" to="360 {C} {C}" dur="40s" repeatCount="indefinite"/></circle>')
out.append(f'<text x="{C}" y="{C-4}" text-anchor="middle" style="font-family:var(--serif);font-size:17px;fill:var(--ink);font-style:italic">Whole of</text><text x="{C}" y="{C+16}" text-anchor="middle" style="font-family:var(--serif);font-size:17px;fill:var(--ink);font-style:italic">society</text>')
for (name,ang,off,anch),(x,y) in zip(nodes,pos):
    out.append(f'<g class="net-node"><circle class="halo" cx="{f(x)}" cy="{f(y)}" r="15"/><circle class="core" cx="{f(x)}" cy="{f(y)}" r="6"/><text x="{f(x+off[0])}" y="{f(y+off[1])}" text-anchor="{anch}">{name}</text></g>')
out.append('</svg>')
print("\n".join(out))
