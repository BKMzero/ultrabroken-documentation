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
The archives run on open-source tooling across GitHub and Cloudflare. Media uploads require authentication via the `ultrabroken-archivists` GitHub organisation — membership is managed by invite only. No personal data is collected; Cloudflare Access verifies org membership through GitHub OAuth and does not store credentials beyond session tokens.

<div class="diagram-pan">
  <div class="diagram-zoom">
    <input type="range" min="40" max="400" value="100" oninput="diagramSlide(this)">
    <span class="diagram-level">100%</span>
    <button onclick="diagramReset(this)">Reset</button>
  </div>
  <div class="diagram-inner">

``` mermaid
graph LR
    subgraph people ["Collaborators"]
        direction TB
        OWNER["Owner<br/>nan-gogh"]
        MEMBERS["Org Members<br/>invited by username"]
    end

    subgraph org ["GitHub Org: ultrabroken-archivists"]
        direction TB
        ORG["Membership Roster<br/>access-control list only"]
        OAUTH["OAuth App<br/>credentials shared<br/>with Cloudflare"]
    end

    subgraph repos ["GitHub Repos (nan-gogh)"]
        direction TB
        WIKI_REPO["ultrabroken-documentation<br/>MkDocs wiki source"]
        MEDIA_REPO["ultrabroken-media<br/>Worker source + workflows"]
        subgraph actions ["GitHub Actions"]
            direction TB
            DEPLOY["deploy.yml<br/>auto-deploy Worker"]
            OPTIMIZE["optimize.yml<br/>AVIF via sharp"]
            TRANSCODE["transcode.yml<br/>AV1 via ffmpeg"]
        end
    end

    subgraph cloudflare ["Cloudflare"]
        direction TB
        ACCESS["Cloudflare Access<br/>Zero Trust gateway<br/>requires org membership"]
        WORKER["Worker<br/>serves files + /manage UI<br/>upload · delete · purge"]
        R2["R2 Object Storage<br/>screens/ · video/ · social/"]
        PAGES["GitHub Pages<br/>hosts the wiki"]
    end

    VISITOR["Wiki Visitors<br/>public — no auth"]

    OWNER -->|owns| ORG
    MEMBERS -->|member of| ORG
    ORG -->|membership check| ACCESS
    OAUTH -->|credentials| ACCESS
    OWNER & MEMBERS -->|GitHub login| ACCESS
    ACCESS -->|authenticated| WORKER
    WORKER -->|read / write| R2
    WORKER -->|dispatch via PAT| OPTIMIZE & TRANSCODE
    OPTIMIZE -->|convert + reupload| R2
    TRANSCODE -->|transcode + reupload| R2
    DEPLOY -->|wrangler deploy| WORKER
    MEDIA_REPO -->|push triggers| DEPLOY
    WIKI_REPO -->|push triggers| PAGES
    PAGES -->|media links| R2
    VISITOR -->|reads| PAGES
    VISITOR -->|loads media| R2
```

  </div>
</div>

<script>
(function() {
  function applyZoom(pan, newZoom, pivotX, pivotY) {
    var inner = pan.querySelector('.diagram-inner');
    var slider = pan.querySelector('input[type=range]');
    var label = pan.querySelector('.diagram-level');
    var oldZoom = parseFloat(inner.dataset.zoom || 1);
    newZoom = Math.max(0.4, Math.min(4, newZoom));
    if (newZoom === oldZoom) return;
    var ratio = newZoom / oldZoom;
    var barH = (pan.querySelector('.diagram-zoom') || {}).offsetHeight || 0;
    inner.dataset.zoom = newZoom;
    inner.style.zoom = newZoom;
    slider.value = Math.round(newZoom * 100);
    label.textContent = Math.round(newZoom * 100) + '%';
    pan.scrollLeft = (pan.scrollLeft + pivotX) * ratio - pivotX;
    pan.scrollTop  = (pan.scrollTop + pivotY - barH) * ratio + barH - pivotY;
  }

  window.diagramSlide = function(slider) {
    var pan = slider.closest('.diagram-pan');
    applyZoom(pan, parseInt(slider.value) / 100, pan.clientWidth / 2, pan.clientHeight / 2);
  };

  window.diagramReset = function(btn) {
    var pan = btn.closest('.diagram-pan');
    applyZoom(pan, 1, pan.clientWidth / 2, pan.clientHeight / 2);
  };

  document.querySelectorAll('.diagram-pan').forEach(function(pan) {
    var inner = pan.querySelector('.diagram-inner');
    inner.dataset.zoom = 1;
    var startX, startY, scrollL, scrollT;
    pan.addEventListener('mousedown', function(e) {
      if (e.target.closest('.diagram-zoom')) return;
      pan.classList.add('is-dragging');
      startX = e.clientX; startY = e.clientY;
      scrollL = pan.scrollLeft; scrollT = pan.scrollTop;
    });
    window.addEventListener('mousemove', function(e) {
      if (!pan.classList.contains('is-dragging')) return;
      pan.scrollLeft = scrollL - (e.clientX - startX);
      pan.scrollTop  = scrollT - (e.clientY - startY);
    });
    window.addEventListener('mouseup', function() {
      pan.classList.remove('is-dragging');
    });
    pan.addEventListener('wheel', function(e) {
      if (e.target.closest('.diagram-zoom')) return;
      e.preventDefault();
      var rect = pan.getBoundingClientRect();
      var px = e.clientX - rect.left;
      var py = e.clientY - rect.top;
      var cur = parseFloat(inner.dataset.zoom || 1);
      var delta = e.deltaY > 0 ? -0.1 : 0.1;
      applyZoom(pan, cur + delta, px, py);
    }, { passive: false });
  });
})();
</script>
