"""Assemble the CWSR static site. Output is plain HTML committed to the repo."""
import os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..")
NET = open(os.path.join(os.path.dirname(__file__), 'net.svg')).read()

FORM = "https://forms.office.com/Pages/ResponsePage.aspx?id=cpq-ajTOTkO78oZ8lo_C139YKKTOPjtGtlPz7X8FWPRUN1pBMTRWQVBHTzdWRE9UQlRVMjhPOFU4Mi4u"
LINKEDIN = "https://www.linkedin.com/groups/12970125/"
EMAIL = "connect@wholesocietyresilience.org"
SITE = "https://www.wholesocietyresilience.org"

ARROW = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
OUT_ICON = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M7 13 13.5 6.5M8 6h6v6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'

NAV = [("index.html", "Home"), ("about.html", "About"), ("news.html", "News"), ("governance.html", "Governance")]


def header(active, P):
    links = "\n".join(
        f'        <a href="{P}{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a>'
        for href, label in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="{P}index.html" aria-label="CWSR home">
      <img src="{P}assets/img/logo-mark.png" alt="" width="44" height="44">
      <span class="brand__text">
        <span class="brand__name">Whole of Society Resilience</span>
        <span class="brand__sub">Centre · CWSR</span>
      </span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu"><span></span></button>
    <nav class="nav" id="site-nav" aria-label="Main">
{links}
        <a class="btn" href="{P}join.html"{" aria-current=\"page\"" if active == "join.html" else ""}>Become a member</a>
    </nav>
  </div>
</header>'''


def footer(P):
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer__top">
      <div class="footer__brand">
        <img src="{P}assets/img/logo-mark-light.png" alt="" width="64" height="64">
        <p>Joining the dots between research, practice and policy.</p>
      </div>
      <div>
        <h4>Centre</h4>
        <ul>
          <li><a href="{P}about.html">About us</a></li>
          <li><a href="{P}about.html#people">Founders &amp; steering committee</a></li>
          <li><a href="{P}news.html">News &amp; insight</a></li>
        </ul>
      </div>
      <div>
        <h4>Get involved</h4>
        <ul>
          <li><a href="{P}join.html">Become a member</a></li>
          <li><a href="{FORM}" rel="noopener">Member sign up</a></li>
          <li><a href="{LINKEDIN}" rel="noopener">LinkedIn group</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{P}governance.html#terms">Terms of Reference</a></li>
          <li><a href="{P}governance.html#guidelines">Site rules</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__word" aria-hidden="true">Resilient, together.</div>
    <div class="footer__bottom">
      <span>© 2026 Centre for Whole of Society Resilience (CWSR)</span>
      <span>Building a resilient future, together.</span>
    </div>
  </div>
</footer>
<script src="{P}assets/js/site.js" defer></script>'''


def join_band(P):
    return f'''<section class="section section--ink" id="join" aria-labelledby="join-title">
  <div class="wrap join">
    <div class="reveal">
      <span class="eyebrow">Membership · It's free</span>
      <h2 id="join-title">Become a <em>member</em> of the network.</h2>
      <ul class="join__perks">
        <li>Meet other resilience professionals</li>
        <li>Share knowledge</li>
        <li>Participate in impactful projects</li>
      </ul>
      <div class="join__actions">
        <a class="btn btn--gold" href="{FORM}" rel="noopener">Member sign up {ARROW}</a>
        <a class="btn btn--ghost-light" href="{LINKEDIN}" rel="noopener">Join our LinkedIn group</a>
      </div>
    </div>
    <div class="charter reveal">
      <span class="charter__label">CWSR Membership Charter</span>
      <h3>What members agree to</h3>
      <p>As a Member of the Centre for Whole Society Resilience (CWSR) I agree to work collaboratively and inclusively with other members to forward the purpose of the Centre in delivering Whole Society Resilience. Specifically, I will endeavour to:</p>
      <ol>
        <li>participate in dialogue that promotes and enhances the centre on social media and at industry events;</li>
        <li>be willing to host a CWSR meeting if you have appropriate facilities;</li>
        <li>contribute to discussion forums, papers, articles or projects with other members.</li>
      </ol>
      <p class="charter__foot">Questions? Contact us at <a class="link" href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>
</section>'''


def page(path, title, desc, active, body, join=True):
    depth = path.count('/')
    P = '../' * depth
    full_title = title if title.startswith('Centre for') else f'{title} · Centre for Whole of Society Resilience'
    html = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#12261f">
<link rel="canonical" href="{SITE}/{'' if path == 'index.html' else path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Centre for Whole of Society Resilience">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" type="image/png" href="{P}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{P}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..600,0..100;1,9..144,300..600,0..100&family=IBM+Plex+Mono:wght@400;500;600&family=Public+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{P}assets/css/styles.css">
</head>
<body>
{header(active, P)}
<main id="main">
{body.replace('{{P}}', P).replace('{{ARROW}}', ARROW).replace('{{OUT}}', OUT_ICON).replace('{{FORM}}', FORM).replace('{{EMAIL}}', EMAIL).replace('{{LINKEDIN}}', LINKEDIN)}
{join_band(P) if join else ''}
</main>
{footer(P)}
</body>
</html>
'''
    dest = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, 'w') as f:
        f.write(html)


# --------------------------------------------------------------------------
# News data (copy carried over from the original site)
# --------------------------------------------------------------------------

POSTS = [
    dict(slug="members-day-2026", tag="Event", date="2 September 2026", short="2 Sep 2026", author="Stefano Piscitelli", read="1 min read",
         title="Save the Date: CWSR Members’ Day 2026",
         summary="Thursday 15 October 2026 · London. CWSR Members’ Day returns, bringing together members from across sectors to explore this year’s theme of human-centred resilience."),
    dict(slug="annual-resilience-statement-2026", tag="Insight", date="15 July 2026", short="15 Jul 2026", author="Caroline Field", read="6 min read",
         title="The annual resilience statement: what progress matters most for a whole-of-society approach?",
         summary="The key question is not simply what activity has been announced, but whether the UK is becoming better at building resilience as a genuinely whole-of-society capability."),
    dict(slug="resilient-leaders-programme-cohort-2", tag="Programme", date="23 April 2026", short="23 Apr 2026", author="Zoe Yap", read="2 min read",
         title="Sign up to be a part of Resilient Leaders Programme Cohort 2!",
         summary="CWSR is excited to announce the launch of our second Resilient Leaders Programme for Resilience Professionals."),
    dict(slug="measuring-resilience-webinar", tag="Webinar", date="18 February 2026", short="18 Feb 2026", author="Zoe Yap", read="1 min read",
         title="Measuring Resilience Webinar (11th February 2026)",
         summary="A panel spanning government, rail, international standards, academia and consulting on how resilience can be measured and linked to outcomes."),
]
BY = {p['slug']: p for p in POSTS}


def card(p, P, lead=False):
    return f'''<a class="card{' card--lead' if lead else ''} reveal" href="{P}news/{p['slug']}.html">
        <div class="card__meta"><span class="card__tag">{p['tag']}</span><span>{p['short']}</span></div>
        <h3>{p['title']}</h3>
        <p>{p['summary']}</p>
        <span class="card__more">Read {'the piece' if lead else 'more'} {ARROW}</span>
      </a>'''


# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------

ICON_SHIFT = '<svg class="pillar__icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M8 44c10 0 14-24 26-24s14 12 22 12"/><circle cx="8" cy="44" r="3" fill="currentColor"/><path d="M50 26l6 6-6 6"/></svg>'
ICON_SYSTEM = '<svg class="pillar__icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="32" cy="32" r="6"/><circle cx="12" cy="14" r="4"/><circle cx="52" cy="14" r="4"/><circle cx="12" cy="50" r="4"/><circle cx="52" cy="50" r="4"/><path d="M15 17l12 11M49 17 37 28M15 47l12-11M49 47 37 36M16 14h32M16 50h32"/></svg>'
ICON_SHARED = '<svg class="pillar__icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="24" cy="32" r="16"/><circle cx="40" cy="32" r="16"/><circle cx="32" cy="32" r="3" fill="currentColor"/></svg>'

home = f'''<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <span class="eyebrow">Centre for Whole of Society Resilience</span>
      <h1>Empowering <em>whole of society</em> resilience</h1>
      <p class="lede">Building a resilient future, together. We connect the people who study resilience, deliver it, shape it and live with its consequences.</p>
      <div class="hero__actions">
        <a class="btn btn--gold" href="{{{{P}}}}join.html">Become a member · it's free {{{{ARROW}}}}</a>
        <a class="btn btn--ghost" href="{{{{P}}}}about.html">About the Centre</a>
      </div>
      <div class="hero__meta">
        <span><strong>200+</strong> members</span>
        <span><strong>Transdisciplinary</strong> network</span>
        <span><strong>UK</strong> resilience framework</span>
      </div>
    </div>
    <div class="hero__visual" aria-hidden="false">
{NET}
    </div>
  </div>
</section>

<section class="section section--ink" aria-labelledby="hc-title">
  <div class="wrap">
    <div class="statement">
      <div class="statement__mark"><span class="eyebrow" id="hc-title">Our purpose</span></div>
      <div>
        <blockquote class="reveal">Whole of Society Resilience means that everyone, at every level of the system, works together to build a <em>thriving, adaptive and sustainable</em> society.</blockquote>
        <div class="statement__body reveal">
          <p><strong style="color:var(--paper)">We champion human-centred resilience.</strong> That means putting people — their needs, behaviours, relationships, agency and lived experience — at the heart of every system.</p>
          <p>It means helping people feel empowered to take action within their own circle of influence, while connecting research, practice, policy and lived experience to build resilience that is more human, more joined-up and more effective.</p>
        </div>
      </div>
    </div>

    <div class="quad">
      <div class="quad__item reveal"><span class="quad__num">01</span><h3>Who study it</h3><p>Researchers and academics building the evidence base.</p></div>
      <div class="quad__item reveal"><span class="quad__num">02</span><h3>Who deliver it</h3><p>Practitioners, consultants and resilience professionals.</p></div>
      <div class="quad__item reveal"><span class="quad__num">03</span><h3>Who shape it</h3><p>Policymakers and leaders across government and industry.</p></div>
      <div class="quad__item reveal"><span class="quad__num">04</span><h3>Who live with it</h3><p>Communities, households and the people resilience is for.</p></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="approach-title">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="approach-title">How we <em>think</em> about resilience</h2>
      <p class="muted">It includes, but goes way beyond, the more traditional understanding of resilience as preparedness for adversity and responding to shock events.</p>
    </div>
    <div class="pillars">
      <article class="pillar reveal">
        <div><div class="pillar__num">01</div>{ICON_SHIFT}</div>
        <h3>A mindset shift</h3>
        <div class="pillar__body">
          <p class="pillar__lead">Whole Society Resilience requires a radical shift in mindset from a reactive to a proactive stance — a collaborative approach that breaks down silos and empowers community-led resilience initiatives.</p>
          <p>It involves empowering people to respond effectively and collaboratively to complex challenges. To make sense of the deluge of data and information in a way that is purposeful and leads towards greater human, societal and planetary wellbeing.</p>
        </div>
      </article>
      <article class="pillar reveal">
        <div><div class="pillar__num">02</div>{ICON_SYSTEM}</div>
        <h3>A whole system approach</h3>
        <div class="pillar__body">
          <p class="pillar__lead">A whole system approach, underpinned by (complex) systems thinking, that connects the human, personal and social world with the technical, political and environmental ‘wicked’ challenges facing societies and our planet.</p>
          <p>The unique contribution of the Centre is to deliberately bring together such capabilities — including the measurement models and data that inform them — to support and enhance the work that emerges from this ‘silo-busting’ approach.</p>
          <p>We do this through innovative, industry-led projects and leadership and learning programmes which explore, model and advance a whole of society approach to resilience at multiple levels. We are developing a digital infrastructure to capture, model and analyse data so it can be used effectively for leadership decision-making for whole of society and place-based resilience policies.</p>
        </div>
      </article>
      <article class="pillar reveal">
        <div><div class="pillar__num">03</div>{ICON_SHARED}</div>
        <h3>A shared understanding</h3>
        <div class="pillar__body">
          <p class="pillar__lead">We promote a shared understanding of our purpose, shocks, stresses, opportunities and interdependencies.</p>
          <p>The Centre provides an independent hub that holds the creative tension between the differing and often competing values and lifecycles of research, policy, practice, commerce and digital innovation.</p>
          <p>We procure and promote projects and programmes that contribute new knowledge and know-how to the whole of society, including the most disadvantaged.</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--paper2" aria-labelledby="members-title">
  <div class="wrap stats">
    <div class="reveal">
      <div class="bignum">200<sup>+</sup></div>
      <div class="bignum-label">Members across the network</div>
    </div>
    <div class="reveal">
      <span class="eyebrow">Our members</span>
      <h2 id="members-title">A network broad enough to <em>join the dots</em>.</h2>
      <p class="muted">Our transdisciplinary members span industries from the public sector, defence and transport to NGOs, education and cybersecurity. This breadth is critical to join the dots and share insights to improve societal resilience.</p>
      <ul class="chips">
        <li>Public sector</li><li>Defence</li><li>Transport</li><li>NGOs</li><li>Education</li><li>Cybersecurity</li><li>Consulting</li><li>Academia</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="rlp-title">
  <div class="wrap">
    <div class="feature reveal">
      <div class="feature__body">
        <span class="eyebrow">Leadership &amp; learning</span>
        <h2 id="rlp-title">The Resilient Leaders Programme</h2>
        <p>Building resilience requires a proactive, systems-focused leadership approach that empowers communities and organisations to take ownership. This programme develops the leadership capabilities and mindsets needed to embed resilience across the system and deliver lasting change.</p>
        <p>Delivered by PA and Leading4Change, both accredited Resilient Leaders Consultants, for resilience professionals across central government, local government, business and the voluntary sector.</p>
        <p style="margin-top:28px"><a class="btn btn--gold" href="{{{{P}}}}news/resilient-leaders-programme-cohort-2.html">About the programme {{{{ARROW}}}}</a></p>
      </div>
      <div class="feature__side">
        <dl class="feature__facts">
          <div><dt>Duration</dt><dd>14 weeks</dd></div>
          <div><dt>Cohort size</dt><dd>12 leaders</dd></div>
          <div><dt>Cohort 1 growth</dt><dd>11% overall</dd></div>
          <div><dt>Highest growth</dt><dd>40%+</dd></div>
        </dl>
        <blockquote>“Inspiring, informative, grounding… enabled some deep self-reflection which was incredibly welcome.”</blockquote>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper2" aria-labelledby="news-title">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="news-title">Latest from the Centre</h2>
      <p class="muted">Events, programmes and perspectives on the UK’s resilience agenda. <a class="link" href="{{{{P}}}}news.html">All news</a></p>
    </div>
    <div class="cards">
      {card(BY['annual-resilience-statement-2026'], '{{P}}', lead=True)}
      {card(BY['members-day-2026'], '{{P}}')}
    </div>
    <div class="cards cards--2" style="margin-top:24px">
      {card(BY['resilient-leaders-programme-cohort-2'], '{{P}}')}
      {card(BY['measuring-resilience-webinar'], '{{P}}')}
    </div>
  </div>
</section>
'''
# home was built as an f-string, so the {{P}} placeholders were doubled to survive; normalise them
home = home.replace('{{{{', '{{').replace('}}}}', '}}')

page('index.html', 'Centre for Whole of Society Resilience (CWSR)',
     'A transdisciplinary network joining the dots between research, practice, policy and lived experience to build whole of society resilience.',
     'index.html', home)

# --------------------------------------------------------------------------
# About
# --------------------------------------------------------------------------

def li(url, name):
    return f'<a class="link" href="https://www.linkedin.com/in/{url}/" rel="noopener">{name}’s LinkedIn</a>'

founders = [
    ("ruth-crick", "Prof. Ruth Crick", "Co-Founder", [
        "Ruth is Founder of WILD Learning Sciences CIC and WILD Learning Ltd. She has held leadership roles in research, practice, policy and enterprise with a common focus on the development of competence in self-leadership, learning relationships and complex problem solving for individuals, teams and organisations.",
        "Ruth brings extensive thought leadership based on 25 years of research into dispositional learning analytics at the University of Bristol and the Connected Intelligence Centre at UTS in Sydney. This provides the evidence base for Work Integrated Learning Design (WILD) as a digital learning infrastructure which scaffolds, develops and measures personal and team resilience. Her work has spanned business, education and community in projects around the world. The Crick Learning for Resilient Agency profile was published in 2015 and has been translated into several languages."],
     '<a class="link" href="mailto:ruth.crick@wildlearn.co.uk">ruth.crick@wildlearn.co.uk</a>'),
    ("caroline-field", "Prof. Caroline Field, CEng FICE", "Co-Founder &amp; Executive Director", [
        "Caroline works in industry leading National Resilience at PA Consulting, helping clients develop and deliver resilience strategies whilst providing a framework for measuring the benefits.",
        "Caroline brings expertise in resilient leadership and decision making — catalysing behaviour change in organisations and communities to deliver greater resilience. She is accredited in resilient leadership and has expertise in systems-based decision making to de-silo and prioritise resilience building efforts — understanding interdependencies and linking resilience to measured strategic outcomes.",
        "Caroline is a Royal Academy of Engineering Visiting Professor of Structural and Infrastructural Resilience at Loughborough University, linking research and practice and helping to shape the future of the profession."],
     li("caroline-field-21185921", "Caroline")),
    ("adeela-shafi", "Prof. Adeela Shafi, MBE", "Co-Founder", [
        "Adeela is Professor of Education at the University of Gloucestershire in Youth Justice with a particular interest in resilience, as well as how diversity in thought, research and leadership contributes to the best outcomes for individuals, communities and society as a whole.",
        "Adeela is accustomed to leading large multi-national research projects from international funders like the EU and the British Council involving multiple countries. These bring together academics, practitioners, policymakers and industry leaders to inform both policy and impact on practice.",
        "Adeela brings the academic network and expertise to CWSR that are needed in order to bring together whole society resilience-building. She was awarded an MBE in 2020 for services to social justice and academia."],
     '<a class="link" href="mailto:ashafi@glos.ac.uk">ashafi@glos.ac.uk</a>'),
]

committee = [
    ("richard-smith-bingham", "Richard Smith-Bingham", "Chair", [
        "Richard is the new Chair of CWSR. He has deep expertise in global risks and resilience, shaped by many years at Marsh McLennan, where he advised multinational businesses and countries on how to get ahead of disruptive trends and possible crises. Richard now provides independent, targeted challenge and strategic support to leaders in government and the private sector so they can better align strategic priorities and pressing resilience demands.",
        "As well as being a specialist in the implications of intersecting risks, he brings fresh perspectives on organisational and systemic resilience practices, decision-making under uncertainty, and oversight arrangements, helping leadership teams embed approaches that are forward-looking, adaptive and durable. Richard is a commissioner on the National Preparedness Commission, for whom he has recently issued a report on how the UK can strengthen supply chain resilience for critical materials, components and goods."],
     li("richard-smith-bingham", "Richard")),
    ("claire-crichton-allen", "Claire Crichton-Allen", "Operations Director", [
        "Claire is a change readiness and learning resilience expert who helps people and organisations perform well through uncertainty, complexity and rapid change.",
        "She strengthens agency, confidence and adaptability, turning ambiguity into clear priorities and practical action. Her approach blends strategic rigour with human-centred leadership, building resilient cultures that sustain momentum.",
        "As an Educational Strategist, Sustainability Advocate and Researcher at the University of Strathclyde, Claire translates leading pedagogical research into innovative learning design that embeds sustainability competencies for real-world impact."],
     li("claire-crichton-allen", "Claire")),
    ("wendy-tipper", "Wendy Tipper", "Learning &amp; Development Director", [
        "Wendy has recently joined CWSR as Learning &amp; Development Director, where she leads the L&amp;D programme of activities, including the Resilient Leadership Development Programme (RLDP) for resilience professional development. An accredited Resilient Leadership Consultant with over 30 years’ cross-sector experience, Wendy specialises in building leadership capability, resilience and strategic effectiveness.",
        "Drawing on senior roles including Associate Director at Arup, she brings deep expertise in transformation and people development across complex organisations. Wendy is also a judge for the Management Consultancies Association Awards, assessing excellence in leadership and people, and brings a human-centred, systems-thinking approach to enabling sustainable, purpose-driven leadership."],
     li("wendy-tipper", "Wendy")),
    ("phoebe-andrew", "Phoebe Andrew", "Marketing &amp; Comms Director", [
        "Phoebe is Head of Place-Based Solutions at the Centre for Energy Equality and a Director of Looped Energy Communities CIC. She specialises in engineering design and systems thinking, leading multi-stakeholder innovation projects that tackle energy inequality and accelerate community-led approaches to decarbonisation."],
     li("phoebe-andrew", "Phoebe")),
    ("tim-norton", "Tim Norton", "Projects Director", [
        "Tim is Head of Rail Resilience at the Department for Transport and has extensive experience in public sector resilience. A hydrologist by background, he spent much of his career focusing on flood resilience.",
        "He is interested in how resilience can make tangible differences, linking strategic developments to practical improvements, working across organisational and sector boundaries, and joining professional and community resilience."],
     li("tim-norton-a8437b18b", "Tim")),
    ("nadine-sulkowski", "Nadine Sulkowski", "Partnerships Director", [
        "Nadine is a Senior Lecturer in Systemic Resilience Management at the University of Gloucestershire and a Fellow of the Institute of Strategic Risk Management. She has extensive experience in international collaborations and multi-stakeholder partnerships.",
        "Nadine has contributed significantly to higher education governance structures, leading notable projects such as the Erasmus+ capacity building project “BUiLD”, which established a systemic disaster resilience framework and Centres of Excellence across Indonesia. As part of the Erasmus+ empowerment4pandemias project, she has designed an organisational pandemic resilience framework for the healthcare sector.",
        "Nadine teaches resilience planning and crisis management, focusing on enhancing systemic resilience and effective crisis communication, and aims to inspire students to become future change agents and innovators."],
     li("nadine-sulkowski", "Nadine")),
]

def bio(paras):
    return "".join(f"<p>{p}</p>" for p in paras)

founders_html = "\n".join(f'''      <article class="person reveal">
        <div class="person__photo"><img src="{{{{P}}}}assets/img/team/{slug}.jpg" alt="Portrait of {name.split(',')[0]}" loading="lazy" width="480" height="480"></div>
        <div class="person__role">{role}</div>
        <h3>{name}</h3>
        <div class="person__bio">{bio(paras)}</div>
        <div class="person__links">{link}</div>
      </article>''' for slug, name, role, paras, link in founders)

committee_html = "\n".join(f'''      <article class="member reveal">
        <div class="member__photo"><img src="{{{{P}}}}assets/img/team/{slug}.jpg" alt="Portrait of {name}" loading="lazy" width="480" height="480"></div>
        <div>
          <div class="person__role">{role}</div>
          <h3>{name}</h3>
          <div class="person__links">{link}</div>
        </div>
        <div class="member__bio">{bio(paras)}</div>
      </article>''' for slug, name, role, paras, link in committee)

about = f'''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{{{{P}}}}index.html">Home</a> / About</div>
    <h1>Joining the dots between <em>research, practice and policy</em>.</h1>
    <p class="lede">Welcome to the Centre for Whole of Society Resilience (CWSR) — a transdisciplinary network working to deliver whole of society resilience.</p>
  </div>
  <img class="page-hero__mark" src="{{{{P}}}}assets/img/logo-mark.png" alt="">
</section>

<section class="section">
  <div class="wrap intro-grid">
    <p class="big reveal">We are a transdisciplinary network of consultants, business leaders, academics and practitioners who have come together to advance research-informed resilience policy and practice.</p>
    <div class="body reveal">
      <p>Our aim is to build long-term whole of society resilience, as outlined in the UK government’s resilience framework (UKGRF).</p>
      <p>We aim to do this through creating a network of passionate professionals who want to work collaboratively to solve this challenge together. We are funded through delivering innovative projects that address these challenges by harnessing the immense capability of our network and developing teams with the right expertise to contribute to the issue at hand.</p>
      <p>If you are passionate about resilience and have some skills to offer — <a class="link" href="{{{{P}}}}join.html">please join our network</a>.</p>
    </div>
  </div>
</section>

<section class="section section--paper2" id="people" aria-labelledby="founders-title">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="founders-title">Our founders</h2>
      <p class="muted">Three professors bridging industry, academia and practice, who established the Centre to bring whole society resilience-building together.</p>
    </div>
    <div class="founders">
{founders_html}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="sc-title">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="sc-title">Our steering committee</h2>
      <p class="muted">The steering committee guides the Centre’s direction, programmes, partnerships and communication with members. <a class="link" href="{{{{P}}}}governance.html#terms">Terms of Reference</a></p>
    </div>
    <div class="committee">
{committee_html}
    </div>
  </div>
</section>

<section class="section section--paper2 section--tight" aria-labelledby="mem-title">
  <div class="wrap stats">
    <div class="reveal">
      <div class="bignum">200<sup>+</sup></div>
      <div class="bignum-label">Members and growing</div>
    </div>
    <div class="reveal">
      <span class="eyebrow">Our members</span>
      <h2 id="mem-title">Breadth is the point.</h2>
      <p class="muted">The Centre for Whole of Society Resilience has a transdisciplinary network of over 200 members, spanning a number of industries from the public sector, defence and transport to NGOs, education and cybersecurity. This breadth is critical to join the dots and share insights to improve societal resilience. Join our growing network!</p>
    </div>
  </div>
</section>
'''.replace('{{{{', '{{').replace('}}}}', '}}')

page('about.html', 'About', 'Founders, steering committee and members of the Centre for Whole of Society Resilience.', 'about.html', about)

# --------------------------------------------------------------------------
# News index
# --------------------------------------------------------------------------

news = f'''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{{{{P}}}}index.html">Home</a> / News</div>
    <h1>News &amp; <em>insight</em></h1>
    <p class="lede">Events, programmes and perspectives on building resilience as a genuinely whole-of-society capability.</p>
  </div>
  <img class="page-hero__mark" src="{{{{P}}}}assets/img/logo-mark.png" alt="">
</section>
<section class="section section--tight">
  <div class="wrap">
    <div class="cards">
      {card(POSTS[0], '{{P}}', lead=True)}
      {card(POSTS[1], '{{P}}')}
    </div>
    <div class="cards cards--2" style="margin-top:24px">
      {card(POSTS[2], '{{P}}')}
      {card(POSTS[3], '{{P}}')}
    </div>
  </div>
</section>
'''.replace('{{{{', '{{').replace('}}}}', '}}')
page('news.html', 'News', 'News, events and insight from the Centre for Whole of Society Resilience.', 'news.html', news)

# --------------------------------------------------------------------------
# Articles
# --------------------------------------------------------------------------

def article(p, body_html):
    idx = POSTS.index(p)
    newer = POSTS[idx - 1] if idx > 0 else None
    older = POSTS[idx + 1] if idx + 1 < len(POSTS) else None
    nav = '<nav class="post-nav" aria-label="More posts">'
    nav += f'<a class="link" href="{{{{P}}}}news/{older["slug"]}.html">← {older["title"]}</a>' if older else '<span></span>'
    nav += f'<a class="link" href="{{{{P}}}}news/{newer["slug"]}.html">{newer["title"]} →</a>' if newer else ''
    nav += '</nav>'
    body = f'''<section class="article-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{{{{P}}}}index.html">Home</a> / <a href="{{{{P}}}}news.html">News</a> / {p['tag']}</div>
    <h1>{p['title']}</h1>
    <div class="article-meta"><span><strong>{p['date']}</strong></span><span>By {p['author']}</span><span>{p['read']}</span></div>
  </div>
</section>
<div class="wrap">
  <article class="article">
    <div class="prose">
{body_html}
    {nav}
    </div>
  </article>
</div>
'''.replace('{{{{', '{{').replace('}}}}', '}}')
    page(f"news/{p['slug']}.html", p['title'], p['summary'].replace('"', '&quot;'), 'news.html', body)


article(BY['members-day-2026'], '''      <div class="callout"><p><strong>Thursday 15 October 2026</strong></p><p>London · 10.00am to 4.00pm</p></div>
      <p class="first">CWSR Members’ Day returns this October, bringing together members from across sectors to explore this year’s theme of <strong>human-centred resilience</strong>.</p>
      <p>The day will look at resilience across individuals, households, organisations and communities, and what this means for how we prepare, respond and work together.</p>
      <p>Members can expect a mix of external perspectives, discussion and practical reflection, with plenty of opportunity to share experience, challenge thinking and help shape the future direction of CWSR.</p>
      <p>We are currently confirming speakers and contributors, with the full programme to follow shortly.</p>
      <h2>Help shape the conversation</h2>
      <p>We want the day to reflect the priorities of our members. As part of registration, we are asking:</p>
      <ul>
        <li>What issue or challenge relating to human-centred resilience would you most like Members’ Day to explore?</li>
        <li>Is there an example, experience, person or piece of work that other CWSR members could learn from?</li>
      </ul>
      <p>Your responses will help us shape the programme and focus the discussion on the issues that matter most.</p>
      <p>Places are limited, so members are encouraged to <a href="https://url.uk.m.mimecastprotect.com/s/K0wTCxGoZH365BKUvhEEiy9IC9?domain=docs.google.com" rel="noopener">register their interest here</a>.</p>
      <p>Not yet a CWSR member? Find out more about the network and <a href="{{P}}join.html">how to get involved</a>.</p>''')

article(BY['annual-resilience-statement-2026'], '''      <p class="first">Today’s annual resilience statement to Parliament offers an important opportunity to take stock of the UK’s progress on resilience. From the perspective of the Centre for Whole of Society Resilience, the key question is not simply what activity has been announced, but whether the UK is becoming better at building resilience as a genuinely <strong>whole-of-society capability</strong>.</p>
      <p>That means resilience that is not confined to central government or emergency planning structures, but is shared across <strong>households, communities, civil society, businesses, local systems and national institutions</strong>. It means connecting policy to practice, and ensuring that resilience is not only planned for, but also understood, measured and enabled across society.</p>
      <p>The government’s latest statement and implementation report suggest a positive direction of travel. The Resilience Action Plan continues to be organised around three core objectives: to <strong>continuously assess how resilient the UK is</strong>, to <strong>enable the whole of society to take action</strong>, and to <strong>strengthen the public sector resilience system</strong>. Several elements of this year’s statement are particularly relevant to the Centre’s work.</p>

      <h2>Measuring resilience more meaningfully</h2>
      <p>One of the most important developments is the growing focus on how resilience is actually measured.</p>
      <p>For too long, national readiness has often been judged through partial proxies: the existence of plans, the speed of response, or assessments of capability after a crisis has already occurred. What has been missing is a clearer, more consolidated picture of how resilient the UK is <em>before</em> shocks happen.</p>
      <p>That is why the government’s emphasis on continuously assessing resilience is so important. If resilience is to be improved strategically, it must be measured in a way that captures the relationship between <strong>individual and household preparedness, community and local capacity, and wider national and systemic factors</strong>. Without that, it is difficult to know where vulnerability sits, where investment is most needed, and whether policy is improving resilience over time.</p>
      <p>This is an area of particular importance to the Centre. <strong>Caroline Field</strong> has been leading the Cabinet Office working group on measuring whole-of-society resilience, and as an <strong>Affiliate of the UK Resilience Academy</strong>, the Centre welcomes the collaborative work now under way to strengthen standards, capability and learning across the system. The implementation report also highlights the UK Resilience Academy’s role in revising and expanding National Occupational Standards, alongside work to update the National Resilience Standards for Local Resilience Forums later this year.</p>
      <p>The opportunity now is to ensure that this work remains genuinely whole-system in nature. A resilience baseline must not become a narrow technical exercise. It should illuminate not only institutional readiness, but also local networks, public confidence, social and economic vulnerability, and the community conditions that shape resilience in practice.</p>

      <h2>Public preparedness is becoming more visible</h2>
      <p>A second encouraging area of progress is the stronger emphasis on public preparedness.</p>
      <p>The annual statement confirms plans for a <strong>multi-year public information campaign</strong> to support new household advice on preparing for disruption and emergencies, focused on simple steps people can take to improve their resilience. The implementation report adds that this campaign is being developed in collaboration with civil society organisations, will include resources for schools, colleges, and children and young people, and will sit alongside further development of <a href="https://www.gov.uk/prepare" rel="noopener">GOV.UK/Prepare</a>.</p>
      <p>This matters because a whole-of-society approach depends on resilience being something people can understand and act on in everyday life. Preparedness cannot remain the preserve of specialists.</p>
      <p>This also connects directly to the Centre’s wider perspective. <strong>Ruth Crick’s research</strong> highlights a vital principle: people only change their behaviour when change is <strong>meaningful to them</strong>. That insight is highly relevant to resilience. If preparedness is framed only in abstract or technical terms, it is unlikely to generate action. Resilience needs to connect with what people value in everyday life: safety, continuity, wellbeing, fairness and belonging.</p>
      <blockquote>Building whole-of-society resilience requires a “profound cultural and behavioural change” informed by robust social and behavioural science evidence.</blockquote>
      <p>The implementation report itself recognises this — an important acknowledgement. The next step is to ensure that public communication on resilience is not only clear, but also meaningful and achievable for people in very different circumstances.</p>

      <h2>Cross-system exercising and preparedness are strengthening</h2>
      <p>The annual statement and implementation report also point to significant progress in exercising and preparedness.</p>
      <p>Most notably, the government reports that it has delivered <strong>Exercise PEGASUS</strong>, described as the largest national pandemic scenario exercise in UK history. Across its core exercise days, PEGASUS brought together UK government departments, devolved governments, arm’s-length bodies and Local Resilience Forums, while also engaging businesses, voluntary, community and faith sector organisations, academics and other external stakeholders. The annual statement similarly highlights PEGASUS as the largest Tier 1 pandemic exercise in UK history.</p>
      <p>This matters because resilience is not built only through plans and frameworks. It is also built through rehearsal, relationships and the ability to work across boundaries under pressure. Exercises that include not only government but also wider society are much more consistent with a whole-of-society model of resilience.</p>
      <p>The same is true of the <strong>Home Defence Programme</strong>, which the statement says includes revitalisation of the government warbooks, accelerated departmental planning and an intention to deliver a Tier 1 national exercise on Home Defence in 2027. The implementation report presents this as closer integration across government, industry and society, embedding resilience and a whole-of-society approach.</p>

      <h2>Leadership capability remains essential</h2>
      <p>If resilience is to be shared across society, leadership capability matters just as much as structures.</p>
      <p>A resilient system depends on people who can work across organisational boundaries, navigate uncertainty, build trust and lead collaboratively through adversity and change. Those are not secondary qualities; they are central to whether systems adapt effectively when facing disruption.</p>
      <p>This is why the Centre places such emphasis on leadership development. The Centre’s <a href="{{P}}news/resilient-leaders-programme-cohort-2.html">Resilient Leaders Programme</a> reflects the kind of support that is needed more widely across the system: helping resilience professionals lead proactively and collaboratively rather than simply react to events. If resilience is to become embedded across institutions and places, leadership development needs to sit alongside technical capability, standards and doctrine.</p>
      <p>The growing role of the <strong>UK Resilience Academy</strong>, including its contribution to standards and capability-building, is therefore welcome. The next phase should go further in recognising that whole-of-society resilience requires leadership at every level: national, regional, local, organisational and community.</p>

      <h2>Communities need scaffolding, not just recognition</h2>
      <p>For the Centre, one of the most important tests of a whole-of-society approach is whether communities and civil society are being properly enabled to contribute.</p>
      <p>The implementation report contains several encouraging signs. It highlights work to strengthen partnership working with the <strong>voluntary, community and faith sector</strong>, including guidance developed collaboratively with VCFS organisations, and a <strong>Civil Society Resilience Infrastructure Fund</strong> of up to £2.5 million to support civil society infrastructure in England. It also notes the introduction of <strong>five Chief Resilience Officers as part of the Stronger LRF Trailblazer programme</strong>.</p>
      <p>These developments matter because community resilience does not happen by rhetoric alone. It needs what we often describe as <strong>scaffolding</strong>: coordination, convening, information-sharing, trusted relationships and practical empowerment.</p>
      <p>This is where <strong>Chief Resilience Officers in Local Resilience Forums</strong> can play a particularly important role. Done well, they can provide the scaffolding that allows communities to contribute effectively, linking local capability and local knowledge with formal planning and response arrangements. That is essential if resilience is to be built with communities, not simply for them.</p>

      <h2>A positive direction — with implementation now the test</h2>
      <p>Overall, this year’s annual resilience statement points to a resilience agenda that is becoming more systemic, more evidence-led and more open to whole-of-society thinking. The updated <strong>National Risk Register</strong>, published with accompanying guidance to make it more user-friendly and to situate it in local context, is another example of this wider shift.</p>
      <p>From the perspective of the Centre for Whole of Society Resilience, the most meaningful progress is progress that helps connect the dots:</p>
      <ul class="connect-list">
        <li><span>Measurement</span><i></i><span>Action</span></li>
        <li><span>Leadership</span><i></i><span>Delivery</span></li>
        <li><span>Risk information</span><i></i><span>Public meaning</span></li>
        <li><span>Community capability</span><i></i><span>Formal coordination</span></li>
      </ul>
      <p>The next phase is now about implementation. Resilience will not be built by statements alone. It will be built when evidence shapes decisions, when leadership is developed at every level, when communities are properly enabled to act, and when resilience becomes meaningful in the lives of the people it is intended to protect.</p>
      <p><strong>That is the test of a truly whole-of-society approach.</strong></p>''')

article(BY['resilient-leaders-programme-cohort-2'], '''      <p class="first">The Centre for Whole of Society Resilience (CWSR) is excited to announce the launch of our second Resilient Leaders Programme for Resilience Professionals.</p>
      <p>In a world shaped by unpredictability, the role of resilient leaders has never been more critical. The UK Government’s resilience framework and action plan signal a shift from emergency response to whole-society resilience, with every part of the national ecosystem playing a role. Chief Resilience Officers and resilience professionals are central to driving this change and must be equipped with the right mindsets, skills and peer support.</p>
      <p>While traditional crisis response remains essential, it is no longer sufficient. Building resilience requires a proactive, systems-focused leadership approach that empowers communities and organisations to take ownership. This programme develops the leadership capabilities and mindsets needed to embed resilience across the system and deliver lasting change, and is delivered by PA and Leading4Change, both accredited Resilient Leaders Consultants.</p>
      <p>We recently completed the first cohort of the programme with resilience professionals from across central government, local government, business and voluntary sectors. Participants described their experience as:</p>
      <blockquote>“Inspiring, informative, grounding… enabled some deep self-reflection which was incredibly welcome.” “Transformative.”</blockquote>
      <p>The overall cohort growth was <strong>11% across the board</strong>, with highest growth (<strong>40%+</strong>) in determination, strategic intent and personal resilience.</p>
      <h2>Proposed dates</h2>
      <p>The programme extends across <strong>14 weeks</strong>.</p>
      <ul class="schedule">
        <li><b>08/09/26</b><span>Briefing (online), 09:30 · 90 mins</span></li>
        <li><b>22/09/26</b><span>In person, 1 day, 10:00–17:00 · PA Offices Victoria (essential attendance)</span></li>
        <li><b>w/c 29/09/26</b><span>1-2-1 one-hour coaching session, to suit your schedule</span></li>
        <li><b>06/10 · 20/10</b><span>Online development sessions, 09:30–11:30</span></li>
        <li><b>03/11/26</b><span>Hybrid mid-point check-in and guest lecture, 09:30–12:30</span></li>
        <li><b>17/11 · 01/12</b><span>Online development sessions, 09:30–11:30</span></li>
        <li><b>15/12/26</b><span>In person finale, 10:00–17:00 · PA Offices Victoria (essential attendance)</span></li>
      </ul>
      <div class="callout">
        <p><strong>Cost:</strong> £1,975 + VAT per person</p>
        <p>The programme is limited to 12 individuals and is expected to fill up quickly. If interested, please contact <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>.</p>
      </div>''')

article(BY['measuring-resilience-webinar'], '''      <p class="first">On Wednesday 11th February, the CWSR held a webinar on Measuring Resilience, featuring a panel including:</p>
      <ul>
        <li><strong>Anjali Gurung</strong>, Economist at the Department for Business and Trade</li>
        <li><strong>Lynnda Nelson</strong>, President of The International Consortium for Organizational Resilience (ICOR)</li>
        <li><strong>Nadine Sulkowski</strong>, Senior Lecturer in Systemic Resilience Management at the University of Gloucestershire</li>
        <li><strong>Caroline Field</strong>, PA Consulting and Co-Founder of CWSR</li>
        <li><strong>Aaron Gracey</strong>, Transport Resilience Professional</li>
      </ul>
      <p>Anjali Gurung from the Department for Business and Trade provided a government perspective on measuring resilience, explaining the importance of measuring resilience in government decision-making, highlighting the challenges of quantifying resilience benefits and the development of new guidance with Caroline and their team to address these gaps. Dr Aaron Gracey, Lynnda Nelson, Nadine Sulkowski and Caroline Field provided focused inputs from their respective industries.</p>
      <p><strong>Dr Aaron Gracey</strong> from Network Rail outlined the organisation’s systemic approach to measuring and embedding resilience, focusing on cultural change, cross-departmental collaboration, and the development of operational tools and frameworks.</p>
      <p><strong>Lynnda Nelson</strong> from the International Consortium for Organisational Resilience presented a comprehensive framework for assessing organisational resilience, focusing on dimensions, strategies, capabilities and behaviours, and discussed practical assessment methods and tools.</p>
      <p><strong>Nadine Sulkowski</strong> from the University of Gloucestershire discussed the Empowerment for Pandemias project, which developed a pandemic resilience training programme and maturity model for the healthcare sector, focusing on both organisational and individual resilience.</p>
      <p><strong>Caroline Field</strong> synthesised the various approaches discussed, presenting a systems-based methodology for measuring resilience that links behaviours, capabilities and interventions to quantifiable outcomes and value at risk.</p>''')

# --------------------------------------------------------------------------
# Join
# --------------------------------------------------------------------------

join = '''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{{P}}index.html">Home</a> / Membership</div>
    <h1>Join a network building a <em>resilient future</em>, together.</h1>
    <p class="lede">Membership is free. If you are passionate about resilience and have some skills to offer, we would love you to join us. Please review our charter below, then complete the member sign-up form.</p>
    <div class="hero__actions" style="margin-top:36px">
      <a class="btn btn--gold" href="{{FORM}}" rel="noopener">Member sign up {{ARROW}}</a>
      <a class="btn btn--ghost" href="mailto:{{EMAIL}}">Email the Centre</a>
    </div>
  </div>
  <img class="page-hero__mark" src="{{P}}assets/img/logo-mark.png" alt="">
</section>
'''
page('join.html', 'Become a member', 'Membership of the Centre for Whole of Society Resilience is free. Meet other resilience professionals, share knowledge and take part in impactful projects.', 'join.html', join)

# --------------------------------------------------------------------------
# Governance
# --------------------------------------------------------------------------

def clauses(sec, items):
    return '<ol class="clauses">' + ''.join(f'<li data-sec="{sec}">{t}</li>' for t in items) + '</ol>'

membership = [
    "Steering Group (SG) members must be members of CWSR.",
    "The inaugural members of the SG are the three Founding Members of CWSR.",
    "The inaugural members will serve an initial term of 3 years, following which they may seek re-appointment to the SG.",
    "At least annually, the membership of CWSR will be given the opportunity to nominate candidates for SG membership for an initial term of 2 years, and existing SG members whose terms are due to expire may seek an additional term of 3 years.",
    "CWSR members will vote to determine which of the new nominees or existing SG members seeking an additional term will be appointed — if there is a sufficient number of vacancies on the SG then all those who receive more votes for than against their membership will be appointed.",
    "There may be a minimum of 3 and a maximum of 5 SG members at any time.",
]
meetings = [
    "SG meetings will be facilitated by a Chair. The inaugural Chair will be Jim Bentley, but any CWSR member may nominate an alternative Chair at any time, to be voted on by the steering committee.",
    "A minimum of two thirds of SG members must be present for a meeting to be quorate.",
    "Attendance at SG meetings will normally be restricted to the SG members and the Chair. SG members may delegate attendance to an agreed surrogate for the purpose of representing the SG members. Other attendees must be agreed by SG members and will normally be limited to participation in a specific agenda item or be a member of the CWSR administration team.",
    "The Chair is responsible for drafting the agenda for SG meetings based on suggestions for agenda items put forward by SG members and will seek approval of SG members for the agenda in advance of the meeting.",
    "The Chair is responsible for facilitating SG meetings in a way in which all SG members can have their say and for allocating time to agenda items so that matters of importance to all SG members are treated fairly.",
    "All SG members are responsible for ensuring that they behave in a way that demonstrates that each member’s opinions are valued.",
    "Decisions will be taken by SG members, not including the Chair, and will be made by consensus rather than by majority voting. Every effort shall be made to reach a consensus but in the event of disagreement, the majority vote shall apply.",
    "Following each meeting the Chair will issue draft minutes to SG members, seeking their feedback, so these can be approved at the subsequent meeting.",
    "Following approval of the minutes the Chair will produce a summary note of the meeting to be shared with CWSR members.",
]
scope = [
    "SG may commit to spending CWSR funds up to the amount held in the bank account at the time of making a decision but may not commit to borrowing money on behalf of the CWSR and may not commit CWSR to future financial obligations.",
    "As CWSR is not a legal entity it does not have a mechanism for entering into contracts either as client or as service provider.",
    "CWSR members or the organisations to which they belong may decide to award contracts or to submit proposals to funding organisations or clients without reference to any other CWSR member, but this cannot be done in the name of CWSR.",
    "Any CWSR member or group of members is entitled to include a statement to the effect that they are members of the CWSR to go with any proposal submission.",
    "The SG may decide that there would be value for CWSR for a proposal to be submitted in the name of the CWSR. For this to happen, the SG must invite expressions of interest from members of CWSR and consider any responses before deciding on the membership and contractual mechanisms and leadership/governance arrangements of any consortium. A recovery of funds to the CWSR should be made on successful award of a contract.",
    "CWSR members who are not part of the CWSR consortium for any proposal are entitled to submit their own proposal for the same opportunity and may refer to their membership of CWSR in their proposal but may not submit on behalf of the CWSR.",
    "SG will be responsible for ensuring that arrangements are in place for regular communication with members, networking and thought leadership events to promote the interests of the members of CWSR.",
    "SG will identify resource requirements and consult with the membership regarding roles to contribute to the administration of the centre. In addition, the SG will consult the membership on focus areas and topics.",
]
rules = ["Promote Positive Engagement", "Uphold Copyright Laws", "Maintain Trust and Authenticity", "Fair Administration", "Kindness Matters"]

gov = f'''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{{{{P}}}}index.html">Home</a> / Governance</div>
    <h1>How the Centre is <em>run</em></h1>
    <p class="lede">The Steering Group Terms of Reference and the guidelines we ask everyone in our community to follow.</p>
  </div>
  <img class="page-hero__mark" src="{{{{P}}}}assets/img/logo-mark.png" alt="">
</section>
<section class="section section--tight">
  <div class="wrap toc-layout">
    <aside class="toc" aria-label="On this page">
      <p>On this page</p>
      <ol>
        <li><a href="#terms">Terms of Reference</a></li>
        <li><a href="#membership">1 · Membership</a></li>
        <li><a href="#meetings">2 · SG meetings</a></li>
        <li><a href="#scope">3 · SG scope</a></li>
        <li><a href="#guidelines">Site guidelines</a></li>
      </ol>
    </aside>
    <div>
      <div class="gov-block" id="terms">
        <span class="eyebrow">Steering Group</span>
        <h2>Centre for Whole of Society Resilience Steering Group — Terms of Reference</h2>
      </div>
      <div class="gov-block" id="membership"><h3>1 · Membership</h3>{clauses(1, membership)}</div>
      <div class="gov-block" id="meetings"><h3>2 · SG meetings</h3>{clauses(2, meetings)}</div>
      <div class="gov-block" id="scope"><h3>3 · SG scope</h3>{clauses(3, scope)}</div>
      <div class="gov-block" id="guidelines">
        <span class="eyebrow">Community</span>
        <h2>Site guidelines</h2>
        <div class="rules">{''.join(f'<div class="rule"><span>#{i}</span><h3>{r}</h3></div>' for i, r in enumerate(rules, 1))}</div>
      </div>
    </div>
  </div>
</section>
'''.replace('{{{{', '{{').replace('}}}}', '}}')
page('governance.html', 'Governance', 'Steering Group Terms of Reference and site guidelines for the Centre for Whole of Society Resilience.', 'governance.html', gov)

# --------------------------------------------------------------------------
# 404
# --------------------------------------------------------------------------

page('404.html', 'Page not found', 'This page could not be found.', '', '''<section class="page-hero" style="border:0">
  <div class="wrap">
    <span class="eyebrow">404</span>
    <h1>This path doesn’t <em>connect</em> anywhere.</h1>
    <p class="lede">The page you were looking for has moved or no longer exists.</p>
    <div class="hero__actions" style="margin-top:36px"><a class="btn" href="/index.html">Back to the homepage {{ARROW}}</a></div>
  </div>
</section>''', join=False)

print("built")
