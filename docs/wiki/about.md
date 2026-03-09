---
title: About the Archives
---

# About the Archives

## Community
---
This site's content is the result of extensive community research, development and curation. All glitches documented here are the product of a phenomenal community glitch hunt and collaborative research effort in The Legend of Zelda: Tears of the Kingdom. Please credit the following volunteer QA communities and contributors, who helped Nintendo Ninjas push several patches, when sharing or referencing material from this site.

## Contribution
---
If you'd like to document glitches, techniques, setups or builds for the archives, read [this guide](https://github.com/nan-gogh/ultrabroken-documentation/blob/main/README.md), then load [this blank file](https://github.com/nan-gogh/ultrabroken-documentation/blob/main/docs/wiki/_wip/blank.md) to fill it out and post it [here](https://discord.com/channels/1086729144307564648/1471224902890684557).

## Goal
---
Concise, community-based documentation for glitches and techniques — readable guides, glitch writeups, and practical how‑tos. We prioritise clear reproduction steps, annotated media, and reproducible setups so readers can verify findings themselves. Entries aim to be useful both for players seeking practical tactics and for researchers analysing systemic behaviour.

## Content
---
Detailed glitch reports, step‑by‑step instructions and examples; organized into the site's main sections. Each report includes a short summary, the required setup, stepwise reproduction instructions, and analysis of contributing factors. Where useful we attach screenshots, graphics, links to short clips, timing notes, and community-sourced test cases to make verification straightforward.

## Experience
---
Built with MkDocs + Material for fast search, clear navigation, and readable typesetting on desktop and mobile. The site adapts responsively across devices, supports keyboard navigation and semantic markup for accessibility, and includes lightweight client features to help you find information quickly while testing in-game. We balance a compact layout with readable media so guides remain practical during hands-on verification.

## Discovery
---
The integrated site search, searchbar- and permalinks as well as AI assisted querying let you find and share related topics quickly. Use the search box to match keywords or filter by section; each page provides stable permalinks for easy sharing. For broader exploration, browse section lists and tags to discover related techniques, investigations, and curated libraries.

## AI Search
---
When you ask The Librarian, an algorithm searches our archives for documents that match your query and supplies only those matched records to the answer syntesizer. The syntesizer creates a response and assembles searchbar links from involved sources for your single request based solely on the provided records — it does not retain your query nor learn from it or the answer it created. This way we don't trade our archives for the conveniece of AI-assisted navigation features. The accuracy of responses depends mainly the zeal of our Archivists and the quality of their contributions - always verify against the source pages.

