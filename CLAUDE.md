# Arctic Green Lawn & Landscaping

Static business website for a lawn care company. Hugo site deployed to GitHub Pages with custom domain.

## Live site
https://arcticgreenlandscaping.com

## Stack
- Hugo static site generator (v0.160.1 extended)
- Custom theme in `themes/arctic/`
- GitHub Pages hosting
- GitHub Actions auto-deploy on push to `master`

## Run locally
```
hugo server -D
```
Hugo binary on this machine: `~/AppData/Local/Microsoft/WinGet/Packages/Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe/hugo.exe`

## Deploy
Push to `master` — GitHub Actions builds and deploys automatically. Check status with `gh run list --limit 1`.

## Structure
- `content/` — Page content (markdown)
- `layouts/` — HTML templates (mostly in theme)
- `static/` — Static assets (images, CNAME)
- `static/images/` — Homepage photos (`hero-lawn.jpg`, `garden-tools.jpg`)
- `themes/arctic/layouts/` — Page templates (`index.html`, partials, `_default/`)
- `themes/arctic/static/css/style.css` — Single stylesheet (design tokens at top)
- `hugo.toml` — Site config (title, contact info, menus)

## Key info
- Owner: Brayant Rodriguez
- Phone: (903) 658-8244
- Email: agl1025@yahoo.com
- Service area: Northwest Houston, TX — Cypress, Tomball, Spring, Katy, The Woodlands, Magnolia, Hockley, Waller, Jersey Village, Copperfield, Cy-Fair, Champions
- Contact form via formsubmit.co → info@arcticgreenlandscaping.com
- HTTPS enforced, custom domain DNS pointing to GitHub Pages IPs

## Design system
- **Fonts**: Fraunces (display, headings) + Inter (body) — loaded from Google Fonts
- **Colors**: greens (`--green-700` primary, `--green-900` deep), gold accent, stone neutrals. Defined as CSS custom properties in `style.css`.
- **Icons**: inline Lucide SVGs (no icon library dependency). Service icons are dispatched by markdown filename via a `$serviceIcons` dict in `index.html`.
- **Buttons**: pill-shaped (`border-radius: 999px`). Primary = solid green, ghost = transparent-on-dark.
- **Sticky mobile CTA**: always-visible "Call" bar at bottom of viewport on mobile — lives in `baseof.html`.

## Content rules to preserve
- **No 5-star / review claims anywhere on the site.** No star icons in stats, no testimonial stars, no "5.0 rating" cards. Remove on sight if re-introduced. (Nothing verifiable to back them.)
- **Specific copy, not generic.** Hero names the service area explicitly. Footer lists every city served.
- **Placeholders are marked.** Hero + why-section photos are Unsplash stock (`hero-lawn.jpg`). Swap for Brayant's real yard photos when available — drop into `static/images/` and reference with `/images/filename.jpg`.

## Today's redesign (2026-04-14)
- Full homepage rebuild: photographic hero, stats strip, service cards with icons, why-us section with photo + licensed/insured badge, service-area chip grid, CTA banner, blog strip, richer footer.
- Business relocated from Northwest Indiana → Northwest Houston, TX. Phone, tagline, testimonial attribution, service-area list, and footer all updated.
- All star-rating / review claims removed.
