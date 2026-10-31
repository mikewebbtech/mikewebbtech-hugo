<h1 align="center""> My Hugo Site Theme </h1>
<h3 align="center">Static Site Built using HUGO </h3>
<p align="center">
<a href="https://gohugo.io">
  <img alt="HUGO LOGO" title="Hugo website" src="https://gohugo.io/images/hugo-logo-wide.svg" width="200">
</a>
<br>
<br>
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/mikewebbtech/mikewebbtech-hugo/site-deploy.yml?label=Site%20CI%2FCD%20Build">
</p>
<h4>Table of Contents</h4>

- [What is Hugo](#hugo)
- [Features and Progress](#progress)
- [Stylesheets](#stylesheets)

<p align="center">
<img alt "theme look" src="./site_look.png" >
</p>

---

## Hugo

> "The world’s fastest framework for building websites" - _Hugo Devs_

Hugo is a static site generator framework written in go and sites are created using html templates with embedded go template language snippets. The content for the site is generated from text files such as markdown, json, asciiDoc etc.

The [hugo documentation](https://gohugo.io/documentation) is extensive and well structured and there is an active community to lean on for help. There are lots of blog articles and theme examples to draw inspiration and get started with creating a site. If an existing theme meets your needs, Hugo is even easier and faster to get started with.

:point_right: **What is a SSG and Why?**

Static site generators offer faster performance, enhanced security, and greater scalability by pre-building web pages as static files rather than generating them on demand using a database back end. This approach simplifies hosting and maintenance, allows for better content version control, and provides a lighter back end with fewer dependencies. As a result, static sites are more reliable, more secure, and often offer better SEO due to their speed.

---

## Stylesheets

Styles are written in Sass using the SCSS syntax in `assets/scss/`. Hugo compiles
`style.scss` into CSS, then minifies and fingerprints it for the browser.

Local builds require Hugo and the Dart Sass executable (`sass`) on your `PATH`.
For a Nix environment, include `dart-sass` alongside Hugo; with Homebrew, use
`brew install sass/sass/sass`. See the [Hugo Sass documentation](https://gohugo.io/functions/css/sass/)
for installation details. The GitHub Pages workflow already installs Dart Sass.

Run `hugo server` for local preview or `hugo --minify` for a production build.
There is no separate Sass build command.

Edit the partial that contains the styles you want to change:

| Partial | Styles |
| --- | --- |
| `_vendor.scss` | External Font Awesome stylesheet import |
| `_theme.scss` | Colour palettes and CSS custom properties |
| `_base.scss` | Base typography, resets and text helpers |
| `_layout.scss` | Site grid, sidebar, navigation, header and main area |
| `_articles.scss` | Article content, metadata, tags and article lists |
| `_pages.scss` | Shared page, home and category styles |
| `_components.scss` | Buttons, callouts and series navigation |
| `_code-tables.scss` | Code blocks and tables |
| `_cards-breadcrumbs.scss` | Recent article cards and breadcrumbs |
| `_pagination.scss` | Hugo pagination |
| `_images.scss` | Image and figure alignment |
| `_source-link.scss` | Article source links |

`style.scss` loads these partials with `@use` in the original cascade order.
Add new partials there in the order their rules should appear. Keep theme colours
as CSS custom properties (`var(--color-...)`) so they remain available in the
browser. The existing selectors and declarations are preserved during this migration.
Edit the SCSS sources rather than the generated CSS under `public/`.

## Progress

Progress is slow, there is a lot about using the hugo framework that is not intuitive, but I am working my way through the [documentation](https://gohugo.io/documentation/) and implementing functionality as learn or driven by want.

### Todo list:

- [x] Design site layout and CSS
- [x] Slice up site html template into hugo partials
- [x] Create home page markdown (content/\_index.md)
- [x] Create about page markdown (contnent/about/\_index.md)
- [x] First Hugo template layouts/pages/single.html for home and about page
- [x] Nav bar template with place holders for _home_, _about_, _articles_, _categories_, _series_ and _tags_
- [x] Huge layout/\_default/list.html for list pages (articles, categories, series and tags)
- [x] Articles feature ingesting content/articles/\*.md article files
- [x] Implement _categories_ list page using terms template
- [x] _Category_ feature using terms template and content/categories/category-name/\_index.md leaf bundle
- [x] Create named _categories_, style, add categories list array to articles front matter
- [x] Implement _tags_ and \*tag-name\* list page using terms list template and style
- [x] Add metadata to list page items (in layout/\_default/list.html template)
- [x] Add metadata to article page head (created in layout/page/single.html template)
- [x] Separate article files out to own git repo and embed back as submodule
- [x] Implement "**Series**" list feature and style using categories term template as guide.
- [x] Add pagination to **Series** articles.
- [x] Create list of member articles to series article pages.
- [x] Automate blank article creation with front matter (not Hugo built in method)
- [x] Automate git repo and submodule update and push process
- [x] Host site on GitHub for development using actions (update: really half done. revisit)
- [x] Host site on GiHub using _Actions_ and _Pages_ for my Hugo siterepo (a hugo action?)
- [x] Configure _Pages_ custom domain to use mikewebb.tech domain (Namecheap changes?)
- [x] Implement SSL and enforce for GitHub _Pages_
- [x] ~~Implement breadcrumbs feature across site.~~ (note: no longer using)
- [x] Use shortcodes to open external links in new tab or window (html \_blank)
- [x] implement embedding images using markdown notation and shortcodes.
- [x] Trigger GitHub CICD action when submodule external repo is updated.
- [ ] Move away from Font Awesome. Look at svg or mdi as solution?
- [x] serve webp instead of png or jpeg for all images
  - [x] explore using Hugo convert function in template for sites.
  - [x] change format for article images at creation. Explore way to use Hugo function on render
- [x] Refactor CSS to use :root for colors
- [ ] Site statistics (visitor and page views, geolocations etc)
- [ ] Visitor feedback and interaction (security first by design)
- [ ] Implement an Archive section. Display by Year, Month.
- [x] link for articles to markdown source on GitHub
- [x] Add support for Mermaid.js diagrams