## Infrastructure
---
The archives run on open-source tooling across GitHub and Cloudflare. Media uploads require authentication via the [`ultrabroken-archivists`](https://github.com/ultrabroken-archivists) GitHub organisation — membership is managed by invite only. No personal data is collected; Cloudflare Access verifies org membership through GitHub OAuth and does not store credentials beyond session tokens.

<script>
(function(){
  // Minimal, reusable diagram viewer for any content inside .diagram-inner
  function DiagramPanZoom(pan) {
    const inner = pan.querySelector('.diagram-inner');
    const slider = pan.querySelector('input[type=range]');
    const label = pan.querySelector('.diagram-level');
    const resetBtn = pan.querySelector('button');
    let zoom = 1, minZoom = 0.4, maxZoom = 4;
    let baseW = 0, baseH = 0;
    let dragging = false, dragX = 0, dragY = 0, scrollL = 0, scrollT = 0;
    let lastTouchDist = null, lastTouchMid = null;

    // Wait for content to render and measure base size
    function measureBase() {
      const mermaid = inner.querySelector('.mermaid');
      if (!mermaid || pan.clientWidth === 0) return requestAnimationFrame(measureBase);
      // Wait for SVG to appear (textContent empty)
      if (mermaid.textContent.trim().length > 0) return requestAnimationFrame(measureBase);
      const rect = mermaid.getBoundingClientRect();
      if (rect.width === 0 || rect.height === 0) return requestAnimationFrame(measureBase);
      // Remove any transform for base measurement
      inner.style.transform = '';
      baseW = inner.offsetWidth;
      baseH = Math.ceil(rect.height + parseFloat(getComputedStyle(inner).paddingTop) + parseFloat(getComputedStyle(inner).paddingBottom));
      inner.style.width = baseW + 'px';
      inner.style.height = baseH + 'px';
      setZoom(1, true);
    }

    // Set zoom, optionally centering
    function setZoom(newZoom, center) {
      zoom = Math.max(minZoom, Math.min(maxZoom, newZoom));
      inner.style.transform = `scale(${zoom})`;
      inner.style.width = baseW * zoom + 'px';
      inner.style.height = baseH * zoom + 'px';
      slider.value = Math.round(zoom * 100);
      label.textContent = Math.round(zoom * 100) + '%';
      if (center) {
        pan.scrollLeft = (inner.offsetWidth - pan.clientWidth) / 2;
        pan.scrollTop = (inner.offsetHeight - pan.clientHeight) / 2;
      }
    }

    // Zoom to a pivot point (px, py in pan coords)
    function zoomTo(newZoom, px, py) {
      const oldZoom = zoom;
      newZoom = Math.max(minZoom, Math.min(maxZoom, newZoom));
      if (newZoom === oldZoom) return;
      // Calculate scroll so (px,py) stays fixed
      const relX = px + pan.scrollLeft;
      const relY = py + pan.scrollTop;
      setZoom(newZoom);
      const ratio = newZoom / oldZoom;
      pan.scrollLeft = relX * ratio - px;
      pan.scrollTop = relY * ratio - py;
    }

    // Slider: always zoom to center
    slider.addEventListener('input', () => {
      setZoom(parseInt(slider.value) / 100, true);
    });
    // Reset: zoom to 1, center
    resetBtn.addEventListener('click', () => setZoom(1, true));
    // Wheel: zoom to cursor
    pan.addEventListener('wheel', e => {
      if (e.target.closest('.diagram-zoom')) return;
      e.preventDefault();
      const rect = pan.getBoundingClientRect();
      const px = e.clientX - rect.left;
      const py = e.clientY - rect.top;
      const delta = e.deltaY > 0 ? -0.1 : 0.1;
      zoomTo(zoom + delta, px, py);
    }, { passive: false });
    // Drag: pan by mouse
    pan.addEventListener('mousedown', e => {
      if (e.target.closest('.diagram-zoom')) return;
      dragging = true;
      pan.classList.add('is-dragging');
      dragX = e.clientX; dragY = e.clientY;
      scrollL = pan.scrollLeft; scrollT = pan.scrollTop;
    });
    window.addEventListener('mousemove', e => {
      if (!dragging) return;
      pan.scrollLeft = scrollL - (e.clientX - dragX);
      pan.scrollTop = scrollT - (e.clientY - dragY);
    });
    window.addEventListener('mouseup', () => {
      dragging = false;
      pan.classList.remove('is-dragging');
    });
    // Touch: pinch to zoom, drag to pan
    pan.addEventListener('touchstart', e => {
      if (e.touches.length === 2) {
        lastTouchDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        lastTouchMid = {
          x: (e.touches[0].clientX + e.touches[1].clientX) / 2 - pan.getBoundingClientRect().left,
          y: (e.touches[0].clientY + e.touches[1].clientY) / 2 - pan.getBoundingClientRect().top
        };
      } else if (e.touches.length === 1) {
        dragging = true;
        dragX = e.touches[0].clientX; dragY = e.touches[0].clientY;
        scrollL = pan.scrollLeft; scrollT = pan.scrollTop;
      }
    }, { passive: false });
    pan.addEventListener('touchmove', e => {
      if (e.touches.length === 2 && lastTouchDist && lastTouchMid) {
        e.preventDefault();
        const dist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        const mid = {
          x: (e.touches[0].clientX + e.touches[1].clientX) / 2 - pan.getBoundingClientRect().left,
          y: (e.touches[0].clientY + e.touches[1].clientY) / 2 - pan.getBoundingClientRect().top
        };
        const scale = dist / lastTouchDist;
        zoomTo(zoom * scale, mid.x, mid.y);
        lastTouchDist = dist;
        lastTouchMid = mid;
      } else if (e.touches.length === 1 && dragging) {
        e.preventDefault();
        pan.scrollLeft = scrollL - (e.touches[0].clientX - dragX);
        pan.scrollTop = scrollT - (e.touches[0].clientY - dragY);
      }
    }, { passive: false });
    pan.addEventListener('touchend', e => {
      if (e.touches.length < 2) {
        lastTouchDist = null;
        lastTouchMid = null;
      }
      if (e.touches.length === 0) {
        dragging = false;
        pan.classList.remove('is-dragging');
      }
    });
    // On resize, re-center
    window.addEventListener('resize', () => setZoom(zoom, true));
    // Start
    measureBase();
  }
  // Init all diagrams
  document.querySelectorAll('.diagram-pan').forEach(DiagramPanZoom);
})();
</script>

<div class="diagram-pan">
  <div class="diagram-zoom">
    <input type="range" min="40" max="400" value="100">
    <span class="diagram-level">100%</span>
    <button>Reset</button>
  </div>
  <div class="diagram-inner">
```mermaid
graph TD
    OWNER["👤 Owner<br/>nan-gogh"]
    MEMBERS["👥 Org Members<br/>invited by username"]
    ORG["📋 Membership Roster<br/>access-control list only"]
    OAUTH["🔐 OAuth App<br/>credentials shared<br/>with Cloudflare"]
    
    MEDIA_REPO["📦 ultrabroken-media<br/>Worker source + workflows"]
    WIKI_REPO["📚 ultrabroken-documentation<br/>MkDocs wiki source"]
    DEPLOY["⚙️ deploy.yml<br/>auto-deploy Worker"]
    OPTIMIZE["🖼️ optimize.yml<br/>AVIF via sharp"]
    TRANSCODE["🎬 transcode.yml<br/>AV1 via ffmpeg"]
    
    ACCESS["🚪 Cloudflare Access<br/>Zero Trust gateway<br/>requires org membership"]
    WORKER["💼 Worker<br/>serves files + /manage UI<br/>upload · delete · purge"]
    R2["🗄️ R2 Object Storage<br/>screens/ · video/ · social/"]
    PAGES["📖 GitHub Pages<br/>hosts the wiki"]
    VISITOR["👁️ Wiki Visitors<br/>public — no auth"]
    
    OWNER -->|owns| ORG
    MEMBERS -->|member of| ORG
    ORG -->|membership check| ACCESS
    OAUTH -->|credentials| ACCESS
    OWNER -->|GitHub login| ACCESS
    MEMBERS -->|GitHub login| ACCESS
    ACCESS -->|authenticated| WORKER
    WORKER -->|read / write| R2
    
    MEDIA_REPO -->|push triggers| DEPLOY
    DEPLOY -->|wrangler deploy| ACCESS
    DEPLOY -->|dispatch via PAT| OPTIMIZE
    DEPLOY -->|dispatch via PAT| TRANSCODE
    OPTIMIZE -->|convert + reupload| R2
    TRANSCODE -->|transcode + reupload| R2
    
    WIKI_REPO -->|push triggers| PAGES
    PAGES -->|media links| R2
    VISITOR -->|reads| PAGES
    VISITOR -->|loads media| R2
```
  </div>
</div>
