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

<script>
(function(){
  function DiagramPanZoom(pan) {
    var inner = pan.querySelector('.diagram-inner');
    var slider = pan.querySelector('input[type=range]');
    var label = pan.querySelector('.diagram-level');
    var resetBtn = pan.querySelector('button');
    var zoom = 1, minZoom = 0.4, maxZoom = 4;
    var baseW = 0, baseH = 0;
    var dragging = false, dragX = 0, dragY = 0, scrollL = 0, scrollT = 0;
    var lastTouchDist = null, lastTouchMid = null;

    function measureBase() {
      var mermaid = inner.querySelector('.mermaid');
      if (!mermaid || pan.clientWidth === 0) return requestAnimationFrame(measureBase);
      if (mermaid.textContent.trim().length > 0) return requestAnimationFrame(measureBase);
      var rect = mermaid.getBoundingClientRect();
      if (rect.width === 0 || rect.height === 0) return requestAnimationFrame(measureBase);
      inner.style.transform = '';
      inner.style.margin = '0';
      baseW = inner.offsetWidth;
      var cs = getComputedStyle(inner);
      baseH = Math.ceil(rect.height + parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom));
      applyZoom(1, true);
    }

    // Apply layout: inner stays at natural size, transform does visual scaling,
    // constant half-viewport padding lets content be positioned anywhere via scroll
    function applyLayout() {
      inner.style.transform = 'scale(' + zoom + ')';
      inner.style.width = baseW + 'px';
      inner.style.height = baseH + 'px';
      var padX = pan.clientWidth / 2;
      var padY = pan.clientHeight / 2;
      inner.style.marginLeft = padX + 'px';
      inner.style.marginTop = padY + 'px';
      inner.style.marginRight = Math.max(0, baseW * (zoom - 1)) + padX + 'px';
      inner.style.marginBottom = Math.max(0, baseH * (zoom - 1)) + padY + 'px';
      slider.value = Math.round(zoom * 100);
      label.textContent = Math.round(zoom * 100) + '%';
    }

    // Zoom and center scroll (used for init and reset only)
    function applyZoom(newZoom, center) {
      zoom = Math.max(minZoom, Math.min(maxZoom, newZoom));
      applyLayout();
      if (center) {
        // Content left edge is at scroll offset padX; center it in viewport
        pan.scrollLeft = pan.clientWidth / 2 + baseW * zoom / 2 - pan.clientWidth / 2;
        pan.scrollTop = pan.clientHeight / 2 + baseH * zoom / 2 - pan.clientHeight / 2;
      }
    }

    // Zoom keeping the point at (px, py) in viewport coords fixed
    function zoomAt(newZoom, px, py) {
      newZoom = Math.max(minZoom, Math.min(maxZoom, newZoom));
      if (newZoom === zoom) return;
      var padX = pan.clientWidth / 2;
      var padY = pan.clientHeight / 2;
      // Convert viewport point to unscaled content coordinates
      var cx = (pan.scrollLeft + px - padX) / zoom;
      var cy = (pan.scrollTop + py - padY) / zoom;
      zoom = newZoom;
      applyLayout();
      // Reposition scroll so the same content point is under (px, py)
      pan.scrollLeft = padX + cx * zoom - px;
      pan.scrollTop = padY + cy * zoom - py;
    }

    // Slider: zoom toward viewport center (not a positional reset)
    slider.addEventListener('input', function() {
      zoomAt(parseInt(slider.value) / 100, pan.clientWidth / 2, pan.clientHeight / 2);
    });
    // Reset: zoom to 1, center
    resetBtn.addEventListener('click', function() { applyZoom(1, true); });

    // Wheel: zoom to cursor
    pan.addEventListener('wheel', function(e) {
      if (e.target.closest('.diagram-zoom')) return;
      e.preventDefault();
      var r = pan.getBoundingClientRect();
      zoomAt(zoom + (e.deltaY > 0 ? -0.1 : 0.1), e.clientX - r.left, e.clientY - r.top);
    }, { passive: false });

    // Drag: pan by mouse
    pan.addEventListener('mousedown', function(e) {
      if (e.target.closest('.diagram-zoom')) return;
      dragging = true;
      pan.classList.add('is-dragging');
      dragX = e.clientX; dragY = e.clientY;
      scrollL = pan.scrollLeft; scrollT = pan.scrollTop;
    });
    window.addEventListener('mousemove', function(e) {
      if (!dragging) return;
      pan.scrollLeft = scrollL - (e.clientX - dragX);
      pan.scrollTop = scrollT - (e.clientY - dragY);
    });
    window.addEventListener('mouseup', function() {
      dragging = false;
      pan.classList.remove('is-dragging');
    });

    // Touch: pinch to zoom + pan, single-finger drag to pan
    pan.addEventListener('touchstart', function(e) {
      if (e.touches.length === 2) {
        var r = pan.getBoundingClientRect();
        lastTouchDist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
        lastTouchMid = {x: (e.touches[0].clientX + e.touches[1].clientX) / 2 - r.left, y: (e.touches[0].clientY + e.touches[1].clientY) / 2 - r.top};
      } else if (e.touches.length === 1) {
        dragging = true;
        dragX = e.touches[0].clientX; dragY = e.touches[0].clientY;
        scrollL = pan.scrollLeft; scrollT = pan.scrollTop;
      }
    }, { passive: false });
    pan.addEventListener('touchmove', function(e) {
      if (e.touches.length === 2 && lastTouchDist !== null) {
        e.preventDefault();
        var r = pan.getBoundingClientRect();
        var dist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
        var mid = {x: (e.touches[0].clientX + e.touches[1].clientX) / 2 - r.left, y: (e.touches[0].clientY + e.touches[1].clientY) / 2 - r.top};
        // Pan by pinch center movement
        pan.scrollLeft -= (mid.x - lastTouchMid.x);
        pan.scrollTop -= (mid.y - lastTouchMid.y);
        // Zoom towards pinch center
        if (dist !== lastTouchDist) {
          zoomAt(zoom * dist / lastTouchDist, mid.x, mid.y);
        }
        lastTouchDist = dist;
        lastTouchMid = mid;
      } else if (e.touches.length === 1 && dragging) {
        e.preventDefault();
        pan.scrollLeft = scrollL - (e.touches[0].clientX - dragX);
        pan.scrollTop = scrollT - (e.touches[0].clientY - dragY);
      }
    }, { passive: false });
    pan.addEventListener('touchend', function(e) {
      if (e.touches.length < 2) { lastTouchDist = null; lastTouchMid = null; }
      if (e.touches.length === 1) {
        // One finger remains after pinch — reinit drag state so it doesn't snap
        dragging = true;
        dragX = e.touches[0].clientX; dragY = e.touches[0].clientY;
        scrollL = pan.scrollLeft; scrollT = pan.scrollTop;
      }
      if (e.touches.length === 0) { dragging = false; pan.classList.remove('is-dragging'); }
    });
    
    window.addEventListener('resize', function() { applyZoom(zoom, true); });
    measureBase();
  }
  document.querySelectorAll('.diagram-pan').forEach(DiagramPanZoom);
})();
</script>
