# Centre for Whole of Society Resilience — website

A static redesign of [wholesocietyresilience.org](https://www.wholesocietyresilience.org). It's plain HTML, CSS and a small JS file, with no framework and no build step needed to host it. Copy is carried over from the original site.

## The identity

Four moons, one whole. The Centre brings together four groups: the people who study resilience, deliver it, shape it, and live with it. Each is a crescent in its own colour; together they close a ring. Where the colours overlap they overprint (CSS `mix-blend-mode: multiply`), like risograph inks.

| Strand | Colour | Tint |
| --- | --- | --- |
| Study (research) | Cornflower `#7B9CFF` | `#E4EAFF` |
| Deliver (practice) | Mint `#4FD1A5` | `#DCF6EC` |
| Shape (policy) | Sunflower `#FFC93C` | `#FFF1CC` |
| Live with (lived experience) | Peony `#FF7EB0` | `#FFE3EE` |

Text is always Ink `#231E3D` on Paper `#FFF9F1` or any tint. Headings are Figtree; body text is Atkinson Hyperlegible. Everything is a circle or part of one: round portraits, pill buttons, 28px card corners.

## Pages

| File | Content |
| --- | --- |
| `index.html` | Home: purpose, the four groups, how the Centre works, latest news, membership |
| `about.html` | Introduction, members, founders, steering committee |
| `news.html`, `news/*.html` | News index and the four posts |
| `join.html` | Membership charter and link to the sign-up form |
| `governance.html` | Steering Group terms of reference, site guidelines, questions |
| `404.html` | Not-found page |

## Editing

Every page is generated, so edit the source and regenerate:

```sh
python3 tools/build.py      # rewrites all *.html in the repo root and news/
```

- `tools/content.py`: all copy — news posts and article text, team bios, governance clauses
- `tools/build.py`: page layouts, header, footer, the mark (drawn inline as SVG so the overprint works)
- `assets/css/styles.css`: styles, with colour and type tokens at the top

## Logo files

`assets/img/logo/` holds the full PNG logo suite, named `cwsr-[form]-[colourway].png`:

- forms: `halo` (mark only), `horizon` (mark beside name), `moonrise` (mark above name), `signature` (name only), `seal` (round badge), `appicon`, `favicon-*`
- colourways: `colour` (transparent, for light backgrounds), `paper`, `night` (on ink), `ink`, `noir` (black), `chalk` (white, transparent)

`assets/img/favicon.png` and `assets/img/apple-touch-icon.png` are generated from the favicon files.

## Hosting

Any static host works (Cloudflare Pages, GitHub Pages, Netlify). Serve the repo root. `.nojekyll` is included for GitHub Pages.

## Features from the Wix site that need a replacement

- **Members Area / member log-in**: Wix-only. The site links to the existing Microsoft Forms sign-up and the LinkedIn group instead. Member data can be exported from Wix (Contacts → Export, site owner only) to move into whatever replaces it.
- **Newsletter subscribe form**: Wix-only. Removed. Add an embed from Mailchimp, Buttondown or similar if needed.
- **Resilient Leaders Programme PDF**: hosted on Wix. Add it to `assets/` and link it from the post if it should stay downloadable.
