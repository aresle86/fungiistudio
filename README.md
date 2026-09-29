# Fungii Studio website

Static site for GitHub Pages. No build step on GitHub: `index.html` is the whole site.

- `index.html` — the site (three.js loads from jsDelivr, fonts from Google Fonts)
- `media/` — film files (`name.mp4` full film, `name-loop.mp4` short silent loop, `name.jpg` poster)
- `favicon.svg`, `apple-touch-icon.png`, `og.jpg` — tab icon, home-screen icon, link preview image
- `.nojekyll` — tells GitHub Pages to serve files as-is

All site text and the film list live in the `window.COPY` block inside `index.html`.
