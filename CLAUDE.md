# Arctic Green Lawn & Landscaping

Static business website for a lawn care company. Hugo site deployed to GitHub Pages with custom domain.

## Live site
https://arcticgreenlandscaping.com

## Stack
- Hugo static site generator (v0.160.1)
- Custom theme in `themes/arctic/`
- GitHub Pages hosting
- GitHub Actions auto-deploy on push to `master`

## Run locally
```
hugo server -D
```

## Deploy
Push to `master` — GitHub Actions builds and deploys automatically.

## Structure
- `content/` — Page content (markdown)
- `layouts/` — HTML templates
- `static/` — Images, CSS, JS
- `themes/arctic/` — Custom theme
- `hugo.toml` — Site config (title, contact info, menus)

## Key info
- Owner: Brayant Rodriguez
- Phone: (219) 387-6402
- Email: agl1025@yahoo.com
- Contact form via formsubmit.co
- HTTPS enforced, custom domain DNS pointing to GitHub Pages IPs
