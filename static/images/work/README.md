# Service page work photos

Drop JPG/PNG/WEBP files into the matching service folder. Hugo auto-discovers and renders them on the service detail page — no template edits needed.

## Folder → Page mapping

| Folder | Live page |
|---|---|
| `lawn-mowing-maintenance/` | https://arcticgreenlandscaping.com/services/lawn-mowing-maintenance/ |
| `spring-fall-cleanup/` | https://arcticgreenlandscaping.com/services/spring-fall-cleanup/ |
| `landscape-design-consultation/` | https://arcticgreenlandscaping.com/services/landscape-design-consultation/ |
| `irrigation-system-check/` | https://arcticgreenlandscaping.com/services/irrigation-system-check/ |
| `tree-shrub-trimming/` | https://arcticgreenlandscaping.com/services/tree-shrub-trimming/ |
| `hardscape-paver-walkways/` | https://arcticgreenlandscaping.com/services/hardscape-paver-walkways/ |
| `free-in-home-consultation/` | https://arcticgreenlandscaping.com/services/free-in-home-consultation/ |

## Photo guidelines

- **Aspect ratio:** any. Hero card is 16:9, others are 4:3 — Hugo crops via background-size: cover.
- **Min resolution:** 1200px wide. iPhone-quality is fine.
- **File format:** .jpg preferred (smaller). .png OK for screenshots. .webp best for size.
- **Filename:** descriptive lowercase-with-dashes. Examples — `bridgeland-bermuda-front-cut.jpg`, `cypress-corner-bed-after.jpg`. First file alphabetically gets the hero (16:9) slot.
- **Number per page:** 3-6 ideal. More = slower page load.
- **Real work only.** No stock photos.

## How to deploy

```
git add static/images/work/
git commit -m "Add work photos for <service>"
git push
```

GitHub Actions auto-deploys in ~30 sec.
