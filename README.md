# BillMat LLC Static Website

BillMat LLC is a fully static GitHub Pages website for an independent insurance education platform and licensed agency partner. The site explains common insurance payment options for Progressive, Allstate, and Bristol West while directing every payment action to official insurer websites.

> **Important:** BillMat LLC is **not** an insurer, **not** a payment processor, and **not** affiliated with Progressive, Allstate, Bristol West, or Farmers. The site does not collect payment data or access policy accounts.

## Live site

- **GitHub Pages URL:** <https://getlivesupport.github.io/billmat/>
- **Deployment model:** GitHub Pages project site
- **Publishing source:** `main` branch, repository root

## Project purpose

The website is designed to be:

- **Human-first:** clear, practical explanations of how to pay insurance premiums through official channels
- **Trust-forward:** visible review dates, strong disclaimers, legal pages, editorial transparency, and correction instructions
- **Search-ready:** unique titles, meta descriptions, canonical URLs, structured data, sitemap, robots file, breadcrumb navigation, and internal linking
- **Fast and accessible:** static HTML, small CSS and JavaScript, system fonts, async stylesheet loading, keyboard navigation, dark mode, and reduced-motion support

## File structure

```text
BillMat/
├── 404.html
├── README.md
├── about.html
├── contact.html
├── disclaimer.html
├── editorial-policy.html
├── index.html
├── privacy-policy.html
├── robots.txt
├── site.webmanifest
├── sitemap.xml
├── terms-of-service.html
├── assets/
│   ├── favicon.svg
│   └── social-card.svg
├── css/
│   └── style.css
├── insurance-partners/
│   ├── allstate.html
│   ├── bristol-west.html
│   ├── index.html
│   └── progressive.html
└── js/
    └── main.js
```

## Page overview

### Core pages

- `index.html` — homepage covering insurance payment options, payment safety checklists, FAQs, and related trust pages
- `insurance-partners/index.html` — guide hub for insurer-specific payment pages
- `insurance-partners/progressive.html` — Progressive payment guide with Quick Pay information, comparison table, contacts, FAQ, and related content
- `insurance-partners/allstate.html` — Allstate billing options guide with payment methods, discount questions, contacts, FAQ, and related content
- `insurance-partners/bristol-west.html` — Bristol West payment methods guide with retail payment reminders, contacts, FAQ, and related content

### Trust and policy pages

- `about.html` — mission, audience, editorial standards, review cadence, and corrections approach
- `contact.html` — content-question contact instructions and official insurer contact links
- `editorial-policy.html` — sourcing standards, review cadence, correction policy, and disclosure approach
- `privacy-policy.html` — data collection, no payment-data collection, cookies, analytics disclosure, third-party links, children's privacy, and data requests
- `terms-of-service.html` — educational-use terms, no-advice notice, third-party link notice, and limitation of liability
- `disclaimer.html` — independence statement, no-payment-processing notice, and verification reminder
- `404.html` — branded not-found page with recovery links

## Local preview

No build step is required.

### Option 1: Python

```bash
cd /home/runner/work/Billmat/Billmat
python3 -m http.server 8000
```

Open <http://localhost:8000/>.

### Option 2: Any static server

You can use any simple static server so long as it serves the repository root directly.

## GitHub Pages deployment

1. Open the repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select:
   - **Branch:** `main`
   - **Folder:** `/ (root)`
5. Save the settings.
6. GitHub Pages will publish the project site at:
   - <https://getlivesupport.github.io/billmat/>

## SEO features implemented

The site includes:

- unique, keyword-focused `<title>` tags for every page
- unique meta descriptions on every page
- canonical URLs using the GitHub Pages project-site path
- Open Graph and Twitter Card metadata for every page
- shared social preview image at `assets/social-card.svg`
- visible breadcrumb navigation and matching `BreadcrumbList` JSON-LD
- homepage `Organization` + `WebSite` structured data
- guide page `Article` + `FAQPage` + `BreadcrumbList` structured data
- legal/trust page `WebPage`, `AboutPage`, or `ContactPage` structured data as appropriate
- descriptive internal linking and related-content sections
- `robots.txt` and `sitemap.xml`
- `site.webmanifest` and SVG favicon

## Performance targets and implementation

This is a no-framework static site built to support strong Core Web Vitals and high Lighthouse scores.

### Performance choices

- inline critical CSS in each page head for above-the-fold stability
- shared stylesheet loaded asynchronously from `css/style.css`
- small deferred JavaScript in `js/main.js`
- no jQuery, frameworks, or third-party trackers
- system-font stack instead of external font requests
- SVG assets instead of external image CDNs
- text-based hero sections rather than large LCP images

### Accessibility targets

- WCAG 2.1 AA color contrast targets
- one `<h1>` per page with consistent heading hierarchy
- skip link to main content
- keyboard-operable navigation and FAQ accordions
- visible focus states
- responsive layouts for 320px through large desktop widths
- dark-mode support via `prefers-color-scheme`
- reduced-motion support via `prefers-reduced-motion`

## Structured data overview

- **Homepage:** `Organization`, `WebSite`
- **Guide hub:** `CollectionPage`, `BreadcrumbList`
- **Guide pages:** `Article`, `FAQPage`, `BreadcrumbList`
- **About page:** `AboutPage`, `BreadcrumbList`
- **Contact page:** `ContactPage`, `BreadcrumbList`
- **Policy pages:** `WebPage`, `BreadcrumbList`

All JSON-LD is plain, factual, and avoids unverified claims.

## Content verification policy

BillMat's content is educational. It should be treated as a guide to help users ask better questions and reach official insurer channels.

### What the site does

- explains common insurance payment options in plain language
- provides official insurer links for verification and payment actions
- repeats reminders to verify fees, discounts, grace periods, service hours, and mailing details with the insurer

### What the site does not do

- does not collect payment credentials
- does not process payments
- does not access policy balances or account status
- does not promise universal insurer discounts, fees, grace periods, or posting times
- does not claim affiliation with Progressive, Allstate, Bristol West, or Farmers

## Customization guide

To customize the site:

1. **Update content pages** directly in the HTML files.
2. **Adjust styling** in `css/style.css`.
3. **Update shared interactions** in `js/main.js`.
4. **Replace social or icon assets** in `assets/` if branding changes.
5. **Refresh `sitemap.xml`** if you add or remove pages.
6. **Review metadata** on any page you change so SEO remains consistent.

### Brand colors used

- BillMat sage teal: `#2d7a6e`
- Progressive accent: `#0066cc`
- Allstate accent: `#c41e3a`
- Bristol West accent: `#2e7d32`

## Maintenance checklist

When editing the site in the future, verify:

- all internal links still work at the `/billmat/` subpath
- all external insurer links still point to official domains
- every page still shows `Last reviewed: September 18, 2026` or a newer correct date
- `sitemap.xml` includes all live pages
- structured data remains valid JSON-LD
- trust and disclaimer language remains accurate

## Independence and payment disclaimer

BillMat LLC is an independent insurance education platform and licensed agency partner. It is **not** an insurer, **not** a payment processor, and **not** affiliated with Progressive, Allstate, Bristol West, or Farmers. All payment actions must direct users to official insurer websites.
