"""Assemble the CWSR static site. Output is plain HTML committed to the repo.

Copy lives in content.py; layout lives here; styles live in assets/css/styles.css.
Run:  python3 tools/build.py
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import POSTS, BY, founders, committee, ARTICLES, membership, meetings, scope, rules  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..")

FORM = "https://forms.office.com/Pages/ResponsePage.aspx?id=cpq-ajTOTkO78oZ8lo_C139YKKTOPjtGtlPz7X8FWPRUN1pBMTRWQVBHTzdWRE9UQlRVMjhPOFU4Mi4u"
LINKEDIN = "https://www.linkedin.com/groups/12970125/"
EMAIL = "connect@wholesocietyresilience.org"
SITE = "https://www.wholesocietyresilience.org"

ARROW = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ---------------------------------------------------------------- the mark
# One crescent: a circle (r=44) with an equal circle cut away 16 units to its right.
CRES = "M8,-43.27 A44,44 0 1,0 8,43.27 A44,44 0 0,1 8,-43.27 Z"
STRANDS = {  # name: (colour, tint, deep, rotation)
    "blue": ("#7B9CFF", "#E4EAFF", "#3B4C99", 45),
    "mint": ("#4FD1A5", "#DCF6EC", "#1F6B50", 135),
    "sun": ("#FFC93C", "#FFF1CC", "#7A5A00", 225),
    "peony": ("#FF7EB0", "#FFE3EE", "#9B2C5C", 315),
}
ORDER = ["blue", "mint", "sun", "peony"]


def mark(size, label=None):
    paths = "".join(f'<path d="{CRES}" transform="rotate({STRANDS[k][3]})" fill="{STRANDS[k][0]}"/>' for k in ORDER)
    a11y = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg class="mark" width="{size}" height="{size}" viewBox="-50 -50 100 100" {a11y}><g>{paths}</g></svg>'


def moon(strand, extra=""):
    c, _, _, r = STRANDS[strand]
    return f'<svg viewBox="-50 -50 100 100" aria-hidden="true" {extra}><path d="{CRES}" transform="rotate({r})" fill="{c}"/></svg>'


TAG_STRAND = {"Event": "sun", "Insight": "blue", "Programme": "peony", "Webinar": "mint"}

NAV = [("index.html", "Home", "peony"), ("about.html", "About", "blue"), ("news.html", "News", "sun"), ("governance.html", "Governance", "mint")]


# ---------------------------------------------------------------- frame
def header(active, P):
    links = "\n".join(
        f'      <a href="{P}{href}"' + (f' aria-current="page" style="--dot:{STRANDS[s][0]}"' if href == active else "") + f'>{label}</a>'
        for href, label, s in NAV)
    cur = ' aria-current="page"' if active == "join.html" else ""
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="{P}index.html" aria-label="Centre for Whole of Society Resilience, home">
      {mark(44)}
      <span class="brand__text"><span class="brand__sub">centre for</span><span class="brand__name">whole of society resilience</span></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu"><span></span></button>
    <nav class="nav" id="site-nav" aria-label="Main">
{links}
      <a class="btn" href="{P}join.html"{cur}>Join the network</a>
    </nav>
  </div>
</header>'''


def footer(P):
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer__top">
      <div class="footer__brand">
        {mark(48)}
        <p>Joining the dots between research, practice, policy and lived experience.</p>
      </div>
      <div class="footer__cols">
        <div>
          <h4>Centre</h4>
          <ul>
            <li><a href="{P}about.html">About us</a></li>
            <li><a href="{P}about.html#people">Founders &amp; committee</a></li>
            <li><a href="{P}news.html">News &amp; events</a></li>
          </ul>
        </div>
        <div>
          <h4>Get involved</h4>
          <ul>
            <li><a href="{P}join.html">Become a member</a></li>
            <li><a href="{FORM}" rel="noopener">Member sign-up form</a></li>
            <li><a href="{LINKEDIN}" rel="noopener">LinkedIn group</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><a href="{P}governance.html#terms">Terms of reference</a></li>
            <li><a href="{P}governance.html#faq">Guidelines &amp; questions</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 Centre for Whole of Society Resilience</span>
      <span>Building a resilient future, together</span>
    </div>
  </div>
</footer>
<script src="{P}assets/js/site.js" defer></script>'''


def join_band(P):
    return f'''<section class="section" aria-labelledby="join-title">
  <div class="wrap">
    <div class="join-band reveal">
      {mark(520)}
      <div class="join-band__body">
        <h2 id="join-title">Join the network</h2>
        <p>Meet other resilience professionals, share what you know, and take part in projects. Membership is free. We ask only that you sign the members' charter.</p>
        <div class="actions">
          <a class="btn btn--ink" href="{P}join.html">Become a member {ARROW}</a>
          <a class="btn btn--outline" href="{LINKEDIN}" rel="noopener">LinkedIn group</a>
        </div>
      </div>
    </div>
  </div>
</section>'''


def page(path, title, desc, active, body, join=True):
    P = "../" * path.count("/")
    full = title if title.startswith("Centre for") else f"{title} · Centre for Whole of Society Resilience"
    body = (body.replace("{{P}}", P).replace("{{ARROW}}", ARROW).replace("{{FORM}}", FORM)
                .replace("{{EMAIL}}", EMAIL).replace("{{LINKEDIN}}", LINKEDIN))
    html = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#FFF9F1">
<link rel="canonical" href="{SITE}/{'' if path == 'index.html' else path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Centre for Whole of Society Resilience">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/img/logo/cwsr-seal-paper-1024.png">
<link rel="icon" type="image/svg+xml" href="{P}assets/img/favicon.svg?v=2">
<link rel="icon" type="image/png" href="{P}assets/img/favicon.png?v=2">
<link rel="apple-touch-icon" href="{P}assets/img/apple-touch-icon.png?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{P}assets/css/styles.css">
</head>
<body>
{header(active, P)}
<main id="main">
{body}
{join_band(P) if join else ''}
</main>
{footer(P)}
</body>
</html>
'''
    dest = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as f:
        f.write(html)


def card(p):
    s = TAG_STRAND[p["tag"]]
    return f'''      <a class="card reveal" href="{{{{P}}}}news/{p['slug']}.html">
        <div class="card__art" style="background:{STRANDS[s][1]}">{moon(s)}</div>
        <div class="card__meta"><span class="dot dot--{s}"></span><strong>{p['tag']}</strong><span>{p['short']}</span></div>
        <h3>{p['title']}</h3>
        <p>{p['summary']}</p>
      </a>'''


# ---------------------------------------------------------------- home
HERO_PHOTO = "https://images.unsplash.com/photo-1503785640985-f62e3aeee448?fm=jpg&q=80&w=1400&fit=crop"

groups = [
    ("blue", "Research", "People who study it", "Academics and researchers developing the evidence, models and measures behind resilience."),
    ("mint", "Practice", "People who deliver it", "Practitioners and organisations building resilience on the ground, in services, infrastructure and business."),
    ("sun", "Policy", "People who shape it", "Leaders in government and institutions who set the frameworks and priorities."),
    ("peony", "Lived experience", "People who live with it", "Communities and individuals who live with the consequences, and often know best what works."),
]
groups_html = "\n".join(f'''      <article class="group t-{s} reveal">
        {moon(s, 'width="56" height="56"')}
        <span class="group__kind">{kind}</span>
        <h3>{title}</h3>
        <p>{text}</p>
      </article>''' for s, kind, title, text in groups)

home = f'''<section class="hero">
  <div class="wrap">
    <div class="hero__grid">
      <div class="hero__copy">
        <h1>Building a resilient future, together</h1>
        <p class="lede">We connect the people who study resilience, deliver it, shape it and live with it, so that everyone, at every level, can help build a society that adapts and thrives.</p>
        <div class="actions">
          <a class="btn" href="{{{{P}}}}join.html">Join the network, free {{{{ARROW}}}}</a>
          <a class="btn btn--outline" href="{{{{P}}}}about.html">About the Centre</a>
        </div>
        <p class="small">More than 200 members across government, transport, defence, education, NGOs and cybersecurity.</p>
      </div>
      <figure class="hero-photo">
        <img src="{HERO_PHOTO}" alt="Looking up through tall pine trees" width="1400" height="1750">
        <figcaption>Photo: <a href="https://unsplash.com/@mattartz" rel="noopener">Matt Artz</a> / Unsplash</figcaption>
      </figure>
    </div>
    <div class="banner reveal">
      <p><strong>Members' Day 2026</strong> took place in London on 15 October, on the theme of human-centred resilience.</p>
      <a href="{{{{P}}}}news/members-day-2026.html">About the day</a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="who-title">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="who-title">Who we bring together</h2>
      <p class="muted">Resilience gets stuck in silos. The Centre is an independent hub where four groups that rarely share a room work on the same problems.</p>
    </div>
    <div class="groups">
{groups_html}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="purpose-title">
  <div class="wrap split">
    <div class="stack reveal">
      <h2 id="purpose-title">What we mean by whole of society resilience</h2>
      <p>Everyone, at every level of the system, working together to build a thriving, adaptive and sustainable society.</p>
      <p>We champion human-centred resilience. That means putting people's needs, behaviours, relationships, agency and lived experience at the heart of every system, and helping people feel able to act within their own circle of influence.</p>
    </div>
    <div class="pillars">
      <div class="pillar reveal"><span class="dot dot--blue"></span><div><h3>A shift in mindset</h3><p>From reactive to proactive. It includes, but goes well beyond, preparing for shocks: it means responding together to complex challenges in ways that improve human, social and planetary wellbeing.</p></div></div>
      <div class="pillar reveal"><span class="dot dot--mint"></span><div><h3>A whole-system approach</h3><p>Grounded in complex systems thinking, connecting personal and social life with the technical, political and environmental challenges societies face, and with the data that informs decisions.</p></div></div>
      <div class="pillar reveal"><span class="dot dot--peony"></span><div><h3>A shared understanding</h3><p>A common picture of purpose, shocks, stresses, opportunities and interdependencies, so that new knowledge reaches all of society, including the most disadvantaged.</p></div></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="how-title">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="how-title">How the Centre works</h2>
      <p class="muted">The Centre is funded by the projects it delivers, not by membership fees.</p>
    </div>
    <div class="ruled reveal">
      <div><h3>Projects</h3><p>Industry-led projects with teams drawn from the network to explore, model and advance a whole of society approach.</p></div>
      <div><h3>Leadership &amp; learning</h3><p>The <a class="link" href="{{{{P}}}}news/resilient-leaders-programme-cohort-2.html">Resilient Leaders Programme</a> and a masterclass series for resilience professionals.</p></div>
      <div><h3>Data &amp; measurement</h3><p>A digital infrastructure to capture, model and analyse data for place-based resilience decisions.</p></div>
      <div><h3>Convening</h3><p>Webinars, roundtables and an annual conference with partners such as ISRM and Resilience First.</p></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="news-title">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="news-title">Latest news</h2>
      <a class="link" href="{{{{P}}}}news.html"><strong>All news &amp; events</strong></a>
    </div>
    <div class="cards">
{card(BY['annual-resilience-statement-2026'])}
{card(BY['resilient-leaders-programme-cohort-2'])}
{card(BY['measuring-resilience-webinar'])}
    </div>
  </div>
</section>
'''.replace("{{{{", "{{").replace("}}}}", "}}")

page("index.html", "Centre for Whole of Society Resilience (CWSR)",
     "A free, transdisciplinary network connecting the people who study resilience, deliver it, shape it and live with it.",
     "index.html", home)

# ---------------------------------------------------------------- about
def bio(paras):
    return "".join(f"<p>{p}</p>" for p in paras)

founders_html = "\n".join(f'''      <article class="person reveal">
        <div class="person__photo"><img src="{{{{P}}}}assets/img/team/{slug}.jpg" alt="Portrait of {name.split(',')[0]}" loading="lazy" width="480" height="480" style="--ring:{STRANDS[ORDER[(i + 1) % 4]][0]}"></div>
        <div><h3>{name}</h3><div class="role">{role}</div></div>
        <div class="bio">{bio(paras)}</div>
        <div>{link}</div>
      </article>''' for i, (slug, name, role, paras, link) in enumerate(founders))

committee_html = "\n".join(f'''      <article class="member reveal">
        <div class="member__head">
          <img src="{{{{P}}}}assets/img/team/{slug}.jpg" alt="Portrait of {name}" loading="lazy" width="480" height="480" style="--ring:{STRANDS[ORDER[i % 4]][0]}">
          <div><h3>{name}</h3><div class="role">{role}</div></div>
        </div>
        <div class="bio">{bio(paras)}</div>
        <div>{link}</div>
      </article>''' for i, (slug, name, role, paras, link) in enumerate(committee))

about = f'''<section class="page-hero">
  <div class="wrap intro">
    <div class="stack">
      <div class="crumbs"><a href="{{{{P}}}}index.html">Home</a> / About</div>
      <h1>Joining the dots between research, practice and policy</h1>
    </div>
    <div class="stack" style="padding-top:40px">
      <p>We are a transdisciplinary network of consultants, business leaders, academics and practitioners who have come together to advance research-informed resilience policy and practice. Our aim is to build long-term whole of society resilience, as outlined in the UK Government Resilience Framework.</p>
      <p>We are funded by delivering innovative projects, drawing on the network to form teams with the right expertise for each challenge. If you are passionate about resilience and have skills to offer, <a class="link" href="{{{{P}}}}join.html">please join us</a>.</p>
    </div>
  </div>
</section>

<section class="section" aria-label="Our members">
  <div class="wrap">
    <ul class="chips reveal">
      <span class="chips__count">200+ members</span>
      <li>Public sector</li><li>Defence</li><li>Transport</li><li>NGOs</li><li>Education &amp; research</li><li>Cybersecurity</li><li>Consultancy</li><li>Academia</li>
    </ul>
  </div>
</section>

<section class="section" id="people" aria-labelledby="founders-title">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="founders-title">Founders</h2>
      <p class="muted">Three professors bridging industry, academia and practice, who set up the Centre to bring whole of society resilience-building together.</p>
    </div>
    <div class="founders">
{founders_html}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="sc-title">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="sc-title">Steering committee</h2>
      <a class="link" href="{{{{P}}}}governance.html#terms"><strong>How the committee is chosen</strong></a>
    </div>
    <div class="committee">
{committee_html}
    </div>
  </div>
</section>
'''.replace("{{{{", "{{").replace("}}}}", "}}")

page("about.html", "About", "Founders, steering committee and members of the Centre for Whole of Society Resilience.", "about.html", about)

# ---------------------------------------------------------------- news
lead = POSTS[0]
news = f'''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{{{{P}}}}index.html">Home</a> / News</div>
    <h1>News &amp; events</h1>
    <p class="lede">Events, programmes and perspectives on building resilience as a genuinely whole of society capability.</p>
  </div>
</section>
<section class="section" style="padding-top:56px">
  <div class="wrap">
    <a class="feature reveal" href="{{{{P}}}}news/{lead['slug']}.html">
      <div class="feature__body">
        <span><strong>{lead['tag']}</strong> · {lead['date']}</span>
        <h2>{lead['title']}</h2>
        <p class="muted">{lead['summary']}</p>
        <span class="btn btn--ink" style="align-self:flex-start">Read more {{{{ARROW}}}}</span>
      </div>
      <div class="feature__art">{moon('peony')}</div>
    </a>
  </div>
</section>
<section class="section" style="padding-top:72px">
  <div class="wrap">
    <div class="cards">
{chr(10).join(card(p) for p in POSTS[1:])}
    </div>
  </div>
</section>
'''.replace("{{{{", "{{").replace("}}}}", "}}")
page("news.html", "News", "News, events and insight from the Centre for Whole of Society Resilience.", "news.html", news)


def article(p):
    idx = POSTS.index(p)
    newer = POSTS[idx - 1] if idx > 0 else None
    older = POSTS[idx + 1] if idx + 1 < len(POSTS) else None
    nav = '<nav class="post-nav" aria-label="More posts">'
    nav += f'<a class="link" href="{{{{P}}}}news/{older["slug"]}.html">← {older["title"]}</a>' if older else "<span></span>"
    nav += f'<a class="link" href="{{{{P}}}}news/{newer["slug"]}.html">{newer["title"]} →</a>' if newer else ""
    nav += "</nav>"
    s = TAG_STRAND[p["tag"]]
    body = f'''<section class="article-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{{{{P}}}}index.html">Home</a> / <a href="{{{{P}}}}news.html">News</a> / {p['tag']}</div>
    <h1>{p['title']}</h1>
    <div class="article-meta"><span class="dot dot--{s}"></span><strong>{p['date']}</strong><span>By {p['author']}</span><span>{p['read']}</span></div>
  </div>
</section>
<article class="article">
  <div class="prose">
{ARTICLES[p['slug']]}
  {nav}
  </div>
</article>
'''.replace("{{{{", "{{").replace("}}}}", "}}")
    page(f"news/{p['slug']}.html", p["title"], p["summary"].replace('"', "&quot;"), "news.html", body)


for p in POSTS:
    article(p)

# ---------------------------------------------------------------- join
join = f'''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{{{{P}}}}index.html">Home</a> / Membership</div>
    <h1>Join the network</h1>
    <p class="lede">Membership is free. If you care about resilience and have skills to offer, we'd like you to join us. Read the charter, then fill in the short sign-up form.</p>
  </div>
</section>
<section class="section" style="padding-top:56px">
  <div class="wrap join-grid">
    <div class="charter reveal">
      <h2>The members' charter</h2>
      <p>As a member of the Centre for Whole of Society Resilience, I agree to work collaboratively and inclusively with other members to further the Centre's purpose of delivering whole of society resilience. Specifically, I will endeavour to:</p>
      <ol>
        <li>participate in dialogue that promotes and enhances the Centre on social media and at industry events;</li>
        <li>be willing to host a CWSR meeting if I have appropriate facilities;</li>
        <li>contribute to discussion forums, papers, articles or projects with other members.</li>
      </ol>
      <div class="actions" style="margin-top:8px">
        <a class="btn" href="{{{{FORM}}}}" rel="noopener">Agree and sign up {{{{ARROW}}}}</a>
      </div>
      <p class="small">The sign-up form opens in Microsoft Forms.</p>
    </div>
    <div class="aside">
      <div class="aside__card t-mint reveal">
        {moon('mint')}
        <h2>What members get</h2>
        <p>Meet other resilience professionals, share knowledge, and take part in projects with real impact.</p>
      </div>
      <div class="aside__card reveal" style="background:#FFFFFF">
        <h2>Not ready to join?</h2>
        <a href="{{{{LINKEDIN}}}}" rel="noopener">Follow our LinkedIn group</a>
        <a href="mailto:{{{{EMAIL}}}}">{{{{EMAIL}}}}</a>
      </div>
    </div>
  </div>
</section>
'''.replace("{{{{", "{{").replace("}}}}", "}}")
page("join.html", "Become a member", "Membership of the Centre for Whole of Society Resilience is free. Meet other resilience professionals, share knowledge and take part in projects.", "join.html", join, join=False)

# ---------------------------------------------------------------- governance
def block(strand, anchor, title, items):
    lis = "".join(f"<li>{t}</li>" for t in items)
    return f'<div class="gov-block reveal" id="{anchor}"><h3>{moon(strand, "width=26 height=26")}{title}</h3><ol>{lis}</ol></div>'

faqs = [
    ("Is membership really free?", "Yes. The Centre is funded by the projects it delivers, not by membership fees."),
    ("Who can join?", "Anyone who cares about resilience and has something to offer. That includes researchers, practitioners, people in policy roles, and people bringing community or lived experience. Members come from government, transport, defence, NGOs, education, cybersecurity and more."),
    ("What does the members' charter ask of me?", "To work collaboratively and inclusively with other members. Where you can, we also ask you to talk about the Centre at events and online, host a meeting if you have the space, and contribute to discussions, papers or projects."),
    ("How do I sign up?", "Read the charter on the membership page, then complete the short sign-up form. We'll be in touch by email."),
    ("Can I bid for work as CWSR?", "Not on your own, because the Centre is not a legal entity. You can mention your membership in any proposal. Bids in the Centre's name only go through the Steering Group's expressions-of-interest process."),
    ("How is the Steering Group chosen?", "At least once a year members can nominate candidates, and the membership votes. A first term lasts two years, and further terms last three."),
    ("I only want updates, not membership.", "Follow our LinkedIn group for news and events."),
]
faq_html = "".join(f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>" for i, (q, a) in enumerate(faqs))

gov = f'''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="{{{{P}}}}index.html">Home</a> / Governance</div>
    <h1>How the Centre is run</h1>
    <p class="lede">The Centre is led by its members and guided by an elected Steering Group. These are its terms of reference, and the guidelines we ask everyone in our community to follow.</p>
  </div>
</section>
<section class="section" style="padding-top:56px">
  <div class="wrap toc-layout">
    <nav class="toc" aria-label="On this page">
      <p>On this page</p>
      <a href="#terms"><span class="dot dot--blue"></span>Terms of reference</a>
      <a href="#guidelines"><span class="dot dot--sun"></span>Site guidelines</a>
      <a href="#faq"><span class="dot dot--peony"></span>Questions</a>
    </nav>
    <div class="gov">
      <h2 id="terms">Steering Group terms of reference</h2>
      {block('blue', 'membership', 'Membership', membership)}
      {block('mint', 'meetings', 'Meetings', meetings)}
      {block('sun', 'scope', 'Scope', scope)}
      <h2 id="guidelines">Site guidelines</h2>
      <ul class="rules reveal">{''.join(f'<li>{r}</li>' for r in rules)}</ul>
      <h2 id="faq">Questions</h2>
      <div class="faq">{faq_html}</div>
      <p class="muted">Anything else: <a class="link" href="mailto:{{{{EMAIL}}}}">{{{{EMAIL}}}}</a></p>
    </div>
  </div>
</section>
'''.replace("{{{{", "{{").replace("}}}}", "}}")
page("governance.html", "Governance", "Steering Group terms of reference, site guidelines and common questions for the Centre for Whole of Society Resilience.", "governance.html", gov)

# ---------------------------------------------------------------- 404
page("404.html", "Page not found", "This page could not be found.", "", f'''<section class="page-hero">
  <div class="wrap">
    {mark(120)}
    <h1>We couldn't find that page</h1>
    <p class="lede">It may have moved, or it may not exist any more.</p>
    <div class="actions"><a class="btn" href="/index.html">Back to the homepage {{{{ARROW}}}}</a></div>
  </div>
</section>'''.replace("{{{{", "{{").replace("}}}}", "}}"), join=False)

print("built")
