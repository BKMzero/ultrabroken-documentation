# Diff changelog from 1e0a6934b4d5a929724e9c68e7ea36c7ee804b98 to HEAD
Generated: 2026-02-25T09:27:02.5683574+01:00

*** COMMIT: 8b403b1d8832de8afa80dc84d0e729767f6dc221
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 11:08:40 2026 +0100
Subject: fix: clarify memorial section description in index

commit 8b403b1d8832de8afa80dc84d0e729767f6dc221
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 11:08:40 2026 +0100

    fix: clarify memorial section description in index

diff --git a/docs/wiki/index.md b/docs/wiki/index.md
index 5cad01422..958dcef1f 100644
--- a/docs/wiki/index.md
+++ b/docs/wiki/index.md
@@ -20,4 +20,4 @@ This site is a community-driven encyclopedia of glitches, techniques, and invest
 - **[Out of Bounds section](oob/)** - Glitches and strats that get you Out of Bounds
 - **[Message Not Found](mnf/)** - Explore the powers of MessageNotFound items in this section
 - **[Overload section](overload/)** - Detailed setups and techniques for reaching Overload states
-- **[Memorial](memorial/)** - Leaderboard and hall of fame
\ No newline at end of file
+- **[Memorial](memorial/)** - Leaderboard for glitch hunters and hall of fame for archivists
\ No newline at end of file

----

*** COMMIT: abf4a84cec15918305a1309129f9c5aac2ed77eb
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 11:38:12 2026 +0100
Subject: Add social media links and leaderboard data in JSON format

commit abf4a84cec15918305a1309129f9c5aac2ed77eb
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 11:38:12 2026 +0100

    Add social media links and leaderboard data in JSON format
    
    - Created hunter-socials.json to store social media links for various users.
    - Added leaderboard-data.json containing ranking information, user names, URLs, and counts.

diff --git a/.cache/plugin/social/manifest.json b/.cache/plugin/social/manifest.json
deleted file mode 100644
index 9e26dfeeb..000000000
--- a/.cache/plugin/social/manifest.json
+++ /dev/null
@@ -1 +0,0 @@
-{}
\ No newline at end of file
diff --git a/docs/wiki/glitchcraft/_grimoire-data.json b/docs/assets/data/grimoire-data.json
similarity index 100%
rename from docs/wiki/glitchcraft/_grimoire-data.json
rename to docs/assets/data/grimoire-data.json
diff --git a/docs/assets/scripts/hunter-socials.json b/docs/assets/data/hunter-socials.json
similarity index 80%
rename from docs/assets/scripts/hunter-socials.json
rename to docs/assets/data/hunter-socials.json
index 5de2a3b04..6a1de0e35 100644
--- a/docs/assets/scripts/hunter-socials.json
+++ b/docs/assets/data/hunter-socials.json
@@ -7,5 +7,6 @@
   "NaN Gogh": "https://x.com/_nan_gogh",
   "suusi": "https://www.youtube.com/channel/UCbUwlQ_88XfXD2bfU_4kxYg",
   "GamSla341": "https://www.youtube.com/@gamsla3413",
-  "Modoki_returns": "https://twitter.com/Modoki_returns"
+  "Modoki_returns": "https://twitter.com/Modoki_returns",
+  "Suishi": "https://www.youtube.com/@SuishiYT"
 }
diff --git a/docs/assets/scripts/leaderboard-data.json b/docs/assets/data/leaderboard-data.json
similarity index 98%
rename from docs/assets/scripts/leaderboard-data.json
rename to docs/assets/data/leaderboard-data.json
index 98c048261..b424f9e55 100644
--- a/docs/assets/scripts/leaderboard-data.json
+++ b/docs/assets/data/leaderboard-data.json
@@ -1,5 +1,5 @@
 {
-  "total": 137,
+  "total": 136,
   "updated": "2026-02-24",
   "entries": [
     {
@@ -338,6 +338,12 @@
       "url": null,
       "count": 2
     },
+    {
+      "rank": 14,
+      "name": "Tahata",
+      "url": null,
+      "count": 2
+    },
     {
       "rank": 14,
       "name": "Tauktes",
@@ -719,7 +725,7 @@
     {
       "rank": 15,
       "name": "Suishi",
-      "url": null,
+      "url": "https://www.youtube.com/@SuishiYT",
       "count": 1
     },
     {
@@ -728,18 +734,6 @@
       "url": null,
       "count": 1
     },
-    {
-      "rank": 15,
-      "name": "Tahata",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Tahata",
-      "url": null,
-      "count": 1
-    },
     {
       "rank": 15,
       "name": "Takosensai1",
diff --git a/docs/assets/hooks/contributor_links.py b/docs/assets/hooks/contributor_links.py
index 715917b0d..6d14acc69 100644
--- a/docs/assets/hooks/contributor_links.py
+++ b/docs/assets/hooks/contributor_links.py
@@ -19,7 +19,7 @@ from pathlib import Path
 
 _CONTRIBUTORS_JSON = (
     Path(__file__).parent.parent  # docs/assets/
-    / 'scripts' / 'hunter-socials.json'
+    / 'data' / 'hunter-socials.json'
 )
 
 # Loaded once per build on first page processed
diff --git a/docs/assets/scripts/grimoire-filter.js b/docs/assets/scripts/grimoire-filter.js
index abf5513c6..09ad78027 100644
--- a/docs/assets/scripts/grimoire-filter.js
+++ b/docs/assets/scripts/grimoire-filter.js
@@ -59,17 +59,12 @@
      Data
      ================================================================ */
   function fetchData(cb) {
-    fetch('../_grimoire-data.json').then(function (r) {
+    fetch('../../assets/data/grimoire-data.json').then(function (r) {
       if (!r.ok) throw new Error(r.status);
       return r.json();
-    }).then(cb).catch(function () {
-      fetch('./_grimoire-data.json').then(function (r) {
-        if (!r.ok) throw new Error(r.status);
-        return r.json();
-      }).then(cb).catch(function (e) {
-        console.error('[Grimoire] load failed', e);
-        cb(null);
-      });
+    }).then(cb).catch(function (e) {
+      console.error('[Grimoire] load failed', e);
+      cb(null);
     });
   }
 
diff --git a/docs/assets/scripts/leaderboard.js b/docs/assets/scripts/leaderboard.js
index b301956fe..c6824e6a4 100644
--- a/docs/assets/scripts/leaderboard.js
+++ b/docs/assets/scripts/leaderboard.js
@@ -34,7 +34,7 @@
      ================================================================ */
 
   function fetchData(cb) {
-    fetch('../../assets/scripts/leaderboard-data.json')
+    fetch('../../assets/data/leaderboard-data.json')
       .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
       .then(cb)
       .catch(function () { cb(null); });
diff --git a/docs/wiki/build_bm25_index.py b/docs/wiki/build_bm25_index.py
index 3fd3b3d56..238704def 100644
--- a/docs/wiki/build_bm25_index.py
+++ b/docs/wiki/build_bm25_index.py
@@ -334,7 +334,7 @@ def build_grimoire_data(output: str):
 
 
 
-_CONTRIBUTORS_JSON = ROOT / 'docs' / 'assets' / 'scripts' / 'hunter-socials.json'
+_CONTRIBUTORS_JSON = ROOT / 'docs' / 'assets' / 'data' / 'hunter-socials.json'
 
 
 def build_leaderboard(json_path: str):
@@ -400,15 +400,15 @@ def main():
     p.add_argument('--docs-dir', default='docs', help='Path under the repo root to read markdown from (e.g. docs/wiki)')
     p.add_argument(
         '--grimoire-output', '-g',
-        default=str(ROOT / 'docs' / 'wiki' / 'glitchcraft' / '_grimoire-data.json'),
-        help='Path to write _grimoire-data.json (default: docs/wiki/glitchcraft/_grimoire-data.json)',
+        default=str(ROOT / 'docs' / 'assets' / 'data' / 'grimoire-data.json'),
+        help='Path to write grimoire-data.json (default: docs/assets/data/grimoire-data.json)',
     )
     p.add_argument('--no-grimoire', dest='grimoire', action='store_false',
                    help='Skip generating grimoire-data.json')
     p.add_argument(
         '--leaderboard-output', '-l',
-        default=str(ROOT / 'docs' / 'assets' / 'scripts' / 'leaderboard-data.json'),
-        help='Path to write leaderboard-data.json (default: docs/assets/scripts/leaderboard-data.json)',
+        default=str(ROOT / 'docs' / 'assets' / 'data' / 'leaderboard-data.json'),
+        help='Path to write leaderboard-data.json (default: docs/assets/data/leaderboard-data.json)',
     )
     p.add_argument('--no-leaderboard', dest='leaderboard', action='store_false',
                    help='Skip updating the Hall of Fame leaderboard')
diff --git a/docs/wiki/memorial.md b/docs/wiki/memorial.md
index 610d816f4..39a361d6e 100644
--- a/docs/wiki/memorial.md
+++ b/docs/wiki/memorial.md
@@ -36,4 +36,4 @@ The glitch hunting, speedrunning, and research communities that made this docume
 
 ---
 
-**Thank you** to everyone who participated in discovering, testing, documenting, and sharing glitches. This community effort pushes the boundaries of what's possible in The Legend of Zelda: Tears of the Kingdom, and continues to inspire new discoveries.
+**Thank you** to everyone who participates in discovering, testing, documenting, and sharing glitches. This community effort pushes the boundaries of what's possible in The Legend of Zelda: Tears of the Kingdom, and continues to inspire new discoveries.

----

*** COMMIT: 245996c0e27d505655bb8c70c6d4be06f36d43a9
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 12:05:40 2026 +0100
Subject: fix: update fetch path for grimoire data

commit 245996c0e27d505655bb8c70c6d4be06f36d43a9
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 12:05:40 2026 +0100

    fix: update fetch path for grimoire data

diff --git a/docs/assets/scripts/grimoire-filter.js b/docs/assets/scripts/grimoire-filter.js
index 09ad78027..4406e8a5c 100644
--- a/docs/assets/scripts/grimoire-filter.js
+++ b/docs/assets/scripts/grimoire-filter.js
@@ -59,7 +59,7 @@
      Data
      ================================================================ */
   function fetchData(cb) {
-    fetch('../../assets/data/grimoire-data.json').then(function (r) {
+    fetch('../../../assets/data/grimoire-data.json').then(function (r) {
       if (!r.ok) throw new Error(r.status);
       return r.json();
     }).then(cb).catch(function (e) {

----

*** COMMIT: d0a54f76d6ef8374efaebd0740c4abf3f70fd91f
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 12:21:16 2026 +0100
Subject: refactor: enhance evidence rendering and clarify related sources handling

commit d0a54f76d6ef8374efaebd0740c4abf3f70fd91f
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 12:21:16 2026 +0100

    refactor: enhance evidence rendering and clarify related sources handling

diff --git a/docs/assets/scripts/ai-worker-client.js b/docs/assets/scripts/ai-worker-client.js
index 571baeeb0..530f89d09 100644
--- a/docs/assets/scripts/ai-worker-client.js
+++ b/docs/assets/scripts/ai-worker-client.js
@@ -12,17 +12,13 @@
     return e;
   }
   
-  // Internal flag: controls whether model-returned `Source:` lines are rendered.
-  // This is intentionally an internal toggle (not user-facing). Set to `true`
-  // to enable rendering of model-supplied sources, or `false` to disable.
+  // Internal flag: controls whether model-returned source titles are rendered
+  // under a "Related" heading as search links. Set to `true` to enable, `false`
+  // to hide them entirely. Worker evidence ("Resources") is always shown.
   const SHOW_MODEL_SOURCES = true;
-  // Internal toggle: when true, model-supplied source titles are rendered as
-  // homepage search links (`/wiki/?q=Title`) that navigate to the wiki root
-  // and auto-trigger the search bar via the `?q=` param handler in search-link.js.
-  // When false they render as direct wiki page links.
-  const USE_TITLE_SEARCH_LINKS = false;
-  // Base URL used to build `?q=` search links when USE_TITLE_SEARCH_LINKS is true.
-  const WIKI_SEARCH_BASE = 'https://nan-gogh.github.io/ultrabroken-documentation/wiki/';
+  // Site root and wiki base used to build direct page links and search links.
+  const SITE_ROOT = 'https://nan-gogh.github.io/ultrabroken-documentation';
+  const WIKI_SEARCH_BASE = SITE_ROOT + '/wiki/';
   // Hard cap on query length sent to the worker. Configurable via `window.AI_MAX_QUERY_CHARS`.
   const MAX_QUERY_CHARS = 50;
   // Idle texts shown in the output area before any query is made and after
@@ -206,7 +202,8 @@
       w._idleMode = true;    // true while showing idle/cleared state; false while showing a query result
       w._silenceMode = false; // true after a silence response while the user hasn't yet focused the input
       w._lastResponseText = null; // raw markdown response text stored for share-to-clipboard
-      w._lastSources = [];        // rendered source titles extracted after response, for share footer
+      w._lastResources = [];      // rendered Resource entries [{text, href}] (direct wiki links)
+      w._lastRelated = [];        // rendered Related entries [{text, query}] (search links)
       // No user-facing toggle: `SHOW_MODEL_SOURCES` controls whether model-
       // returned `Source:` lines are rendered. This is intentionally internal.
       // The Worker now returns structured `response_text`, optional `response_sources` (text block)
@@ -219,7 +216,8 @@
         try{ if (typeof lockInput === 'function') lockInput(); }catch(e){}
         w._idleMode = false;
         w._lastResponseText = null;
-        w._lastSources = [];
+        w._lastResources = [];
+        w._lastRelated = [];
         try{ if (typeof updateVisibility === 'function') updateVisibility(); }catch(e){}
         w.out.textContent = LOADING_TEXT;
         if (w.evidence) w.evidence.innerHTML = '';
@@ -293,97 +291,60 @@
         } else {
           w.out.textContent = '';
         }
-        // Render model-provided structured `r.sources` as links when present
+        // ÔöÇÔöÇ Resources: Worker-provided evidence as direct wiki links ÔöÇÔöÇ
         try{
-          //const base = 'https://nan-gogh.github.io/ultrabroken-documentation/wiki/';
-          const modelSources = Array.isArray(r.sources) ? r.sources : [];
-          const showModelSources = SHOW_MODEL_SOURCES && modelSources && modelSources.length;
-          // When rendering as homepage search links we need to dedupe model-provided
-          // sources and Worker-provided evidence so the final list contains
-          // unique search queries. `seenQueries` tracks already-emitted queries
-          // (case-sensitive, using the display string) and ensures the uppermost
-          // instance is kept.
-          const seenQueries = new Set();
-          if (showModelSources){
-            if (w.evidence && !w.evidence.querySelector('.ub-ai-resources')){
-              const heading = el('h2', { class: 'ub-ai-resources md-typeset' }, 'Resources');
-              if (w.evidence) w.evidence.appendChild(heading);
-              const sep = el('hr', { class: 'ub-ai-resources-sep' }, '');
-              if (w.evidence) w.evidence.appendChild(sep);
-            }
-            let list = el('ul', { class: 'ub-ai-evidence-list' }, []);
-            if (w.evidence) w.evidence.appendChild(list);
-            const siteRoot = 'https://nan-gogh.github.io/ultrabroken-documentation';
-            modelSources.forEach(s => {
-              const text = s.title || (s.path||s.id) || '';
-              const query = String(text).trim();
-              if (USE_TITLE_SEARCH_LINKS) {
-                if (seenQueries.has(query)) return; // skip duplicate
-                seenQueries.add(query);
-                const href = 'search:' + encodeURIComponent(query);
-                const a = el('a', { href: href, class: 'search-link', 'data-query': query }, text);
-                const li = el('li', {}, a);
-                list.appendChild(li);
+          const ev = r.evidence || [];
+          if (Array.isArray(ev) && ev.length && w.evidence){
+            const heading = el('h2', { class: 'ub-ai-resources md-typeset' }, 'Resources');
+            w.evidence.appendChild(heading);
+            const sep = el('hr', { class: 'ub-ai-resources-sep' }, '');
+            w.evidence.appendChild(sep);
+            const list = el('ul', { class: 'ub-ai-evidence-list' }, []);
+            w.evidence.appendChild(list);
+            ev.forEach(item => {
+              const id = item.id || item.path || '';
+              const titleText = item.title || '';
+              let slug = String(id).replace(/\.md$/,'').replace(/^\/+|\/+$/g, '');
+              const text = titleText || slug || id;
+              if (!text.trim()) return;
+              // Build direct wiki link
+              let href;
+              if (slug.startsWith('wiki/')) {
+                href = SITE_ROOT + '/' + slug + '/';
               } else {
-                const p = (s.path || s.id || '').toString();
-                let href;
-                if (p && p.startsWith('/wiki/')) {
-                  href = siteRoot + p;
-                } else {
-                  const slug = p.replace(/^\/+|\/+$/g,'').replace(/\.md$/,'');
-                  href = WIKI_SEARCH_BASE + encodeURI(slug);
-                }
-                const a = el('a', { href: href, target: '_blank', rel: 'noopener noreferrer' }, text);
-                const li = el('li', {}, a);
-                list.appendChild(li);
+                href = SITE_ROOT + '/wiki/' + slug + '/';
               }
+              const a = el('a', { href: href, target: '_blank', rel: 'noopener noreferrer' }, text);
+              const li = el('li', {}, a);
+              list.appendChild(li);
+              w._lastResources.push({ text: text.trim(), href: href });
             });
           }
+        }catch(e){ /* ignore evidence rendering errors */ }
 
-          // Always render Worker-provided evidence as authoritative clickable links
-          try{
-            const ev = r.evidence || [];
-            // Worker evidence rendering controlled by internal flag.
-            if (Array.isArray(ev) && ev.length){
-              // reuse existing list if model sources created one, otherwise create
-              let list = w.evidence && w.evidence.querySelector && w.evidence.querySelector('.ub-ai-evidence-list');
-              if (!list) { list = el('ul', { class: 'ub-ai-evidence-list' }, []); if (w.evidence) w.evidence.appendChild(list); }
-              ev.forEach(item => {
-                const id = item.id || item.path || '';
-                // Prefer item.title for search queries; fallback to normalized id
-                const titleText = item.title || '';
-                // Normalize id to a wiki path without .md
-                let slug = String(id).replace(/\.md$/,'').replace(/^\/+|\/+$/g, '');
-                const text = titleText || slug || id;
-                if (USE_TITLE_SEARCH_LINKS) {
-                  const query = String(text).trim();
-                  if (seenQueries.has(query)) return; // already emitted by model sources
-                  seenQueries.add(query);
-                  const href = 'search:' + encodeURIComponent(query);
-                  const a = el('a', { href: href, class: 'search-link', 'data-query': query }, text);
-                  const li = el('li', {}, a);
-                  list.appendChild(li);
-                } else {
-                  const href = WIKI_SEARCH_BASE + encodeURI(slug);
-                  const a = el('a', { href: href, target: '_blank', rel: 'noopener noreferrer' }, text);
-                  const li = el('li', {}, a);
-                  list.appendChild(li);
-                }
-              });
-            }
-          }catch(e){ /* ignore rendering errors */ }
-        }catch(e){ /* ignore model source parsing errors */ }
-        // Collect rendered source titles from the evidence list for share-to-clipboard
+        // ÔöÇÔöÇ Related: Model-provided sources as search links ÔöÇÔöÇ
         try{
-          w._lastSources = [];
-          if (w.evidence) {
-            w.evidence.querySelectorAll('.ub-ai-evidence-list a, .ub-ai-evidence-list button').forEach(a => {
-              const t = a.getAttribute('data-query') || a.textContent || '';
-              if (t.trim()) w._lastSources.push(t.trim());
+          const modelSources = Array.isArray(r.sources) ? r.sources : [];
+          if (SHOW_MODEL_SOURCES && modelSources.length && w.evidence){
+            const heading = el('h2', { class: 'ub-ai-related md-typeset' }, 'Related');
+            w.evidence.appendChild(heading);
+            const sep = el('hr', { class: 'ub-ai-related-sep' }, '');
+            w.evidence.appendChild(sep);
+            const list = el('ul', { class: 'ub-ai-related-list' }, []);
+            w.evidence.appendChild(list);
+            modelSources.forEach(s => {
+              const text = s.title || (s.path || s.id) || '';
+              const query = String(text).trim();
+              if (!query) return;
+              const href = 'search:' + encodeURIComponent(query);
+              const a = el('a', { href: href, class: 'search-link', 'data-query': query }, text);
+              const li = el('li', {}, a);
+              list.appendChild(li);
+              w._lastRelated.push({ text: query, query: query });
             });
           }
-          try{ updateVisibility(); }catch(e){}
-        }catch(e){}
+        }catch(e){ /* ignore model source rendering errors */ }
+        try{ updateVisibility(); }catch(e){}
         // If nothing was rendered and there was no answer, show silence
         if (!w.out.textContent && (!r.evidence || !r.evidence.length)) w.out.textContent = 'silence';
         // Silence response: unlock the input so the user can edit/correct their query.
@@ -506,7 +467,8 @@
       const doClear = () => {
         w._idleMode = true;
         w._lastResponseText = null;
-        w._lastSources = [];
+        w._lastResources = [];
+        w._lastRelated = [];
         try{ if (typeof unlockInput === 'function') unlockInput(); }catch(e){}
         try{ if (typeof w.setValue === 'function') w.setValue(''); else if (w.input) w.input.value = ''; }catch(e){}
         // Only show idle text immediately if input is not focused; otherwise let the typewriter callback restore it.
@@ -534,7 +496,7 @@
         if (has) {
           try{ if (w.clear) { w.clear.style.display = 'flex'; w.clear.disabled = false; } }catch(e){}
           try{ if (w.btn)   { w.btn.style.display   = 'flex'; w.btn.disabled   = false; } }catch(e){}
-          // Share: visible with input text; enabled only when a response is available to copy
+          // Share: visible with input text; enabled only when a response is available
           try{ if (w.share) { w.share.style.display = 'flex'; w.share.disabled = !w._lastResponseText; } }catch(e){}
         } else {
           try{ if (w.clear) { w.clear.style.display = 'none'; w.clear.disabled = true; } }catch(e){}
@@ -683,14 +645,20 @@
                   const q = String((typeof w.getValue === 'function' ? w.getValue() : (w.input && w.input.value || '')) || '').trim();
                   if (q) queryHeading = '## ' + q + '\n\n';
                 } catch(e){}
-                // Build plain-text sources footer from rendered evidence titles
-                let sourcesFooter = '';
+                // Build Resources footer with direct wiki links
+                let resourcesFooter = '';
+                try {
+                  const res = w._lastResources || [];
+                  if (res.length) resourcesFooter = '\n\n### Resources\n' + res.map(r => '- [' + r.text + '](' + r.href + ')').join('\n');
+                } catch(e){}
+                // Build Related footer with search links
+                let relatedFooter = '';
                 try {
-                  const titles = w._lastSources || [];
-                  if (titles.length) sourcesFooter = '\n\n### Sources\n' + titles.map(t => '- [' + t + '](' + WIKI_SEARCH_BASE + '?q=' + encodeURIComponent(t) + ')').join('\n');
+                  const rel = w._lastRelated || [];
+                  if (rel.length) relatedFooter = '\n\n### Related\n' + rel.map(r => '- [' + r.text + '](' + WIKI_SEARCH_BASE + '?q=' + encodeURIComponent(r.query) + ')').join('\n');
                 } catch(e){}
                 const disclaimer = '\n\n### Disclaimer\nThis response was synthesized by [The Librarian](https://nan-gogh.github.io/ultrabroken-documentation/wiki/about/#ai-search). Take it with a grain of salt ÔÇö always verify against the source pages.';
-                const text = queryHeading + responseText.trim() + sourcesFooter + disclaimer;
+                const text = queryHeading + responseText.trim() + resourcesFooter + relatedFooter + disclaimer;
                 navigator.clipboard.writeText(text).then(() => {
                   try { showCopiedToast && showCopiedToast('Copied to clipboard'); } catch (e) {}
                 }).catch(err => {

----

*** COMMIT: 6e02a2e4d011ce43b6859c4c3a9b431992d72c4b
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 12:37:13 2026 +0100
Subject: feat: enhance scoring mechanism with abbreviation and alias matching boosts

commit 6e02a2e4d011ce43b6859c4c3a9b431992d72c4b
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 12:37:13 2026 +0100

    feat: enhance scoring mechanism with abbreviation and alias matching boosts

diff --git a/docs/worker/synonyms.json b/docs/worker/synonyms.json
index 51feefa25..220078dc9 100644
--- a/docs/worker/synonyms.json
+++ b/docs/worker/synonyms.json
@@ -2,6 +2,7 @@
   ["oob", "out of bounds", "out-of-bounds", "out of bounds glitch", "o.o.b.", "out of map"],
   ["sld", "persistent save load object transfer", "save-load-dupe", "save load dupe", "save/load dupe"],
   ["sd", "stick_desync", "stick desync", "stickdesync"],
+  ["sdc", "stick desync clip", "stick-desync-clip"],
   ["ultrabroken", "ultrabreak", "UB", "ultra-broken"],
   ["zuggle", "zuggling", "zugl", "zug", "zuggle overload"],
   ["tulin pump", "tulin-pump", "pump tulin", "tulin pumping", "tulinpump"],
diff --git a/docs/worker/worker.js b/docs/worker/worker.js
index 0ed0dc8d9..ca3f1a4ca 100644
--- a/docs/worker/worker.js
+++ b/docs/worker/worker.js
@@ -383,7 +383,35 @@ export default {
           const overlap = Math.max(setA && Object.keys(setA).length ? inter / Math.max(Object.keys(setA).length,1) : 0, 0);
           titleBoost = overlap; // 0..1
         }
-        const finalScore = score * (1 + (titleBoost * 0.25));
+        // Abbreviation exact-match boost: if any query token exactly matches the
+        // page's abbreviation field, apply a strong boost so e.g. "SDC" reliably
+        // surfaces the Stick Desync Clip page above pages that merely mention "SDC".
+        let abbrBoost = 0;
+        if (it.abbreviation){
+          const abbrLower = String(it.abbreviation).toLowerCase();
+          for (const t of qTokens){
+            if (String(t).toLowerCase() === abbrLower){ abbrBoost = 1.0; break; }
+          }
+        }
+        // Alias matching boost: phrase hit (full alias in query) is stronger than
+        // token hit (any query token matches any alias token).
+        let aliasBoost = 0;
+        if (Array.isArray(it.aliases) && it.aliases.length) {
+          const queryLower = query.toLowerCase();
+          const qTokenSet = Object.create(null);
+          for (const t of qTokens) qTokenSet[String(t).toLowerCase()] = 1;
+          let phraseHit = false;
+          let tokenHit = false;
+          for (const alias of it.aliases) {
+            const aLower = String(alias).toLowerCase();
+            if (queryLower.includes(aLower)) { phraseHit = true; break; }
+            for (const at of tokenize(aLower)) {
+              if (qTokenSet[at]) { tokenHit = true; break; }
+            }
+          }
+          aliasBoost = phraseHit ? 0.75 : tokenHit ? 0.35 : 0;
+        }
+        const finalScore = score * (1 + (titleBoost * 0.25) + abbrBoost + aliasBoost);
         return { item: it, score: finalScore, raw_score: score };
         });
       }

----

*** COMMIT: b8e46f180f31252227a5eaea669f3102e3ef50b5
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 12:46:15 2026 +0100
Subject: fix: remove outdated synonyms and streamline synonym list

commit b8e46f180f31252227a5eaea669f3102e3ef50b5
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 12:46:15 2026 +0100

    fix: remove outdated synonyms and streamline synonym list

diff --git a/docs/worker/synonyms.json b/docs/worker/synonyms.json
index 220078dc9..d1786c4fc 100644
--- a/docs/worker/synonyms.json
+++ b/docs/worker/synonyms.json
@@ -1,8 +1,4 @@
 [
-  ["oob", "out of bounds", "out-of-bounds", "out of bounds glitch", "o.o.b.", "out of map"],
-  ["sld", "persistent save load object transfer", "save-load-dupe", "save load dupe", "save/load dupe"],
-  ["sd", "stick_desync", "stick desync", "stickdesync"],
-  ["sdc", "stick desync clip", "stick-desync-clip"],
   ["ultrabroken", "ultrabreak", "UB", "ultra-broken"],
   ["zuggle", "zuggling", "zugl", "zug", "zuggle overload"],
   ["tulin pump", "tulin-pump", "pump tulin", "tulin pumping", "tulinpump"],
@@ -48,8 +44,6 @@
   ["bow sprint", "bow-sprinting", "bow sprinting"],
   ["throw tap", "throw-tap", "throw tap sprinting"],
   ["oob laser", "laser-oob", "laser oob"],
-  ["weapon state transfer", "wst", "weapon transfer"],
-  ["midair item transmutation", "mit", "midair transmute"],
   ["message not found zuggle", "mnf zuggle", "mnf-zuggle"],
   ["recall clip", "recall-clip", "recallclip"],
   ["storage ascend", "ascend-storage", "ascend storage"],
@@ -63,6 +57,5 @@
   ["oob entry", "out-of-bounds entry", "oob entry"],
   ["zuggle stacking", "zuggle-stack", "zuggle stack"],
   ["equipment dupe", "equipment-duplication", "equipment dupe"],
-  ["glitchcraft", "glitch-craft", "glitch craft"],
-  ["mnf", "message-not-found", "message not found"]
+  ["glitchcraft", "glitch-craft", "glitch craft"]
 ]

----

*** COMMIT: ad5e05e2f17868acc00e5ddbe43f9f71610c5d93
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 12:59:49 2026 +0100
Subject: fix: update resource and related section headings for consistency

commit ad5e05e2f17868acc00e5ddbe43f9f71610c5d93
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 12:59:49 2026 +0100

    fix: update resource and related section headings for consistency

diff --git a/docs/assets/scripts/ai-worker-client.js b/docs/assets/scripts/ai-worker-client.js
index 530f89d09..717c08895 100644
--- a/docs/assets/scripts/ai-worker-client.js
+++ b/docs/assets/scripts/ai-worker-client.js
@@ -649,13 +649,13 @@
                 let resourcesFooter = '';
                 try {
                   const res = w._lastResources || [];
-                  if (res.length) resourcesFooter = '\n\n### Resources\n' + res.map(r => '- [' + r.text + '](' + r.href + ')').join('\n');
+                  if (res.length) resourcesFooter = '\n\n## Resources\n' + res.map(r => '- [' + r.text + '](' + r.href + ')').join('\n');
                 } catch(e){}
                 // Build Related footer with search links
                 let relatedFooter = '';
                 try {
                   const rel = w._lastRelated || [];
-                  if (rel.length) relatedFooter = '\n\n### Related\n' + rel.map(r => '- [' + r.text + '](' + WIKI_SEARCH_BASE + '?q=' + encodeURIComponent(r.query) + ')').join('\n');
+                  if (rel.length) relatedFooter = '\n\n## Related\n' + rel.map(r => '- [' + r.text + '](' + WIKI_SEARCH_BASE + '?q=' + encodeURIComponent(r.query) + ')').join('\n');
                 } catch(e){}
                 const disclaimer = '\n\n### Disclaimer\nThis response was synthesized by [The Librarian](https://nan-gogh.github.io/ultrabroken-documentation/wiki/about/#ai-search). Take it with a grain of salt ÔÇö always verify against the source pages.';
                 const text = queryHeading + responseText.trim() + resourcesFooter + relatedFooter + disclaimer;
diff --git a/docs/worker/worker.js b/docs/worker/worker.js
index ca3f1a4ca..4627c821b 100644
--- a/docs/worker/worker.js
+++ b/docs/worker/worker.js
@@ -430,14 +430,14 @@ export default {
         evidences.push(s);
         seenPaths[key] = 1;
       }
-      if (evidences.length >= 3) break;
+      if (evidences.length >= 6) break;
     }
 
     // Prepare a stable evidence list (title + short preview) to return with answers
     // Use full `text` for model context but provide a small `text_preview` for UI.
     // Include referencing files (backlinks) for each evidence to provide independent file references
     const maps = index.__maps || {};
-    const evidenceList = evidences.slice(0,3).map(s=>{
+    const evidenceList = evidences.slice(0,6).map(s=>{
       const item = s.item;
       const canonicalPath = (item.path || item.id || '').replace(/\/$/, '');
       const refs = (maps.backlinks && maps.backlinks[canonicalPath]) || [];

----

*** COMMIT: de39256edb0159e7e761962f9ceb8e5893229c42
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 13:51:43 2026 +0100
Subject: Refactor aliases and tags across multiple glitchcraft documentation files

commit de39256edb0159e7e761962f9ceb8e5893229c42
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 13:51:43 2026 +0100

    Refactor aliases and tags across multiple glitchcraft documentation files
    
    - Removed or updated aliases for clarity and consistency in:
      - animation-swap
      - ascend-storage
      - autobuild-cancel-slide
      - back-to-back-bloodmoon
      - banc-storage
      - dive-cancel-glide-boost
      - double-unfuse-duplicashen-dud
      - forced-blood-moon
      - jumpslash-canceling
      - long-jump
      - message-not-found-mnf
      - midair-sort-duplication
      - midair-throw-duplication
      - minecart-rail-collision-launching
      - mnf-zuggle-fuse
      - mozdor-jumping-slashing
      - persistent-save-load-object-transfer
      - recall-clip
      - recall-launch
      - save-load-dupe-sld
      - scope-render-cancel
      - smuggle-stacking-zuggle
      - stamina-depletion-freeze
      - weapon-stacking-duplication
      - zuggle
      - zuggle-overload
      - zuggle-overload-oob (deleted)
      - zuggle-overload-out-of-bounds (newly created)
    
    - Updated synonyms in synonyms.json for better searchability.

diff --git a/docs/assets/data/grimoire-data.json b/docs/assets/data/grimoire-data.json
index 8779bd8df..76f3cb007 100644
--- a/docs/assets/data/grimoire-data.json
+++ b/docs/assets/data/grimoire-data.json
@@ -1 +1 @@
-[{"name": "Grimoire of Glitchcraft", "abbr": "", "date": "", "tags": [], "versions": [], "credits": [], "href": "./_glitchcraft-grimoire.md"}, {"name": "Ability Wheel Loop", "abbr": "AWL", "date": "2024-03-11", "tags": ["menu", "ultrahand", "zonai"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./ability-wheel-loop.md"}, {"name": "Aeroculling", "abbr": "AC", "date": "2024-08-11", "tags": ["equipment", "culling", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./aeroculling.md"}, {"name": "Animation Swap", "abbr": "ASWP", "date": "2023-05-17", "tags": ["zuggling", "animation", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Swinginman"], "href": "./animation-swap.md"}, {"name": "Anti-gravity GAS", "abbr": "AGAS", "date": "2025-01-22", "tags": ["gas"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./anti-gravity-gas.md"}, {"name": "Anti-Gravity Glitch", "abbr": "AGG", "date": "2023-05-13", "tags": ["paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Kaldemar"], "href": "./anti-gravity-glitch.md"}, {"name": "Anti-Gravity Objects", "abbr": "AGO", "date": "Unknown", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./anti-gravity-objects.md"}, {"name": "AntiGrav Weapons", "abbr": "AGW", "date": "2023-05-28", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Blize"], "href": "./antigrav-weapons.md"}, {"name": "Arrow Prompt Storage", "abbr": "APS", "date": "2023-10-04", "tags": ["storage", "culling", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NghtmaR3"], "href": "./arrow-prompt-storage-aps.md"}, {"name": "Arrow Smuggling", "abbr": "ASMU", "date": "2023-06-04", "tags": ["zuggling", "equipment", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./arrow-smuggling.md"}, {"name": "Arrow Unlink", "abbr": "AUL", "date": "2023-10-26", "tags": ["fuse", "arrow"], "versions": ["1.0.0"], "credits": ["R4000"], "href": "./arrow-unlink.md"}, {"name": "Arrow Unloading", "abbr": "AU", "date": "2023-06-18", "tags": ["culling", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk", "Zas"], "href": "./arrow-unloading.md"}, {"name": "Ascend Camera Glitch", "abbr": "ACG", "date": "Unknown", "tags": ["ascend", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./ascend-camera-glitch.md"}, {"name": "Ascend Rushing", "abbr": "AR", "date": "2023-06-15", "tags": ["ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./ascend-rushing.md"}, {"name": "Ascend Storage", "abbr": "ASTR", "date": "2023-05-19", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Saria"], "href": "./ascend-storage.md"}, {"name": "Attached Rangeless Active Zonai", "abbr": "ARAZ", "date": "2023-06-16", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?", "NX721"], "href": "./attached-rangeless-active-zonai-araz.md"}, {"name": "Autobuild Cancel Slide", "abbr": "ABCS", "date": "2023-05-18", "tags": ["animation", "movement", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Takosensai1"], "href": "./autobuild-cancel-slide-abcs.md"}, {"name": "Autobuild Duplication", "abbr": "ABD", "date": "2023-06-11", "tags": ["duplication", "item", "ultrahand", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./autobuild-duplication-abd.md"}, {"name": "Autobuild Storage", "abbr": "ABST", "date": "2023-08-28", "tags": ["storage", "item", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "R4000"], "href": "./autobuild-storage.md"}, {"name": "Awakened Master Sword", "abbr": "AMS", "date": "2023-09-04", "tags": ["weapon", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tahata"], "href": "./awakened-master-sword-ams.md"}, {"name": "Back-in-Time Art", "abbr": "BIT", "date": "2023-06-18", "tags": ["save-load"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Zas"], "href": "./back-in-time-art.md"}, {"name": "Back to Back Bloodmoon", "abbr": "BTBB", "date": "2023-05-17", "tags": ["blood-moon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lopitty"], "href": "./back-to-back-bloodmoon.md"}, {"name": "Balloon Overload", "abbr": "BO", "date": "2025-03-08", "tags": ["menu", "equipment", "overload", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Jordan", "mulberry", "ofstrings2"], "href": "./balloon-overload.md"}, {"name": "Banc Storage", "abbr": "BANC", "date": "2024-10-01", "tags": ["storage", "warping", "save-load", "blood-moon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos", "mulberry", "Aergyl", "EOH_NS_SS"], "href": "./banc-storage.md"}, {"name": "Bomb Skew", "abbr": "BSK", "date": "2023-09-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl", "FerrusCube", "Mozz"], "href": "./bomb-skew.md"}, {"name": "Bow Attachment Desync", "abbr": "BAD", "date": "2023-07-11", "tags": ["desync", "item", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Aeolian"], "href": "./bow-attachment-desync-bad-arrows.md"}, {"name": "Bow Attachment Storage", "abbr": "BAS", "date": "2023-12-03", "tags": ["storage", "item", "fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./bow-attachment-storage.md"}, {"name": "Bow Sprinting", "abbr": "BS", "date": "2023-05-14", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./bow-sprinting.md"}, {"name": "Breaking Awakened Master Sword", "abbr": "BAMS", "date": "2023-11-26", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Infrasolid"], "href": "./breaking-awakened-master-sword.md"}, {"name": "BThrow Sprinting", "abbr": "BTS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./bthrow-sprinting.md"}, {"name": "Bundled Item Duplication", "abbr": "BID", "date": "2023-12-12", "tags": ["duplication", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./bundled-item-duplication-bid.md"}, {"name": "Buoy Bouncing", "abbr": "BB", "date": "2023-05-25", "tags": ["equipment", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup"], "href": "./buoy-bouncing.md"}, {"name": "Camera CFW", "abbr": "CFW", "date": "2023-07-11", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh"], "href": "./camera-cfw.md"}, {"name": "Camera Pose Glitch", "abbr": "CPG", "date": "Unknown", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./camera-pose-glitch.md"}, {"name": "Capsule Cel Shader Removal", "abbr": "CCSR", "date": "2023-12-04", "tags": ["duplication", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./capsule-cel-shader-removal.md"}, {"name": "Cave Flag Culling", "abbr": "CFC", "date": "2023-11-24", "tags": ["duplication", "culling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Aergyl"], "href": "./cave-flag-culling.md"}, {"name": "Chasm Delay Zuggle", "abbr": "CDZ", "date": "2024-05-31", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock", "mulberry", "WinnerBoi77"], "href": "./chasm-delay-zuggle-cdz.md"}, {"name": "Chasm Device Dupe", "abbr": "CDD", "date": "2025-10-12", "tags": ["duplication", "item", "culling", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic", "mulberry"], "href": "./chasm-device-dupe.md"}, {"name": "Clear Camera/Scope", "abbr": "CCS", "date": "2023-07-03", "tags": ["bow", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./clear-camera-scope.md"}, {"name": "Cold Fuse Stick Desync Clip", "abbr": "CSSDC", "date": "2024-06-04", "tags": ["clipping", "desync", "weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "KiloVictor"], "href": "./cold-fuse-stick-desync-clip-cold-fuse-sdc.md"}, {"name": "Cold Fuse", "abbr": "CF", "date": "2023-07-23", "tags": ["weapon", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk", "Ryan?", "Zas"], "href": "./cold-fuse.md"}, {"name": "Construct Fuse Entanglement", "abbr": "CNFE", "date": "2024-06-30", "tags": ["equipment", "entanglement", "fuse", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./construct-fuse-entanglement.md"}, {"name": "Corrupt Meal", "abbr": "CM", "date": "2025-02-07", "tags": ["cooking"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Telkic"], "href": "./corrupt-meal.md"}, {"name": "Crouch Sprinting", "abbr": "CS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./crouch-sprinting.md"}, {"name": "Crouch Throw Tap Sprinting", "abbr": "CTTS", "date": "2023-05-15", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer"], "href": "./crouch-throw-tap-sprinting-ctts.md"}, {"name": "Cucco Warping", "abbr": "CW", "date": "2023-07-23", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi"], "href": "./cucco-warping.md"}, {"name": "Cull Cold Fuse", "abbr": "CCF", "date": "2024-02-01", "tags": ["weapon", "culling", "ultrahand", "fuse"], "versions": ["Unknown"], "credits": ["mulberry"], "href": "./cull-cold-fuse.md"}, {"name": "Cull Equipment Desync", "abbr": "CED", "date": "2023-10-10", "tags": ["desync", "menu", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blize", "Ock"], "href": "./cull-equipment-desync.md"}, {"name": "Cull Fuse Entanglement", "abbr": "CFE", "date": "2023-09-21", "tags": ["entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "suusi", "Ock", "SteFen45"], "href": "./cull-fuse-entanglement-cull-fe.md"}, {"name": "Cull Launching", "abbr": "CL", "date": "2023-07-01", "tags": ["launching", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Asgorne"], "href": "./cull-launching.md"}, {"name": "Cull Pickup Dynamic Zuggle", "abbr": "CPDZ", "date": "2025-05-18", "tags": ["zuggling", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./cull-pickup-dynamic-zuggle.md"}, {"name": "Cull Smuggle", "abbr": "CSMU", "date": "2023-06-27", "tags": ["zuggling", "equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "ROBUXY2ND", "Ock"], "href": "./cull-smuggle.md"}, {"name": "Cull Storage Zuggle", "abbr": "CSZ", "date": "2024-07-18", "tags": ["zuggling", "storage", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars"], "href": "./cull-storage-zuggle-csz.md"}, {"name": "Cull Storage", "abbr": "CSTR", "date": "2024-01-20", "tags": ["storage", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./cull-storage.md"}, {"name": "Cull Zone Culling", "abbr": "CZC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./cull-zone-culling.md"}, {"name": "Culling Area Fuse Storage Fuse Entanglement", "abbr": "CFSFE", "date": "2024-02-25", "tags": ["storage", "entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee", "Zas"], "href": "./culling-area-fuse-storage-fuse-entanglement.md"}, {"name": "Culling Area Fuse Storage", "abbr": "CAFS", "date": "2023-06-30", "tags": ["storage", "culling", "fuse"], "versions": ["Unknown"], "credits": ["Mozz", "pyuk"], "href": "./culling-area-fuse-storage.md"}, {"name": "Cutscene Combo Amplifier", "abbr": "CCA", "date": "2023-12-22", "tags": ["item", "buff", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos"], "href": "./cutscene-combo-amplifier.md"}, {"name": "Damage Amnesia", "abbr": "DA", "date": "2023-05-27", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./damage-amnesia.md"}, {"name": "Death Persistent Save Load Object Transfer", "abbr": "DPSLOT", "date": "2025-06-26", "tags": ["item", "save-load", "zuggling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./death-persistent-save-load-object-transfer.md"}, {"name": "Detached Rangeless Active Zonai", "abbr": "DRAZ", "date": "2023-06-15", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Venaticus"], "href": "./detached-rangeless-active-zonai-draz.md"}, {"name": "Detanglement", "abbr": "DTG", "date": "2023-09-09", "tags": ["launching", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./detanglement.md"}, {"name": "Dialog Permacull", "abbr": "DPC", "date": "2025-11-28", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./dialog-permacull.md"}, {"name": "Disabled Enemy", "abbr": "DE", "date": "2023-06-27", "tags": ["enemy"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["shio_0725", "ralseidewitt"], "href": "./disabled-enemy.md"}, {"name": "Dispenser Storage", "abbr": "DISP", "date": "2023-07-02", "tags": ["storage", "item", "ultrahand", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./dispenser-storage.md"}, {"name": "Display Duping", "abbr": "DD", "date": "2023-05-27", "tags": ["duplication", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Pistonight"], "href": "./display-duping.md"}, {"name": "Display Master Sword", "abbr": "DMS", "date": "2023-06-08", "tags": ["weapon", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Zas"], "href": "./display-master-sword.md"}, {"name": "Dive Cancel Glide Boost", "abbr": "DCGB", "date": "2023-05-14", "tags": ["animation", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "Mety333"], "href": "./dive-cancel-glide-boost.md"}, {"name": "Double Bypass Zuggle", "abbr": "DBZ", "date": "2025-06-16", "tags": ["zuggling", "item", "culling", "ultrahand"], "versions": ["1.2.0"], "credits": ["mulberry", "dt13269"], "href": "./double-bypass-zuggle-dbz.md"}, {"name": "Double Shield Desync Clip Fuse Entanglement", "abbr": "DSDCFE", "date": "2024-06-06", "tags": ["duplication", "clipping", "desync", "equipment", "entanglement", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee"], "href": "./double-shield-desync-clip-fuse-entanglement-double-sdc-fe.md"}, {"name": "Double Tulin Boost", "abbr": "DTB", "date": "2023-05-17", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./double-tulin-boost.md"}, {"name": "Double Unfuse Duplicashen", "abbr": "DUD", "date": "2023-05-15", "tags": ["duplication", "item", "weapon", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Li Shen (Ú»ëþÑ×)"], "href": "./double-unfuse-duplicashen-dud.md"}, {"name": "Dpadlock-less Invizuggle", "abbr": "DLI", "date": "2024-07-17", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars", "NghtmaR3"], "href": "./dpadlock-less-invizuggle.md"}, {"name": "Drop Delay Zuggle", "abbr": "DDZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-delay-zuggle-ddz.md"}, {"name": "Drop Restriction", "abbr": "DR", "date": "2023-06-19", "tags": ["menu", "item", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["SCFD-GK2", "NicNac"], "href": "./drop-restriction.md"}, {"name": "Drop Smuggling", "abbr": "DSMU", "date": "2023-05-31", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-smuggling.md"}, {"name": "Drop Zuggle", "abbr": "DZ", "date": "2023-06-15", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO"], "href": "./drop-zuggle.md"}, {"name": "Durability-", "abbr": "DUR", "date": "2023-09-11", "tags": ["item", "weapon", "bow"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./durability.md"}, {"name": "Dynamic Purgatory Zuggle", "abbr": "DPZ", "date": "2025-02-14", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./dynamic-purgatory-zuggle.md"}, {"name": "Dynamic Zuggle", "abbr": "DZG", "date": "2023-09-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "Zas", "mulberry", "WinnerBoi77", "Ryan?", "CS16"], "href": "./dynamic-zuggle.md"}, {"name": "Eaten Despawn Interrupt", "abbr": "EDI", "date": "2026-01-16", "tags": ["item", "zuggling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Squidwest"], "href": "./eaten-despawn-interrupt.md"}, {"name": "Enemy Pickpocketing", "abbr": "EP", "date": "2023-09-16", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KAIDUDE64"], "href": "./enemy-pickpocketing.md"}, {"name": "Entanglement Height Glitch", "abbr": "EHG", "date": "2023-05-24", "tags": ["equipment", "entanglement", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./entanglement-height-glitch.md"}, {"name": "Equipment Collision Zuggle", "abbr": "ECZ", "date": "2023-05-16", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zvleon"], "href": "./equipment-collision-zuggle.md"}, {"name": "Equipment Mitosis", "abbr": "EM", "date": "2023-09-05", "tags": ["duplication", "zuggling", "equipment", "overload"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./equipment-mitosis.md"}, {"name": "Equipment Shock Duping", "abbr": "ESD", "date": "2023-12-12", "tags": ["duplication", "item", "equipment"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./equipment-shock-duping.md"}, {"name": "Equipment Smuggle", "abbr": "ESMU", "date": "2023-06-01", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["sleepyppls", "Mozz", "mulberry", "NaN Gogh"], "href": "./equipment-smuggle.md"}, {"name": "Equipped Throken", "abbr": "ETHK", "date": "2025-05-20", "tags": ["weapon", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./equipped-throken.md"}, {"name": "Extended Throw Sprinting", "abbr": "ETS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["briochoc"], "href": "./extended-throw-sprinting-ets.md"}, {"name": "Fall Damage Cancel", "abbr": "FDC", "date": "2023-05-23", "tags": ["animation", "damage", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter"], "href": "./fall-damage-cancel-fdc.md"}, {"name": "Floorping", "abbr": "FLP", "date": "2024-01-02", "tags": ["warping"], "versions": ["1.1.0", "1.1.1"], "credits": ["koreth"], "href": "./floorping.md"}, {"name": "Food Ability Buff Swap", "abbr": "FABS", "date": "2023-05-16", "tags": ["cooking", "item", "buff", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["fabs"], "href": "./food-ability-buff-swap-fabs.md"}, {"name": "Force Equip Zuggling", "abbr": "FEZ", "date": "2023-06-07", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "Mozz", "Rhkellz", "Syb", "NaN Gogh"], "href": "./force-equip-zuggling-fez.md"}, {"name": "Forced Blood Moon", "abbr": "FBM", "date": "2023-05-28", "tags": ["blood-moon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["1789(@W0ERYySQgZyGOY3)", "Simonfirefighter", "Maxmasher", "Flash", "acaepius"], "href": "./forced-blood-moon.md"}, {"name": "Freecall", "abbr": "FC", "date": "2023-09-09", "tags": ["ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["suusi", "ROBUXY2ND"], "href": "./freecall.md"}, {"name": "Fuse Entangle Drop Zuggle", "abbr": "FEDZ", "date": "2023-06-17", "tags": ["zuggling", "item", "weapon", "equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-drop-zuggle-fedz.md"}, {"name": "Fuse Entangle Weapon Zuggle", "abbr": "FEWZ", "date": "2023-06-10", "tags": ["zuggling", "item", "weapon", "damage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-weapon-zuggle-fewz.md"}, {"name": "Fuse Entanglement Clipping", "abbr": "FEC", "date": "2023-06-16", "tags": ["clipping", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["circyit"], "href": "./fuse-entanglement-clipping-fec.md"}, {"name": "Fuse Entanglement Desync", "abbr": "FED", "date": "2023-05-26", "tags": ["duplication", "desync", "item", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement-desync-fed.md"}, {"name": "Fuse Entanglement Drop Smuggling", "abbr": "FEDS", "date": "2023-08-15", "tags": ["zuggling", "item", "equipment", "entanglement", "fuse"], "versions": ["1.2.0"], "credits": ["Blize", "Blackmars"], "href": "./fuse-entanglement-drop-smuggling.md"}, {"name": "Fuse Entanglement", "abbr": "FE", "date": "2023-05-24", "tags": ["equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement.md"}, {"name": "Fuse Overload", "abbr": "FO", "date": "2023-11-03", "tags": ["weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "NghtmaR3"], "href": "./fuse-overload-fo.md"}, {"name": "Fuse Overload Fuse Entanglement", "abbr": "FOFE", "date": "2025-05-26", "tags": ["entanglement", "overload", "ultrahand", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry"], "href": "./fuse-overload-fuse-entanglement-fofe.md"}, {"name": "Fuse Storage", "abbr": "FS", "date": "2023-06-18", "tags": ["storage", "item", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./fuse-storage-fs.md"}, {"name": "Fuse Storage Fuse Entanglement", "abbr": "FSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./fuse-storage-fuse-entanglement-fsfe.md"}, {"name": "GAS Launching", "abbr": "GASL", "date": "2023-06-25", "tags": ["gas", "launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "pyuk", "Flash", "Mozz", "Blize"], "href": "./gas-launching-previously-known-as-ascend-launching.md"}, {"name": "GAS Warping", "abbr": "GASW", "date": "2023-06-26", "tags": ["gas", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Flash", "pyuk"], "href": "./gas-warping.md"}, {"name": "Ghost Save Load Object Transfer", "abbr": "GSLOT", "date": "2024-03-08", "tags": ["save-load", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./ghost-save-load-object-transfer.md"}, {"name": "Ghost Stick Clipping", "abbr": "GSC", "date": "2023-05-28", "tags": ["clipping"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["rocomox"], "href": "./ghost-stick-clipping.md"}, {"name": "Glue Removal", "abbr": "GR", "date": "2023-10-05", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./glue-removal.md"}, {"name": "Guard-less Active Shield", "abbr": "GAS", "date": "2023-06-12", "tags": ["equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Venaticus"], "href": "./guard-less-active-shield-gas.md"}, {"name": "Hand Locked Equipment Smuggling", "abbr": "HLES", "date": "2023-07-11", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0"], "credits": ["Aeolian"], "href": "./hand-locked-equipment-smuggling-hles.md"}, {"name": "Handy Job", "abbr": "HJ", "date": "2023-11-20", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./handy-job.md"}, {"name": "Hero Path Link Storage", "abbr": "HPLS", "date": "2023-06-20", "tags": ["storage"], "versions": ["1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./hero-path-link-storage-hpls.md"}, {"name": "Hestu Scamming", "abbr": "HSCA", "date": "2024-04-19", "tags": ["menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "Tahata", "EM"], "href": "./hestu-scamming.md"}, {"name": "Hold Smuggling", "abbr": "HSM", "date": "2023-07-04", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "NaN Gogh"], "href": "./hold-smuggling.md"}, {"name": "Hold Storage Duplication", "abbr": "HSD", "date": "2023-07-03", "tags": ["duplication", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Mozz"], "href": "./hold-storage-duplication-also-known-as-minus-dupe.md"}, {"name": "Hold Storage", "abbr": "HS", "date": "2023-07-02", "tags": ["storage", "desync", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NaN Gogh", "Mozz"], "href": "./hold-storage.md"}, {"name": "Horse Duping", "abbr": "HD", "date": "2024-03-22", "tags": ["duplication", "culling", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./horse-duping.md"}, {"name": "Hydro Clipping", "abbr": "HC", "date": "2023-06-15", "tags": ["clipping", "storage", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter", "Maxmasher", "KnightPohtaytoh", "pyuk"], "href": "./hydro-clipping.md"}, {"name": "Infinite Balloon", "abbr": "IBAL", "date": "2024-06-13", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurone_yuu"], "href": "./infinite-balloon.md"}, {"name": "Infinite Bubbul Frog Gems", "abbr": "IBFG", "date": "2023-05-21", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Unknown"], "href": "./infinite-bubbul-frog-gems.md"}, {"name": "Infinite Damage 2.0", "abbr": "ID2", "date": "2024-01-21", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./infinite-damage-2-0.md"}, {"name": "Infinite Damage", "abbr": "IDMG", "date": "2023-05-13", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["GamSla341"], "href": "./infinite-damage.md"}, {"name": "Infinite Height", "abbr": "IH", "date": "2023-05-22", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "Physioninja"], "href": "./infinite-height.md"}, {"name": "Inventory Shift Duplication", "abbr": "ISD", "date": "2023-06-25", "tags": ["duplication", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Blizzard Blanc", "BigDUCCO", "Maxmasher", "pyuk", "Zas"], "href": "./inventory-shift-duplication-isd.md"}, {"name": "Invizuggle", "abbr": "IVZ", "date": "2024-01-03", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Yee"], "href": "./invizuggle.md"}, {"name": "Item Save Load Transfer", "abbr": "ISLT", "date": "2023-12-22", "tags": ["item", "save-load", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Luckstyle"], "href": "./item-save-load-transfer-islt.md"}, {"name": "Item Throw Hitbox Disable", "abbr": "ITHD", "date": "2023-06-18", "tags": ["item", "recall", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Arfix", "Moonrise"], "href": "./item-throw-hitbox-disable.md"}, {"name": "Jumpslash Cancel Clipping", "abbr": "JCC", "date": "2023-06-16", "tags": ["clipping", "animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./jumpslash-cancel-clipping-jcc.md"}, {"name": "Jumpslash Canceling", "abbr": "JSC", "date": "2023-05-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Mozz"], "href": "./jumpslash-canceling.md"}, {"name": "Kilovictor's quicksmuggle", "abbr": "KQS", "date": "2024-02-23", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KiloVictor"], "href": "./kilovictor-s-quicksmuggle.md"}, {"name": "L Sprinting", "abbr": "LS", "date": "2023-05-12", "tags": ["sprinting", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tauktes"], "href": "./l-sprinting.md"}, {"name": "Lag Machines", "abbr": "LM", "date": "2023-10-05", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lag-machines.md"}, {"name": "Laser-OOB", "abbr": "LOOB", "date": "2023-05-13", "tags": ["duplication", "oob"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Xeryph"], "href": "./laser-oob.md"}, {"name": "Lift Fuse Interrupt", "abbr": "LFI", "date": "2025-04-22", "tags": ["weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee"], "href": "./lift-fuse-interrupt.md"}, {"name": "Lift Smuggle", "abbr": "LSMU", "date": "2024-02-03", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars"], "href": "./lift-smuggle.md"}, {"name": "Lift Storage Warping", "abbr": "LSW", "date": "2024-01-08", "tags": ["storage", "item", "culling", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./lift-storage-warping-lsw.md"}, {"name": "Lift Warping", "abbr": "LW", "date": "2023-06-15", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lift-warping.md"}, {"name": "Like-Like Culling", "abbr": "LLC", "date": "2023-06-13", "tags": ["culling", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-culling.md"}, {"name": "Like-Like Drop Smuggling", "abbr": "LLDS", "date": "2023-06-15", "tags": ["zuggling", "item", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-drop-smuggling.md"}, {"name": "Like-Like FSFE", "abbr": "LLFSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./like-like-fsfe.md"}, {"name": "Like-Like Fuse Storage", "abbr": "LLFS", "date": "2023-06-18", "tags": ["storage", "item", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Mozz"], "href": "./like-like-fuse-storage.md"}, {"name": "Like Like New Textbox Softlock", "abbr": "LLTS", "date": "2023-06-16", "tags": ["item", "like-like", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./like-like-new-textbox-softlock.md"}, {"name": "Like-Like Smuggle Desync", "abbr": "LLSD", "date": "2023-06-15", "tags": ["zuggling", "desync", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-smuggle-desync-lsd.md"}, {"name": "Like-Like Smuggling", "abbr": "LLS", "date": "2023-06-15", "tags": ["zuggling", "equipment", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-smuggling.md"}, {"name": "Like-Like Warping", "abbr": "LLW", "date": "2023-06-15", "tags": ["warping", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-warping.md"}, {"name": "Like-Like Zuggling", "abbr": "LLZ", "date": "2023-06-15", "tags": ["zuggling", "like-like", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Ryan?", "Blackmars"], "href": "./like-like-zuggling.md"}, {"name": "LikeLike Stick Smuggling", "abbr": "LLSS", "date": "Unknown", "tags": ["zuggling", "item", "equipment", "culling", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./likelike-stick-smuggling.md"}, {"name": "Long Jump", "abbr": "LJ", "date": "2023-05-18", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./long-jump.md"}, {"name": "Map Flickering", "abbr": "MF", "date": "Unknown", "tags": ["map"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Unknown"], "href": "./map-flickering.md"}, {"name": "Map Storage", "abbr": "MSTR", "date": "2023-05-29", "tags": ["storage", "map"], "versions": ["1.1.0", "1.1.1"], "credits": ["blueberryoats"], "href": "./map-storage.md"}, {"name": "Map Zuggling", "abbr": "MZ", "date": "2023-05-23", "tags": ["zuggling", "map", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["BigDUCCO"], "href": "./map-zuggling-mz.md"}, {"name": "Mass Amnesia", "abbr": "MA", "date": "2023-08-02", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./mass-amnesia.md"}, {"name": "Master Sword Liberation", "abbr": "MSL", "date": "2023-11-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./master-sword-liberation.md"}, {"name": "Master Sword Zuggling/ Decayed Master Sword Zuggling", "abbr": "MSZ", "date": "2023-11-06", "tags": ["zuggling", "desync", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./master-sword-zuggling-decayed-master-sword-zuggling.md"}, {"name": "Memory Buffering", "abbr": "MB", "date": "2023-05-29", "tags": ["menu", "buff"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./memory-buffering.md"}, {"name": "Memory Interrupt", "abbr": "MI", "date": "2024-10-01", "tags": ["Unknown"], "versions": ["1.0.0"], "credits": ["mulberry"], "href": "./memory-interrupt.md"}, {"name": "Menu Overload", "abbr": "MO", "date": "2024-01-11", "tags": ["oob", "menu", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./menu-overload.md"}, {"name": "Message Not Found", "abbr": "MNF", "date": "2023-05-17", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Abahbob"], "href": "./message-not-found-mnf.md"}, {"name": "Midair Item Transmutation", "abbr": "MIT", "date": "2023-05-20", "tags": ["item", "paraglide", "zuggling"], "versions": ["1.1.0", "1.1.1"], "credits": ["eXe"], "href": "./midair-item-transmutation-mit.md"}, {"name": "Midair Sort Duplication", "abbr": "MSD", "date": "2023-05-21", "tags": ["duplication", "menu", "item", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zas", "kurocat471"], "href": "./midair-sort-duplication-msd.md"}, {"name": "Midair Throw Duplication", "abbr": "MTD", "date": "2023-07-02", "tags": ["duplication", "item", "zonai", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["quantim"], "href": "./midair-throw-duplication-mtd.md"}, {"name": "Minecart Rail Collision Launching", "abbr": "MRCL", "date": "2023-05-18", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüØÒéë-ÒüòÒéô"], "href": "./minecart-rail-collision-launching-mrcl.md"}, {"name": "Mineru Ability Desync", "abbr": "MAD", "date": "2023-05-30", "tags": ["desync", "mineru"], "versions": ["1.1.0", "1.1.1"], "credits": ["Sillicat"], "href": "./mineru-ability-desync.md"}, {"name": "Mineru Aim Permanence", "abbr": "MAIP", "date": "Unknown", "tags": ["mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./mineru-aim-permanence.md"}, {"name": "Mineru Cull Storage", "abbr": "MCS", "date": "2025-11-09", "tags": ["zuggling", "storage", "culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["ofstrings2"], "href": "./mineru-cull-storage.md"}, {"name": "Mineru Culling", "abbr": "MC", "date": "2023-07-31", "tags": ["culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./mineru-culling.md"}, {"name": "Mineru Fuse Entanglement", "abbr": "MFE", "date": "2023-10-18", "tags": ["entanglement", "culling", "ultrahand", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "WinnerBoi77"], "href": "./mineru-fuse-entanglement-mineru-fe.md"}, {"name": "Mineru Hold Smuggle", "abbr": "MHS", "date": "2023-12-20", "tags": ["zuggling", "menu", "item", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./mineru-hold-smuggle-mhs.md"}, {"name": "Mineru Persistent Save Load Object Transfer", "abbr": "MPSLOT", "date": "2024-07-27", "tags": ["equipment", "culling", "save-load", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry", "Armindo", "Emiya"], "href": "./mineru-persistent-save-load-object-transfer.md"}, {"name": "Mineru Text Storage", "abbr": "MTS", "date": "2024-07-11", "tags": ["storage", "mineru"], "versions": ["1.0.0"], "credits": ["CM30"], "href": "./mineru-text-storage.md"}, {"name": "MNF Fusing", "abbr": "MNFF", "date": "2023-06-05", "tags": ["fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./mnf-fusing.md"}, {"name": "MNF Glow Overload", "abbr": "MGO", "date": "2025-01-03", "tags": ["item", "overload", "mnf"], "versions": ["1.0.0"], "credits": ["Toti Sauce"], "href": "./mnf-glow-overload.md"}, {"name": "MNF Zuggle Fuse", "abbr": "MZF", "date": "2023-05-18", "tags": ["zuggling", "weapon", "fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./mnf-zuggle-fuse.md"}, {"name": "Model Teleport Desync", "abbr": "MTEL", "date": "2023-07-29", "tags": ["desync", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./model-teleport-desync.md"}, {"name": "Modifier Deletion Weapon State Transfer", "abbr": "MDWST", "date": "Unknown", "tags": ["duplication", "weapon"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md"}, {"name": "Modifier ONLY Transfer", "abbr": "MOT", "date": "2023-06-09", "tags": ["weapon"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "BigDUCCO"], "href": "./modifier-only-transfer.md"}, {"name": "Moobe Warping", "abbr": "MW", "date": "2024-01-12", "tags": ["oob", "warping", "movement", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./moobe-warping.md"}, {"name": "Mount Lock", "abbr": "ML", "date": "2023-05-21", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./mount-lock.md"}, {"name": "Mozdor Jumping/Slashing", "abbr": "MJS", "date": "2023-05-20", "tags": ["movement", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "AgdoR"], "href": "./mozdor-jumping-slashing.md"}, {"name": "MSNF glowing", "abbr": "MG", "date": "2023-08-02", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["evilgabe"], "href": "./msnf-glowing.md"}, {"name": "Mulberry's Out of Body Experience", "abbr": "MOOBE", "date": "2024-01-06", "tags": ["warping", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./mulberry-s-out-of-body-experience-moobe.md"}, {"name": "New Item Desync", "abbr": "NID", "date": "2023-05-12", "tags": ["duplication", "desync", "menu", "item", "equipment", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Modoki_returns"], "href": "./new-item-desync-equipment-duping.md"}, {"name": "No Bow Sprinting", "abbr": "NBS", "date": "2023-05-12", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./no-bow-sprinting-nbs.md"}, {"name": "Null Dropping", "abbr": "ND", "date": "2024-03-16", "tags": ["menu", "item", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl"], "href": "./null-dropping.md"}, {"name": "Object Culling", "abbr": "OC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "tori", "mulberry", "Timber"], "href": "./object-culling.md"}, {"name": "Object (Moe) Enlargement", "abbr": "MOE", "date": "2024-10-30", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "PetitFrapo", "Jordan"], "href": "./object-moe-enlargement.md"}, {"name": "Ocklusion Hovering", "abbr": "OCKH", "date": "2025-10-12", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic"], "href": "./ocklusion-hovering.md"}, {"name": "Ocklusion", "abbr": "OCKL", "date": "2024-05-29", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./ocklusion.md"}, {"name": "Octo-balloon Detanglement", "abbr": "OBD", "date": "2025-11-16", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./octo-balloon-detanglement.md"}, {"name": "Octodupe", "abbr": "OD", "date": "2023-05-26", "tags": ["duplication", "item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./octodupe.md"}, {"name": "Overload at Home", "abbr": "OAH", "date": "2024-03-20", "tags": ["zuggling", "culling", "overload"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./overload-at-home-aka-pickup-overload.md"}, {"name": "Overload Cold Fuse", "abbr": "OCF", "date": "2023-07-23", "tags": ["item", "weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["F. Buffalo"], "href": "./overload-cold-fuse.md"}, {"name": "Overload Drop Smuggling", "abbr": "ODS", "date": "2023-06-12", "tags": ["zuggling", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ChargeVolt", "Windocks"], "href": "./overload-drop-smuggling.md"}, {"name": "Overload Dynamic Zuggle", "abbr": "ODZ", "date": "2025-05-19", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./overload-dynamic-zuggle.md"}, {"name": "Overload Fuse Entanglement", "abbr": "OFE", "date": "2024-07-23", "tags": ["zuggling", "entanglement", "culling", "overload", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./overload-fuse-entanglement.md"}, {"name": "Overload Persistent Save Load Object Transfer", "abbr": "OPSLOT", "date": "2024-07-26", "tags": ["overload", "save-load"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./overload-persistent-save-load-object-transfer.md"}, {"name": "Pelison Duping", "abbr": "PD", "date": "2023-05-25", "tags": ["duplication", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["AngryEgg", "BigDUCCO"], "href": "./pelison-duping.md"}, {"name": "Persistent Save Load Object Transfer", "abbr": "PSLOT", "date": "2024-01-25", "tags": ["culling", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./persistent-save-load-object-transfer-pslot.md"}, {"name": "Pickup Smuggling", "abbr": "PSMU", "date": "2023-05-28", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ame"], "href": "./pickup-smuggling.md"}, {"name": "Pocket Rocket", "abbr": "PR", "date": "2023-06-15", "tags": ["launching", "equipment", "paraglide", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "SmallAnt"], "href": "./pocket-rocket.md"}, {"name": "Portable Cull Save Load Dupe", "abbr": "PSLD", "date": "2024-07-17", "tags": ["duplication", "culling", "save-load"], "versions": ["1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./portable-cull-save-load-dupe-portacull-sld.md"}, {"name": "Portable Culling", "abbr": "PCULL", "date": "2024-02-27", "tags": ["zuggling", "desync", "item", "culling", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./portable-culling.md"}, {"name": "Portacull Invismuggle", "abbr": "PCI", "date": "2024-02-29", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./portacull-invismuggle.md"}, {"name": "Weapon Despawn Prevention", "abbr": "WDP", "date": "2023-06-28", "tags": ["weapon", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./prevent-weapon-despawn.md"}, {"name": "Prologue Escape", "abbr": "PE", "date": "2024-10-01", "tags": ["duplication", "storage"], "versions": ["1.0.0"], "credits": ["LegendofLinkk", "mulberry", "Aergyl", "Lightos", "EOH_NS_SS"], "href": "./prologue-escape.md"}, {"name": "Proxy Glitches", "abbr": "PG", "date": "Unknown", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./proxy-glitches.md"}, {"name": "Purgatory Save Load Dupe", "abbr": "PGSLD", "date": "2024-02-11", "tags": ["duplication", "equipment", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./purgatory-save-load-dupe.md"}, {"name": "Pyroculling", "abbr": "PYR", "date": "2023-11-17", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.2.0"], "credits": ["ROBUXY2ND"], "href": "./pyroculling.md"}, {"name": "Quantum Linking", "abbr": "QL", "date": "2023-08-30", "tags": ["culling", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "pyuk"], "href": "./quantum-linking-ql.md"}, {"name": "Quick Drop Smuggle", "abbr": "QDS", "date": "2024-03-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0"], "credits": ["mulberry", "Zas", "Aeolian", "WinnerBoi77", "Ryan?"], "href": "./quick-drop-smuggle-qds.md"}, {"name": "Quick Smuggling", "abbr": "QS", "date": "2023-07-10", "tags": ["zuggling", "equipment", "arrow"], "versions": ["1.2.0"], "credits": ["Suishi"], "href": "./quick-smuggling.md"}, {"name": "Reball", "abbr": "RBL", "date": "2023-07-06", "tags": ["movement", "recall", "zonai"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./reball.md"}, {"name": "Recall Cancel", "abbr": "RCC", "date": "2023-07-20", "tags": ["animation", "item", "recall"], "versions": ["1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./recall-cancel.md"}, {"name": "Recall Clip", "abbr": "RC", "date": "2023-05-16", "tags": ["clipping", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüôÒéôÒüØÒéü"], "href": "./recall-clip.md"}, {"name": "Recall Drop Stacking", "abbr": "RDS", "date": "2025-01-04", "tags": ["item", "recall", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Telkic", "mulberry"], "href": "./recall-drop-stacking.md"}, {"name": "Recall Launch", "abbr": "RL", "date": "2023-05-17", "tags": ["launching", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deep"], "href": "./recall-launch.md"}, {"name": "Recall Locking", "abbr": "RLK", "date": "2023-06-11", "tags": ["recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./recall-locking.md"}, {"name": "Recall Sluggle", "abbr": "RSL", "date": "2025-07-12", "tags": ["zuggling", "menu", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["WinnerBoi77"], "href": "./recall-sluggle.md"}, {"name": "Recipe Storage", "abbr": "RS", "date": "2024-09-14", "tags": ["storage", "menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./recipe-storage.md"}, {"name": "Remote Arrow", "abbr": "RAT", "date": "2023-06-02", "tags": ["arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Flash", "ElDuende", "kirigaya"], "href": "./remote-arrow-trap.md"}, {"name": "Replacement Actor Fuse Entanglement", "abbr": "RAFE", "date": "2024-11-09", "tags": ["entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["dt13269", "mulberry"], "href": "./replacement-actor-fuse-entanglement.md"}, {"name": "Resync Fuse Entanglement", "abbr": "RFE", "date": "2023-12-18", "tags": ["item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./resync-fuse-entanglement-resync-fe.md"}, {"name": "Reverse Ascend Storage", "abbr": "RAS", "date": "2023-11-27", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Redrooey"], "href": "./reverse-ascend-storage.md"}, {"name": "Sage Madness", "abbr": "SM", "date": "2023-07-18", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aci"], "href": "./sage-madness.md"}, {"name": "Sage Recycling", "abbr": "SRCY", "date": "2023-05-28", "tags": ["duplication", "tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Knight7108", "Candlelor"], "href": "./sage-recycling.md"}, {"name": "Save Load Dupe", "abbr": "SLD", "date": "2023-05-16", "tags": ["duplication", "equipment", "save-load", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ZombieBoy225", "ness", "ElDuende"], "href": "./save-load-dupe-sld.md"}, {"name": "Save Load Zuggling", "abbr": "SLZ", "date": "2023-05-23", "tags": ["zuggling", "save-load", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["NicNac", "Flash", "BigDUCCO", "Wip long sticks enjoyer"], "href": "./save-load-zuggling-slz.md"}, {"name": "Scope Render Cancel", "abbr": "SRC", "date": "2023-05-19", "tags": ["animation", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "eXe"], "href": "./scope-render-cancel.md"}, {"name": "Shadow/Void Icons", "abbr": "SVI", "date": "2024-10-16", "tags": ["equipment", "fuse", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Lightos", "PetitFrapo"], "href": "./shadow-void-icons.md"}, {"name": "Shock Cold Fuse", "abbr": "SCF", "date": "2023-09-11", "tags": ["weapon", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-cold-fuse.md"}, {"name": "Shock Effect Overload", "abbr": "SEO", "date": "2023-07-26", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "R4000"], "href": "./shock-effect-overload-seo.md"}, {"name": "Shock Fuse Entanglement", "abbr": "SFE", "date": "2023-09-12", "tags": ["zuggling", "item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-fuse-entanglement.md"}, {"name": "Shock Smuggle", "abbr": "SSMU", "date": "2023-06-01", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["sleepyppls"], "href": "./shock-smuggle.md"}, {"name": "Shrunken Actors", "abbr": "SA", "date": "2025-10-26", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./shrunken-actors.md"}, {"name": "Slate Storage", "abbr": "SLST", "date": "2024-09-21", "tags": ["storage", "damage"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk"], "href": "./slate-storage.md"}, {"name": "Slugging", "abbr": "SLG", "date": "2023-06-15", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./slugging.md"}, {"name": "Smuggle Retrieval", "abbr": "SRET", "date": "2024-12-18", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["PetitFrapo"], "href": "./smuggle-retrieval.md"}, {"name": "Smuggle Stacking Zuggle", "abbr": "SSZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "LegendofLinkk", "Mozz"], "href": "./smuggle-stacking-zuggle-ssz.md"}, {"name": "Split Item Duplication", "abbr": "SID", "date": "2025-06-19", "tags": ["duplication", "item", "zuggling"], "versions": ["1.2.0"], "credits": ["Telkic", "mulberry", "WinnerBoi77"], "href": "./split-item-duplication-sid.md"}, {"name": "Spring Fall Damage Cancel", "abbr": "SFDC", "date": "2023-05-15", "tags": ["animation", "damage", "movement", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./spring-fall-damage-cancel.md"}, {"name": "Spring Strangeness", "abbr": "STRS", "date": "2023-05-15", "tags": ["spring", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi", "Owen"], "href": "./spring-strangeness.md"}, {"name": "Springboard Clipping", "abbr": "SBC", "date": "2023-05-27", "tags": ["clipping", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ab2x3z"], "href": "./springboard-clipping.md"}, {"name": "Springboarding", "abbr": "SBRD", "date": "2023-05-24", "tags": ["equipment", "shield", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springboarding.md"}, {"name": "Springdolling", "abbr": "SDOL", "date": "2023-05-15", "tags": ["launching", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springdolling.md"}, {"name": "Stack Splitting", "abbr": "SSPL", "date": "2024-12-31", "tags": ["item", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["s0ft", "Telkic", "mulberry"], "href": "./stack-splitting.md"}, {"name": "Stamina Depletion Freeze", "abbr": "SDF", "date": "2023-05-20", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./stamina-depletion-freeze-sdf.md"}, {"name": "Stick Desync Clip", "abbr": "SDC", "date": "2023-07-01", "tags": ["clipping", "desync", "item", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "DisguisedMoth"], "href": "./stick-desync-clip-sdc.md"}, {"name": "Sticky Dynamic Purgatory", "abbr": "SDP", "date": "2024-02-15", "tags": ["equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./sticky-dynamic-purgatory.md"}, {"name": "Super Bomb Jump", "abbr": "SBJ", "date": "2023-09-14", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["FerrusCube", "Aergyl"], "href": "./super-bomb-jump.md"}, {"name": "Super Fuse Overload", "abbr": "SFO", "date": "2025-12-06", "tags": ["weapon", "overload", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Aergyl", "Jordan", "MandelbrotChaylay"], "href": "./super-fuse-overload.md"}, {"name": "Surf storage", "abbr": "SSTR", "date": "2023-09-22", "tags": ["storage"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./surf-storage.md"}, {"name": "Swap Resync Zuggle", "abbr": "SRZ", "date": "2025-08-11", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry", "MandelbrotChaylay"], "href": "./swap-resync-zuggle-srz.md"}, {"name": "Swap Resync", "abbr": "SR", "date": "2025-08-10", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["MandelbrotChaylay"], "href": "./swap-resync.md"}, {"name": "Temporary Devices", "abbr": "TD", "date": "2024-11-30", "tags": ["fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./temporary-devices.md"}, {"name": "Texture Tearing", "abbr": "TT", "date": "2024-01-13", "tags": ["oob", "menu", "equipment", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./texture-tearing.md"}, {"name": "Throken", "abbr": "THK", "date": "2025-05-17", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikaboze"], "href": "./throken.md"}, {"name": "Throw Cancelling", "abbr": "TC", "date": "Unknown", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Quelfth"], "href": "./throw-cancelling.md"}, {"name": "Throw Tap Sprinting", "abbr": "TTS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer", "Tauktes"], "href": "./throw-tap-sprinting-tts.md"}, {"name": "Throwless Storage", "abbr": "THS", "date": "2023-06-19", "tags": ["storage", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["evilgabe", "NX721"], "href": "./throwless-storage-previously-known-as-beam-storage.md"}, {"name": "Time Bomb cancel", "abbr": "TBC", "date": "2023-11-04", "tags": ["animation", "equipment", "damage", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["tzakazuki"], "href": "./time-bomb-cancel.md"}, {"name": "Toti Saucery", "abbr": "TOTS", "date": "2024-08-17", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "Telkic"], "href": "./toti-saucery.md"}, {"name": "Travel Medallion storage", "abbr": "TMS", "date": "2023-06-16", "tags": ["storage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kirigaya"], "href": "./travel-medallion-storage-tms.md"}, {"name": "Tulin Pumping", "abbr": "TP", "date": "2023-05-14", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikkitrix"], "href": "./tulin-pumping.md"}, {"name": "Two Handed With Shield", "abbr": "THWS", "date": "2023-08-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Bucket_Sloe"], "href": "./two-handed-with-shield.md"}, {"name": "Ultimate Pocket Rocket", "abbr": "UPR", "date": "2025-05-20", "tags": ["launching", "warping", "ultrahand"], "versions": ["1.0.0"], "credits": ["Aergyl", "mulberry", "Ikaboze", "Jordan"], "href": "./ultimate-pocket-rocket.md"}, {"name": "Ultra Save Load Object Transfer", "abbr": "USLOT", "date": "2024-02-15", "tags": ["save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./ultra-save-load-object-transfer.md"}, {"name": "Ultrabroken Smuggling", "abbr": "UBS", "date": "2023-06-13", "tags": ["zuggling", "equipment", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["The_Andromeda"], "href": "./ultrabroken-smuggling-ubs.md"}, {"name": "Ultrabroken", "abbr": "UB", "date": "2023-05-29", "tags": ["item", "ultrahand", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Duncan"], "href": "./ultrabroken.md"}, {"name": "Unload Duping", "abbr": "UD", "date": "2023-05-31", "tags": ["duplication", "item", "culling", "fuse", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª", "ÕìâÕ╣┤ÞîÂÚÑ╝"], "href": "./unload-duping.md"}, {"name": "Unload WST", "abbr": "UWST", "date": "Unknown", "tags": ["item", "culling", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "Vee.Might.Exist", "Syb"], "href": "./unload-wst.md"}, {"name": "Unsheathed Mastersword", "abbr": "UMS", "date": "2023-07-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "DanielNeia"], "href": "./unsheathed-mastersword.md"}, {"name": "Vendor Scamming", "abbr": "VS", "date": "2023-07-03", "tags": ["zuggling", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "Mozz", "NaN Gogh"], "href": "./vendor-scamming.md"}, {"name": "Void Dipping", "abbr": "VD", "date": "2025-12-29", "tags": ["item", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Squidwest", "mulberry", "Aergyl"], "href": "./void-dipping.md"}, {"name": "Void Hold Storage", "abbr": "VHS", "date": "2023-07-22", "tags": ["storage", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "NX721"], "href": "./void-hold-storage.md"}, {"name": "Void Holding", "abbr": "VH", "date": "2023-06-10", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Lightos"], "href": "./void-holding.md"}, {"name": "Wacko Attacko", "abbr": "WATK", "date": "2024-01-21", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3", "WinnerBoi77"], "href": "./wacko-attacko.md"}, {"name": "Warp Bumping", "abbr": "WB", "date": "2023-06-07", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Mozz", "InAMuffinCup"], "href": "./warp-bumping.md"}, {"name": "Weapon Dash GAS", "abbr": "WDGAS", "date": "2025-11-28", "tags": ["gas", "weapon", "culling", "fuse", "zonai"], "versions": ["1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Toti Sauce"], "href": "./weapon-dash-gas.md"}, {"name": "Weapon Extensions", "abbr": "WEXT", "date": "2023-06-20", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deltenic", "Flash", "Zas"], "href": "./weapon-extensions.md"}, {"name": "Weapon FE", "abbr": "WFE", "date": "2023-06-01", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ROBUXY2ND", "Physioninja"], "href": "./weapon-fe.md"}, {"name": "Weapon Sheath Offset", "abbr": "WSO", "date": "2023-06-25", "tags": ["zuggling", "weapon", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["circyit", "dash"], "href": "./weapon-sheath-offset-wso.md"}, {"name": "Weapon Stacking Duplication", "abbr": "WSD", "date": "2023-05-16", "tags": ["duplication", "item", "weapon", "equipment", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ErlingÚÖäÞ║½"], "href": "./weapon-stacking-duplication-wsd.md"}, {"name": "Weapon Stand Dynamic Zuggle", "abbr": "WSDZ", "date": "2024-03-14", "tags": ["zuggling", "weapon", "item", "equipment"], "versions": ["1.0.0"], "credits": ["WinnerBoi77"], "href": "./weapon-stand-dynamic-zuggle.md"}, {"name": "Weapon State Transfer", "abbr": "WST", "date": "2023-05-19", "tags": ["weapon", "fuse", "entanglement", "equipment", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "kurocat471", "ElDuende", "Mentor_Kurt"], "href": "./weapon-state-transfer-wst.md"}, {"name": "Weather Amnesia", "abbr": "WA", "date": "2023-06-25", "tags": ["environment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk"], "href": "./weather-amnesia-wa.md"}, {"name": "Wheel Warping", "abbr": "WW", "date": "2023-06-18", "tags": ["launching", "warping", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk"], "href": "./wheel-warping.md"}, {"name": "Wheel Zoomy", "abbr": "WZ", "date": "2023-07-12", "tags": ["movement", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Solo_Turtle"], "href": "./wheel-zoomy-also-known-as-wheel-wacko-boingo.md"}, {"name": "Wireless Energy", "abbr": "WE", "date": "2023-07-11", "tags": ["equipment", "culling", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./wireless-energy.md"}, {"name": "Wuggle", "abbr": "WGL", "date": "2023-12-29", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "ROBUXY2ND"], "href": "./wuggle-weird-zuggle.md"}, {"name": "Yee Fuse Entanglement", "abbr": "YEEFE", "date": "2024-02-20", "tags": ["entanglement", "culling", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee", "mulberry"], "href": "./yee-fuse-entanglement.md"}, {"name": "Zapshield", "abbr": "ZAP", "date": "2024-09-16", "tags": ["equipment", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./zapshield.md"}, {"name": "ZL Animation Reset", "abbr": "ZLAR", "date": "2024-01-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./zl-animation-reset-zlar.md"}, {"name": "Zoggle", "abbr": "ZOG", "date": "2024-01-04", "tags": ["zuggling", "ultrahand", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ryan?", "Ock"], "href": "./zoggle.md"}, {"name": "Zonai Inventory Shift Dupe", "abbr": "ZISD", "date": "2023-07-10", "tags": ["duplication", "menu", "buff", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "quantim"], "href": "./zonai-inventory-shift-dupe-zisd.md"}, {"name": "Zonai Sort Duplication", "abbr": "ZSD", "date": "2023-05-22", "tags": ["duplication", "menu", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Quelfth", "Flash"], "href": "./zonai-sort-duplication-zsd.md"}, {"name": "Zonai Storage", "abbr": "ZS", "date": "2023-08-13", "tags": ["storage", "zonai"], "versions": ["1.0.0"], "credits": ["bebu0815"], "href": "./zonai-storage.md"}, {"name": "Zuggle Load Object Transfering", "abbr": "ZLOT", "date": "2023-06-07", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup", "ChargeVolt"], "href": "./zuggle-load-object-transfering-zlot.md"}, {"name": "Zuggle Overload Desync", "abbr": "ZOD", "date": "Unknown", "tags": ["zuggling", "desync", "menu", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./zuggle-overload-desync.md"}, {"name": "Zuggle Overload OOB", "abbr": "ZOOB", "date": "2023-05-18", "tags": ["clipping", "oob", "zuggling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["AngryEgg"], "href": "./zuggle-overload-oob.md"}, {"name": "Zuggle Overload", "abbr": "ZO", "date": "2023-05-17", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle-overload.md"}, {"name": "Zuggle", "abbr": "ZGL", "date": "2023-05-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle.md"}]
\ No newline at end of file
+[{"name": "Grimoire of Glitchcraft", "abbr": "", "date": "", "tags": [], "versions": [], "credits": [], "href": "./_glitchcraft-grimoire.md"}, {"name": "Ability Wheel Loop", "abbr": "AWL", "date": "2024-03-11", "tags": ["menu", "ultrahand", "zonai"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./ability-wheel-loop.md"}, {"name": "Aeroculling", "abbr": "AC", "date": "2024-08-11", "tags": ["equipment", "culling", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./aeroculling.md"}, {"name": "Animation Swap", "abbr": "ASWP", "date": "2023-05-17", "tags": ["zuggling", "animation", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Swinginman"], "href": "./animation-swap.md"}, {"name": "Anti-gravity GAS", "abbr": "AGAS", "date": "2025-01-22", "tags": ["gas"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./anti-gravity-gas.md"}, {"name": "Anti-Gravity Glitch", "abbr": "AGG", "date": "2023-05-13", "tags": ["paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Kaldemar"], "href": "./anti-gravity-glitch.md"}, {"name": "Anti-Gravity Objects", "abbr": "AGO", "date": "Unknown", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./anti-gravity-objects.md"}, {"name": "AntiGrav Weapons", "abbr": "AGW", "date": "2023-05-28", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Blize"], "href": "./antigrav-weapons.md"}, {"name": "Arrow Prompt Storage", "abbr": "APS", "date": "2023-10-04", "tags": ["storage", "culling", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NghtmaR3"], "href": "./arrow-prompt-storage-aps.md"}, {"name": "Arrow Smuggling", "abbr": "ASMU", "date": "2023-06-04", "tags": ["zuggling", "equipment", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./arrow-smuggling.md"}, {"name": "Arrow Unlink", "abbr": "AUL", "date": "2023-10-26", "tags": ["fuse", "arrow"], "versions": ["1.0.0"], "credits": ["R4000"], "href": "./arrow-unlink.md"}, {"name": "Arrow Unloading", "abbr": "AU", "date": "2023-06-18", "tags": ["culling", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk", "Zas"], "href": "./arrow-unloading.md"}, {"name": "Ascend Camera Glitch", "abbr": "ACG", "date": "Unknown", "tags": ["ascend", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./ascend-camera-glitch.md"}, {"name": "Ascend Rushing", "abbr": "AR", "date": "2023-06-15", "tags": ["ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./ascend-rushing.md"}, {"name": "Ascend Storage", "abbr": "ASTR", "date": "2023-05-19", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Saria"], "href": "./ascend-storage.md"}, {"name": "Attached Rangeless Active Zonai", "abbr": "ARAZ", "date": "2023-06-16", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?", "NX721"], "href": "./attached-rangeless-active-zonai-araz.md"}, {"name": "Autobuild Cancel Slide", "abbr": "ABCS", "date": "2023-05-18", "tags": ["animation", "movement", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Takosensai1"], "href": "./autobuild-cancel-slide-abcs.md"}, {"name": "Autobuild Duplication", "abbr": "ABD", "date": "2023-06-11", "tags": ["duplication", "item", "ultrahand", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./autobuild-duplication-abd.md"}, {"name": "Autobuild Storage", "abbr": "ABST", "date": "2023-08-28", "tags": ["storage", "item", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "R4000"], "href": "./autobuild-storage.md"}, {"name": "Awakened Master Sword", "abbr": "AMS", "date": "2023-09-04", "tags": ["weapon", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tahata"], "href": "./awakened-master-sword-ams.md"}, {"name": "Back-in-Time Art", "abbr": "BIT", "date": "2023-06-18", "tags": ["save-load"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Zas"], "href": "./back-in-time-art.md"}, {"name": "Back to Back Bloodmoon", "abbr": "BTBB", "date": "2023-05-17", "tags": ["bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lopitty"], "href": "./back-to-back-bloodmoon.md"}, {"name": "Balloon Overload", "abbr": "BO", "date": "2025-03-08", "tags": ["menu", "equipment", "overload", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Jordan", "mulberry", "ofstrings2"], "href": "./balloon-overload.md"}, {"name": "Banc Storage", "abbr": "BANC", "date": "2024-10-01", "tags": ["storage", "warping", "save-load", "bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos", "mulberry", "Aergyl", "EOH_NS_SS"], "href": "./banc-storage.md"}, {"name": "Bomb Skew", "abbr": "BSK", "date": "2023-09-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl", "FerrusCube", "Mozz"], "href": "./bomb-skew.md"}, {"name": "Bow Attachment Desync", "abbr": "BAD", "date": "2023-07-11", "tags": ["desync", "item", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Aeolian"], "href": "./bow-attachment-desync-bad-arrows.md"}, {"name": "Bow Attachment Storage", "abbr": "BAS", "date": "2023-12-03", "tags": ["storage", "item", "fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./bow-attachment-storage.md"}, {"name": "Bow Sprinting", "abbr": "BS", "date": "2023-05-14", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./bow-sprinting.md"}, {"name": "Breaking Awakened Master Sword", "abbr": "BAMS", "date": "2023-11-26", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Infrasolid"], "href": "./breaking-awakened-master-sword.md"}, {"name": "BThrow Sprinting", "abbr": "BTS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./bthrow-sprinting.md"}, {"name": "Bundled Item Duplication", "abbr": "BID", "date": "2023-12-12", "tags": ["duplication", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./bundled-item-duplication-bid.md"}, {"name": "Buoy Bouncing", "abbr": "BB", "date": "2023-05-25", "tags": ["equipment", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup"], "href": "./buoy-bouncing.md"}, {"name": "Camera CFW", "abbr": "CFW", "date": "2023-07-11", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh"], "href": "./camera-cfw.md"}, {"name": "Camera Pose Glitch", "abbr": "CPG", "date": "Unknown", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./camera-pose-glitch.md"}, {"name": "Capsule Cel Shader Removal", "abbr": "CCSR", "date": "2023-12-04", "tags": ["duplication", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./capsule-cel-shader-removal.md"}, {"name": "Cave Flag Culling", "abbr": "CFC", "date": "2023-11-24", "tags": ["duplication", "culling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Aergyl"], "href": "./cave-flag-culling.md"}, {"name": "Chasm Delay Zuggle", "abbr": "CDZ", "date": "2024-05-31", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock", "mulberry", "WinnerBoi77"], "href": "./chasm-delay-zuggle-cdz.md"}, {"name": "Chasm Device Dupe", "abbr": "CDD", "date": "2025-10-12", "tags": ["duplication", "item", "culling", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic", "mulberry"], "href": "./chasm-device-dupe.md"}, {"name": "Clear Camera/Scope", "abbr": "CCS", "date": "2023-07-03", "tags": ["bow", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./clear-camera-scope.md"}, {"name": "Cold Fuse Stick Desync Clip", "abbr": "CSSDC", "date": "2024-06-04", "tags": ["clipping", "desync", "weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "KiloVictor"], "href": "./cold-fuse-stick-desync-clip-cold-fuse-sdc.md"}, {"name": "Cold Fuse", "abbr": "CF", "date": "2023-07-23", "tags": ["weapon", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk", "Ryan?", "Zas"], "href": "./cold-fuse.md"}, {"name": "Construct Fuse Entanglement", "abbr": "CNFE", "date": "2024-06-30", "tags": ["equipment", "entanglement", "fuse", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./construct-fuse-entanglement.md"}, {"name": "Corrupt Meal", "abbr": "CM", "date": "2025-02-07", "tags": ["cooking"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Telkic"], "href": "./corrupt-meal.md"}, {"name": "Crouch Sprinting", "abbr": "CS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./crouch-sprinting.md"}, {"name": "Crouch Throw Tap Sprinting", "abbr": "CTTS", "date": "2023-05-15", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer"], "href": "./crouch-throw-tap-sprinting-ctts.md"}, {"name": "Cucco Warping", "abbr": "CW", "date": "2023-07-23", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi"], "href": "./cucco-warping.md"}, {"name": "Cull Cold Fuse", "abbr": "CCF", "date": "2024-02-01", "tags": ["weapon", "culling", "ultrahand", "fuse"], "versions": ["Unknown"], "credits": ["mulberry"], "href": "./cull-cold-fuse.md"}, {"name": "Cull Equipment Desync", "abbr": "CED", "date": "2023-10-10", "tags": ["desync", "menu", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blize", "Ock"], "href": "./cull-equipment-desync.md"}, {"name": "Cull Fuse Entanglement", "abbr": "CFE", "date": "2023-09-21", "tags": ["entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "suusi", "Ock", "SteFen45"], "href": "./cull-fuse-entanglement-cull-fe.md"}, {"name": "Cull Launching", "abbr": "CL", "date": "2023-07-01", "tags": ["launching", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Asgorne"], "href": "./cull-launching.md"}, {"name": "Cull Pickup Dynamic Zuggle", "abbr": "CPDZ", "date": "2025-05-18", "tags": ["zuggling", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./cull-pickup-dynamic-zuggle.md"}, {"name": "Cull Smuggle", "abbr": "CSMU", "date": "2023-06-27", "tags": ["zuggling", "equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "ROBUXY2ND", "Ock"], "href": "./cull-smuggle.md"}, {"name": "Cull Storage Zuggle", "abbr": "CSZ", "date": "2024-07-18", "tags": ["zuggling", "storage", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars"], "href": "./cull-storage-zuggle-csz.md"}, {"name": "Cull Storage", "abbr": "CSTR", "date": "2024-01-20", "tags": ["storage", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./cull-storage.md"}, {"name": "Cull Zone Culling", "abbr": "CZC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./cull-zone-culling.md"}, {"name": "Culling Area Fuse Storage Fuse Entanglement", "abbr": "CFSFE", "date": "2024-02-25", "tags": ["storage", "entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee", "Zas"], "href": "./culling-area-fuse-storage-fuse-entanglement.md"}, {"name": "Culling Area Fuse Storage", "abbr": "CAFS", "date": "2023-06-30", "tags": ["storage", "culling", "fuse"], "versions": ["Unknown"], "credits": ["Mozz", "pyuk"], "href": "./culling-area-fuse-storage.md"}, {"name": "Cutscene Combo Amplifier", "abbr": "CCA", "date": "2023-12-22", "tags": ["item", "buff", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos"], "href": "./cutscene-combo-amplifier.md"}, {"name": "Damage Amnesia", "abbr": "DA", "date": "2023-05-27", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./damage-amnesia.md"}, {"name": "Death Persistent Save Load Object Transfer", "abbr": "DPSLOT", "date": "2025-06-26", "tags": ["item", "save-load", "zuggling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./death-persistent-save-load-object-transfer.md"}, {"name": "Detached Rangeless Active Zonai", "abbr": "DRAZ", "date": "2023-06-15", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Venaticus"], "href": "./detached-rangeless-active-zonai-draz.md"}, {"name": "Detanglement", "abbr": "DTG", "date": "2023-09-09", "tags": ["launching", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./detanglement.md"}, {"name": "Dialog Permacull", "abbr": "DPC", "date": "2025-11-28", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./dialog-permacull.md"}, {"name": "Disabled Enemy", "abbr": "DE", "date": "2023-06-27", "tags": ["enemy"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["shio_0725", "ralseidewitt"], "href": "./disabled-enemy.md"}, {"name": "Dispenser Storage", "abbr": "DISP", "date": "2023-07-02", "tags": ["storage", "item", "ultrahand", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./dispenser-storage.md"}, {"name": "Display Duping", "abbr": "DD", "date": "2023-05-27", "tags": ["duplication", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Pistonight"], "href": "./display-duping.md"}, {"name": "Display Master Sword", "abbr": "DMS", "date": "2023-06-08", "tags": ["weapon", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Zas"], "href": "./display-master-sword.md"}, {"name": "Dive Cancel Glide Boost", "abbr": "DCGB", "date": "2023-05-14", "tags": ["animation", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "Mety333"], "href": "./dive-cancel-glide-boost.md"}, {"name": "Double Bypass Zuggle", "abbr": "DBZ", "date": "2025-06-16", "tags": ["zuggling", "item", "culling", "ultrahand"], "versions": ["1.2.0"], "credits": ["mulberry", "dt13269"], "href": "./double-bypass-zuggle-dbz.md"}, {"name": "Double Shield Desync Clip Fuse Entanglement", "abbr": "DSDCFE", "date": "2024-06-06", "tags": ["duplication", "clipping", "desync", "equipment", "entanglement", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee"], "href": "./double-shield-desync-clip-fuse-entanglement-double-sdc-fe.md"}, {"name": "Double Tulin Boost", "abbr": "DTB", "date": "2023-05-17", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./double-tulin-boost.md"}, {"name": "Double Unfuse Duplicashen", "abbr": "DUD", "date": "2023-05-15", "tags": ["duplication", "item", "weapon", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Li Shen (Ú»ëþÑ×)"], "href": "./double-unfuse-duplicashen-dud.md"}, {"name": "Dpadlock-less Invizuggle", "abbr": "DLI", "date": "2024-07-17", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars", "NghtmaR3"], "href": "./dpadlock-less-invizuggle.md"}, {"name": "Drop Delay Zuggle", "abbr": "DDZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-delay-zuggle-ddz.md"}, {"name": "Drop Restriction", "abbr": "DR", "date": "2023-06-19", "tags": ["menu", "item", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["SCFD-GK2", "NicNac"], "href": "./drop-restriction.md"}, {"name": "Drop Smuggling", "abbr": "DSMU", "date": "2023-05-31", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-smuggling.md"}, {"name": "Drop Zuggle", "abbr": "DZ", "date": "2023-06-15", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO"], "href": "./drop-zuggle.md"}, {"name": "Durability-", "abbr": "DUR", "date": "2023-09-11", "tags": ["item", "weapon", "bow"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./durability.md"}, {"name": "Dynamic Purgatory Zuggle", "abbr": "DPZ", "date": "2025-02-14", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./dynamic-purgatory-zuggle.md"}, {"name": "Dynamic Zuggle", "abbr": "DZG", "date": "2023-09-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "Zas", "mulberry", "WinnerBoi77", "Ryan?", "CS16"], "href": "./dynamic-zuggle.md"}, {"name": "Eaten Despawn Interrupt", "abbr": "EDI", "date": "2026-01-16", "tags": ["item", "zuggling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Squidwest"], "href": "./eaten-despawn-interrupt.md"}, {"name": "Enemy Pickpocketing", "abbr": "EP", "date": "2023-09-16", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KAIDUDE64"], "href": "./enemy-pickpocketing.md"}, {"name": "Entanglement Height Glitch", "abbr": "EHG", "date": "2023-05-24", "tags": ["equipment", "entanglement", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./entanglement-height-glitch.md"}, {"name": "Equipment Collision Zuggle", "abbr": "ECZ", "date": "2023-05-16", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zvleon"], "href": "./equipment-collision-zuggle.md"}, {"name": "Equipment Mitosis", "abbr": "EM", "date": "2023-09-05", "tags": ["duplication", "zuggling", "equipment", "overload"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./equipment-mitosis.md"}, {"name": "Equipment Shock Duping", "abbr": "ESD", "date": "2023-12-12", "tags": ["duplication", "item", "equipment"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./equipment-shock-duping.md"}, {"name": "Equipment Smuggle", "abbr": "ESMU", "date": "2023-06-01", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["sleepyppls", "Mozz", "mulberry", "NaN Gogh"], "href": "./equipment-smuggle.md"}, {"name": "Equipped Throken", "abbr": "ETHK", "date": "2025-05-20", "tags": ["weapon", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./equipped-throken.md"}, {"name": "Extended Throw Sprinting", "abbr": "ETS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["briochoc"], "href": "./extended-throw-sprinting-ets.md"}, {"name": "Fall Damage Cancel", "abbr": "FDC", "date": "2023-05-23", "tags": ["animation", "damage", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter"], "href": "./fall-damage-cancel-fdc.md"}, {"name": "Floorping", "abbr": "FLP", "date": "2024-01-02", "tags": ["warping"], "versions": ["1.1.0", "1.1.1"], "credits": ["koreth"], "href": "./floorping.md"}, {"name": "Food Ability Buff Swap", "abbr": "FABS", "date": "2023-05-16", "tags": ["cooking", "item", "buff", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["fabs"], "href": "./food-ability-buff-swap-fabs.md"}, {"name": "Force Equip Zuggling", "abbr": "FEZ", "date": "2023-06-07", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "Mozz", "Rhkellz", "Syb", "NaN Gogh"], "href": "./force-equip-zuggling-fez.md"}, {"name": "Forced Blood Moon", "abbr": "FBM", "date": "2023-05-28", "tags": ["bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["1789(@W0ERYySQgZyGOY3)", "Simonfirefighter", "Maxmasher", "Flash", "acaepius"], "href": "./forced-blood-moon.md"}, {"name": "Freecall", "abbr": "FC", "date": "2023-09-09", "tags": ["ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["suusi", "ROBUXY2ND"], "href": "./freecall.md"}, {"name": "Fuse Entangle Drop Zuggle", "abbr": "FEDZ", "date": "2023-06-17", "tags": ["zuggling", "item", "weapon", "equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-drop-zuggle-fedz.md"}, {"name": "Fuse Entangle Weapon Zuggle", "abbr": "FEWZ", "date": "2023-06-10", "tags": ["zuggling", "item", "weapon", "damage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-weapon-zuggle-fewz.md"}, {"name": "Fuse Entanglement Clipping", "abbr": "FEC", "date": "2023-06-16", "tags": ["clipping", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["circyit"], "href": "./fuse-entanglement-clipping-fec.md"}, {"name": "Fuse Entanglement Desync", "abbr": "FED", "date": "2023-05-26", "tags": ["duplication", "desync", "item", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement-desync-fed.md"}, {"name": "Fuse Entanglement Drop Smuggling", "abbr": "FEDS", "date": "2023-08-15", "tags": ["zuggling", "item", "equipment", "entanglement", "fuse"], "versions": ["1.2.0"], "credits": ["Blize", "Blackmars"], "href": "./fuse-entanglement-drop-smuggling.md"}, {"name": "Fuse Entanglement", "abbr": "FE", "date": "2023-05-24", "tags": ["equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement.md"}, {"name": "Fuse Overload", "abbr": "FO", "date": "2023-11-03", "tags": ["weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "NghtmaR3"], "href": "./fuse-overload-fo.md"}, {"name": "Fuse Overload Fuse Entanglement", "abbr": "FOFE", "date": "2025-05-26", "tags": ["entanglement", "overload", "ultrahand", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry"], "href": "./fuse-overload-fuse-entanglement-fofe.md"}, {"name": "Fuse Storage", "abbr": "FS", "date": "2023-06-18", "tags": ["storage", "item", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./fuse-storage-fs.md"}, {"name": "Fuse Storage Fuse Entanglement", "abbr": "FSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./fuse-storage-fuse-entanglement-fsfe.md"}, {"name": "GAS Launching", "abbr": "GASL", "date": "2023-06-25", "tags": ["gas", "launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "pyuk", "Flash", "Mozz", "Blize"], "href": "./gas-launching-previously-known-as-ascend-launching.md"}, {"name": "GAS Warping", "abbr": "GASW", "date": "2023-06-26", "tags": ["gas", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Flash", "pyuk"], "href": "./gas-warping.md"}, {"name": "Ghost Save Load Object Transfer", "abbr": "GSLOT", "date": "2024-03-08", "tags": ["save-load", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./ghost-save-load-object-transfer.md"}, {"name": "Ghost Stick Clipping", "abbr": "GSC", "date": "2023-05-28", "tags": ["clipping"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["rocomox"], "href": "./ghost-stick-clipping.md"}, {"name": "Glue Removal", "abbr": "GR", "date": "2023-10-05", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./glue-removal.md"}, {"name": "Guard-less Active Shield", "abbr": "GAS", "date": "2023-06-12", "tags": ["equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Venaticus"], "href": "./guard-less-active-shield-gas.md"}, {"name": "Hand Locked Equipment Smuggling", "abbr": "HLES", "date": "2023-07-11", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0"], "credits": ["Aeolian"], "href": "./hand-locked-equipment-smuggling-hles.md"}, {"name": "Handy Job", "abbr": "HJ", "date": "2023-11-20", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./handy-job.md"}, {"name": "Hero Path Link Storage", "abbr": "HPLS", "date": "2023-06-20", "tags": ["storage"], "versions": ["1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./hero-path-link-storage-hpls.md"}, {"name": "Hestu Scamming", "abbr": "HSCA", "date": "2024-04-19", "tags": ["menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "Tahata", "EM"], "href": "./hestu-scamming.md"}, {"name": "Hold Smuggling", "abbr": "HSM", "date": "2023-07-04", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "NaN Gogh"], "href": "./hold-smuggling.md"}, {"name": "Hold Storage Duplication", "abbr": "HSD", "date": "2023-07-03", "tags": ["duplication", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Mozz"], "href": "./hold-storage-duplication-also-known-as-minus-dupe.md"}, {"name": "Hold Storage", "abbr": "HS", "date": "2023-07-02", "tags": ["storage", "desync", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NaN Gogh", "Mozz"], "href": "./hold-storage.md"}, {"name": "Horse Duping", "abbr": "HD", "date": "2024-03-22", "tags": ["duplication", "culling", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./horse-duping.md"}, {"name": "Hydro Clipping", "abbr": "HC", "date": "2023-06-15", "tags": ["clipping", "storage", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter", "Maxmasher", "KnightPohtaytoh", "pyuk"], "href": "./hydro-clipping.md"}, {"name": "Infinite Balloon", "abbr": "IBAL", "date": "2024-06-13", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurone_yuu"], "href": "./infinite-balloon.md"}, {"name": "Infinite Bubbul Frog Gems", "abbr": "IBFG", "date": "2023-05-21", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Unknown"], "href": "./infinite-bubbul-frog-gems.md"}, {"name": "Infinite Damage 2.0", "abbr": "ID2", "date": "2024-01-21", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./infinite-damage-2-0.md"}, {"name": "Infinite Damage", "abbr": "IDMG", "date": "2023-05-13", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["GamSla341"], "href": "./infinite-damage.md"}, {"name": "Infinite Height", "abbr": "IH", "date": "2023-05-22", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "Physioninja"], "href": "./infinite-height.md"}, {"name": "Inventory Shift Duplication", "abbr": "ISD", "date": "2023-06-25", "tags": ["duplication", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Blizzard Blanc", "BigDUCCO", "Maxmasher", "pyuk", "Zas"], "href": "./inventory-shift-duplication-isd.md"}, {"name": "Invizuggle", "abbr": "IVZ", "date": "2024-01-03", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Yee"], "href": "./invizuggle.md"}, {"name": "Item Save Load Transfer", "abbr": "ISLT", "date": "2023-12-22", "tags": ["item", "save-load", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Luckstyle"], "href": "./item-save-load-transfer-islt.md"}, {"name": "Item Throw Hitbox Disable", "abbr": "ITHD", "date": "2023-06-18", "tags": ["item", "recall", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Arfix", "Moonrise"], "href": "./item-throw-hitbox-disable.md"}, {"name": "Jumpslash Cancel Clipping", "abbr": "JCC", "date": "2023-06-16", "tags": ["clipping", "animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./jumpslash-cancel-clipping-jcc.md"}, {"name": "Jumpslash Canceling", "abbr": "JSC", "date": "2023-05-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Mozz"], "href": "./jumpslash-canceling.md"}, {"name": "Kilovictor's quicksmuggle", "abbr": "KQS", "date": "2024-02-23", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KiloVictor"], "href": "./kilovictor-s-quicksmuggle.md"}, {"name": "L Sprinting", "abbr": "LS", "date": "2023-05-12", "tags": ["sprinting", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tauktes"], "href": "./l-sprinting.md"}, {"name": "Lag Machines", "abbr": "LM", "date": "2023-10-05", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lag-machines.md"}, {"name": "Laser-OOB", "abbr": "LOOB", "date": "2023-05-13", "tags": ["duplication", "oob"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Xeryph"], "href": "./laser-oob.md"}, {"name": "Lift Fuse Interrupt", "abbr": "LFI", "date": "2025-04-22", "tags": ["weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee"], "href": "./lift-fuse-interrupt.md"}, {"name": "Lift Smuggle", "abbr": "LSMU", "date": "2024-02-03", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars"], "href": "./lift-smuggle.md"}, {"name": "Lift Storage Warping", "abbr": "LSW", "date": "2024-01-08", "tags": ["storage", "item", "culling", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./lift-storage-warping-lsw.md"}, {"name": "Lift Warping", "abbr": "LW", "date": "2023-06-15", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lift-warping.md"}, {"name": "Like-Like Culling", "abbr": "LLC", "date": "2023-06-13", "tags": ["culling", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-culling.md"}, {"name": "Like-Like Drop Smuggling", "abbr": "LLDS", "date": "2023-06-15", "tags": ["zuggling", "item", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-drop-smuggling.md"}, {"name": "Like-Like FSFE", "abbr": "LLFSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./like-like-fsfe.md"}, {"name": "Like-Like Fuse Storage", "abbr": "LLFS", "date": "2023-06-18", "tags": ["storage", "item", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Mozz"], "href": "./like-like-fuse-storage.md"}, {"name": "Like Like New Textbox Softlock", "abbr": "LLTS", "date": "2023-06-16", "tags": ["item", "like-like", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./like-like-new-textbox-softlock.md"}, {"name": "Like-Like Smuggle Desync", "abbr": "LLSD", "date": "2023-06-15", "tags": ["zuggling", "desync", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-smuggle-desync-lsd.md"}, {"name": "Like-Like Smuggling", "abbr": "LLS", "date": "2023-06-15", "tags": ["zuggling", "equipment", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-smuggling.md"}, {"name": "Like-Like Warping", "abbr": "LLW", "date": "2023-06-15", "tags": ["warping", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-warping.md"}, {"name": "Like-Like Zuggling", "abbr": "LLZ", "date": "2023-06-15", "tags": ["zuggling", "like-like", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Ryan?", "Blackmars"], "href": "./like-like-zuggling.md"}, {"name": "LikeLike Stick Smuggling", "abbr": "LLSS", "date": "Unknown", "tags": ["zuggling", "item", "equipment", "culling", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./likelike-stick-smuggling.md"}, {"name": "Long Jump", "abbr": "LJ", "date": "2023-05-18", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./long-jump.md"}, {"name": "Map Flickering", "abbr": "MF", "date": "Unknown", "tags": ["map"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Unknown"], "href": "./map-flickering.md"}, {"name": "Map Storage", "abbr": "MSTR", "date": "2023-05-29", "tags": ["storage", "map"], "versions": ["1.1.0", "1.1.1"], "credits": ["blueberryoats"], "href": "./map-storage.md"}, {"name": "Map Zuggling", "abbr": "MZ", "date": "2023-05-23", "tags": ["zuggling", "map", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["BigDUCCO"], "href": "./map-zuggling-mz.md"}, {"name": "Mass Amnesia", "abbr": "MA", "date": "2023-08-02", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./mass-amnesia.md"}, {"name": "Master Sword Liberation", "abbr": "MSL", "date": "2023-11-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./master-sword-liberation.md"}, {"name": "Master Sword Zuggling/ Decayed Master Sword Zuggling", "abbr": "MSZ", "date": "2023-11-06", "tags": ["zuggling", "desync", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./master-sword-zuggling-decayed-master-sword-zuggling.md"}, {"name": "Memory Buffering", "abbr": "MB", "date": "2023-05-29", "tags": ["menu", "buff"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./memory-buffering.md"}, {"name": "Memory Interrupt", "abbr": "MI", "date": "2024-10-01", "tags": ["Unknown"], "versions": ["1.0.0"], "credits": ["mulberry"], "href": "./memory-interrupt.md"}, {"name": "Menu Overload", "abbr": "MO", "date": "2024-01-11", "tags": ["oob", "menu", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./menu-overload.md"}, {"name": "Message Not Found", "abbr": "MNF", "date": "2023-05-17", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Abahbob"], "href": "./message-not-found-mnf.md"}, {"name": "Midair Item Transmutation", "abbr": "MIT", "date": "2023-05-20", "tags": ["item", "paraglide", "zuggling"], "versions": ["1.1.0", "1.1.1"], "credits": ["eXe"], "href": "./midair-item-transmutation-mit.md"}, {"name": "Midair Sort Duplication", "abbr": "MSD", "date": "2023-05-21", "tags": ["duplication", "menu", "item", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zas", "kurocat471"], "href": "./midair-sort-duplication-msd.md"}, {"name": "Midair Throw Duplication", "abbr": "MTD", "date": "2023-07-02", "tags": ["duplication", "item", "zonai", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["quantim"], "href": "./midair-throw-duplication-mtd.md"}, {"name": "Minecart Rail Collision Launching", "abbr": "MRCL", "date": "2023-05-18", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüØÒéë-ÒüòÒéô"], "href": "./minecart-rail-collision-launching-mrcl.md"}, {"name": "Mineru Ability Desync", "abbr": "MAD", "date": "2023-05-30", "tags": ["desync", "mineru"], "versions": ["1.1.0", "1.1.1"], "credits": ["Sillicat"], "href": "./mineru-ability-desync.md"}, {"name": "Mineru Aim Permanence", "abbr": "MAIP", "date": "Unknown", "tags": ["mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./mineru-aim-permanence.md"}, {"name": "Mineru Cull Storage", "abbr": "MCS", "date": "2025-11-09", "tags": ["zuggling", "storage", "culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["ofstrings2"], "href": "./mineru-cull-storage.md"}, {"name": "Mineru Culling", "abbr": "MC", "date": "2023-07-31", "tags": ["culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./mineru-culling.md"}, {"name": "Mineru Fuse Entanglement", "abbr": "MFE", "date": "2023-10-18", "tags": ["entanglement", "culling", "ultrahand", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "WinnerBoi77"], "href": "./mineru-fuse-entanglement-mineru-fe.md"}, {"name": "Mineru Hold Smuggle", "abbr": "MHS", "date": "2023-12-20", "tags": ["zuggling", "menu", "item", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./mineru-hold-smuggle-mhs.md"}, {"name": "Mineru Persistent Save Load Object Transfer", "abbr": "MPSLOT", "date": "2024-07-27", "tags": ["equipment", "culling", "save-load", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry", "Armindo", "Emiya"], "href": "./mineru-persistent-save-load-object-transfer.md"}, {"name": "Mineru Text Storage", "abbr": "MTS", "date": "2024-07-11", "tags": ["storage", "mineru"], "versions": ["1.0.0"], "credits": ["CM30"], "href": "./mineru-text-storage.md"}, {"name": "MNF Fusing", "abbr": "MNFF", "date": "2023-06-05", "tags": ["fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./mnf-fusing.md"}, {"name": "MNF Glow Overload", "abbr": "MGO", "date": "2025-01-03", "tags": ["item", "overload", "mnf"], "versions": ["1.0.0"], "credits": ["Toti Sauce"], "href": "./mnf-glow-overload.md"}, {"name": "MNF Zuggle Fuse", "abbr": "MZF", "date": "2023-05-18", "tags": ["zuggling", "weapon", "fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./mnf-zuggle-fuse.md"}, {"name": "Model Teleport Desync", "abbr": "MTEL", "date": "2023-07-29", "tags": ["desync", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./model-teleport-desync.md"}, {"name": "Modifier Deletion Weapon State Transfer", "abbr": "MDWST", "date": "Unknown", "tags": ["duplication", "weapon"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md"}, {"name": "Modifier ONLY Transfer", "abbr": "MOT", "date": "2023-06-09", "tags": ["weapon"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "BigDUCCO"], "href": "./modifier-only-transfer.md"}, {"name": "Moobe Warping", "abbr": "MW", "date": "2024-01-12", "tags": ["oob", "warping", "movement", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./moobe-warping.md"}, {"name": "Mount Lock", "abbr": "ML", "date": "2023-05-21", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./mount-lock.md"}, {"name": "Mozdor Jumping/Slashing", "abbr": "MJS", "date": "2023-05-20", "tags": ["movement", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "AgdoR"], "href": "./mozdor-jumping-slashing.md"}, {"name": "MSNF glowing", "abbr": "MG", "date": "2023-08-02", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["evilgabe"], "href": "./msnf-glowing.md"}, {"name": "Mulberry's Out of Body Experience", "abbr": "MOOBE", "date": "2024-01-06", "tags": ["warping", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./mulberry-s-out-of-body-experience-moobe.md"}, {"name": "New Item Desync", "abbr": "NID", "date": "2023-05-12", "tags": ["duplication", "desync", "menu", "item", "equipment", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Modoki_returns"], "href": "./new-item-desync-equipment-duping.md"}, {"name": "No Bow Sprinting", "abbr": "NBS", "date": "2023-05-12", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./no-bow-sprinting-nbs.md"}, {"name": "Null Dropping", "abbr": "ND", "date": "2024-03-16", "tags": ["menu", "item", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl"], "href": "./null-dropping.md"}, {"name": "Object Culling", "abbr": "OC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "tori", "mulberry", "Timber"], "href": "./object-culling.md"}, {"name": "Object (Moe) Enlargement", "abbr": "MOE", "date": "2024-10-30", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "PetitFrapo", "Jordan"], "href": "./object-moe-enlargement.md"}, {"name": "Ocklusion Hovering", "abbr": "OCKH", "date": "2025-10-12", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic"], "href": "./ocklusion-hovering.md"}, {"name": "Ocklusion", "abbr": "OCKL", "date": "2024-05-29", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./ocklusion.md"}, {"name": "Octo-balloon Detanglement", "abbr": "OBD", "date": "2025-11-16", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./octo-balloon-detanglement.md"}, {"name": "Octodupe", "abbr": "OD", "date": "2023-05-26", "tags": ["duplication", "item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./octodupe.md"}, {"name": "Overload at Home", "abbr": "OAH", "date": "2024-03-20", "tags": ["zuggling", "culling", "overload"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./overload-at-home-aka-pickup-overload.md"}, {"name": "Overload Cold Fuse", "abbr": "OCF", "date": "2023-07-23", "tags": ["item", "weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["F. Buffalo"], "href": "./overload-cold-fuse.md"}, {"name": "Overload Drop Smuggling", "abbr": "ODS", "date": "2023-06-12", "tags": ["zuggling", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ChargeVolt", "Windocks"], "href": "./overload-drop-smuggling.md"}, {"name": "Overload Dynamic Zuggle", "abbr": "ODZ", "date": "2025-05-19", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./overload-dynamic-zuggle.md"}, {"name": "Overload Fuse Entanglement", "abbr": "OFE", "date": "2024-07-23", "tags": ["zuggling", "entanglement", "culling", "overload", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./overload-fuse-entanglement.md"}, {"name": "Overload Persistent Save Load Object Transfer", "abbr": "OPSLOT", "date": "2024-07-26", "tags": ["overload", "save-load"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./overload-persistent-save-load-object-transfer.md"}, {"name": "Pelison Duping", "abbr": "PD", "date": "2023-05-25", "tags": ["duplication", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["AngryEgg", "BigDUCCO"], "href": "./pelison-duping.md"}, {"name": "Persistent Save Load Object Transfer", "abbr": "PSLOT", "date": "2024-01-25", "tags": ["culling", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./persistent-save-load-object-transfer-pslot.md"}, {"name": "Pickup Smuggling", "abbr": "PSMU", "date": "2023-05-28", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ame"], "href": "./pickup-smuggling.md"}, {"name": "Pocket Rocket", "abbr": "PR", "date": "2023-06-15", "tags": ["launching", "equipment", "paraglide", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "SmallAnt"], "href": "./pocket-rocket.md"}, {"name": "Portable Cull Save Load Dupe", "abbr": "PSLD", "date": "2024-07-17", "tags": ["duplication", "culling", "save-load"], "versions": ["1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./portable-cull-save-load-dupe-portacull-sld.md"}, {"name": "Portable Culling", "abbr": "PCULL", "date": "2024-02-27", "tags": ["zuggling", "desync", "item", "culling", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./portable-culling.md"}, {"name": "Portacull Invismuggle", "abbr": "PCI", "date": "2024-02-29", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./portacull-invismuggle.md"}, {"name": "Weapon Despawn Prevention", "abbr": "WDP", "date": "2023-06-28", "tags": ["weapon", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./prevent-weapon-despawn.md"}, {"name": "Prologue Escape", "abbr": "PE", "date": "2024-10-01", "tags": ["duplication", "storage"], "versions": ["1.0.0"], "credits": ["LegendofLinkk", "mulberry", "Aergyl", "Lightos", "EOH_NS_SS"], "href": "./prologue-escape.md"}, {"name": "Proxy Glitches", "abbr": "PG", "date": "Unknown", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./proxy-glitches.md"}, {"name": "Purgatory Save Load Dupe", "abbr": "PGSLD", "date": "2024-02-11", "tags": ["duplication", "equipment", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./purgatory-save-load-dupe.md"}, {"name": "Pyroculling", "abbr": "PYR", "date": "2023-11-17", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.2.0"], "credits": ["ROBUXY2ND"], "href": "./pyroculling.md"}, {"name": "Quantum Linking", "abbr": "QL", "date": "2023-08-30", "tags": ["culling", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "pyuk"], "href": "./quantum-linking-ql.md"}, {"name": "Quick Drop Smuggle", "abbr": "QDS", "date": "2024-03-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0"], "credits": ["mulberry", "Zas", "Aeolian", "WinnerBoi77", "Ryan?"], "href": "./quick-drop-smuggle-qds.md"}, {"name": "Quick Smuggling", "abbr": "QS", "date": "2023-07-10", "tags": ["zuggling", "equipment", "arrow"], "versions": ["1.2.0"], "credits": ["Suishi"], "href": "./quick-smuggling.md"}, {"name": "Reball", "abbr": "RBL", "date": "2023-07-06", "tags": ["movement", "recall", "zonai"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./reball.md"}, {"name": "Recall Cancel", "abbr": "RCC", "date": "2023-07-20", "tags": ["animation", "item", "recall"], "versions": ["1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./recall-cancel.md"}, {"name": "Recall Clip", "abbr": "RC", "date": "2023-05-16", "tags": ["clipping", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüôÒéôÒüØÒéü"], "href": "./recall-clip.md"}, {"name": "Recall Drop Stacking", "abbr": "RDS", "date": "2025-01-04", "tags": ["item", "recall", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Telkic", "mulberry"], "href": "./recall-drop-stacking.md"}, {"name": "Recall Launch", "abbr": "RL", "date": "2023-05-17", "tags": ["launching", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deep"], "href": "./recall-launch.md"}, {"name": "Recall Locking", "abbr": "RLK", "date": "2023-06-11", "tags": ["recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./recall-locking.md"}, {"name": "Recall Sluggle", "abbr": "RSL", "date": "2025-07-12", "tags": ["zuggling", "menu", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["WinnerBoi77"], "href": "./recall-sluggle.md"}, {"name": "Recipe Storage", "abbr": "RS", "date": "2024-09-14", "tags": ["storage", "menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./recipe-storage.md"}, {"name": "Remote Arrow", "abbr": "RAT", "date": "2023-06-02", "tags": ["arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Flash", "ElDuende", "kirigaya"], "href": "./remote-arrow-trap.md"}, {"name": "Replacement Actor Fuse Entanglement", "abbr": "RAFE", "date": "2024-11-09", "tags": ["entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["dt13269", "mulberry"], "href": "./replacement-actor-fuse-entanglement.md"}, {"name": "Resync Fuse Entanglement", "abbr": "RFE", "date": "2023-12-18", "tags": ["item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./resync-fuse-entanglement-resync-fe.md"}, {"name": "Reverse Ascend Storage", "abbr": "RAS", "date": "2023-11-27", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Redrooey"], "href": "./reverse-ascend-storage.md"}, {"name": "Sage Madness", "abbr": "SM", "date": "2023-07-18", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aci"], "href": "./sage-madness.md"}, {"name": "Sage Recycling", "abbr": "SRCY", "date": "2023-05-28", "tags": ["duplication", "tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Knight7108", "Candlelor"], "href": "./sage-recycling.md"}, {"name": "Save Load Dupe", "abbr": "SLD", "date": "2023-05-16", "tags": ["duplication", "equipment", "save-load", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ZombieBoy225", "ness", "ElDuende"], "href": "./save-load-dupe-sld.md"}, {"name": "Save Load Zuggling", "abbr": "SLZ", "date": "2023-05-23", "tags": ["zuggling", "save-load", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["NicNac", "Flash", "BigDUCCO", "Wip long sticks enjoyer"], "href": "./save-load-zuggling-slz.md"}, {"name": "Scope Render Cancel", "abbr": "SRC", "date": "2023-05-19", "tags": ["animation", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "eXe"], "href": "./scope-render-cancel.md"}, {"name": "Shadow/Void Icons", "abbr": "SVI", "date": "2024-10-16", "tags": ["equipment", "fuse", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Lightos", "PetitFrapo"], "href": "./shadow-void-icons.md"}, {"name": "Shock Cold Fuse", "abbr": "SCF", "date": "2023-09-11", "tags": ["weapon", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-cold-fuse.md"}, {"name": "Shock Effect Overload", "abbr": "SEO", "date": "2023-07-26", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "R4000"], "href": "./shock-effect-overload-seo.md"}, {"name": "Shock Fuse Entanglement", "abbr": "SFE", "date": "2023-09-12", "tags": ["zuggling", "item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-fuse-entanglement.md"}, {"name": "Shock Smuggle", "abbr": "SSMU", "date": "2023-06-01", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["sleepyppls"], "href": "./shock-smuggle.md"}, {"name": "Shrunken Actors", "abbr": "SA", "date": "2025-10-26", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./shrunken-actors.md"}, {"name": "Slate Storage", "abbr": "SLST", "date": "2024-09-21", "tags": ["storage", "damage"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk"], "href": "./slate-storage.md"}, {"name": "Slugging", "abbr": "SLG", "date": "2023-06-15", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./slugging.md"}, {"name": "Smuggle Retrieval", "abbr": "SRET", "date": "2024-12-18", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["PetitFrapo"], "href": "./smuggle-retrieval.md"}, {"name": "Smuggle Stacking Zuggle", "abbr": "SSZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "LegendofLinkk", "Mozz"], "href": "./smuggle-stacking-zuggle-ssz.md"}, {"name": "Split Item Duplication", "abbr": "SID", "date": "2025-06-19", "tags": ["duplication", "item", "zuggling"], "versions": ["1.2.0"], "credits": ["Telkic", "mulberry", "WinnerBoi77"], "href": "./split-item-duplication-sid.md"}, {"name": "Spring Fall Damage Cancel", "abbr": "SFDC", "date": "2023-05-15", "tags": ["animation", "damage", "movement", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./spring-fall-damage-cancel.md"}, {"name": "Spring Strangeness", "abbr": "STRS", "date": "2023-05-15", "tags": ["spring", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi", "Owen"], "href": "./spring-strangeness.md"}, {"name": "Springboard Clipping", "abbr": "SBC", "date": "2023-05-27", "tags": ["clipping", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ab2x3z"], "href": "./springboard-clipping.md"}, {"name": "Springboarding", "abbr": "SBRD", "date": "2023-05-24", "tags": ["equipment", "shield", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springboarding.md"}, {"name": "Springdolling", "abbr": "SDOL", "date": "2023-05-15", "tags": ["launching", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springdolling.md"}, {"name": "Stack Splitting", "abbr": "SSPL", "date": "2024-12-31", "tags": ["item", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["s0ft", "Telkic", "mulberry"], "href": "./stack-splitting.md"}, {"name": "Stamina Depletion Freeze", "abbr": "SDF", "date": "2023-05-20", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./stamina-depletion-freeze-sdf.md"}, {"name": "Stick Desync Clip", "abbr": "SDC", "date": "2023-07-01", "tags": ["clipping", "desync", "item", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "DisguisedMoth"], "href": "./stick-desync-clip-sdc.md"}, {"name": "Sticky Dynamic Purgatory", "abbr": "SDP", "date": "2024-02-15", "tags": ["equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./sticky-dynamic-purgatory.md"}, {"name": "Super Bomb Jump", "abbr": "SBJ", "date": "2023-09-14", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["FerrusCube", "Aergyl"], "href": "./super-bomb-jump.md"}, {"name": "Super Fuse Overload", "abbr": "SFO", "date": "2025-12-06", "tags": ["weapon", "overload", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Aergyl", "Jordan", "MandelbrotChaylay"], "href": "./super-fuse-overload.md"}, {"name": "Surf storage", "abbr": "SSTR", "date": "2023-09-22", "tags": ["storage"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./surf-storage.md"}, {"name": "Swap Resync Zuggle", "abbr": "SRZ", "date": "2025-08-11", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry", "MandelbrotChaylay"], "href": "./swap-resync-zuggle-srz.md"}, {"name": "Swap Resync", "abbr": "SR", "date": "2025-08-10", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["MandelbrotChaylay"], "href": "./swap-resync.md"}, {"name": "Temporary Devices", "abbr": "TD", "date": "2024-11-30", "tags": ["fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./temporary-devices.md"}, {"name": "Texture Tearing", "abbr": "TT", "date": "2024-01-13", "tags": ["oob", "menu", "equipment", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./texture-tearing.md"}, {"name": "Throken", "abbr": "THK", "date": "2025-05-17", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikaboze"], "href": "./throken.md"}, {"name": "Throw Cancelling", "abbr": "TC", "date": "Unknown", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Quelfth"], "href": "./throw-cancelling.md"}, {"name": "Throw Tap Sprinting", "abbr": "TTS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer", "Tauktes"], "href": "./throw-tap-sprinting-tts.md"}, {"name": "Throwless Storage", "abbr": "THS", "date": "2023-06-19", "tags": ["storage", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["evilgabe", "NX721"], "href": "./throwless-storage-previously-known-as-beam-storage.md"}, {"name": "Time Bomb cancel", "abbr": "TBC", "date": "2023-11-04", "tags": ["animation", "equipment", "damage", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["tzakazuki"], "href": "./time-bomb-cancel.md"}, {"name": "Toti Saucery", "abbr": "TOTS", "date": "2024-08-17", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "Telkic"], "href": "./toti-saucery.md"}, {"name": "Travel Medallion storage", "abbr": "TMS", "date": "2023-06-16", "tags": ["storage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kirigaya"], "href": "./travel-medallion-storage-tms.md"}, {"name": "Tulin Pumping", "abbr": "TP", "date": "2023-05-14", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikkitrix"], "href": "./tulin-pumping.md"}, {"name": "Two Handed With Shield", "abbr": "THWS", "date": "2023-08-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Bucket_Sloe"], "href": "./two-handed-with-shield.md"}, {"name": "Ultimate Pocket Rocket", "abbr": "UPR", "date": "2025-05-20", "tags": ["launching", "warping", "ultrahand"], "versions": ["1.0.0"], "credits": ["Aergyl", "mulberry", "Ikaboze", "Jordan"], "href": "./ultimate-pocket-rocket.md"}, {"name": "Ultra Save Load Object Transfer", "abbr": "USLOT", "date": "2024-02-15", "tags": ["save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./ultra-save-load-object-transfer.md"}, {"name": "Ultrabroken Smuggling", "abbr": "UBS", "date": "2023-06-13", "tags": ["zuggling", "equipment", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["The_Andromeda"], "href": "./ultrabroken-smuggling-ubs.md"}, {"name": "Ultrabroken", "abbr": "UB", "date": "2023-05-29", "tags": ["item", "ultrahand", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Duncan"], "href": "./ultrabroken.md"}, {"name": "Unload Duping", "abbr": "UD", "date": "2023-05-31", "tags": ["duplication", "item", "culling", "fuse", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª", "ÕìâÕ╣┤ÞîÂÚÑ╝"], "href": "./unload-duping.md"}, {"name": "Unload WST", "abbr": "UWST", "date": "Unknown", "tags": ["item", "culling", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "Vee.Might.Exist", "Syb"], "href": "./unload-wst.md"}, {"name": "Unsheathed Mastersword", "abbr": "UMS", "date": "2023-07-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "DanielNeia"], "href": "./unsheathed-mastersword.md"}, {"name": "Vendor Scamming", "abbr": "VS", "date": "2023-07-03", "tags": ["zuggling", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "Mozz", "NaN Gogh"], "href": "./vendor-scamming.md"}, {"name": "Void Dipping", "abbr": "VD", "date": "2025-12-29", "tags": ["item", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Squidwest", "mulberry", "Aergyl"], "href": "./void-dipping.md"}, {"name": "Void Hold Storage", "abbr": "VHS", "date": "2023-07-22", "tags": ["storage", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "NX721"], "href": "./void-hold-storage.md"}, {"name": "Void Holding", "abbr": "VH", "date": "2023-06-10", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Lightos"], "href": "./void-holding.md"}, {"name": "Wacko Attacko", "abbr": "WATK", "date": "2024-01-21", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3", "WinnerBoi77"], "href": "./wacko-attacko.md"}, {"name": "Warp Bumping", "abbr": "WB", "date": "2023-06-07", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Mozz", "InAMuffinCup"], "href": "./warp-bumping.md"}, {"name": "Weapon Dash GAS", "abbr": "WDGAS", "date": "2025-11-28", "tags": ["gas", "weapon", "culling", "fuse", "zonai"], "versions": ["1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Toti Sauce"], "href": "./weapon-dash-gas.md"}, {"name": "Weapon Extensions", "abbr": "WEXT", "date": "2023-06-20", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deltenic", "Flash", "Zas"], "href": "./weapon-extensions.md"}, {"name": "Weapon FE", "abbr": "WFE", "date": "2023-06-01", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ROBUXY2ND", "Physioninja"], "href": "./weapon-fe.md"}, {"name": "Weapon Sheath Offset", "abbr": "WSO", "date": "2023-06-25", "tags": ["zuggling", "weapon", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["circyit", "dash"], "href": "./weapon-sheath-offset-wso.md"}, {"name": "Weapon Stacking Duplication", "abbr": "WSD", "date": "2023-05-16", "tags": ["duplication", "item", "weapon", "equipment", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ErlingÚÖäÞ║½"], "href": "./weapon-stacking-duplication-wsd.md"}, {"name": "Weapon Stand Dynamic Zuggle", "abbr": "WSDZ", "date": "2024-03-14", "tags": ["zuggling", "weapon", "item", "equipment"], "versions": ["1.0.0"], "credits": ["WinnerBoi77"], "href": "./weapon-stand-dynamic-zuggle.md"}, {"name": "Weapon State Transfer", "abbr": "WST", "date": "2023-05-19", "tags": ["weapon", "fuse", "entanglement", "equipment", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "kurocat471", "ElDuende", "Mentor_Kurt"], "href": "./weapon-state-transfer-wst.md"}, {"name": "Weather Amnesia", "abbr": "WA", "date": "2023-06-25", "tags": ["environment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk"], "href": "./weather-amnesia-wa.md"}, {"name": "Wheel Warping", "abbr": "WW", "date": "2023-06-18", "tags": ["launching", "warping", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk"], "href": "./wheel-warping.md"}, {"name": "Wheel Zoomy", "abbr": "WZ", "date": "2023-07-12", "tags": ["movement", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Solo_Turtle"], "href": "./wheel-zoomy-also-known-as-wheel-wacko-boingo.md"}, {"name": "Wireless Energy", "abbr": "WE", "date": "2023-07-11", "tags": ["equipment", "culling", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./wireless-energy.md"}, {"name": "Wuggle", "abbr": "WGL", "date": "2023-12-29", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "ROBUXY2ND"], "href": "./wuggle-weird-zuggle.md"}, {"name": "Yee Fuse Entanglement", "abbr": "YEEFE", "date": "2024-02-20", "tags": ["entanglement", "culling", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee", "mulberry"], "href": "./yee-fuse-entanglement.md"}, {"name": "Zapshield", "abbr": "ZAP", "date": "2024-09-16", "tags": ["equipment", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./zapshield.md"}, {"name": "ZL Animation Reset", "abbr": "ZLAR", "date": "2024-01-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./zl-animation-reset-zlar.md"}, {"name": "Zoggle", "abbr": "ZOG", "date": "2024-01-04", "tags": ["zuggling", "ultrahand", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ryan?", "Ock"], "href": "./zoggle.md"}, {"name": "Zonai Inventory Shift Dupe", "abbr": "ZISD", "date": "2023-07-10", "tags": ["duplication", "menu", "buff", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "quantim"], "href": "./zonai-inventory-shift-dupe-zisd.md"}, {"name": "Zonai Sort Duplication", "abbr": "ZSD", "date": "2023-05-22", "tags": ["duplication", "menu", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Quelfth", "Flash"], "href": "./zonai-sort-duplication-zsd.md"}, {"name": "Zonai Storage", "abbr": "ZS", "date": "2023-08-13", "tags": ["storage", "zonai"], "versions": ["1.0.0"], "credits": ["bebu0815"], "href": "./zonai-storage.md"}, {"name": "Zuggle Load Object Transfering", "abbr": "ZLOT", "date": "2023-06-07", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup", "ChargeVolt"], "href": "./zuggle-load-object-transfering-zlot.md"}, {"name": "Zuggle Overload Desync", "abbr": "ZOD", "date": "Unknown", "tags": ["zuggling", "desync", "menu", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./zuggle-overload-desync.md"}, {"name": "Zuggle Overload Out Of Bounds", "abbr": "ZOOB", "date": "2023-05-18", "tags": ["clipping", "oob", "zuggling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["AngryEgg"], "href": "./zuggle-overload-out-of-bounds.md"}, {"name": "Zuggle Overload", "abbr": "ZO", "date": "2023-05-17", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle-overload.md"}, {"name": "Zuggle", "abbr": "ZGL", "date": "2023-05-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle.md"}]
\ No newline at end of file
diff --git a/docs/wiki/glitchcraft/animation-swap.md b/docs/wiki/glitchcraft/animation-swap.md
index 6c417085a..cba7f7335 100644
--- a/docs/wiki/glitchcraft/animation-swap.md
+++ b/docs/wiki/glitchcraft/animation-swap.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["Swinginman"]
 date: "2023-05-17"
 description: "Combine animation sets when zuggle overloaded."
-aliases: ["anim-swap", "animation-swap", "animation-swap glitch"]
+aliases: []
 tags: ["zuggling", "animation", "overload"]
 ---
 
diff --git a/docs/wiki/glitchcraft/ascend-storage.md b/docs/wiki/glitchcraft/ascend-storage.md
index 4be9c94c3..928a2a2c2 100644
--- a/docs/wiki/glitchcraft/ascend-storage.md
+++ b/docs/wiki/glitchcraft/ascend-storage.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["Saria"]
 date: "2023-05-19"
 description: "Misplaces the point where Link goes after using Ascend."
-aliases: ["ascend-storage", "storage ascend"]
+aliases: ["ascend storage", "ascend storage glitch", "ascend-storage", "storage ascend"]
 tags: ["storage", "ascend"]
 ---
 
diff --git a/docs/wiki/glitchcraft/autobuild-cancel-slide-abcs.md b/docs/wiki/glitchcraft/autobuild-cancel-slide-abcs.md
index 51b1cf0da..8c41f6073 100644
--- a/docs/wiki/glitchcraft/autobuild-cancel-slide-abcs.md
+++ b/docs/wiki/glitchcraft/autobuild-cancel-slide-abcs.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1"]
 credits: ["Takosensai1"]
 date: "2023-05-18"
 description: "Allows you to slide on top of the blueprint build over the map at insane speeds, or gain immense amounts of height."
-aliases: ["auto-build", "autobuild", "autobuild cancel", "autobuild-cancel-slide"]
+aliases: ["autobuild cancel", "auto-build"]
 tags: ["animation", "movement", "autobuild"]
 ---
 
diff --git a/docs/wiki/glitchcraft/back-to-back-bloodmoon.md b/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
index 246f3fe90..8d7346e0d 100644
--- a/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
+++ b/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
@@ -5,8 +5,8 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["Lopitty"]
 date: "2023-05-17"
 description: "A strange phenominon where blood moons occured back to back."
-aliases: ["back-to-back bloodmoon", "back-to-back-bloodmoon", "btb", "btb bloodmoon"]
-tags: ["blood-moon"]
+aliases: ["back-to-back bloodmoon", "btb bloodmoon"]
+tags: ["bloodmoon"]
 ---
 
 # Back to Back Bloodmoon `BTBB`
diff --git a/docs/wiki/glitchcraft/banc-storage.md b/docs/wiki/glitchcraft/banc-storage.md
index cd0d48369..29b44479c 100644
--- a/docs/wiki/glitchcraft/banc-storage.md
+++ b/docs/wiki/glitchcraft/banc-storage.md
@@ -6,7 +6,7 @@ credits: ["Lightos", "mulberry", "Aergyl", "EOH_NS_SS"]
 date: "2024-10-01"
 description: "Store banc changes to another save file using memory interrupt"
 aliases: ["banc-storage"]
-tags: ["storage", "warping", "save-load", "blood-moon"]
+tags: ["storage", "warping", "save-load", "bloodmoon"]
 ---
 
 # Banc Storage `BANC`
diff --git a/docs/wiki/glitchcraft/dive-cancel-glide-boost.md b/docs/wiki/glitchcraft/dive-cancel-glide-boost.md
index 005be6dc0..a7aaef15c 100644
--- a/docs/wiki/glitchcraft/dive-cancel-glide-boost.md
+++ b/docs/wiki/glitchcraft/dive-cancel-glide-boost.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["kurocat471", "Mety333"]
 date: "2023-05-14"
 description: "Allows you to preserve the increased speed from diving with the Glide Suit into paragliding"
-aliases: ["dive-cancel-glide-boost"]
+aliases: ["dive cancel", "dive cancel gliding", "dive cancel glide", "glide boost", "dive-cancel-glide-boost"]
 tags: ["animation", "paraglide"]
 ---
 
diff --git a/docs/wiki/glitchcraft/double-unfuse-duplicashen-dud.md b/docs/wiki/glitchcraft/double-unfuse-duplicashen-dud.md
index 0560a2b66..fa11b3cf5 100644
--- a/docs/wiki/glitchcraft/double-unfuse-duplicashen-dud.md
+++ b/docs/wiki/glitchcraft/double-unfuse-duplicashen-dud.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1"]
 credits: ["Li Shen (Ú»ëþÑ×)"]
 date: "2023-05-15"
 description: "Allows you to duplicate any material that can be fused to an arrow"
-aliases: ["double unfuse", "double-unfuse", "double-unfuse-duplicashen", "dupe unfuse"]
+aliases: ["double unfuse", "double unfuse duplicashen", "dupe unfuse"]
 tags: ["duplication", "item", "weapon", "fuse", "arrow"]
 ---
 
diff --git a/docs/wiki/glitchcraft/forced-blood-moon.md b/docs/wiki/glitchcraft/forced-blood-moon.md
index cd9ac7fb5..2120be149 100644
--- a/docs/wiki/glitchcraft/forced-blood-moon.md
+++ b/docs/wiki/glitchcraft/forced-blood-moon.md
@@ -6,7 +6,7 @@ credits: ["1789(@W0ERYySQgZyGOY3)", "Simonfirefighter", "Maxmasher", "Flash", "a
 date: "2023-05-28"
 description: "Allows you to force a blood moon whenever you want"
 aliases: ["forced-blood-moon"]
-tags: ["blood-moon"]
+tags: ["bloodmoon"]
 ---
 
 # Forced Blood Moon `FBM`
diff --git a/docs/wiki/glitchcraft/jumpslash-canceling.md b/docs/wiki/glitchcraft/jumpslash-canceling.md
index 51f101501..599eaa38c 100644
--- a/docs/wiki/glitchcraft/jumpslash-canceling.md
+++ b/docs/wiki/glitchcraft/jumpslash-canceling.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["LegendofLinkk", "Mozz"]
 date: "2023-05-21"
 description: "Interrupt jumpslashes by swapping a shield mid-animation"
-aliases: ["jumpslash-canceling"]
+aliases: ["jumpslash cancel", "jump slash", "jumpslash", "jump-slash", "jump slash cancel", "jumpslash-canceling"]
 tags: ["animation", "equipment", "shield"]
 ---
 
diff --git a/docs/wiki/glitchcraft/long-jump.md b/docs/wiki/glitchcraft/long-jump.md
index 0fd4b208c..84bbe5e33 100644
--- a/docs/wiki/glitchcraft/long-jump.md
+++ b/docs/wiki/glitchcraft/long-jump.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["Mozz"]
 date: "2023-05-18"
 description: "Jump farther"
-aliases: ["long-jump", "longjump"]
+aliases: ["long jump", "long-jump", "longjump"]
 tags: ["movement"]
 ---
 
diff --git a/docs/wiki/glitchcraft/message-not-found-mnf.md b/docs/wiki/glitchcraft/message-not-found-mnf.md
index d29f1f218..8b9e860d6 100644
--- a/docs/wiki/glitchcraft/message-not-found-mnf.md
+++ b/docs/wiki/glitchcraft/message-not-found-mnf.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["LegendofLinkk", "Abahbob"]
 date: "2023-05-17"
 description: "Allows you to obtain the prologue master sword (named MsgNotFound or MNF), whose durability cannot decrease"
-aliases: ["message-not-found"]
+aliases: ["message not found", "message not found error", "message-not-found"]
 tags: ["mnf"]
 ---
 
diff --git a/docs/wiki/glitchcraft/midair-sort-duplication-msd.md b/docs/wiki/glitchcraft/midair-sort-duplication-msd.md
index cdd712160..baa33d3a3 100644
--- a/docs/wiki/glitchcraft/midair-sort-duplication-msd.md
+++ b/docs/wiki/glitchcraft/midair-sort-duplication-msd.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1"]
 credits: ["Zas", "kurocat471"]
 date: "2023-05-21"
 description: "Allows duplication of materials while midair."
-aliases: ["midair-sort-duplication"]
+aliases: ["midair sort duplication", "midair-sort-duplication"]
 tags: ["duplication", "menu", "item", "paraglide"]
 ---
 
diff --git a/docs/wiki/glitchcraft/midair-throw-duplication-mtd.md b/docs/wiki/glitchcraft/midair-throw-duplication-mtd.md
index 77652ab13..76b8e62ec 100644
--- a/docs/wiki/glitchcraft/midair-throw-duplication-mtd.md
+++ b/docs/wiki/glitchcraft/midair-throw-duplication-mtd.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["quantim"]
 date: "2023-07-02"
 description: "Allows you to dupe any item that can be thrown, including Zonai capsules."
-aliases: ["midair-throw-duplication"]
+aliases: ["midair duplication", "air dupe", "midair-throw-duplication"]
 tags: ["duplication", "item", "zonai", "paraglide"]
 ---
 
diff --git a/docs/wiki/glitchcraft/minecart-rail-collision-launching-mrcl.md b/docs/wiki/glitchcraft/minecart-rail-collision-launching-mrcl.md
index b7d84185e..99e6f6f85 100644
--- a/docs/wiki/glitchcraft/minecart-rail-collision-launching-mrcl.md
+++ b/docs/wiki/glitchcraft/minecart-rail-collision-launching-mrcl.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1"]
 credits: ["ÒüØÒéë-ÒüòÒéô"]
 date: "2023-05-18"
 description: "Allows the usage of minecarts to be launched from awkward collision grabbing on rails."
-aliases: ["minecart collision", "minecart rail collision", "minecart-rail-collision-launching", "rail collision launching"]
+aliases: ["minecart collision", "minecart rail collision", "rail collision launching", "collision launch", "collision launching"]
 tags: ["launching"]
 ---
 
diff --git a/docs/wiki/glitchcraft/mnf-zuggle-fuse.md b/docs/wiki/glitchcraft/mnf-zuggle-fuse.md
index c41970079..5af5a6fd4 100644
--- a/docs/wiki/glitchcraft/mnf-zuggle-fuse.md
+++ b/docs/wiki/glitchcraft/mnf-zuggle-fuse.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["Zvleon"]
 date: "2023-05-18"
 description: "Allows to fuse to the MNF"
-aliases: ["mnf-zuggle-fuse"]
+aliases: ["message not found zuggle", "mnf zuggle", "mnf-zuggle-fuse"]
 tags: ["zuggling", "weapon", "fuse", "mnf"]
 ---
 
diff --git a/docs/wiki/glitchcraft/mozdor-jumping-slashing.md b/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
index cdced2a31..592971dad 100644
--- a/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
+++ b/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["Mozz", "AgdoR"]
 date: "2023-05-20"
 description: "Allows you to jump very far (can be chained infinitly)"
-aliases: ["mozdor-jumping/slashing"]
+aliases: ["mozdor jumping slashing", "mozdor", "mozdor-jumping/slashing"]
 tags: ["movement", "weapon"]
 ---
 
diff --git a/docs/wiki/glitchcraft/persistent-save-load-object-transfer-pslot.md b/docs/wiki/glitchcraft/persistent-save-load-object-transfer-pslot.md
index 225cb0e02..782ca0ae2 100644
--- a/docs/wiki/glitchcraft/persistent-save-load-object-transfer-pslot.md
+++ b/docs/wiki/glitchcraft/persistent-save-load-object-transfer-pslot.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["mulberry"]
 date: "2024-01-25"
 description: "Allows objects to go through saves by permanently culling their FE bases (parents)."
-aliases: ["persistent-save-load-object-transfer", "save load dupe", "save-load-dupe", "save/load dupe", "sld"]
+aliases: ["save load dupe", "save/load dupe"]
 tags: ["culling", "save-load", "ultrahand"]
 ---
 
diff --git a/docs/wiki/glitchcraft/recall-clip.md b/docs/wiki/glitchcraft/recall-clip.md
index 4036d54fe..0c9034b8c 100644
--- a/docs/wiki/glitchcraft/recall-clip.md
+++ b/docs/wiki/glitchcraft/recall-clip.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1"]
 credits: ["ÒüôÒéôÒüØÒéü"]
 date: "2023-05-16"
 description: "Allows you to clip through things using a large object and recall"
-aliases: ["recall-clip", "recallclip"]
+aliases: ["recall clip", "recall-clip glitch", "recall-clip", "recallclip"]
 tags: ["clipping", "ultrahand", "recall"]
 ---
 
diff --git a/docs/wiki/glitchcraft/recall-launch.md b/docs/wiki/glitchcraft/recall-launch.md
index 93c2d5f13..f6a14587a 100644
--- a/docs/wiki/glitchcraft/recall-launch.md
+++ b/docs/wiki/glitchcraft/recall-launch.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["Deep"]
 date: "2023-05-17"
 description: "Allows you to launch yourself very far"
-aliases: ["recall launch glitch", "recall-launch"]
+aliases: ["recall launch", "recall launch glitch", "recall-launch"]
 tags: ["launching", "ultrahand", "recall"]
 ---
 
diff --git a/docs/wiki/glitchcraft/save-load-dupe-sld.md b/docs/wiki/glitchcraft/save-load-dupe-sld.md
index 2a163b3f6..d17d67d56 100644
--- a/docs/wiki/glitchcraft/save-load-dupe-sld.md
+++ b/docs/wiki/glitchcraft/save-load-dupe-sld.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["ZombieBoy225", "ness", "ElDuende"]
 date: "2023-05-16"
 description: "Allows easy duplication of your weapons, bows, and shields"
-aliases: ["persistent save load object transfer", "save-load-dupe", "save-load-duplication", "save/load dupe", "sld dupe"]
+aliases: ["save-load-dupe", "save/load dupe", "save load duplication"]
 tags: ["duplication", "equipment", "save-load", "shield", "bow"]
 ---
 
diff --git a/docs/wiki/glitchcraft/scope-render-cancel.md b/docs/wiki/glitchcraft/scope-render-cancel.md
index baa07fcbe..9e275396c 100644
--- a/docs/wiki/glitchcraft/scope-render-cancel.md
+++ b/docs/wiki/glitchcraft/scope-render-cancel.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["NX721", "eXe"]
 date: "2023-05-19"
 description: "Removes scope HUD and reveals two borders that show an overlay that renders flames, visual effects, etc."
-aliases: ["scope-render-cancel"]
+aliases: ["scope render cancel", "scope-render-cancel"]
 tags: ["animation", "bow"]
 ---
 
diff --git a/docs/wiki/glitchcraft/smuggle-stacking-zuggle-ssz.md b/docs/wiki/glitchcraft/smuggle-stacking-zuggle-ssz.md
index 0f1eece45..bd056e199 100644
--- a/docs/wiki/glitchcraft/smuggle-stacking-zuggle-ssz.md
+++ b/docs/wiki/glitchcraft/smuggle-stacking-zuggle-ssz.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
 credits: ["BigDUCCO", "LegendofLinkk", "Mozz"]
 date: "2023-06-06"
 description: "Allows to zuggle bows and shields in version 1.1.2. Weapon zuggle on 1.1.2 is a little bit more complicated. Check the next glitch (FEZ) for that."
-aliases: ["smuggle-stacking-zuggle"]
+aliases: ["zuggle stacking", "zuggle stack", "smuggle-stacking-zuggle"]
 tags: ["zuggling", "item", "equipment", "shield", "bow"]
 ---
 
diff --git a/docs/wiki/glitchcraft/stamina-depletion-freeze-sdf.md b/docs/wiki/glitchcraft/stamina-depletion-freeze-sdf.md
index 55f25fbe7..f6b6e703b 100644
--- a/docs/wiki/glitchcraft/stamina-depletion-freeze-sdf.md
+++ b/docs/wiki/glitchcraft/stamina-depletion-freeze-sdf.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
 credits: ["Lightos"]
 date: "2023-05-20"
 description: "Certain actions can cause the stamina depletion to glitch out."
-aliases: ["stamina-depletion-freeze"]
+aliases: ["stamina depletion freeze", "stamina-depletion-freeze"]
 tags: ["Unknown"]
 ---
 
diff --git a/docs/wiki/glitchcraft/weapon-stacking-duplication-wsd.md b/docs/wiki/glitchcraft/weapon-stacking-duplication-wsd.md
index 0f9c2ebab..4a3fee2f6 100644
--- a/docs/wiki/glitchcraft/weapon-stacking-duplication-wsd.md
+++ b/docs/wiki/glitchcraft/weapon-stacking-duplication-wsd.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1"]
 credits: ["ErlingÚÖäÞ║½"]
 date: "2023-05-16"
 description: "Allows for a quick dupe of any weapon, bow or shield"
-aliases: ["weapon stacking dupe", "weapon-stacking-duplication"]
+aliases: ["weapon stacking", "stacking weapons", "weapon stacking dupe", "weapon-stacking-duplication"]
 tags: ["duplication", "item", "weapon", "equipment", "bow"]
 ---
 
diff --git a/docs/wiki/glitchcraft/zuggle-overload-oob.md b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
similarity index 83%
rename from docs/wiki/glitchcraft/zuggle-overload-oob.md
rename to docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
index c92e38e86..4e1497c62 100644
--- a/docs/wiki/glitchcraft/zuggle-overload-oob.md
+++ b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
@@ -1,15 +1,15 @@
 ---
-title: "Zuggle Overload OOB"
+title: "Zuggle Overload Out Of Bounds"
 abbreviation: "ZOOB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
 credits: ["AngryEgg"]
 date: "2023-05-18"
 description: "Allows you to clip OOB using zuggle overload"
-aliases: ["zuggle overload", "zuggle-overload", "zuggle-overload-oob"]
+aliases: ["zuggle-overload-oob", "zuggle overload oob", "zo oob"]
 tags: ["clipping", "oob", "zuggling", "overload"]
 ---
 
-# Zuggle Overload OOB `ZOOB`
+# Zuggle Overload Out Of Bounds `ZOOB`
 `1.0.0` `1.1.0` `1.1.1` `1.1.2`
 
 ## Summary
diff --git a/docs/wiki/glitchcraft/zuggle-overload.md b/docs/wiki/glitchcraft/zuggle-overload.md
index 030d762d2..958e18294 100644
--- a/docs/wiki/glitchcraft/zuggle-overload.md
+++ b/docs/wiki/glitchcraft/zuggle-overload.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["Zvleon"]
 date: "2023-05-17"
 description: "Allows you to overload your game, causing many other glitches"
-aliases: ["zuggle overload oob", "zuggle-overload"]
+aliases: ["zuggle-overload"]
 tags: ["zuggling", "overload", "item", "equipment"]
 ---
 
diff --git a/docs/wiki/glitchcraft/zuggle.md b/docs/wiki/glitchcraft/zuggle.md
index 7ae671b36..5fe218c85 100644
--- a/docs/wiki/glitchcraft/zuggle.md
+++ b/docs/wiki/glitchcraft/zuggle.md
@@ -5,7 +5,7 @@ versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
 credits: ["Zvleon"]
 date: "2023-05-16"
 description: "Zuggling allows you to stack weapons to get more attack power by cloning equiment onto Link, adding hitboxes on top of each other."
-aliases: ["zuggle overload"]
+aliases: ["zuggling", "zugl", "zug"]
 tags: ["zuggling", "item", "equipment"]
 ---
 
diff --git a/docs/wiki/zuggling/zuggle-library.md b/docs/wiki/zuggling/zuggle-library.md
index 73322329d..b9b51ac21 100644
--- a/docs/wiki/zuggling/zuggle-library.md
+++ b/docs/wiki/zuggling/zuggle-library.md
@@ -12,7 +12,7 @@ This page complies Smuggling and Zuggling related glitches for quick reference.
 - [Equipment Collision Zuggle](../glitchcraft/equipment-collision-zuggle.md)
 - [Zuggle Overload](../glitchcraft/zuggle-overload.md)
 - [MNF Zuggle Fuse](../glitchcraft/mnf-zuggle-fuse.md)
-- [Zuggle Overload OOB](../glitchcraft/zuggle-overload-oob.md)
+- [Zuggle Overload Out Of Bounds](../glitchcraft/zuggle-overload-out-of-bounds.md)
 - [Map Zuggling (MZ)](../glitchcraft/map-zuggling-mz.md)
 - [Save Load Zuggling (SLZ)](../glitchcraft/save-load-zuggling-slz.md)
 - [Pickup Smuggling](../glitchcraft/pickup-smuggling.md)
diff --git a/docs/worker/synonyms.json b/docs/worker/synonyms.json
index d1786c4fc..41c23a3f6 100644
--- a/docs/worker/synonyms.json
+++ b/docs/worker/synonyms.json
@@ -1,61 +1,10 @@
 [
-  ["ultrabroken", "ultrabreak", "UB", "ultra-broken"],
-  ["zuggle", "zuggling", "zugl", "zug", "zuggle overload"],
-  ["tulin pump", "tulin-pump", "pump tulin", "tulin pumping", "tulinpump"],
-  ["recall-clip", "recall clip", "recallclip", "recall-clip glitch"],
-  ["back-to-back bloodmoon", "back to back bloodmoon", "btb bloodmoon", "btb"],
-  ["weapon stacking", "weapon-stack", "stacking weapons", "weapon stacking dupe"],
-  ["save-load-dupe", "save load dupe", "save load duplication"],
-  ["minecart rail collision", "minecart rail collision launching", "rail collision launching", "minecart collision"],
-  ["jump slash", "jumpslash", "jump-slash", "jump slash cancel", "jumpslash cancel"],
-  ["throw tap sprinting", "throw-tap-sprinting", "tts", "throw tap"],
-  ["bow sprinting", "bow-sprinting", "bow-sprint", "bow sprint"],
-  ["bthrow sprinting", "bthrow-sprinting", "bthrow sprint"],
-  ["infinite damage", "infinite-damage", "infinite dmg", "infinite HP damage"],
-  ["anti gravity glitch", "antigravity glitch", "anti-gravity glitch", "anti gravity"],
-  ["laser oob", "laser-oob", "laser out of bounds"],
-  ["crouch sprinting", "crouch-sprinting", "crouch sprint", "crouch-sprint"],
-  ["dive cancel", "dive-cancel", "dive cancel gliding", "dive cancel glide"],
-  ["animation swap", "animation-swap", "anim swap"],
-  ["message not found", "message-not-found", "mnf", "message not found error"],
-  ["zuggle overload", "zuggle-overload", "zuggle overload oob"],
-  ["autobuild cancel slide", "autobuild-cancel-slide", "abcs", "autobuild cancel"],
-  ["long jump", "long-jump", "longjump", "lj"],
-  ["weapon state transfer", "weapon-state-transfer", "weapon state transfer wst"],
-  ["ascend storage", "ascend-storage", "ascend storage glitch"],
-  ["scope render cancel", "scope-render-cancel", "scope render cancel"],
-  ["midair item transmutation", "midair-item-transmutation", "midair item transmutation", "mit"],
-  ["mozdor jumping slashing", "mozdor-jumping-slashing", "mozdor jumping slashing", "mozdor"],
-  ["teleport", "teleport glitch", "teleportation", "tp"],
+  ["ultrabroken", "ultrabreak", "ultra-broken"],
+  ["teleport", "teleport glitch", "teleportation"],
   ["clip", "clipping", "clipping glitch", "map clip"],
   ["launch", "launch glitch", "launching", "propel launch"],
-  ["glide boost", "glide-boost", "glide boost glitch"],
-  ["fall damage cancel", "fall-damage-cancel", "fall damage cancel"],
-  ["double unfuse", "double-unfuse", "double unfuse duplicashen", "dupe unfuse"],
-  ["weapon stacking duplication", "weapon-stacking-duplication", "weapon stacking dupe", "wsd"],
-  ["save load dupe", "save-load-duplication", "sld dupe"],
-  ["recall launch", "recall-launch", "recall launch glitch"],
-  ["animation swap", "anim-swap", "animation-swap glitch"],
-  ["autobuild", "auto-build", "autobuild cancel slide"],
-  ["midair sort duplication", "midair-sort-duplication", "msd"],
-  ["infinite stamina", "infinite-stamina", "stamina dup"],
-  ["stamina depletion freeze", "stamina-depletion-freeze", "sdf"],
-  ["jumpslash cancel", "jumpslash-cancel", "jump slash cancel"],
-  ["bow sprint", "bow-sprinting", "bow sprinting"],
-  ["throw tap", "throw-tap", "throw tap sprinting"],
-  ["oob laser", "laser-oob", "laser oob"],
-  ["message not found zuggle", "mnf zuggle", "mnf-zuggle"],
-  ["recall clip", "recall-clip", "recallclip"],
-  ["storage ascend", "ascend-storage", "ascend storage"],
-  ["double tulin boost", "double-tulin-boost", "double tulin"],
-  ["equipment collision zuggle", "equipment-collision-zuggle", "equipment collision"],
-  ["longjump", "long-jump", "lj"],
-  ["midair duplication", "midair-duplication", "air dupe"],
-  ["misc glitch", "misc-glitch", "weird glitch"],
   ["duplication", "dupe", "dup"],
-  ["collision launch", "collision-launch", "collision launching"],
-  ["oob entry", "out-of-bounds entry", "oob entry"],
-  ["zuggle stacking", "zuggle-stack", "zuggle stack"],
-  ["equipment dupe", "equipment-duplication", "equipment dupe"],
+  ["misc glitch", "misc-glitch", "weird glitch"],
+  ["oob", "out-of-bounds", "out of bounds"],
   ["glitchcraft", "glitch-craft", "glitch craft"]
 ]

----

*** COMMIT: 9570e5a01f1566cb5e9afd416b4730bad2a52588
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 14:01:02 2026 +0100
Subject: Add new glitchcraft methods for item duplication and manipulation

commit 9570e5a01f1566cb5e9afd416b4730bad2a52588
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 14:01:02 2026 +0100

    Add new glitchcraft methods for item duplication and manipulation
    
    - Create documentation for Save Load Dupe (SLD) to duplicate weapons, bows, and shields.
    - Introduce Save Load Zuggling (SLZ) for zuggling anywhere without wall dependency.
    - Document Shock Effect Overload (SEO) for memory overload using Shock Emitters.
    - Add Smuggle Stacking Zuggle (SSZ) for zuggling bows and shields in version 1.1.2.
    - Implement Split Item Duplication (SID) for material duplication through stack splitting.
    - Document Stamina Depletion Freeze (SDF) for stamina glitching.
    - Introduce Stick Desync Clip (SDC) for clipping through floors using steering sticks.
    - Add Swap Resync Zuggle (SRZ) for zuggling using portacull equipment.
    - Document Throw Tap Sprinting (TTS) for infinite stamina sprinting.
    - Create Travel Medallion Storage (TMS) method for placing medallions at Link's feet.
    - Introduce Ultrabroken Smuggling (UBS) for making FE'd objects follow shields.
    - Document Weapon Sheath Offset (WSO) for offsetting weapon sheaths.
    - Add Weapon Stacking Duplication (WSD) for quick weapon duplication.
    - Implement Weapon State Transfer (WST) for transferring weapon properties.
    - Document Weather Amnesia (WA) for overwriting cave weather with overworld weather.
    - Introduce ZL Animation Reset (ZLAR) for resetting animations during specific glitches.
    - Add Zonai Inventory Shift Dupe (ZISD) for duplicating Zonai devices.
    - Document Zonai Sort Duplication (ZSD) for duplicating Zonai parts back into inventory.
    - Create Zuggle Load Object Transfering (ZLOT) for transferring objects through loads.

diff --git a/docs/wiki/glitchcraft/arrow-prompt-storage-aps.md b/docs/wiki/glitchcraft/arrow-prompt-storage.md
similarity index 100%
rename from docs/wiki/glitchcraft/arrow-prompt-storage-aps.md
rename to docs/wiki/glitchcraft/arrow-prompt-storage.md
diff --git a/docs/wiki/glitchcraft/attached-rangeless-active-zonai-araz.md b/docs/wiki/glitchcraft/attached-rangeless-active-zonai.md
similarity index 100%
rename from docs/wiki/glitchcraft/attached-rangeless-active-zonai-araz.md
rename to docs/wiki/glitchcraft/attached-rangeless-active-zonai.md
diff --git a/docs/wiki/glitchcraft/autobuild-cancel-slide-abcs.md b/docs/wiki/glitchcraft/autobuild-cancel-slide.md
similarity index 100%
rename from docs/wiki/glitchcraft/autobuild-cancel-slide-abcs.md
rename to docs/wiki/glitchcraft/autobuild-cancel-slide.md
diff --git a/docs/wiki/glitchcraft/autobuild-duplication-abd.md b/docs/wiki/glitchcraft/autobuild-duplication.md
similarity index 100%
rename from docs/wiki/glitchcraft/autobuild-duplication-abd.md
rename to docs/wiki/glitchcraft/autobuild-duplication.md
diff --git a/docs/wiki/glitchcraft/awakened-master-sword-ams.md b/docs/wiki/glitchcraft/awakened-master-sword.md
similarity index 100%
rename from docs/wiki/glitchcraft/awakened-master-sword-ams.md
rename to docs/wiki/glitchcraft/awakened-master-sword.md
diff --git a/docs/wiki/glitchcraft/bundled-item-duplication-bid.md b/docs/wiki/glitchcraft/bundled-item-duplication.md
similarity index 100%
rename from docs/wiki/glitchcraft/bundled-item-duplication-bid.md
rename to docs/wiki/glitchcraft/bundled-item-duplication.md
diff --git a/docs/wiki/glitchcraft/chasm-delay-zuggle-cdz.md b/docs/wiki/glitchcraft/chasm-delay-zuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/chasm-delay-zuggle-cdz.md
rename to docs/wiki/glitchcraft/chasm-delay-zuggle.md
diff --git a/docs/wiki/glitchcraft/crouch-throw-tap-sprinting-ctts.md b/docs/wiki/glitchcraft/crouch-throw-tap-sprinting.md
similarity index 100%
rename from docs/wiki/glitchcraft/crouch-throw-tap-sprinting-ctts.md
rename to docs/wiki/glitchcraft/crouch-throw-tap-sprinting.md
diff --git a/docs/wiki/glitchcraft/cull-storage-zuggle-csz.md b/docs/wiki/glitchcraft/cull-storage-zuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/cull-storage-zuggle-csz.md
rename to docs/wiki/glitchcraft/cull-storage-zuggle.md
diff --git a/docs/wiki/glitchcraft/detached-rangeless-active-zonai-draz.md b/docs/wiki/glitchcraft/detached-rangeless-active-zonai.md
similarity index 100%
rename from docs/wiki/glitchcraft/detached-rangeless-active-zonai-draz.md
rename to docs/wiki/glitchcraft/detached-rangeless-active-zonai.md
diff --git a/docs/wiki/glitchcraft/double-bypass-zuggle-dbz.md b/docs/wiki/glitchcraft/double-bypass-zuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/double-bypass-zuggle-dbz.md
rename to docs/wiki/glitchcraft/double-bypass-zuggle.md
diff --git a/docs/wiki/glitchcraft/double-unfuse-duplicashen-dud.md b/docs/wiki/glitchcraft/double-unfuse-duplicashen.md
similarity index 100%
rename from docs/wiki/glitchcraft/double-unfuse-duplicashen-dud.md
rename to docs/wiki/glitchcraft/double-unfuse-duplicashen.md
diff --git a/docs/wiki/glitchcraft/drop-delay-zuggle-ddz.md b/docs/wiki/glitchcraft/drop-delay-zuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/drop-delay-zuggle-ddz.md
rename to docs/wiki/glitchcraft/drop-delay-zuggle.md
diff --git a/docs/wiki/glitchcraft/extended-throw-sprinting-ets.md b/docs/wiki/glitchcraft/extended-throw-sprinting.md
similarity index 100%
rename from docs/wiki/glitchcraft/extended-throw-sprinting-ets.md
rename to docs/wiki/glitchcraft/extended-throw-sprinting.md
diff --git a/docs/wiki/glitchcraft/fall-damage-cancel-fdc.md b/docs/wiki/glitchcraft/fall-damage-cancel.md
similarity index 100%
rename from docs/wiki/glitchcraft/fall-damage-cancel-fdc.md
rename to docs/wiki/glitchcraft/fall-damage-cancel.md
diff --git a/docs/wiki/glitchcraft/food-ability-buff-swap-fabs.md b/docs/wiki/glitchcraft/food-ability-buff-swap.md
similarity index 100%
rename from docs/wiki/glitchcraft/food-ability-buff-swap-fabs.md
rename to docs/wiki/glitchcraft/food-ability-buff-swap.md
diff --git a/docs/wiki/glitchcraft/force-equip-zuggling-fez.md b/docs/wiki/glitchcraft/force-equip-zuggling.md
similarity index 100%
rename from docs/wiki/glitchcraft/force-equip-zuggling-fez.md
rename to docs/wiki/glitchcraft/force-equip-zuggling.md
diff --git a/docs/wiki/glitchcraft/fuse-entangle-drop-zuggle-fedz.md b/docs/wiki/glitchcraft/fuse-entangle-drop-zuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/fuse-entangle-drop-zuggle-fedz.md
rename to docs/wiki/glitchcraft/fuse-entangle-drop-zuggle.md
diff --git a/docs/wiki/glitchcraft/fuse-entangle-weapon-zuggle-fewz.md b/docs/wiki/glitchcraft/fuse-entangle-weapon-zuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/fuse-entangle-weapon-zuggle-fewz.md
rename to docs/wiki/glitchcraft/fuse-entangle-weapon-zuggle.md
diff --git a/docs/wiki/glitchcraft/fuse-entanglement-clipping-fec.md b/docs/wiki/glitchcraft/fuse-entanglement-clipping.md
similarity index 100%
rename from docs/wiki/glitchcraft/fuse-entanglement-clipping-fec.md
rename to docs/wiki/glitchcraft/fuse-entanglement-clipping.md
diff --git a/docs/wiki/glitchcraft/fuse-entanglement-desync-fed.md b/docs/wiki/glitchcraft/fuse-entanglement-desync.md
similarity index 100%
rename from docs/wiki/glitchcraft/fuse-entanglement-desync-fed.md
rename to docs/wiki/glitchcraft/fuse-entanglement-desync.md
diff --git a/docs/wiki/glitchcraft/fuse-overload-fuse-entanglement-fofe.md b/docs/wiki/glitchcraft/fuse-overload-fuse-entanglement.md
similarity index 100%
rename from docs/wiki/glitchcraft/fuse-overload-fuse-entanglement-fofe.md
rename to docs/wiki/glitchcraft/fuse-overload-fuse-entanglement.md
diff --git a/docs/wiki/glitchcraft/fuse-overload-fo.md b/docs/wiki/glitchcraft/fuse-overload.md
similarity index 100%
rename from docs/wiki/glitchcraft/fuse-overload-fo.md
rename to docs/wiki/glitchcraft/fuse-overload.md
diff --git a/docs/wiki/glitchcraft/fuse-storage-fuse-entanglement-fsfe.md b/docs/wiki/glitchcraft/fuse-storage-fuse-entanglement.md
similarity index 100%
rename from docs/wiki/glitchcraft/fuse-storage-fuse-entanglement-fsfe.md
rename to docs/wiki/glitchcraft/fuse-storage-fuse-entanglement.md
diff --git a/docs/wiki/glitchcraft/fuse-storage-fs.md b/docs/wiki/glitchcraft/fuse-storage.md
similarity index 100%
rename from docs/wiki/glitchcraft/fuse-storage-fs.md
rename to docs/wiki/glitchcraft/fuse-storage.md
diff --git a/docs/wiki/glitchcraft/guard-less-active-shield-gas.md b/docs/wiki/glitchcraft/guard-less-active-shield.md
similarity index 100%
rename from docs/wiki/glitchcraft/guard-less-active-shield-gas.md
rename to docs/wiki/glitchcraft/guard-less-active-shield.md
diff --git a/docs/wiki/glitchcraft/hand-locked-equipment-smuggling-hles.md b/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
similarity index 100%
rename from docs/wiki/glitchcraft/hand-locked-equipment-smuggling-hles.md
rename to docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
diff --git a/docs/wiki/glitchcraft/hero-path-link-storage-hpls.md b/docs/wiki/glitchcraft/hero-path-link-storage.md
similarity index 100%
rename from docs/wiki/glitchcraft/hero-path-link-storage-hpls.md
rename to docs/wiki/glitchcraft/hero-path-link-storage.md
diff --git a/docs/wiki/glitchcraft/inventory-shift-duplication-isd.md b/docs/wiki/glitchcraft/inventory-shift-duplication.md
similarity index 100%
rename from docs/wiki/glitchcraft/inventory-shift-duplication-isd.md
rename to docs/wiki/glitchcraft/inventory-shift-duplication.md
diff --git a/docs/wiki/glitchcraft/item-save-load-transfer-islt.md b/docs/wiki/glitchcraft/item-save-load-transfer.md
similarity index 100%
rename from docs/wiki/glitchcraft/item-save-load-transfer-islt.md
rename to docs/wiki/glitchcraft/item-save-load-transfer.md
diff --git a/docs/wiki/glitchcraft/jumpslash-cancel-clipping-jcc.md b/docs/wiki/glitchcraft/jumpslash-cancel-clipping.md
similarity index 100%
rename from docs/wiki/glitchcraft/jumpslash-cancel-clipping-jcc.md
rename to docs/wiki/glitchcraft/jumpslash-cancel-clipping.md
diff --git a/docs/wiki/glitchcraft/lift-storage-warping-lsw.md b/docs/wiki/glitchcraft/lift-storage-warping.md
similarity index 100%
rename from docs/wiki/glitchcraft/lift-storage-warping-lsw.md
rename to docs/wiki/glitchcraft/lift-storage-warping.md
diff --git a/docs/wiki/glitchcraft/map-zuggling-mz.md b/docs/wiki/glitchcraft/map-zuggling.md
similarity index 100%
rename from docs/wiki/glitchcraft/map-zuggling-mz.md
rename to docs/wiki/glitchcraft/map-zuggling.md
diff --git a/docs/wiki/glitchcraft/message-not-found-mnf.md b/docs/wiki/glitchcraft/message-not-found.md
similarity index 100%
rename from docs/wiki/glitchcraft/message-not-found-mnf.md
rename to docs/wiki/glitchcraft/message-not-found.md
diff --git a/docs/wiki/glitchcraft/midair-item-transmutation-mit.md b/docs/wiki/glitchcraft/midair-item-transmutation.md
similarity index 100%
rename from docs/wiki/glitchcraft/midair-item-transmutation-mit.md
rename to docs/wiki/glitchcraft/midair-item-transmutation.md
diff --git a/docs/wiki/glitchcraft/midair-sort-duplication-msd.md b/docs/wiki/glitchcraft/midair-sort-duplication.md
similarity index 100%
rename from docs/wiki/glitchcraft/midair-sort-duplication-msd.md
rename to docs/wiki/glitchcraft/midair-sort-duplication.md
diff --git a/docs/wiki/glitchcraft/midair-throw-duplication-mtd.md b/docs/wiki/glitchcraft/midair-throw-duplication.md
similarity index 100%
rename from docs/wiki/glitchcraft/midair-throw-duplication-mtd.md
rename to docs/wiki/glitchcraft/midair-throw-duplication.md
diff --git a/docs/wiki/glitchcraft/minecart-rail-collision-launching-mrcl.md b/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
similarity index 100%
rename from docs/wiki/glitchcraft/minecart-rail-collision-launching-mrcl.md
rename to docs/wiki/glitchcraft/minecart-rail-collision-launching.md
diff --git a/docs/wiki/glitchcraft/mineru-hold-smuggle-mhs.md b/docs/wiki/glitchcraft/mineru-hold-smuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/mineru-hold-smuggle-mhs.md
rename to docs/wiki/glitchcraft/mineru-hold-smuggle.md
diff --git a/docs/wiki/glitchcraft/mulberry-s-out-of-body-experience-moobe.md b/docs/wiki/glitchcraft/mulberry-s-out-of-body-experience.md
similarity index 100%
rename from docs/wiki/glitchcraft/mulberry-s-out-of-body-experience-moobe.md
rename to docs/wiki/glitchcraft/mulberry-s-out-of-body-experience.md
diff --git a/docs/wiki/glitchcraft/no-bow-sprinting-nbs.md b/docs/wiki/glitchcraft/no-bow-sprinting.md
similarity index 100%
rename from docs/wiki/glitchcraft/no-bow-sprinting-nbs.md
rename to docs/wiki/glitchcraft/no-bow-sprinting.md
diff --git a/docs/wiki/glitchcraft/persistent-save-load-object-transfer-pslot.md b/docs/wiki/glitchcraft/persistent-save-load-object-transfer.md
similarity index 100%
rename from docs/wiki/glitchcraft/persistent-save-load-object-transfer-pslot.md
rename to docs/wiki/glitchcraft/persistent-save-load-object-transfer.md
diff --git a/docs/wiki/glitchcraft/quantum-linking-ql.md b/docs/wiki/glitchcraft/quantum-linking.md
similarity index 100%
rename from docs/wiki/glitchcraft/quantum-linking-ql.md
rename to docs/wiki/glitchcraft/quantum-linking.md
diff --git a/docs/wiki/glitchcraft/quick-drop-smuggle-qds.md b/docs/wiki/glitchcraft/quick-drop-smuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/quick-drop-smuggle-qds.md
rename to docs/wiki/glitchcraft/quick-drop-smuggle.md
diff --git a/docs/wiki/glitchcraft/save-load-dupe-sld.md b/docs/wiki/glitchcraft/save-load-dupe.md
similarity index 100%
rename from docs/wiki/glitchcraft/save-load-dupe-sld.md
rename to docs/wiki/glitchcraft/save-load-dupe.md
diff --git a/docs/wiki/glitchcraft/save-load-zuggling-slz.md b/docs/wiki/glitchcraft/save-load-zuggling.md
similarity index 100%
rename from docs/wiki/glitchcraft/save-load-zuggling-slz.md
rename to docs/wiki/glitchcraft/save-load-zuggling.md
diff --git a/docs/wiki/glitchcraft/shock-effect-overload-seo.md b/docs/wiki/glitchcraft/shock-effect-overload.md
similarity index 100%
rename from docs/wiki/glitchcraft/shock-effect-overload-seo.md
rename to docs/wiki/glitchcraft/shock-effect-overload.md
diff --git a/docs/wiki/glitchcraft/smuggle-stacking-zuggle-ssz.md b/docs/wiki/glitchcraft/smuggle-stacking-zuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/smuggle-stacking-zuggle-ssz.md
rename to docs/wiki/glitchcraft/smuggle-stacking-zuggle.md
diff --git a/docs/wiki/glitchcraft/split-item-duplication-sid.md b/docs/wiki/glitchcraft/split-item-duplication.md
similarity index 100%
rename from docs/wiki/glitchcraft/split-item-duplication-sid.md
rename to docs/wiki/glitchcraft/split-item-duplication.md
diff --git a/docs/wiki/glitchcraft/stamina-depletion-freeze-sdf.md b/docs/wiki/glitchcraft/stamina-depletion-freeze.md
similarity index 100%
rename from docs/wiki/glitchcraft/stamina-depletion-freeze-sdf.md
rename to docs/wiki/glitchcraft/stamina-depletion-freeze.md
diff --git a/docs/wiki/glitchcraft/stick-desync-clip-sdc.md b/docs/wiki/glitchcraft/stick-desync-clip.md
similarity index 100%
rename from docs/wiki/glitchcraft/stick-desync-clip-sdc.md
rename to docs/wiki/glitchcraft/stick-desync-clip.md
diff --git a/docs/wiki/glitchcraft/swap-resync-zuggle-srz.md b/docs/wiki/glitchcraft/swap-resync-zuggle.md
similarity index 100%
rename from docs/wiki/glitchcraft/swap-resync-zuggle-srz.md
rename to docs/wiki/glitchcraft/swap-resync-zuggle.md
diff --git a/docs/wiki/glitchcraft/throw-tap-sprinting-tts.md b/docs/wiki/glitchcraft/throw-tap-sprinting.md
similarity index 100%
rename from docs/wiki/glitchcraft/throw-tap-sprinting-tts.md
rename to docs/wiki/glitchcraft/throw-tap-sprinting.md
diff --git a/docs/wiki/glitchcraft/travel-medallion-storage-tms.md b/docs/wiki/glitchcraft/travel-medallion-storage.md
similarity index 100%
rename from docs/wiki/glitchcraft/travel-medallion-storage-tms.md
rename to docs/wiki/glitchcraft/travel-medallion-storage.md
diff --git a/docs/wiki/glitchcraft/ultrabroken-smuggling-ubs.md b/docs/wiki/glitchcraft/ultrabroken-smuggling.md
similarity index 100%
rename from docs/wiki/glitchcraft/ultrabroken-smuggling-ubs.md
rename to docs/wiki/glitchcraft/ultrabroken-smuggling.md
diff --git a/docs/wiki/glitchcraft/weapon-sheath-offset-wso.md b/docs/wiki/glitchcraft/weapon-sheath-offset.md
similarity index 100%
rename from docs/wiki/glitchcraft/weapon-sheath-offset-wso.md
rename to docs/wiki/glitchcraft/weapon-sheath-offset.md
diff --git a/docs/wiki/glitchcraft/weapon-stacking-duplication-wsd.md b/docs/wiki/glitchcraft/weapon-stacking-duplication.md
similarity index 100%
rename from docs/wiki/glitchcraft/weapon-stacking-duplication-wsd.md
rename to docs/wiki/glitchcraft/weapon-stacking-duplication.md
diff --git a/docs/wiki/glitchcraft/weapon-state-transfer-wst.md b/docs/wiki/glitchcraft/weapon-state-transfer.md
similarity index 100%
rename from docs/wiki/glitchcraft/weapon-state-transfer-wst.md
rename to docs/wiki/glitchcraft/weapon-state-transfer.md
diff --git a/docs/wiki/glitchcraft/weather-amnesia-wa.md b/docs/wiki/glitchcraft/weather-amnesia.md
similarity index 100%
rename from docs/wiki/glitchcraft/weather-amnesia-wa.md
rename to docs/wiki/glitchcraft/weather-amnesia.md
diff --git a/docs/wiki/glitchcraft/zl-animation-reset-zlar.md b/docs/wiki/glitchcraft/zl-animation-reset.md
similarity index 100%
rename from docs/wiki/glitchcraft/zl-animation-reset-zlar.md
rename to docs/wiki/glitchcraft/zl-animation-reset.md
diff --git a/docs/wiki/glitchcraft/zonai-inventory-shift-dupe-zisd.md b/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
similarity index 100%
rename from docs/wiki/glitchcraft/zonai-inventory-shift-dupe-zisd.md
rename to docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
diff --git a/docs/wiki/glitchcraft/zonai-sort-duplication-zsd.md b/docs/wiki/glitchcraft/zonai-sort-duplication.md
similarity index 100%
rename from docs/wiki/glitchcraft/zonai-sort-duplication-zsd.md
rename to docs/wiki/glitchcraft/zonai-sort-duplication.md
diff --git a/docs/wiki/glitchcraft/zuggle-load-object-transfering-zlot.md b/docs/wiki/glitchcraft/zuggle-load-object-transfering.md
similarity index 100%
rename from docs/wiki/glitchcraft/zuggle-load-object-transfering-zlot.md
rename to docs/wiki/glitchcraft/zuggle-load-object-transfering.md

----

*** COMMIT: 286f33045b6659e5ce9a58045b5204391513f775
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 14:03:05 2026 +0100
Subject: Fix links and update documentation for entanglement and zuggling glitches

commit 286f33045b6659e5ce9a58045b5204391513f775
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 14:03:05 2026 +0100

    Fix links and update documentation for entanglement and zuggling glitches
    
    - Updated links in entanglement-library.md to correct file names.
    - Added new weapon fuse entanglement documentation in weapon-fuse-entanglement.md.
    - Corrected links in zuggle-library.md to match updated file names.
    - Adjusted mkdocs.yml to reflect changes in file names and ensure proper navigation.

diff --git a/docs/assets/data/grimoire-data.json b/docs/assets/data/grimoire-data.json
index 76f3cb007..66ef83a26 100644
--- a/docs/assets/data/grimoire-data.json
+++ b/docs/assets/data/grimoire-data.json
@@ -1 +1 @@
-[{"name": "Grimoire of Glitchcraft", "abbr": "", "date": "", "tags": [], "versions": [], "credits": [], "href": "./_glitchcraft-grimoire.md"}, {"name": "Ability Wheel Loop", "abbr": "AWL", "date": "2024-03-11", "tags": ["menu", "ultrahand", "zonai"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./ability-wheel-loop.md"}, {"name": "Aeroculling", "abbr": "AC", "date": "2024-08-11", "tags": ["equipment", "culling", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./aeroculling.md"}, {"name": "Animation Swap", "abbr": "ASWP", "date": "2023-05-17", "tags": ["zuggling", "animation", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Swinginman"], "href": "./animation-swap.md"}, {"name": "Anti-gravity GAS", "abbr": "AGAS", "date": "2025-01-22", "tags": ["gas"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./anti-gravity-gas.md"}, {"name": "Anti-Gravity Glitch", "abbr": "AGG", "date": "2023-05-13", "tags": ["paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Kaldemar"], "href": "./anti-gravity-glitch.md"}, {"name": "Anti-Gravity Objects", "abbr": "AGO", "date": "Unknown", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./anti-gravity-objects.md"}, {"name": "AntiGrav Weapons", "abbr": "AGW", "date": "2023-05-28", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Blize"], "href": "./antigrav-weapons.md"}, {"name": "Arrow Prompt Storage", "abbr": "APS", "date": "2023-10-04", "tags": ["storage", "culling", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NghtmaR3"], "href": "./arrow-prompt-storage-aps.md"}, {"name": "Arrow Smuggling", "abbr": "ASMU", "date": "2023-06-04", "tags": ["zuggling", "equipment", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./arrow-smuggling.md"}, {"name": "Arrow Unlink", "abbr": "AUL", "date": "2023-10-26", "tags": ["fuse", "arrow"], "versions": ["1.0.0"], "credits": ["R4000"], "href": "./arrow-unlink.md"}, {"name": "Arrow Unloading", "abbr": "AU", "date": "2023-06-18", "tags": ["culling", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk", "Zas"], "href": "./arrow-unloading.md"}, {"name": "Ascend Camera Glitch", "abbr": "ACG", "date": "Unknown", "tags": ["ascend", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./ascend-camera-glitch.md"}, {"name": "Ascend Rushing", "abbr": "AR", "date": "2023-06-15", "tags": ["ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./ascend-rushing.md"}, {"name": "Ascend Storage", "abbr": "ASTR", "date": "2023-05-19", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Saria"], "href": "./ascend-storage.md"}, {"name": "Attached Rangeless Active Zonai", "abbr": "ARAZ", "date": "2023-06-16", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?", "NX721"], "href": "./attached-rangeless-active-zonai-araz.md"}, {"name": "Autobuild Cancel Slide", "abbr": "ABCS", "date": "2023-05-18", "tags": ["animation", "movement", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Takosensai1"], "href": "./autobuild-cancel-slide-abcs.md"}, {"name": "Autobuild Duplication", "abbr": "ABD", "date": "2023-06-11", "tags": ["duplication", "item", "ultrahand", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./autobuild-duplication-abd.md"}, {"name": "Autobuild Storage", "abbr": "ABST", "date": "2023-08-28", "tags": ["storage", "item", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "R4000"], "href": "./autobuild-storage.md"}, {"name": "Awakened Master Sword", "abbr": "AMS", "date": "2023-09-04", "tags": ["weapon", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tahata"], "href": "./awakened-master-sword-ams.md"}, {"name": "Back-in-Time Art", "abbr": "BIT", "date": "2023-06-18", "tags": ["save-load"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Zas"], "href": "./back-in-time-art.md"}, {"name": "Back to Back Bloodmoon", "abbr": "BTBB", "date": "2023-05-17", "tags": ["bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lopitty"], "href": "./back-to-back-bloodmoon.md"}, {"name": "Balloon Overload", "abbr": "BO", "date": "2025-03-08", "tags": ["menu", "equipment", "overload", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Jordan", "mulberry", "ofstrings2"], "href": "./balloon-overload.md"}, {"name": "Banc Storage", "abbr": "BANC", "date": "2024-10-01", "tags": ["storage", "warping", "save-load", "bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos", "mulberry", "Aergyl", "EOH_NS_SS"], "href": "./banc-storage.md"}, {"name": "Bomb Skew", "abbr": "BSK", "date": "2023-09-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl", "FerrusCube", "Mozz"], "href": "./bomb-skew.md"}, {"name": "Bow Attachment Desync", "abbr": "BAD", "date": "2023-07-11", "tags": ["desync", "item", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Aeolian"], "href": "./bow-attachment-desync-bad-arrows.md"}, {"name": "Bow Attachment Storage", "abbr": "BAS", "date": "2023-12-03", "tags": ["storage", "item", "fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./bow-attachment-storage.md"}, {"name": "Bow Sprinting", "abbr": "BS", "date": "2023-05-14", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./bow-sprinting.md"}, {"name": "Breaking Awakened Master Sword", "abbr": "BAMS", "date": "2023-11-26", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Infrasolid"], "href": "./breaking-awakened-master-sword.md"}, {"name": "BThrow Sprinting", "abbr": "BTS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./bthrow-sprinting.md"}, {"name": "Bundled Item Duplication", "abbr": "BID", "date": "2023-12-12", "tags": ["duplication", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./bundled-item-duplication-bid.md"}, {"name": "Buoy Bouncing", "abbr": "BB", "date": "2023-05-25", "tags": ["equipment", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup"], "href": "./buoy-bouncing.md"}, {"name": "Camera CFW", "abbr": "CFW", "date": "2023-07-11", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh"], "href": "./camera-cfw.md"}, {"name": "Camera Pose Glitch", "abbr": "CPG", "date": "Unknown", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./camera-pose-glitch.md"}, {"name": "Capsule Cel Shader Removal", "abbr": "CCSR", "date": "2023-12-04", "tags": ["duplication", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./capsule-cel-shader-removal.md"}, {"name": "Cave Flag Culling", "abbr": "CFC", "date": "2023-11-24", "tags": ["duplication", "culling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Aergyl"], "href": "./cave-flag-culling.md"}, {"name": "Chasm Delay Zuggle", "abbr": "CDZ", "date": "2024-05-31", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock", "mulberry", "WinnerBoi77"], "href": "./chasm-delay-zuggle-cdz.md"}, {"name": "Chasm Device Dupe", "abbr": "CDD", "date": "2025-10-12", "tags": ["duplication", "item", "culling", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic", "mulberry"], "href": "./chasm-device-dupe.md"}, {"name": "Clear Camera/Scope", "abbr": "CCS", "date": "2023-07-03", "tags": ["bow", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./clear-camera-scope.md"}, {"name": "Cold Fuse Stick Desync Clip", "abbr": "CSSDC", "date": "2024-06-04", "tags": ["clipping", "desync", "weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "KiloVictor"], "href": "./cold-fuse-stick-desync-clip-cold-fuse-sdc.md"}, {"name": "Cold Fuse", "abbr": "CF", "date": "2023-07-23", "tags": ["weapon", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk", "Ryan?", "Zas"], "href": "./cold-fuse.md"}, {"name": "Construct Fuse Entanglement", "abbr": "CNFE", "date": "2024-06-30", "tags": ["equipment", "entanglement", "fuse", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./construct-fuse-entanglement.md"}, {"name": "Corrupt Meal", "abbr": "CM", "date": "2025-02-07", "tags": ["cooking"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Telkic"], "href": "./corrupt-meal.md"}, {"name": "Crouch Sprinting", "abbr": "CS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./crouch-sprinting.md"}, {"name": "Crouch Throw Tap Sprinting", "abbr": "CTTS", "date": "2023-05-15", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer"], "href": "./crouch-throw-tap-sprinting-ctts.md"}, {"name": "Cucco Warping", "abbr": "CW", "date": "2023-07-23", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi"], "href": "./cucco-warping.md"}, {"name": "Cull Cold Fuse", "abbr": "CCF", "date": "2024-02-01", "tags": ["weapon", "culling", "ultrahand", "fuse"], "versions": ["Unknown"], "credits": ["mulberry"], "href": "./cull-cold-fuse.md"}, {"name": "Cull Equipment Desync", "abbr": "CED", "date": "2023-10-10", "tags": ["desync", "menu", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blize", "Ock"], "href": "./cull-equipment-desync.md"}, {"name": "Cull Fuse Entanglement", "abbr": "CFE", "date": "2023-09-21", "tags": ["entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "suusi", "Ock", "SteFen45"], "href": "./cull-fuse-entanglement-cull-fe.md"}, {"name": "Cull Launching", "abbr": "CL", "date": "2023-07-01", "tags": ["launching", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Asgorne"], "href": "./cull-launching.md"}, {"name": "Cull Pickup Dynamic Zuggle", "abbr": "CPDZ", "date": "2025-05-18", "tags": ["zuggling", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./cull-pickup-dynamic-zuggle.md"}, {"name": "Cull Smuggle", "abbr": "CSMU", "date": "2023-06-27", "tags": ["zuggling", "equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "ROBUXY2ND", "Ock"], "href": "./cull-smuggle.md"}, {"name": "Cull Storage Zuggle", "abbr": "CSZ", "date": "2024-07-18", "tags": ["zuggling", "storage", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars"], "href": "./cull-storage-zuggle-csz.md"}, {"name": "Cull Storage", "abbr": "CSTR", "date": "2024-01-20", "tags": ["storage", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./cull-storage.md"}, {"name": "Cull Zone Culling", "abbr": "CZC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./cull-zone-culling.md"}, {"name": "Culling Area Fuse Storage Fuse Entanglement", "abbr": "CFSFE", "date": "2024-02-25", "tags": ["storage", "entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee", "Zas"], "href": "./culling-area-fuse-storage-fuse-entanglement.md"}, {"name": "Culling Area Fuse Storage", "abbr": "CAFS", "date": "2023-06-30", "tags": ["storage", "culling", "fuse"], "versions": ["Unknown"], "credits": ["Mozz", "pyuk"], "href": "./culling-area-fuse-storage.md"}, {"name": "Cutscene Combo Amplifier", "abbr": "CCA", "date": "2023-12-22", "tags": ["item", "buff", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos"], "href": "./cutscene-combo-amplifier.md"}, {"name": "Damage Amnesia", "abbr": "DA", "date": "2023-05-27", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./damage-amnesia.md"}, {"name": "Death Persistent Save Load Object Transfer", "abbr": "DPSLOT", "date": "2025-06-26", "tags": ["item", "save-load", "zuggling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./death-persistent-save-load-object-transfer.md"}, {"name": "Detached Rangeless Active Zonai", "abbr": "DRAZ", "date": "2023-06-15", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Venaticus"], "href": "./detached-rangeless-active-zonai-draz.md"}, {"name": "Detanglement", "abbr": "DTG", "date": "2023-09-09", "tags": ["launching", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./detanglement.md"}, {"name": "Dialog Permacull", "abbr": "DPC", "date": "2025-11-28", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./dialog-permacull.md"}, {"name": "Disabled Enemy", "abbr": "DE", "date": "2023-06-27", "tags": ["enemy"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["shio_0725", "ralseidewitt"], "href": "./disabled-enemy.md"}, {"name": "Dispenser Storage", "abbr": "DISP", "date": "2023-07-02", "tags": ["storage", "item", "ultrahand", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./dispenser-storage.md"}, {"name": "Display Duping", "abbr": "DD", "date": "2023-05-27", "tags": ["duplication", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Pistonight"], "href": "./display-duping.md"}, {"name": "Display Master Sword", "abbr": "DMS", "date": "2023-06-08", "tags": ["weapon", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Zas"], "href": "./display-master-sword.md"}, {"name": "Dive Cancel Glide Boost", "abbr": "DCGB", "date": "2023-05-14", "tags": ["animation", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "Mety333"], "href": "./dive-cancel-glide-boost.md"}, {"name": "Double Bypass Zuggle", "abbr": "DBZ", "date": "2025-06-16", "tags": ["zuggling", "item", "culling", "ultrahand"], "versions": ["1.2.0"], "credits": ["mulberry", "dt13269"], "href": "./double-bypass-zuggle-dbz.md"}, {"name": "Double Shield Desync Clip Fuse Entanglement", "abbr": "DSDCFE", "date": "2024-06-06", "tags": ["duplication", "clipping", "desync", "equipment", "entanglement", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee"], "href": "./double-shield-desync-clip-fuse-entanglement-double-sdc-fe.md"}, {"name": "Double Tulin Boost", "abbr": "DTB", "date": "2023-05-17", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./double-tulin-boost.md"}, {"name": "Double Unfuse Duplicashen", "abbr": "DUD", "date": "2023-05-15", "tags": ["duplication", "item", "weapon", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Li Shen (Ú»ëþÑ×)"], "href": "./double-unfuse-duplicashen-dud.md"}, {"name": "Dpadlock-less Invizuggle", "abbr": "DLI", "date": "2024-07-17", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars", "NghtmaR3"], "href": "./dpadlock-less-invizuggle.md"}, {"name": "Drop Delay Zuggle", "abbr": "DDZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-delay-zuggle-ddz.md"}, {"name": "Drop Restriction", "abbr": "DR", "date": "2023-06-19", "tags": ["menu", "item", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["SCFD-GK2", "NicNac"], "href": "./drop-restriction.md"}, {"name": "Drop Smuggling", "abbr": "DSMU", "date": "2023-05-31", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-smuggling.md"}, {"name": "Drop Zuggle", "abbr": "DZ", "date": "2023-06-15", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO"], "href": "./drop-zuggle.md"}, {"name": "Durability-", "abbr": "DUR", "date": "2023-09-11", "tags": ["item", "weapon", "bow"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./durability.md"}, {"name": "Dynamic Purgatory Zuggle", "abbr": "DPZ", "date": "2025-02-14", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./dynamic-purgatory-zuggle.md"}, {"name": "Dynamic Zuggle", "abbr": "DZG", "date": "2023-09-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "Zas", "mulberry", "WinnerBoi77", "Ryan?", "CS16"], "href": "./dynamic-zuggle.md"}, {"name": "Eaten Despawn Interrupt", "abbr": "EDI", "date": "2026-01-16", "tags": ["item", "zuggling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Squidwest"], "href": "./eaten-despawn-interrupt.md"}, {"name": "Enemy Pickpocketing", "abbr": "EP", "date": "2023-09-16", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KAIDUDE64"], "href": "./enemy-pickpocketing.md"}, {"name": "Entanglement Height Glitch", "abbr": "EHG", "date": "2023-05-24", "tags": ["equipment", "entanglement", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./entanglement-height-glitch.md"}, {"name": "Equipment Collision Zuggle", "abbr": "ECZ", "date": "2023-05-16", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zvleon"], "href": "./equipment-collision-zuggle.md"}, {"name": "Equipment Mitosis", "abbr": "EM", "date": "2023-09-05", "tags": ["duplication", "zuggling", "equipment", "overload"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./equipment-mitosis.md"}, {"name": "Equipment Shock Duping", "abbr": "ESD", "date": "2023-12-12", "tags": ["duplication", "item", "equipment"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./equipment-shock-duping.md"}, {"name": "Equipment Smuggle", "abbr": "ESMU", "date": "2023-06-01", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["sleepyppls", "Mozz", "mulberry", "NaN Gogh"], "href": "./equipment-smuggle.md"}, {"name": "Equipped Throken", "abbr": "ETHK", "date": "2025-05-20", "tags": ["weapon", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./equipped-throken.md"}, {"name": "Extended Throw Sprinting", "abbr": "ETS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["briochoc"], "href": "./extended-throw-sprinting-ets.md"}, {"name": "Fall Damage Cancel", "abbr": "FDC", "date": "2023-05-23", "tags": ["animation", "damage", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter"], "href": "./fall-damage-cancel-fdc.md"}, {"name": "Floorping", "abbr": "FLP", "date": "2024-01-02", "tags": ["warping"], "versions": ["1.1.0", "1.1.1"], "credits": ["koreth"], "href": "./floorping.md"}, {"name": "Food Ability Buff Swap", "abbr": "FABS", "date": "2023-05-16", "tags": ["cooking", "item", "buff", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["fabs"], "href": "./food-ability-buff-swap-fabs.md"}, {"name": "Force Equip Zuggling", "abbr": "FEZ", "date": "2023-06-07", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "Mozz", "Rhkellz", "Syb", "NaN Gogh"], "href": "./force-equip-zuggling-fez.md"}, {"name": "Forced Blood Moon", "abbr": "FBM", "date": "2023-05-28", "tags": ["bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["1789(@W0ERYySQgZyGOY3)", "Simonfirefighter", "Maxmasher", "Flash", "acaepius"], "href": "./forced-blood-moon.md"}, {"name": "Freecall", "abbr": "FC", "date": "2023-09-09", "tags": ["ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["suusi", "ROBUXY2ND"], "href": "./freecall.md"}, {"name": "Fuse Entangle Drop Zuggle", "abbr": "FEDZ", "date": "2023-06-17", "tags": ["zuggling", "item", "weapon", "equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-drop-zuggle-fedz.md"}, {"name": "Fuse Entangle Weapon Zuggle", "abbr": "FEWZ", "date": "2023-06-10", "tags": ["zuggling", "item", "weapon", "damage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-weapon-zuggle-fewz.md"}, {"name": "Fuse Entanglement Clipping", "abbr": "FEC", "date": "2023-06-16", "tags": ["clipping", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["circyit"], "href": "./fuse-entanglement-clipping-fec.md"}, {"name": "Fuse Entanglement Desync", "abbr": "FED", "date": "2023-05-26", "tags": ["duplication", "desync", "item", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement-desync-fed.md"}, {"name": "Fuse Entanglement Drop Smuggling", "abbr": "FEDS", "date": "2023-08-15", "tags": ["zuggling", "item", "equipment", "entanglement", "fuse"], "versions": ["1.2.0"], "credits": ["Blize", "Blackmars"], "href": "./fuse-entanglement-drop-smuggling.md"}, {"name": "Fuse Entanglement", "abbr": "FE", "date": "2023-05-24", "tags": ["equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement.md"}, {"name": "Fuse Overload", "abbr": "FO", "date": "2023-11-03", "tags": ["weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "NghtmaR3"], "href": "./fuse-overload-fo.md"}, {"name": "Fuse Overload Fuse Entanglement", "abbr": "FOFE", "date": "2025-05-26", "tags": ["entanglement", "overload", "ultrahand", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry"], "href": "./fuse-overload-fuse-entanglement-fofe.md"}, {"name": "Fuse Storage", "abbr": "FS", "date": "2023-06-18", "tags": ["storage", "item", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./fuse-storage-fs.md"}, {"name": "Fuse Storage Fuse Entanglement", "abbr": "FSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./fuse-storage-fuse-entanglement-fsfe.md"}, {"name": "GAS Launching", "abbr": "GASL", "date": "2023-06-25", "tags": ["gas", "launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "pyuk", "Flash", "Mozz", "Blize"], "href": "./gas-launching-previously-known-as-ascend-launching.md"}, {"name": "GAS Warping", "abbr": "GASW", "date": "2023-06-26", "tags": ["gas", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Flash", "pyuk"], "href": "./gas-warping.md"}, {"name": "Ghost Save Load Object Transfer", "abbr": "GSLOT", "date": "2024-03-08", "tags": ["save-load", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./ghost-save-load-object-transfer.md"}, {"name": "Ghost Stick Clipping", "abbr": "GSC", "date": "2023-05-28", "tags": ["clipping"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["rocomox"], "href": "./ghost-stick-clipping.md"}, {"name": "Glue Removal", "abbr": "GR", "date": "2023-10-05", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./glue-removal.md"}, {"name": "Guard-less Active Shield", "abbr": "GAS", "date": "2023-06-12", "tags": ["equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Venaticus"], "href": "./guard-less-active-shield-gas.md"}, {"name": "Hand Locked Equipment Smuggling", "abbr": "HLES", "date": "2023-07-11", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0"], "credits": ["Aeolian"], "href": "./hand-locked-equipment-smuggling-hles.md"}, {"name": "Handy Job", "abbr": "HJ", "date": "2023-11-20", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./handy-job.md"}, {"name": "Hero Path Link Storage", "abbr": "HPLS", "date": "2023-06-20", "tags": ["storage"], "versions": ["1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./hero-path-link-storage-hpls.md"}, {"name": "Hestu Scamming", "abbr": "HSCA", "date": "2024-04-19", "tags": ["menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "Tahata", "EM"], "href": "./hestu-scamming.md"}, {"name": "Hold Smuggling", "abbr": "HSM", "date": "2023-07-04", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "NaN Gogh"], "href": "./hold-smuggling.md"}, {"name": "Hold Storage Duplication", "abbr": "HSD", "date": "2023-07-03", "tags": ["duplication", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Mozz"], "href": "./hold-storage-duplication-also-known-as-minus-dupe.md"}, {"name": "Hold Storage", "abbr": "HS", "date": "2023-07-02", "tags": ["storage", "desync", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NaN Gogh", "Mozz"], "href": "./hold-storage.md"}, {"name": "Horse Duping", "abbr": "HD", "date": "2024-03-22", "tags": ["duplication", "culling", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./horse-duping.md"}, {"name": "Hydro Clipping", "abbr": "HC", "date": "2023-06-15", "tags": ["clipping", "storage", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter", "Maxmasher", "KnightPohtaytoh", "pyuk"], "href": "./hydro-clipping.md"}, {"name": "Infinite Balloon", "abbr": "IBAL", "date": "2024-06-13", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurone_yuu"], "href": "./infinite-balloon.md"}, {"name": "Infinite Bubbul Frog Gems", "abbr": "IBFG", "date": "2023-05-21", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Unknown"], "href": "./infinite-bubbul-frog-gems.md"}, {"name": "Infinite Damage 2.0", "abbr": "ID2", "date": "2024-01-21", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./infinite-damage-2-0.md"}, {"name": "Infinite Damage", "abbr": "IDMG", "date": "2023-05-13", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["GamSla341"], "href": "./infinite-damage.md"}, {"name": "Infinite Height", "abbr": "IH", "date": "2023-05-22", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "Physioninja"], "href": "./infinite-height.md"}, {"name": "Inventory Shift Duplication", "abbr": "ISD", "date": "2023-06-25", "tags": ["duplication", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Blizzard Blanc", "BigDUCCO", "Maxmasher", "pyuk", "Zas"], "href": "./inventory-shift-duplication-isd.md"}, {"name": "Invizuggle", "abbr": "IVZ", "date": "2024-01-03", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Yee"], "href": "./invizuggle.md"}, {"name": "Item Save Load Transfer", "abbr": "ISLT", "date": "2023-12-22", "tags": ["item", "save-load", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Luckstyle"], "href": "./item-save-load-transfer-islt.md"}, {"name": "Item Throw Hitbox Disable", "abbr": "ITHD", "date": "2023-06-18", "tags": ["item", "recall", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Arfix", "Moonrise"], "href": "./item-throw-hitbox-disable.md"}, {"name": "Jumpslash Cancel Clipping", "abbr": "JCC", "date": "2023-06-16", "tags": ["clipping", "animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./jumpslash-cancel-clipping-jcc.md"}, {"name": "Jumpslash Canceling", "abbr": "JSC", "date": "2023-05-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Mozz"], "href": "./jumpslash-canceling.md"}, {"name": "Kilovictor's quicksmuggle", "abbr": "KQS", "date": "2024-02-23", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KiloVictor"], "href": "./kilovictor-s-quicksmuggle.md"}, {"name": "L Sprinting", "abbr": "LS", "date": "2023-05-12", "tags": ["sprinting", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tauktes"], "href": "./l-sprinting.md"}, {"name": "Lag Machines", "abbr": "LM", "date": "2023-10-05", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lag-machines.md"}, {"name": "Laser-OOB", "abbr": "LOOB", "date": "2023-05-13", "tags": ["duplication", "oob"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Xeryph"], "href": "./laser-oob.md"}, {"name": "Lift Fuse Interrupt", "abbr": "LFI", "date": "2025-04-22", "tags": ["weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee"], "href": "./lift-fuse-interrupt.md"}, {"name": "Lift Smuggle", "abbr": "LSMU", "date": "2024-02-03", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars"], "href": "./lift-smuggle.md"}, {"name": "Lift Storage Warping", "abbr": "LSW", "date": "2024-01-08", "tags": ["storage", "item", "culling", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./lift-storage-warping-lsw.md"}, {"name": "Lift Warping", "abbr": "LW", "date": "2023-06-15", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lift-warping.md"}, {"name": "Like-Like Culling", "abbr": "LLC", "date": "2023-06-13", "tags": ["culling", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-culling.md"}, {"name": "Like-Like Drop Smuggling", "abbr": "LLDS", "date": "2023-06-15", "tags": ["zuggling", "item", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-drop-smuggling.md"}, {"name": "Like-Like FSFE", "abbr": "LLFSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./like-like-fsfe.md"}, {"name": "Like-Like Fuse Storage", "abbr": "LLFS", "date": "2023-06-18", "tags": ["storage", "item", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Mozz"], "href": "./like-like-fuse-storage.md"}, {"name": "Like Like New Textbox Softlock", "abbr": "LLTS", "date": "2023-06-16", "tags": ["item", "like-like", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./like-like-new-textbox-softlock.md"}, {"name": "Like-Like Smuggle Desync", "abbr": "LLSD", "date": "2023-06-15", "tags": ["zuggling", "desync", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-smuggle-desync-lsd.md"}, {"name": "Like-Like Smuggling", "abbr": "LLS", "date": "2023-06-15", "tags": ["zuggling", "equipment", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-smuggling.md"}, {"name": "Like-Like Warping", "abbr": "LLW", "date": "2023-06-15", "tags": ["warping", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-warping.md"}, {"name": "Like-Like Zuggling", "abbr": "LLZ", "date": "2023-06-15", "tags": ["zuggling", "like-like", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Ryan?", "Blackmars"], "href": "./like-like-zuggling.md"}, {"name": "LikeLike Stick Smuggling", "abbr": "LLSS", "date": "Unknown", "tags": ["zuggling", "item", "equipment", "culling", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./likelike-stick-smuggling.md"}, {"name": "Long Jump", "abbr": "LJ", "date": "2023-05-18", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./long-jump.md"}, {"name": "Map Flickering", "abbr": "MF", "date": "Unknown", "tags": ["map"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Unknown"], "href": "./map-flickering.md"}, {"name": "Map Storage", "abbr": "MSTR", "date": "2023-05-29", "tags": ["storage", "map"], "versions": ["1.1.0", "1.1.1"], "credits": ["blueberryoats"], "href": "./map-storage.md"}, {"name": "Map Zuggling", "abbr": "MZ", "date": "2023-05-23", "tags": ["zuggling", "map", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["BigDUCCO"], "href": "./map-zuggling-mz.md"}, {"name": "Mass Amnesia", "abbr": "MA", "date": "2023-08-02", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./mass-amnesia.md"}, {"name": "Master Sword Liberation", "abbr": "MSL", "date": "2023-11-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./master-sword-liberation.md"}, {"name": "Master Sword Zuggling/ Decayed Master Sword Zuggling", "abbr": "MSZ", "date": "2023-11-06", "tags": ["zuggling", "desync", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./master-sword-zuggling-decayed-master-sword-zuggling.md"}, {"name": "Memory Buffering", "abbr": "MB", "date": "2023-05-29", "tags": ["menu", "buff"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./memory-buffering.md"}, {"name": "Memory Interrupt", "abbr": "MI", "date": "2024-10-01", "tags": ["Unknown"], "versions": ["1.0.0"], "credits": ["mulberry"], "href": "./memory-interrupt.md"}, {"name": "Menu Overload", "abbr": "MO", "date": "2024-01-11", "tags": ["oob", "menu", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./menu-overload.md"}, {"name": "Message Not Found", "abbr": "MNF", "date": "2023-05-17", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Abahbob"], "href": "./message-not-found-mnf.md"}, {"name": "Midair Item Transmutation", "abbr": "MIT", "date": "2023-05-20", "tags": ["item", "paraglide", "zuggling"], "versions": ["1.1.0", "1.1.1"], "credits": ["eXe"], "href": "./midair-item-transmutation-mit.md"}, {"name": "Midair Sort Duplication", "abbr": "MSD", "date": "2023-05-21", "tags": ["duplication", "menu", "item", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zas", "kurocat471"], "href": "./midair-sort-duplication-msd.md"}, {"name": "Midair Throw Duplication", "abbr": "MTD", "date": "2023-07-02", "tags": ["duplication", "item", "zonai", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["quantim"], "href": "./midair-throw-duplication-mtd.md"}, {"name": "Minecart Rail Collision Launching", "abbr": "MRCL", "date": "2023-05-18", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüØÒéë-ÒüòÒéô"], "href": "./minecart-rail-collision-launching-mrcl.md"}, {"name": "Mineru Ability Desync", "abbr": "MAD", "date": "2023-05-30", "tags": ["desync", "mineru"], "versions": ["1.1.0", "1.1.1"], "credits": ["Sillicat"], "href": "./mineru-ability-desync.md"}, {"name": "Mineru Aim Permanence", "abbr": "MAIP", "date": "Unknown", "tags": ["mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./mineru-aim-permanence.md"}, {"name": "Mineru Cull Storage", "abbr": "MCS", "date": "2025-11-09", "tags": ["zuggling", "storage", "culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["ofstrings2"], "href": "./mineru-cull-storage.md"}, {"name": "Mineru Culling", "abbr": "MC", "date": "2023-07-31", "tags": ["culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./mineru-culling.md"}, {"name": "Mineru Fuse Entanglement", "abbr": "MFE", "date": "2023-10-18", "tags": ["entanglement", "culling", "ultrahand", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "WinnerBoi77"], "href": "./mineru-fuse-entanglement-mineru-fe.md"}, {"name": "Mineru Hold Smuggle", "abbr": "MHS", "date": "2023-12-20", "tags": ["zuggling", "menu", "item", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./mineru-hold-smuggle-mhs.md"}, {"name": "Mineru Persistent Save Load Object Transfer", "abbr": "MPSLOT", "date": "2024-07-27", "tags": ["equipment", "culling", "save-load", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry", "Armindo", "Emiya"], "href": "./mineru-persistent-save-load-object-transfer.md"}, {"name": "Mineru Text Storage", "abbr": "MTS", "date": "2024-07-11", "tags": ["storage", "mineru"], "versions": ["1.0.0"], "credits": ["CM30"], "href": "./mineru-text-storage.md"}, {"name": "MNF Fusing", "abbr": "MNFF", "date": "2023-06-05", "tags": ["fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./mnf-fusing.md"}, {"name": "MNF Glow Overload", "abbr": "MGO", "date": "2025-01-03", "tags": ["item", "overload", "mnf"], "versions": ["1.0.0"], "credits": ["Toti Sauce"], "href": "./mnf-glow-overload.md"}, {"name": "MNF Zuggle Fuse", "abbr": "MZF", "date": "2023-05-18", "tags": ["zuggling", "weapon", "fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./mnf-zuggle-fuse.md"}, {"name": "Model Teleport Desync", "abbr": "MTEL", "date": "2023-07-29", "tags": ["desync", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./model-teleport-desync.md"}, {"name": "Modifier Deletion Weapon State Transfer", "abbr": "MDWST", "date": "Unknown", "tags": ["duplication", "weapon"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md"}, {"name": "Modifier ONLY Transfer", "abbr": "MOT", "date": "2023-06-09", "tags": ["weapon"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "BigDUCCO"], "href": "./modifier-only-transfer.md"}, {"name": "Moobe Warping", "abbr": "MW", "date": "2024-01-12", "tags": ["oob", "warping", "movement", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./moobe-warping.md"}, {"name": "Mount Lock", "abbr": "ML", "date": "2023-05-21", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./mount-lock.md"}, {"name": "Mozdor Jumping/Slashing", "abbr": "MJS", "date": "2023-05-20", "tags": ["movement", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "AgdoR"], "href": "./mozdor-jumping-slashing.md"}, {"name": "MSNF glowing", "abbr": "MG", "date": "2023-08-02", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["evilgabe"], "href": "./msnf-glowing.md"}, {"name": "Mulberry's Out of Body Experience", "abbr": "MOOBE", "date": "2024-01-06", "tags": ["warping", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./mulberry-s-out-of-body-experience-moobe.md"}, {"name": "New Item Desync", "abbr": "NID", "date": "2023-05-12", "tags": ["duplication", "desync", "menu", "item", "equipment", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Modoki_returns"], "href": "./new-item-desync-equipment-duping.md"}, {"name": "No Bow Sprinting", "abbr": "NBS", "date": "2023-05-12", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./no-bow-sprinting-nbs.md"}, {"name": "Null Dropping", "abbr": "ND", "date": "2024-03-16", "tags": ["menu", "item", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl"], "href": "./null-dropping.md"}, {"name": "Object Culling", "abbr": "OC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "tori", "mulberry", "Timber"], "href": "./object-culling.md"}, {"name": "Object (Moe) Enlargement", "abbr": "MOE", "date": "2024-10-30", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "PetitFrapo", "Jordan"], "href": "./object-moe-enlargement.md"}, {"name": "Ocklusion Hovering", "abbr": "OCKH", "date": "2025-10-12", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic"], "href": "./ocklusion-hovering.md"}, {"name": "Ocklusion", "abbr": "OCKL", "date": "2024-05-29", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./ocklusion.md"}, {"name": "Octo-balloon Detanglement", "abbr": "OBD", "date": "2025-11-16", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./octo-balloon-detanglement.md"}, {"name": "Octodupe", "abbr": "OD", "date": "2023-05-26", "tags": ["duplication", "item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./octodupe.md"}, {"name": "Overload at Home", "abbr": "OAH", "date": "2024-03-20", "tags": ["zuggling", "culling", "overload"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./overload-at-home-aka-pickup-overload.md"}, {"name": "Overload Cold Fuse", "abbr": "OCF", "date": "2023-07-23", "tags": ["item", "weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["F. Buffalo"], "href": "./overload-cold-fuse.md"}, {"name": "Overload Drop Smuggling", "abbr": "ODS", "date": "2023-06-12", "tags": ["zuggling", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ChargeVolt", "Windocks"], "href": "./overload-drop-smuggling.md"}, {"name": "Overload Dynamic Zuggle", "abbr": "ODZ", "date": "2025-05-19", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./overload-dynamic-zuggle.md"}, {"name": "Overload Fuse Entanglement", "abbr": "OFE", "date": "2024-07-23", "tags": ["zuggling", "entanglement", "culling", "overload", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./overload-fuse-entanglement.md"}, {"name": "Overload Persistent Save Load Object Transfer", "abbr": "OPSLOT", "date": "2024-07-26", "tags": ["overload", "save-load"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./overload-persistent-save-load-object-transfer.md"}, {"name": "Pelison Duping", "abbr": "PD", "date": "2023-05-25", "tags": ["duplication", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["AngryEgg", "BigDUCCO"], "href": "./pelison-duping.md"}, {"name": "Persistent Save Load Object Transfer", "abbr": "PSLOT", "date": "2024-01-25", "tags": ["culling", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./persistent-save-load-object-transfer-pslot.md"}, {"name": "Pickup Smuggling", "abbr": "PSMU", "date": "2023-05-28", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ame"], "href": "./pickup-smuggling.md"}, {"name": "Pocket Rocket", "abbr": "PR", "date": "2023-06-15", "tags": ["launching", "equipment", "paraglide", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "SmallAnt"], "href": "./pocket-rocket.md"}, {"name": "Portable Cull Save Load Dupe", "abbr": "PSLD", "date": "2024-07-17", "tags": ["duplication", "culling", "save-load"], "versions": ["1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./portable-cull-save-load-dupe-portacull-sld.md"}, {"name": "Portable Culling", "abbr": "PCULL", "date": "2024-02-27", "tags": ["zuggling", "desync", "item", "culling", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./portable-culling.md"}, {"name": "Portacull Invismuggle", "abbr": "PCI", "date": "2024-02-29", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./portacull-invismuggle.md"}, {"name": "Weapon Despawn Prevention", "abbr": "WDP", "date": "2023-06-28", "tags": ["weapon", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./prevent-weapon-despawn.md"}, {"name": "Prologue Escape", "abbr": "PE", "date": "2024-10-01", "tags": ["duplication", "storage"], "versions": ["1.0.0"], "credits": ["LegendofLinkk", "mulberry", "Aergyl", "Lightos", "EOH_NS_SS"], "href": "./prologue-escape.md"}, {"name": "Proxy Glitches", "abbr": "PG", "date": "Unknown", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./proxy-glitches.md"}, {"name": "Purgatory Save Load Dupe", "abbr": "PGSLD", "date": "2024-02-11", "tags": ["duplication", "equipment", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./purgatory-save-load-dupe.md"}, {"name": "Pyroculling", "abbr": "PYR", "date": "2023-11-17", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.2.0"], "credits": ["ROBUXY2ND"], "href": "./pyroculling.md"}, {"name": "Quantum Linking", "abbr": "QL", "date": "2023-08-30", "tags": ["culling", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "pyuk"], "href": "./quantum-linking-ql.md"}, {"name": "Quick Drop Smuggle", "abbr": "QDS", "date": "2024-03-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0"], "credits": ["mulberry", "Zas", "Aeolian", "WinnerBoi77", "Ryan?"], "href": "./quick-drop-smuggle-qds.md"}, {"name": "Quick Smuggling", "abbr": "QS", "date": "2023-07-10", "tags": ["zuggling", "equipment", "arrow"], "versions": ["1.2.0"], "credits": ["Suishi"], "href": "./quick-smuggling.md"}, {"name": "Reball", "abbr": "RBL", "date": "2023-07-06", "tags": ["movement", "recall", "zonai"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./reball.md"}, {"name": "Recall Cancel", "abbr": "RCC", "date": "2023-07-20", "tags": ["animation", "item", "recall"], "versions": ["1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./recall-cancel.md"}, {"name": "Recall Clip", "abbr": "RC", "date": "2023-05-16", "tags": ["clipping", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüôÒéôÒüØÒéü"], "href": "./recall-clip.md"}, {"name": "Recall Drop Stacking", "abbr": "RDS", "date": "2025-01-04", "tags": ["item", "recall", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Telkic", "mulberry"], "href": "./recall-drop-stacking.md"}, {"name": "Recall Launch", "abbr": "RL", "date": "2023-05-17", "tags": ["launching", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deep"], "href": "./recall-launch.md"}, {"name": "Recall Locking", "abbr": "RLK", "date": "2023-06-11", "tags": ["recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./recall-locking.md"}, {"name": "Recall Sluggle", "abbr": "RSL", "date": "2025-07-12", "tags": ["zuggling", "menu", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["WinnerBoi77"], "href": "./recall-sluggle.md"}, {"name": "Recipe Storage", "abbr": "RS", "date": "2024-09-14", "tags": ["storage", "menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./recipe-storage.md"}, {"name": "Remote Arrow", "abbr": "RAT", "date": "2023-06-02", "tags": ["arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Flash", "ElDuende", "kirigaya"], "href": "./remote-arrow-trap.md"}, {"name": "Replacement Actor Fuse Entanglement", "abbr": "RAFE", "date": "2024-11-09", "tags": ["entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["dt13269", "mulberry"], "href": "./replacement-actor-fuse-entanglement.md"}, {"name": "Resync Fuse Entanglement", "abbr": "RFE", "date": "2023-12-18", "tags": ["item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./resync-fuse-entanglement-resync-fe.md"}, {"name": "Reverse Ascend Storage", "abbr": "RAS", "date": "2023-11-27", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Redrooey"], "href": "./reverse-ascend-storage.md"}, {"name": "Sage Madness", "abbr": "SM", "date": "2023-07-18", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aci"], "href": "./sage-madness.md"}, {"name": "Sage Recycling", "abbr": "SRCY", "date": "2023-05-28", "tags": ["duplication", "tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Knight7108", "Candlelor"], "href": "./sage-recycling.md"}, {"name": "Save Load Dupe", "abbr": "SLD", "date": "2023-05-16", "tags": ["duplication", "equipment", "save-load", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ZombieBoy225", "ness", "ElDuende"], "href": "./save-load-dupe-sld.md"}, {"name": "Save Load Zuggling", "abbr": "SLZ", "date": "2023-05-23", "tags": ["zuggling", "save-load", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["NicNac", "Flash", "BigDUCCO", "Wip long sticks enjoyer"], "href": "./save-load-zuggling-slz.md"}, {"name": "Scope Render Cancel", "abbr": "SRC", "date": "2023-05-19", "tags": ["animation", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "eXe"], "href": "./scope-render-cancel.md"}, {"name": "Shadow/Void Icons", "abbr": "SVI", "date": "2024-10-16", "tags": ["equipment", "fuse", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Lightos", "PetitFrapo"], "href": "./shadow-void-icons.md"}, {"name": "Shock Cold Fuse", "abbr": "SCF", "date": "2023-09-11", "tags": ["weapon", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-cold-fuse.md"}, {"name": "Shock Effect Overload", "abbr": "SEO", "date": "2023-07-26", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "R4000"], "href": "./shock-effect-overload-seo.md"}, {"name": "Shock Fuse Entanglement", "abbr": "SFE", "date": "2023-09-12", "tags": ["zuggling", "item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-fuse-entanglement.md"}, {"name": "Shock Smuggle", "abbr": "SSMU", "date": "2023-06-01", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["sleepyppls"], "href": "./shock-smuggle.md"}, {"name": "Shrunken Actors", "abbr": "SA", "date": "2025-10-26", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./shrunken-actors.md"}, {"name": "Slate Storage", "abbr": "SLST", "date": "2024-09-21", "tags": ["storage", "damage"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk"], "href": "./slate-storage.md"}, {"name": "Slugging", "abbr": "SLG", "date": "2023-06-15", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./slugging.md"}, {"name": "Smuggle Retrieval", "abbr": "SRET", "date": "2024-12-18", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["PetitFrapo"], "href": "./smuggle-retrieval.md"}, {"name": "Smuggle Stacking Zuggle", "abbr": "SSZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "LegendofLinkk", "Mozz"], "href": "./smuggle-stacking-zuggle-ssz.md"}, {"name": "Split Item Duplication", "abbr": "SID", "date": "2025-06-19", "tags": ["duplication", "item", "zuggling"], "versions": ["1.2.0"], "credits": ["Telkic", "mulberry", "WinnerBoi77"], "href": "./split-item-duplication-sid.md"}, {"name": "Spring Fall Damage Cancel", "abbr": "SFDC", "date": "2023-05-15", "tags": ["animation", "damage", "movement", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./spring-fall-damage-cancel.md"}, {"name": "Spring Strangeness", "abbr": "STRS", "date": "2023-05-15", "tags": ["spring", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi", "Owen"], "href": "./spring-strangeness.md"}, {"name": "Springboard Clipping", "abbr": "SBC", "date": "2023-05-27", "tags": ["clipping", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ab2x3z"], "href": "./springboard-clipping.md"}, {"name": "Springboarding", "abbr": "SBRD", "date": "2023-05-24", "tags": ["equipment", "shield", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springboarding.md"}, {"name": "Springdolling", "abbr": "SDOL", "date": "2023-05-15", "tags": ["launching", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springdolling.md"}, {"name": "Stack Splitting", "abbr": "SSPL", "date": "2024-12-31", "tags": ["item", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["s0ft", "Telkic", "mulberry"], "href": "./stack-splitting.md"}, {"name": "Stamina Depletion Freeze", "abbr": "SDF", "date": "2023-05-20", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./stamina-depletion-freeze-sdf.md"}, {"name": "Stick Desync Clip", "abbr": "SDC", "date": "2023-07-01", "tags": ["clipping", "desync", "item", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "DisguisedMoth"], "href": "./stick-desync-clip-sdc.md"}, {"name": "Sticky Dynamic Purgatory", "abbr": "SDP", "date": "2024-02-15", "tags": ["equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./sticky-dynamic-purgatory.md"}, {"name": "Super Bomb Jump", "abbr": "SBJ", "date": "2023-09-14", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["FerrusCube", "Aergyl"], "href": "./super-bomb-jump.md"}, {"name": "Super Fuse Overload", "abbr": "SFO", "date": "2025-12-06", "tags": ["weapon", "overload", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Aergyl", "Jordan", "MandelbrotChaylay"], "href": "./super-fuse-overload.md"}, {"name": "Surf storage", "abbr": "SSTR", "date": "2023-09-22", "tags": ["storage"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./surf-storage.md"}, {"name": "Swap Resync Zuggle", "abbr": "SRZ", "date": "2025-08-11", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry", "MandelbrotChaylay"], "href": "./swap-resync-zuggle-srz.md"}, {"name": "Swap Resync", "abbr": "SR", "date": "2025-08-10", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["MandelbrotChaylay"], "href": "./swap-resync.md"}, {"name": "Temporary Devices", "abbr": "TD", "date": "2024-11-30", "tags": ["fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./temporary-devices.md"}, {"name": "Texture Tearing", "abbr": "TT", "date": "2024-01-13", "tags": ["oob", "menu", "equipment", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./texture-tearing.md"}, {"name": "Throken", "abbr": "THK", "date": "2025-05-17", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikaboze"], "href": "./throken.md"}, {"name": "Throw Cancelling", "abbr": "TC", "date": "Unknown", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Quelfth"], "href": "./throw-cancelling.md"}, {"name": "Throw Tap Sprinting", "abbr": "TTS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer", "Tauktes"], "href": "./throw-tap-sprinting-tts.md"}, {"name": "Throwless Storage", "abbr": "THS", "date": "2023-06-19", "tags": ["storage", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["evilgabe", "NX721"], "href": "./throwless-storage-previously-known-as-beam-storage.md"}, {"name": "Time Bomb cancel", "abbr": "TBC", "date": "2023-11-04", "tags": ["animation", "equipment", "damage", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["tzakazuki"], "href": "./time-bomb-cancel.md"}, {"name": "Toti Saucery", "abbr": "TOTS", "date": "2024-08-17", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "Telkic"], "href": "./toti-saucery.md"}, {"name": "Travel Medallion storage", "abbr": "TMS", "date": "2023-06-16", "tags": ["storage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kirigaya"], "href": "./travel-medallion-storage-tms.md"}, {"name": "Tulin Pumping", "abbr": "TP", "date": "2023-05-14", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikkitrix"], "href": "./tulin-pumping.md"}, {"name": "Two Handed With Shield", "abbr": "THWS", "date": "2023-08-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Bucket_Sloe"], "href": "./two-handed-with-shield.md"}, {"name": "Ultimate Pocket Rocket", "abbr": "UPR", "date": "2025-05-20", "tags": ["launching", "warping", "ultrahand"], "versions": ["1.0.0"], "credits": ["Aergyl", "mulberry", "Ikaboze", "Jordan"], "href": "./ultimate-pocket-rocket.md"}, {"name": "Ultra Save Load Object Transfer", "abbr": "USLOT", "date": "2024-02-15", "tags": ["save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./ultra-save-load-object-transfer.md"}, {"name": "Ultrabroken Smuggling", "abbr": "UBS", "date": "2023-06-13", "tags": ["zuggling", "equipment", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["The_Andromeda"], "href": "./ultrabroken-smuggling-ubs.md"}, {"name": "Ultrabroken", "abbr": "UB", "date": "2023-05-29", "tags": ["item", "ultrahand", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Duncan"], "href": "./ultrabroken.md"}, {"name": "Unload Duping", "abbr": "UD", "date": "2023-05-31", "tags": ["duplication", "item", "culling", "fuse", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª", "ÕìâÕ╣┤ÞîÂÚÑ╝"], "href": "./unload-duping.md"}, {"name": "Unload WST", "abbr": "UWST", "date": "Unknown", "tags": ["item", "culling", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "Vee.Might.Exist", "Syb"], "href": "./unload-wst.md"}, {"name": "Unsheathed Mastersword", "abbr": "UMS", "date": "2023-07-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "DanielNeia"], "href": "./unsheathed-mastersword.md"}, {"name": "Vendor Scamming", "abbr": "VS", "date": "2023-07-03", "tags": ["zuggling", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "Mozz", "NaN Gogh"], "href": "./vendor-scamming.md"}, {"name": "Void Dipping", "abbr": "VD", "date": "2025-12-29", "tags": ["item", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Squidwest", "mulberry", "Aergyl"], "href": "./void-dipping.md"}, {"name": "Void Hold Storage", "abbr": "VHS", "date": "2023-07-22", "tags": ["storage", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "NX721"], "href": "./void-hold-storage.md"}, {"name": "Void Holding", "abbr": "VH", "date": "2023-06-10", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Lightos"], "href": "./void-holding.md"}, {"name": "Wacko Attacko", "abbr": "WATK", "date": "2024-01-21", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3", "WinnerBoi77"], "href": "./wacko-attacko.md"}, {"name": "Warp Bumping", "abbr": "WB", "date": "2023-06-07", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Mozz", "InAMuffinCup"], "href": "./warp-bumping.md"}, {"name": "Weapon Dash GAS", "abbr": "WDGAS", "date": "2025-11-28", "tags": ["gas", "weapon", "culling", "fuse", "zonai"], "versions": ["1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Toti Sauce"], "href": "./weapon-dash-gas.md"}, {"name": "Weapon Extensions", "abbr": "WEXT", "date": "2023-06-20", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deltenic", "Flash", "Zas"], "href": "./weapon-extensions.md"}, {"name": "Weapon FE", "abbr": "WFE", "date": "2023-06-01", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ROBUXY2ND", "Physioninja"], "href": "./weapon-fe.md"}, {"name": "Weapon Sheath Offset", "abbr": "WSO", "date": "2023-06-25", "tags": ["zuggling", "weapon", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["circyit", "dash"], "href": "./weapon-sheath-offset-wso.md"}, {"name": "Weapon Stacking Duplication", "abbr": "WSD", "date": "2023-05-16", "tags": ["duplication", "item", "weapon", "equipment", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ErlingÚÖäÞ║½"], "href": "./weapon-stacking-duplication-wsd.md"}, {"name": "Weapon Stand Dynamic Zuggle", "abbr": "WSDZ", "date": "2024-03-14", "tags": ["zuggling", "weapon", "item", "equipment"], "versions": ["1.0.0"], "credits": ["WinnerBoi77"], "href": "./weapon-stand-dynamic-zuggle.md"}, {"name": "Weapon State Transfer", "abbr": "WST", "date": "2023-05-19", "tags": ["weapon", "fuse", "entanglement", "equipment", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "kurocat471", "ElDuende", "Mentor_Kurt"], "href": "./weapon-state-transfer-wst.md"}, {"name": "Weather Amnesia", "abbr": "WA", "date": "2023-06-25", "tags": ["environment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk"], "href": "./weather-amnesia-wa.md"}, {"name": "Wheel Warping", "abbr": "WW", "date": "2023-06-18", "tags": ["launching", "warping", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk"], "href": "./wheel-warping.md"}, {"name": "Wheel Zoomy", "abbr": "WZ", "date": "2023-07-12", "tags": ["movement", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Solo_Turtle"], "href": "./wheel-zoomy-also-known-as-wheel-wacko-boingo.md"}, {"name": "Wireless Energy", "abbr": "WE", "date": "2023-07-11", "tags": ["equipment", "culling", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./wireless-energy.md"}, {"name": "Wuggle", "abbr": "WGL", "date": "2023-12-29", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "ROBUXY2ND"], "href": "./wuggle-weird-zuggle.md"}, {"name": "Yee Fuse Entanglement", "abbr": "YEEFE", "date": "2024-02-20", "tags": ["entanglement", "culling", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee", "mulberry"], "href": "./yee-fuse-entanglement.md"}, {"name": "Zapshield", "abbr": "ZAP", "date": "2024-09-16", "tags": ["equipment", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./zapshield.md"}, {"name": "ZL Animation Reset", "abbr": "ZLAR", "date": "2024-01-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./zl-animation-reset-zlar.md"}, {"name": "Zoggle", "abbr": "ZOG", "date": "2024-01-04", "tags": ["zuggling", "ultrahand", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ryan?", "Ock"], "href": "./zoggle.md"}, {"name": "Zonai Inventory Shift Dupe", "abbr": "ZISD", "date": "2023-07-10", "tags": ["duplication", "menu", "buff", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "quantim"], "href": "./zonai-inventory-shift-dupe-zisd.md"}, {"name": "Zonai Sort Duplication", "abbr": "ZSD", "date": "2023-05-22", "tags": ["duplication", "menu", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Quelfth", "Flash"], "href": "./zonai-sort-duplication-zsd.md"}, {"name": "Zonai Storage", "abbr": "ZS", "date": "2023-08-13", "tags": ["storage", "zonai"], "versions": ["1.0.0"], "credits": ["bebu0815"], "href": "./zonai-storage.md"}, {"name": "Zuggle Load Object Transfering", "abbr": "ZLOT", "date": "2023-06-07", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup", "ChargeVolt"], "href": "./zuggle-load-object-transfering-zlot.md"}, {"name": "Zuggle Overload Desync", "abbr": "ZOD", "date": "Unknown", "tags": ["zuggling", "desync", "menu", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./zuggle-overload-desync.md"}, {"name": "Zuggle Overload Out Of Bounds", "abbr": "ZOOB", "date": "2023-05-18", "tags": ["clipping", "oob", "zuggling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["AngryEgg"], "href": "./zuggle-overload-out-of-bounds.md"}, {"name": "Zuggle Overload", "abbr": "ZO", "date": "2023-05-17", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle-overload.md"}, {"name": "Zuggle", "abbr": "ZGL", "date": "2023-05-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle.md"}]
\ No newline at end of file
+[{"name": "Grimoire of Glitchcraft", "abbr": "", "date": "", "tags": [], "versions": [], "credits": [], "href": "./_glitchcraft-grimoire.md"}, {"name": "Ability Wheel Loop", "abbr": "AWL", "date": "2024-03-11", "tags": ["menu", "ultrahand", "zonai"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./ability-wheel-loop.md"}, {"name": "Aeroculling", "abbr": "AC", "date": "2024-08-11", "tags": ["equipment", "culling", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./aeroculling.md"}, {"name": "Animation Swap", "abbr": "ASWP", "date": "2023-05-17", "tags": ["zuggling", "animation", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Swinginman"], "href": "./animation-swap.md"}, {"name": "Anti-gravity GAS", "abbr": "AGAS", "date": "2025-01-22", "tags": ["gas"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./anti-gravity-gas.md"}, {"name": "Anti-Gravity Glitch", "abbr": "AGG", "date": "2023-05-13", "tags": ["paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Kaldemar"], "href": "./anti-gravity-glitch.md"}, {"name": "Anti-Gravity Objects", "abbr": "AGO", "date": "Unknown", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./anti-gravity-objects.md"}, {"name": "AntiGrav Weapons", "abbr": "AGW", "date": "2023-05-28", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Blize"], "href": "./antigrav-weapons.md"}, {"name": "Arrow Prompt Storage", "abbr": "APS", "date": "2023-10-04", "tags": ["storage", "culling", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NghtmaR3"], "href": "./arrow-prompt-storage-aps.md"}, {"name": "Arrow Smuggling", "abbr": "ASMU", "date": "2023-06-04", "tags": ["zuggling", "equipment", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./arrow-smuggling.md"}, {"name": "Arrow Unlink", "abbr": "AUL", "date": "2023-10-26", "tags": ["fuse", "arrow"], "versions": ["1.0.0"], "credits": ["R4000"], "href": "./arrow-unlink.md"}, {"name": "Arrow Unloading", "abbr": "AU", "date": "2023-06-18", "tags": ["culling", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk", "Zas"], "href": "./arrow-unloading.md"}, {"name": "Ascend Camera Glitch", "abbr": "ACG", "date": "Unknown", "tags": ["ascend", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./ascend-camera-glitch.md"}, {"name": "Ascend Rushing", "abbr": "AR", "date": "2023-06-15", "tags": ["ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./ascend-rushing.md"}, {"name": "Ascend Storage", "abbr": "ASTR", "date": "2023-05-19", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Saria"], "href": "./ascend-storage.md"}, {"name": "Attached Rangeless Active Zonai", "abbr": "ARAZ", "date": "2023-06-16", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?", "NX721"], "href": "./attached-rangeless-active-zonai-araz.md"}, {"name": "Autobuild Cancel Slide", "abbr": "ABCS", "date": "2023-05-18", "tags": ["animation", "movement", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Takosensai1"], "href": "./autobuild-cancel-slide-abcs.md"}, {"name": "Autobuild Duplication", "abbr": "ABD", "date": "2023-06-11", "tags": ["duplication", "item", "ultrahand", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./autobuild-duplication-abd.md"}, {"name": "Autobuild Storage", "abbr": "ABST", "date": "2023-08-28", "tags": ["storage", "item", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "R4000"], "href": "./autobuild-storage.md"}, {"name": "Awakened Master Sword", "abbr": "AMS", "date": "2023-09-04", "tags": ["weapon", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tahata"], "href": "./awakened-master-sword-ams.md"}, {"name": "Back-in-Time Art", "abbr": "BIT", "date": "2023-06-18", "tags": ["save-load"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Zas"], "href": "./back-in-time-art.md"}, {"name": "Back to Back Bloodmoon", "abbr": "BTBB", "date": "2023-05-17", "tags": ["bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lopitty"], "href": "./back-to-back-bloodmoon.md"}, {"name": "Balloon Overload", "abbr": "BO", "date": "2025-03-08", "tags": ["menu", "equipment", "overload", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Jordan", "mulberry", "ofstrings2"], "href": "./balloon-overload.md"}, {"name": "Banc Storage", "abbr": "BANC", "date": "2024-10-01", "tags": ["storage", "warping", "save-load", "bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos", "mulberry", "Aergyl", "EOH_NS_SS"], "href": "./banc-storage.md"}, {"name": "Bomb Skew", "abbr": "BSK", "date": "2023-09-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl", "FerrusCube", "Mozz"], "href": "./bomb-skew.md"}, {"name": "Bow Attachment Desync", "abbr": "BAD", "date": "2023-07-11", "tags": ["desync", "item", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Aeolian"], "href": "./bow-attachment-desync-bad-arrows.md"}, {"name": "Bow Attachment Storage", "abbr": "BAS", "date": "2023-12-03", "tags": ["storage", "item", "fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./bow-attachment-storage.md"}, {"name": "Bow Sprinting", "abbr": "BS", "date": "2023-05-14", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./bow-sprinting.md"}, {"name": "Breaking Awakened Master Sword", "abbr": "BAMS", "date": "2023-11-26", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Infrasolid"], "href": "./breaking-awakened-master-sword.md"}, {"name": "BThrow Sprinting", "abbr": "BTS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./bthrow-sprinting.md"}, {"name": "Bundled Item Duplication", "abbr": "BID", "date": "2023-12-12", "tags": ["duplication", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./bundled-item-duplication-bid.md"}, {"name": "Buoy Bouncing", "abbr": "BB", "date": "2023-05-25", "tags": ["equipment", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup"], "href": "./buoy-bouncing.md"}, {"name": "Camera CFW", "abbr": "CFW", "date": "2023-07-11", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh"], "href": "./camera-cfw.md"}, {"name": "Camera Pose Glitch", "abbr": "CPG", "date": "Unknown", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./camera-pose-glitch.md"}, {"name": "Capsule Cel Shader Removal", "abbr": "CCSR", "date": "2023-12-04", "tags": ["duplication", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./capsule-cel-shader-removal.md"}, {"name": "Cave Flag Culling", "abbr": "CFC", "date": "2023-11-24", "tags": ["duplication", "culling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Aergyl"], "href": "./cave-flag-culling.md"}, {"name": "Chasm Delay Zuggle", "abbr": "CDZ", "date": "2024-05-31", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock", "mulberry", "WinnerBoi77"], "href": "./chasm-delay-zuggle-cdz.md"}, {"name": "Chasm Device Dupe", "abbr": "CDD", "date": "2025-10-12", "tags": ["duplication", "item", "culling", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic", "mulberry"], "href": "./chasm-device-dupe.md"}, {"name": "Clear Camera/Scope", "abbr": "CCS", "date": "2023-07-03", "tags": ["bow", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./clear-camera-scope.md"}, {"name": "Cold Fuse Stick Desync Clip", "abbr": "CSSDC", "date": "2024-06-04", "tags": ["clipping", "desync", "weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "KiloVictor"], "href": "./cold-fuse-stick-desync-clip-cold-fuse-sdc.md"}, {"name": "Cold Fuse", "abbr": "CF", "date": "2023-07-23", "tags": ["weapon", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk", "Ryan?", "Zas"], "href": "./cold-fuse.md"}, {"name": "Construct Fuse Entanglement", "abbr": "CNFE", "date": "2024-06-30", "tags": ["equipment", "entanglement", "fuse", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./construct-fuse-entanglement.md"}, {"name": "Corrupt Meal", "abbr": "CM", "date": "2025-02-07", "tags": ["cooking"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Telkic"], "href": "./corrupt-meal.md"}, {"name": "Crouch Sprinting", "abbr": "CS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./crouch-sprinting.md"}, {"name": "Crouch Throw Tap Sprinting", "abbr": "CTTS", "date": "2023-05-15", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer"], "href": "./crouch-throw-tap-sprinting-ctts.md"}, {"name": "Cucco Warping", "abbr": "CW", "date": "2023-07-23", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi"], "href": "./cucco-warping.md"}, {"name": "Cull Cold Fuse", "abbr": "CCF", "date": "2024-02-01", "tags": ["weapon", "culling", "ultrahand", "fuse"], "versions": ["Unknown"], "credits": ["mulberry"], "href": "./cull-cold-fuse.md"}, {"name": "Cull Equipment Desync", "abbr": "CED", "date": "2023-10-10", "tags": ["desync", "menu", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blize", "Ock"], "href": "./cull-equipment-desync.md"}, {"name": "Cull Fuse Entanglement", "abbr": "CFE", "date": "2023-09-21", "tags": ["entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "suusi", "Ock", "SteFen45"], "href": "./cull-fuse-entanglement-cull-fe.md"}, {"name": "Cull Launching", "abbr": "CL", "date": "2023-07-01", "tags": ["launching", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Asgorne"], "href": "./cull-launching.md"}, {"name": "Cull Pickup Dynamic Zuggle", "abbr": "CPDZ", "date": "2025-05-18", "tags": ["zuggling", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./cull-pickup-dynamic-zuggle.md"}, {"name": "Cull Smuggle", "abbr": "CSMU", "date": "2023-06-27", "tags": ["zuggling", "equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "ROBUXY2ND", "Ock"], "href": "./cull-smuggle.md"}, {"name": "Cull Storage Zuggle", "abbr": "CSZ", "date": "2024-07-18", "tags": ["zuggling", "storage", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars"], "href": "./cull-storage-zuggle-csz.md"}, {"name": "Cull Storage", "abbr": "CSTR", "date": "2024-01-20", "tags": ["storage", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./cull-storage.md"}, {"name": "Cull Zone Culling", "abbr": "CZC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./cull-zone-culling.md"}, {"name": "Culling Area Fuse Storage Fuse Entanglement", "abbr": "CFSFE", "date": "2024-02-25", "tags": ["storage", "entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee", "Zas"], "href": "./culling-area-fuse-storage-fuse-entanglement.md"}, {"name": "Culling Area Fuse Storage", "abbr": "CAFS", "date": "2023-06-30", "tags": ["storage", "culling", "fuse"], "versions": ["Unknown"], "credits": ["Mozz", "pyuk"], "href": "./culling-area-fuse-storage.md"}, {"name": "Cutscene Combo Amplifier", "abbr": "CCA", "date": "2023-12-22", "tags": ["item", "buff", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos"], "href": "./cutscene-combo-amplifier.md"}, {"name": "Damage Amnesia", "abbr": "DA", "date": "2023-05-27", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./damage-amnesia.md"}, {"name": "Death Persistent Save Load Object Transfer", "abbr": "DPSLOT", "date": "2025-06-26", "tags": ["item", "save-load", "zuggling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./death-persistent-save-load-object-transfer.md"}, {"name": "Detached Rangeless Active Zonai", "abbr": "DRAZ", "date": "2023-06-15", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Venaticus"], "href": "./detached-rangeless-active-zonai-draz.md"}, {"name": "Detanglement", "abbr": "DTG", "date": "2023-09-09", "tags": ["launching", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./detanglement.md"}, {"name": "Dialog Permacull", "abbr": "DPC", "date": "2025-11-28", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./dialog-permacull.md"}, {"name": "Disabled Enemy", "abbr": "DE", "date": "2023-06-27", "tags": ["enemy"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["shio_0725", "ralseidewitt"], "href": "./disabled-enemy.md"}, {"name": "Dispenser Storage", "abbr": "DISP", "date": "2023-07-02", "tags": ["storage", "item", "ultrahand", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./dispenser-storage.md"}, {"name": "Display Duping", "abbr": "DD", "date": "2023-05-27", "tags": ["duplication", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Pistonight"], "href": "./display-duping.md"}, {"name": "Display Master Sword", "abbr": "DMS", "date": "2023-06-08", "tags": ["weapon", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Zas"], "href": "./display-master-sword.md"}, {"name": "Dive Cancel Glide Boost", "abbr": "DCGB", "date": "2023-05-14", "tags": ["animation", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "Mety333"], "href": "./dive-cancel-glide-boost.md"}, {"name": "Double Bypass Zuggle", "abbr": "DBZ", "date": "2025-06-16", "tags": ["zuggling", "item", "culling", "ultrahand"], "versions": ["1.2.0"], "credits": ["mulberry", "dt13269"], "href": "./double-bypass-zuggle-dbz.md"}, {"name": "Double Shield Desync Clip Fuse Entanglement", "abbr": "DSDCFE", "date": "2024-06-06", "tags": ["duplication", "clipping", "desync", "equipment", "entanglement", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee"], "href": "./double-shield-desync-clip-fuse-entanglement-double-sdc-fe.md"}, {"name": "Double Tulin Boost", "abbr": "DTB", "date": "2023-05-17", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./double-tulin-boost.md"}, {"name": "Double Unfuse Duplicashen", "abbr": "DUD", "date": "2023-05-15", "tags": ["duplication", "item", "weapon", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Li Shen (Ú»ëþÑ×)"], "href": "./double-unfuse-duplicashen-dud.md"}, {"name": "Dpadlock-less Invizuggle", "abbr": "DLI", "date": "2024-07-17", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars", "NghtmaR3"], "href": "./dpadlock-less-invizuggle.md"}, {"name": "Drop Delay Zuggle", "abbr": "DDZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-delay-zuggle-ddz.md"}, {"name": "Drop Restriction", "abbr": "DR", "date": "2023-06-19", "tags": ["menu", "item", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["SCFD-GK2", "NicNac"], "href": "./drop-restriction.md"}, {"name": "Drop Smuggling", "abbr": "DSMU", "date": "2023-05-31", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-smuggling.md"}, {"name": "Drop Zuggle", "abbr": "DZ", "date": "2023-06-15", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO"], "href": "./drop-zuggle.md"}, {"name": "Durability-", "abbr": "DUR", "date": "2023-09-11", "tags": ["item", "weapon", "bow"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./durability.md"}, {"name": "Dynamic Purgatory Zuggle", "abbr": "DPZ", "date": "2025-02-14", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./dynamic-purgatory-zuggle.md"}, {"name": "Dynamic Zuggle", "abbr": "DZG", "date": "2023-09-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "Zas", "mulberry", "WinnerBoi77", "Ryan?", "CS16"], "href": "./dynamic-zuggle.md"}, {"name": "Eaten Despawn Interrupt", "abbr": "EDI", "date": "2026-01-16", "tags": ["item", "zuggling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Squidwest"], "href": "./eaten-despawn-interrupt.md"}, {"name": "Enemy Pickpocketing", "abbr": "EP", "date": "2023-09-16", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KAIDUDE64"], "href": "./enemy-pickpocketing.md"}, {"name": "Entanglement Height Glitch", "abbr": "EHG", "date": "2023-05-24", "tags": ["equipment", "entanglement", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./entanglement-height-glitch.md"}, {"name": "Equipment Collision Zuggle", "abbr": "ECZ", "date": "2023-05-16", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zvleon"], "href": "./equipment-collision-zuggle.md"}, {"name": "Equipment Mitosis", "abbr": "EM", "date": "2023-09-05", "tags": ["duplication", "zuggling", "equipment", "overload"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./equipment-mitosis.md"}, {"name": "Equipment Shock Duping", "abbr": "ESD", "date": "2023-12-12", "tags": ["duplication", "item", "equipment"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./equipment-shock-duping.md"}, {"name": "Equipment Smuggle", "abbr": "ESMU", "date": "2023-06-01", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["sleepyppls", "Mozz", "mulberry", "NaN Gogh"], "href": "./equipment-smuggle.md"}, {"name": "Equipped Throken", "abbr": "ETHK", "date": "2025-05-20", "tags": ["weapon", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./equipped-throken.md"}, {"name": "Extended Throw Sprinting", "abbr": "ETS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["briochoc"], "href": "./extended-throw-sprinting-ets.md"}, {"name": "Fall Damage Cancel", "abbr": "FDC", "date": "2023-05-23", "tags": ["animation", "damage", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter"], "href": "./fall-damage-cancel-fdc.md"}, {"name": "Floorping", "abbr": "FLP", "date": "2024-01-02", "tags": ["warping"], "versions": ["1.1.0", "1.1.1"], "credits": ["koreth"], "href": "./floorping.md"}, {"name": "Food Ability Buff Swap", "abbr": "FABS", "date": "2023-05-16", "tags": ["cooking", "item", "buff", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["fabs"], "href": "./food-ability-buff-swap-fabs.md"}, {"name": "Force Equip Zuggling", "abbr": "FEZ", "date": "2023-06-07", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "Mozz", "Rhkellz", "Syb", "NaN Gogh"], "href": "./force-equip-zuggling-fez.md"}, {"name": "Forced Blood Moon", "abbr": "FBM", "date": "2023-05-28", "tags": ["bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["1789(@W0ERYySQgZyGOY3)", "Simonfirefighter", "Maxmasher", "Flash", "acaepius"], "href": "./forced-blood-moon.md"}, {"name": "Freecall", "abbr": "FC", "date": "2023-09-09", "tags": ["ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["suusi", "ROBUXY2ND"], "href": "./freecall.md"}, {"name": "Fuse Entangle Drop Zuggle", "abbr": "FEDZ", "date": "2023-06-17", "tags": ["zuggling", "item", "weapon", "equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-drop-zuggle-fedz.md"}, {"name": "Fuse Entangle Weapon Zuggle", "abbr": "FEWZ", "date": "2023-06-10", "tags": ["zuggling", "item", "weapon", "damage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-weapon-zuggle-fewz.md"}, {"name": "Fuse Entanglement Clipping", "abbr": "FEC", "date": "2023-06-16", "tags": ["clipping", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["circyit"], "href": "./fuse-entanglement-clipping-fec.md"}, {"name": "Fuse Entanglement Desync", "abbr": "FED", "date": "2023-05-26", "tags": ["duplication", "desync", "item", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement-desync-fed.md"}, {"name": "Fuse Entanglement Drop Smuggling", "abbr": "FEDS", "date": "2023-08-15", "tags": ["zuggling", "item", "equipment", "entanglement", "fuse"], "versions": ["1.2.0"], "credits": ["Blize", "Blackmars"], "href": "./fuse-entanglement-drop-smuggling.md"}, {"name": "Fuse Entanglement", "abbr": "FE", "date": "2023-05-24", "tags": ["equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement.md"}, {"name": "Fuse Overload", "abbr": "FO", "date": "2023-11-03", "tags": ["weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "NghtmaR3"], "href": "./fuse-overload-fo.md"}, {"name": "Fuse Overload Fuse Entanglement", "abbr": "FOFE", "date": "2025-05-26", "tags": ["entanglement", "overload", "ultrahand", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry"], "href": "./fuse-overload-fuse-entanglement-fofe.md"}, {"name": "Fuse Storage", "abbr": "FS", "date": "2023-06-18", "tags": ["storage", "item", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./fuse-storage-fs.md"}, {"name": "Fuse Storage Fuse Entanglement", "abbr": "FSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./fuse-storage-fuse-entanglement-fsfe.md"}, {"name": "GAS Launching", "abbr": "GASL", "date": "2023-06-25", "tags": ["gas", "launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "pyuk", "Flash", "Mozz", "Blize"], "href": "./gas-launching-previously-known-as-ascend-launching.md"}, {"name": "GAS Warping", "abbr": "GASW", "date": "2023-06-26", "tags": ["gas", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Flash", "pyuk"], "href": "./gas-warping.md"}, {"name": "Ghost Save Load Object Transfer", "abbr": "GSLOT", "date": "2024-03-08", "tags": ["save-load", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./ghost-save-load-object-transfer.md"}, {"name": "Ghost Stick Clipping", "abbr": "GSC", "date": "2023-05-28", "tags": ["clipping"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["rocomox"], "href": "./ghost-stick-clipping.md"}, {"name": "Glue Removal", "abbr": "GR", "date": "2023-10-05", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./glue-removal.md"}, {"name": "Guard-less Active Shield", "abbr": "GAS", "date": "2023-06-12", "tags": ["equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Venaticus"], "href": "./guard-less-active-shield-gas.md"}, {"name": "Hand Locked Equipment Smuggling", "abbr": "HLES", "date": "2023-07-11", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0"], "credits": ["Aeolian"], "href": "./hand-locked-equipment-smuggling-hles.md"}, {"name": "Handy Job", "abbr": "HJ", "date": "2023-11-20", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./handy-job.md"}, {"name": "Hero Path Link Storage", "abbr": "HPLS", "date": "2023-06-20", "tags": ["storage"], "versions": ["1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./hero-path-link-storage-hpls.md"}, {"name": "Hestu Scamming", "abbr": "HSCA", "date": "2024-04-19", "tags": ["menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "Tahata", "EM"], "href": "./hestu-scamming.md"}, {"name": "Hold Smuggling", "abbr": "HSM", "date": "2023-07-04", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "NaN Gogh"], "href": "./hold-smuggling.md"}, {"name": "Hold Storage Duplication", "abbr": "HSD", "date": "2023-07-03", "tags": ["duplication", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Mozz"], "href": "./hold-storage-duplication-also-known-as-minus-dupe.md"}, {"name": "Hold Storage", "abbr": "HS", "date": "2023-07-02", "tags": ["storage", "desync", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NaN Gogh", "Mozz"], "href": "./hold-storage.md"}, {"name": "Horse Duping", "abbr": "HD", "date": "2024-03-22", "tags": ["duplication", "culling", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./horse-duping.md"}, {"name": "Hydro Clipping", "abbr": "HC", "date": "2023-06-15", "tags": ["clipping", "storage", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter", "Maxmasher", "KnightPohtaytoh", "pyuk"], "href": "./hydro-clipping.md"}, {"name": "Infinite Balloon", "abbr": "IBAL", "date": "2024-06-13", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurone_yuu"], "href": "./infinite-balloon.md"}, {"name": "Infinite Bubbul Frog Gems", "abbr": "IBFG", "date": "2023-05-21", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Unknown"], "href": "./infinite-bubbul-frog-gems.md"}, {"name": "Infinite Damage 2.0", "abbr": "ID2", "date": "2024-01-21", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./infinite-damage-2-0.md"}, {"name": "Infinite Damage", "abbr": "IDMG", "date": "2023-05-13", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["GamSla341"], "href": "./infinite-damage.md"}, {"name": "Infinite Height", "abbr": "IH", "date": "2023-05-22", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "Physioninja"], "href": "./infinite-height.md"}, {"name": "Inventory Shift Duplication", "abbr": "ISD", "date": "2023-06-25", "tags": ["duplication", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Blizzard Blanc", "BigDUCCO", "Maxmasher", "pyuk", "Zas"], "href": "./inventory-shift-duplication-isd.md"}, {"name": "Invizuggle", "abbr": "IVZ", "date": "2024-01-03", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Yee"], "href": "./invizuggle.md"}, {"name": "Item Save Load Transfer", "abbr": "ISLT", "date": "2023-12-22", "tags": ["item", "save-load", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Luckstyle"], "href": "./item-save-load-transfer-islt.md"}, {"name": "Item Throw Hitbox Disable", "abbr": "ITHD", "date": "2023-06-18", "tags": ["item", "recall", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Arfix", "Moonrise"], "href": "./item-throw-hitbox-disable.md"}, {"name": "Jumpslash Cancel Clipping", "abbr": "JCC", "date": "2023-06-16", "tags": ["clipping", "animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./jumpslash-cancel-clipping-jcc.md"}, {"name": "Jumpslash Canceling", "abbr": "JSC", "date": "2023-05-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Mozz"], "href": "./jumpslash-canceling.md"}, {"name": "Kilovictor's quicksmuggle", "abbr": "KQS", "date": "2024-02-23", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KiloVictor"], "href": "./kilovictor-s-quicksmuggle.md"}, {"name": "L Sprinting", "abbr": "LS", "date": "2023-05-12", "tags": ["sprinting", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tauktes"], "href": "./l-sprinting.md"}, {"name": "Lag Machines", "abbr": "LM", "date": "2023-10-05", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lag-machines.md"}, {"name": "Laser-OOB", "abbr": "LOOB", "date": "2023-05-13", "tags": ["duplication", "oob"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Xeryph"], "href": "./laser-oob.md"}, {"name": "Lift Fuse Interrupt", "abbr": "LFI", "date": "2025-04-22", "tags": ["weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee"], "href": "./lift-fuse-interrupt.md"}, {"name": "Lift Smuggle", "abbr": "LSMU", "date": "2024-02-03", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars"], "href": "./lift-smuggle.md"}, {"name": "Lift Storage Warping", "abbr": "LSW", "date": "2024-01-08", "tags": ["storage", "item", "culling", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./lift-storage-warping-lsw.md"}, {"name": "Lift Warping", "abbr": "LW", "date": "2023-06-15", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lift-warping.md"}, {"name": "Like-Like Culling", "abbr": "LLC", "date": "2023-06-13", "tags": ["culling", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-culling.md"}, {"name": "Like-Like Drop Smuggling", "abbr": "LLDS", "date": "2023-06-15", "tags": ["zuggling", "item", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-drop-smuggling.md"}, {"name": "Like-Like FSFE", "abbr": "LLFSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./like-like-fsfe.md"}, {"name": "Like-Like Fuse Storage", "abbr": "LLFS", "date": "2023-06-18", "tags": ["storage", "item", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Mozz"], "href": "./like-like-fuse-storage.md"}, {"name": "Like Like New Textbox Softlock", "abbr": "LLTS", "date": "2023-06-16", "tags": ["item", "like-like", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./like-like-new-textbox-softlock.md"}, {"name": "Like-Like Smuggle Desync", "abbr": "LLSD", "date": "2023-06-15", "tags": ["zuggling", "desync", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-smuggle-desync-lsd.md"}, {"name": "Like-Like Smuggling", "abbr": "LLS", "date": "2023-06-15", "tags": ["zuggling", "equipment", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-smuggling.md"}, {"name": "Like-Like Warping", "abbr": "LLW", "date": "2023-06-15", "tags": ["warping", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-warping.md"}, {"name": "Like-Like Zuggling", "abbr": "LLZ", "date": "2023-06-15", "tags": ["zuggling", "like-like", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Ryan?", "Blackmars"], "href": "./like-like-zuggling.md"}, {"name": "LikeLike Stick Smuggling", "abbr": "LLSS", "date": "Unknown", "tags": ["zuggling", "item", "equipment", "culling", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./likelike-stick-smuggling.md"}, {"name": "Long Jump", "abbr": "LJ", "date": "2023-05-18", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./long-jump.md"}, {"name": "Map Flickering", "abbr": "MF", "date": "Unknown", "tags": ["map"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Unknown"], "href": "./map-flickering.md"}, {"name": "Map Storage", "abbr": "MSTR", "date": "2023-05-29", "tags": ["storage", "map"], "versions": ["1.1.0", "1.1.1"], "credits": ["blueberryoats"], "href": "./map-storage.md"}, {"name": "Map Zuggling", "abbr": "MZ", "date": "2023-05-23", "tags": ["zuggling", "map", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["BigDUCCO"], "href": "./map-zuggling-mz.md"}, {"name": "Mass Amnesia", "abbr": "MA", "date": "2023-08-02", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./mass-amnesia.md"}, {"name": "Master Sword Liberation", "abbr": "MSL", "date": "2023-11-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./master-sword-liberation.md"}, {"name": "Master Sword Zuggling/ Decayed Master Sword Zuggling", "abbr": "MSZ", "date": "2023-11-06", "tags": ["zuggling", "desync", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./master-sword-zuggling-decayed-master-sword-zuggling.md"}, {"name": "Memory Buffering", "abbr": "MB", "date": "2023-05-29", "tags": ["menu", "buff"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./memory-buffering.md"}, {"name": "Memory Interrupt", "abbr": "MI", "date": "2024-10-01", "tags": ["Unknown"], "versions": ["1.0.0"], "credits": ["mulberry"], "href": "./memory-interrupt.md"}, {"name": "Menu Overload", "abbr": "MO", "date": "2024-01-11", "tags": ["oob", "menu", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./menu-overload.md"}, {"name": "Message Not Found", "abbr": "MNF", "date": "2023-05-17", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Abahbob"], "href": "./message-not-found-mnf.md"}, {"name": "Midair Item Transmutation", "abbr": "MIT", "date": "2023-05-20", "tags": ["item", "paraglide", "zuggling"], "versions": ["1.1.0", "1.1.1"], "credits": ["eXe"], "href": "./midair-item-transmutation-mit.md"}, {"name": "Midair Sort Duplication", "abbr": "MSD", "date": "2023-05-21", "tags": ["duplication", "menu", "item", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zas", "kurocat471"], "href": "./midair-sort-duplication-msd.md"}, {"name": "Midair Throw Duplication", "abbr": "MTD", "date": "2023-07-02", "tags": ["duplication", "item", "zonai", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["quantim"], "href": "./midair-throw-duplication-mtd.md"}, {"name": "Minecart Rail Collision Launching", "abbr": "MRCL", "date": "2023-05-18", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüØÒéë-ÒüòÒéô"], "href": "./minecart-rail-collision-launching-mrcl.md"}, {"name": "Mineru Ability Desync", "abbr": "MAD", "date": "2023-05-30", "tags": ["desync", "mineru"], "versions": ["1.1.0", "1.1.1"], "credits": ["Sillicat"], "href": "./mineru-ability-desync.md"}, {"name": "Mineru Aim Permanence", "abbr": "MAIP", "date": "Unknown", "tags": ["mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./mineru-aim-permanence.md"}, {"name": "Mineru Cull Storage", "abbr": "MCS", "date": "2025-11-09", "tags": ["zuggling", "storage", "culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["ofstrings2"], "href": "./mineru-cull-storage.md"}, {"name": "Mineru Culling", "abbr": "MC", "date": "2023-07-31", "tags": ["culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./mineru-culling.md"}, {"name": "Mineru Fuse Entanglement", "abbr": "MFE", "date": "2023-10-18", "tags": ["entanglement", "culling", "ultrahand", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "WinnerBoi77"], "href": "./mineru-fuse-entanglement-mineru-fe.md"}, {"name": "Mineru Hold Smuggle", "abbr": "MHS", "date": "2023-12-20", "tags": ["zuggling", "menu", "item", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./mineru-hold-smuggle-mhs.md"}, {"name": "Mineru Persistent Save Load Object Transfer", "abbr": "MPSLOT", "date": "2024-07-27", "tags": ["equipment", "culling", "save-load", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry", "Armindo", "Emiya"], "href": "./mineru-persistent-save-load-object-transfer.md"}, {"name": "Mineru Text Storage", "abbr": "MTS", "date": "2024-07-11", "tags": ["storage", "mineru"], "versions": ["1.0.0"], "credits": ["CM30"], "href": "./mineru-text-storage.md"}, {"name": "MNF Fusing", "abbr": "MNFF", "date": "2023-06-05", "tags": ["fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./mnf-fusing.md"}, {"name": "MNF Glow Overload", "abbr": "MGO", "date": "2025-01-03", "tags": ["item", "overload", "mnf"], "versions": ["1.0.0"], "credits": ["Toti Sauce"], "href": "./mnf-glow-overload.md"}, {"name": "MNF Zuggle Fuse", "abbr": "MZF", "date": "2023-05-18", "tags": ["zuggling", "weapon", "fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./mnf-zuggle-fuse.md"}, {"name": "Model Teleport Desync", "abbr": "MTEL", "date": "2023-07-29", "tags": ["desync", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./model-teleport-desync.md"}, {"name": "Modifier Deletion Weapon State Transfer", "abbr": "MDWST", "date": "Unknown", "tags": ["duplication", "weapon"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md"}, {"name": "Modifier ONLY Transfer", "abbr": "MOT", "date": "2023-06-09", "tags": ["weapon"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "BigDUCCO"], "href": "./modifier-only-transfer.md"}, {"name": "Moobe Warping", "abbr": "MW", "date": "2024-01-12", "tags": ["oob", "warping", "movement", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./moobe-warping.md"}, {"name": "Mount Lock", "abbr": "ML", "date": "2023-05-21", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./mount-lock.md"}, {"name": "Mozdor Jumping/Slashing", "abbr": "MJS", "date": "2023-05-20", "tags": ["movement", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "AgdoR"], "href": "./mozdor-jumping-slashing.md"}, {"name": "MSNF glowing", "abbr": "MG", "date": "2023-08-02", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["evilgabe"], "href": "./msnf-glowing.md"}, {"name": "Mulberry's Out of Body Experience", "abbr": "MOOBE", "date": "2024-01-06", "tags": ["warping", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./mulberry-s-out-of-body-experience-moobe.md"}, {"name": "New Item Desync", "abbr": "NID", "date": "2023-05-12", "tags": ["duplication", "desync", "menu", "item", "equipment", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Modoki_returns"], "href": "./new-item-desync-equipment-duping.md"}, {"name": "No Bow Sprinting", "abbr": "NBS", "date": "2023-05-12", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./no-bow-sprinting-nbs.md"}, {"name": "Null Dropping", "abbr": "ND", "date": "2024-03-16", "tags": ["menu", "item", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl"], "href": "./null-dropping.md"}, {"name": "Object Culling", "abbr": "OC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "tori", "mulberry", "Timber"], "href": "./object-culling.md"}, {"name": "Object (Moe) Enlargement", "abbr": "MOE", "date": "2024-10-30", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "PetitFrapo", "Jordan"], "href": "./object-moe-enlargement.md"}, {"name": "Ocklusion Hovering", "abbr": "OCKH", "date": "2025-10-12", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic"], "href": "./ocklusion-hovering.md"}, {"name": "Ocklusion", "abbr": "OCKL", "date": "2024-05-29", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./ocklusion.md"}, {"name": "Octo-balloon Detanglement", "abbr": "OBD", "date": "2025-11-16", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./octo-balloon-detanglement.md"}, {"name": "Octodupe", "abbr": "OD", "date": "2023-05-26", "tags": ["duplication", "item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./octodupe.md"}, {"name": "Overload at Home", "abbr": "OAH", "date": "2024-03-20", "tags": ["zuggling", "culling", "overload"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./overload-at-home-aka-pickup-overload.md"}, {"name": "Overload Cold Fuse", "abbr": "OCF", "date": "2023-07-23", "tags": ["item", "weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["F. Buffalo"], "href": "./overload-cold-fuse.md"}, {"name": "Overload Drop Smuggling", "abbr": "ODS", "date": "2023-06-12", "tags": ["zuggling", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ChargeVolt", "Windocks"], "href": "./overload-drop-smuggling.md"}, {"name": "Overload Dynamic Zuggle", "abbr": "ODZ", "date": "2025-05-19", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./overload-dynamic-zuggle.md"}, {"name": "Overload Fuse Entanglement", "abbr": "OFE", "date": "2024-07-23", "tags": ["zuggling", "entanglement", "culling", "overload", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./overload-fuse-entanglement.md"}, {"name": "Overload Persistent Save Load Object Transfer", "abbr": "OPSLOT", "date": "2024-07-26", "tags": ["overload", "save-load"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./overload-persistent-save-load-object-transfer.md"}, {"name": "Pelison Duping", "abbr": "PD", "date": "2023-05-25", "tags": ["duplication", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["AngryEgg", "BigDUCCO"], "href": "./pelison-duping.md"}, {"name": "Persistent Save Load Object Transfer", "abbr": "PSLOT", "date": "2024-01-25", "tags": ["culling", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./persistent-save-load-object-transfer-pslot.md"}, {"name": "Pickup Smuggling", "abbr": "PSMU", "date": "2023-05-28", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ame"], "href": "./pickup-smuggling.md"}, {"name": "Pocket Rocket", "abbr": "PR", "date": "2023-06-15", "tags": ["launching", "equipment", "paraglide", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "SmallAnt"], "href": "./pocket-rocket.md"}, {"name": "Portable Cull Save Load Dupe", "abbr": "PSLD", "date": "2024-07-17", "tags": ["duplication", "culling", "save-load"], "versions": ["1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./portable-cull-save-load-dupe-portacull-sld.md"}, {"name": "Portable Culling", "abbr": "PCULL", "date": "2024-02-27", "tags": ["zuggling", "desync", "item", "culling", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./portable-culling.md"}, {"name": "Portacull Invismuggle", "abbr": "PCI", "date": "2024-02-29", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./portacull-invismuggle.md"}, {"name": "Weapon Despawn Prevention", "abbr": "WDP", "date": "2023-06-28", "tags": ["weapon", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./prevent-weapon-despawn.md"}, {"name": "Prologue Escape", "abbr": "PE", "date": "2024-10-01", "tags": ["duplication", "storage"], "versions": ["1.0.0"], "credits": ["LegendofLinkk", "mulberry", "Aergyl", "Lightos", "EOH_NS_SS"], "href": "./prologue-escape.md"}, {"name": "Proxy Glitches", "abbr": "PG", "date": "Unknown", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./proxy-glitches.md"}, {"name": "Purgatory Save Load Dupe", "abbr": "PGSLD", "date": "2024-02-11", "tags": ["duplication", "equipment", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./purgatory-save-load-dupe.md"}, {"name": "Pyroculling", "abbr": "PYR", "date": "2023-11-17", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.2.0"], "credits": ["ROBUXY2ND"], "href": "./pyroculling.md"}, {"name": "Quantum Linking", "abbr": "QL", "date": "2023-08-30", "tags": ["culling", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "pyuk"], "href": "./quantum-linking-ql.md"}, {"name": "Quick Drop Smuggle", "abbr": "QDS", "date": "2024-03-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0"], "credits": ["mulberry", "Zas", "Aeolian", "WinnerBoi77", "Ryan?"], "href": "./quick-drop-smuggle-qds.md"}, {"name": "Quick Smuggling", "abbr": "QS", "date": "2023-07-10", "tags": ["zuggling", "equipment", "arrow"], "versions": ["1.2.0"], "credits": ["Suishi"], "href": "./quick-smuggling.md"}, {"name": "Reball", "abbr": "RBL", "date": "2023-07-06", "tags": ["movement", "recall", "zonai"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./reball.md"}, {"name": "Recall Cancel", "abbr": "RCC", "date": "2023-07-20", "tags": ["animation", "item", "recall"], "versions": ["1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./recall-cancel.md"}, {"name": "Recall Clip", "abbr": "RC", "date": "2023-05-16", "tags": ["clipping", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüôÒéôÒüØÒéü"], "href": "./recall-clip.md"}, {"name": "Recall Drop Stacking", "abbr": "RDS", "date": "2025-01-04", "tags": ["item", "recall", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Telkic", "mulberry"], "href": "./recall-drop-stacking.md"}, {"name": "Recall Launch", "abbr": "RL", "date": "2023-05-17", "tags": ["launching", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deep"], "href": "./recall-launch.md"}, {"name": "Recall Locking", "abbr": "RLK", "date": "2023-06-11", "tags": ["recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./recall-locking.md"}, {"name": "Recall Sluggle", "abbr": "RSL", "date": "2025-07-12", "tags": ["zuggling", "menu", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["WinnerBoi77"], "href": "./recall-sluggle.md"}, {"name": "Recipe Storage", "abbr": "RS", "date": "2024-09-14", "tags": ["storage", "menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./recipe-storage.md"}, {"name": "Remote Arrow", "abbr": "RAT", "date": "2023-06-02", "tags": ["arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Flash", "ElDuende", "kirigaya"], "href": "./remote-arrow-trap.md"}, {"name": "Replacement Actor Fuse Entanglement", "abbr": "RAFE", "date": "2024-11-09", "tags": ["entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["dt13269", "mulberry"], "href": "./replacement-actor-fuse-entanglement.md"}, {"name": "Resync Fuse Entanglement", "abbr": "RFE", "date": "2023-12-18", "tags": ["item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./resync-fuse-entanglement-resync-fe.md"}, {"name": "Reverse Ascend Storage", "abbr": "RAS", "date": "2023-11-27", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Redrooey"], "href": "./reverse-ascend-storage.md"}, {"name": "Sage Madness", "abbr": "SM", "date": "2023-07-18", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aci"], "href": "./sage-madness.md"}, {"name": "Sage Recycling", "abbr": "SRCY", "date": "2023-05-28", "tags": ["duplication", "tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Knight7108", "Candlelor"], "href": "./sage-recycling.md"}, {"name": "Save Load Dupe", "abbr": "SLD", "date": "2023-05-16", "tags": ["duplication", "equipment", "save-load", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ZombieBoy225", "ness", "ElDuende"], "href": "./save-load-dupe-sld.md"}, {"name": "Save Load Zuggling", "abbr": "SLZ", "date": "2023-05-23", "tags": ["zuggling", "save-load", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["NicNac", "Flash", "BigDUCCO", "Wip long sticks enjoyer"], "href": "./save-load-zuggling-slz.md"}, {"name": "Scope Render Cancel", "abbr": "SRC", "date": "2023-05-19", "tags": ["animation", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "eXe"], "href": "./scope-render-cancel.md"}, {"name": "Shadow/Void Icons", "abbr": "SVI", "date": "2024-10-16", "tags": ["equipment", "fuse", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Lightos", "PetitFrapo"], "href": "./shadow-void-icons.md"}, {"name": "Shock Cold Fuse", "abbr": "SCF", "date": "2023-09-11", "tags": ["weapon", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-cold-fuse.md"}, {"name": "Shock Effect Overload", "abbr": "SEO", "date": "2023-07-26", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "R4000"], "href": "./shock-effect-overload-seo.md"}, {"name": "Shock Fuse Entanglement", "abbr": "SFE", "date": "2023-09-12", "tags": ["zuggling", "item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-fuse-entanglement.md"}, {"name": "Shock Smuggle", "abbr": "SSMU", "date": "2023-06-01", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["sleepyppls"], "href": "./shock-smuggle.md"}, {"name": "Shrunken Actors", "abbr": "SA", "date": "2025-10-26", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./shrunken-actors.md"}, {"name": "Slate Storage", "abbr": "SLST", "date": "2024-09-21", "tags": ["storage", "damage"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk"], "href": "./slate-storage.md"}, {"name": "Slugging", "abbr": "SLG", "date": "2023-06-15", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./slugging.md"}, {"name": "Smuggle Retrieval", "abbr": "SRET", "date": "2024-12-18", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["PetitFrapo"], "href": "./smuggle-retrieval.md"}, {"name": "Smuggle Stacking Zuggle", "abbr": "SSZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "LegendofLinkk", "Mozz"], "href": "./smuggle-stacking-zuggle-ssz.md"}, {"name": "Split Item Duplication", "abbr": "SID", "date": "2025-06-19", "tags": ["duplication", "item", "zuggling"], "versions": ["1.2.0"], "credits": ["Telkic", "mulberry", "WinnerBoi77"], "href": "./split-item-duplication-sid.md"}, {"name": "Spring Fall Damage Cancel", "abbr": "SFDC", "date": "2023-05-15", "tags": ["animation", "damage", "movement", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./spring-fall-damage-cancel.md"}, {"name": "Spring Strangeness", "abbr": "STRS", "date": "2023-05-15", "tags": ["spring", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi", "Owen"], "href": "./spring-strangeness.md"}, {"name": "Springboard Clipping", "abbr": "SBC", "date": "2023-05-27", "tags": ["clipping", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ab2x3z"], "href": "./springboard-clipping.md"}, {"name": "Springboarding", "abbr": "SBRD", "date": "2023-05-24", "tags": ["equipment", "shield", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springboarding.md"}, {"name": "Springdolling", "abbr": "SDOL", "date": "2023-05-15", "tags": ["launching", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springdolling.md"}, {"name": "Stack Splitting", "abbr": "SSPL", "date": "2024-12-31", "tags": ["item", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["s0ft", "Telkic", "mulberry"], "href": "./stack-splitting.md"}, {"name": "Stamina Depletion Freeze", "abbr": "SDF", "date": "2023-05-20", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./stamina-depletion-freeze-sdf.md"}, {"name": "Stick Desync Clip", "abbr": "SDC", "date": "2023-07-01", "tags": ["clipping", "desync", "item", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "DisguisedMoth"], "href": "./stick-desync-clip-sdc.md"}, {"name": "Sticky Dynamic Purgatory", "abbr": "SDP", "date": "2024-02-15", "tags": ["equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./sticky-dynamic-purgatory.md"}, {"name": "Super Bomb Jump", "abbr": "SBJ", "date": "2023-09-14", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["FerrusCube", "Aergyl"], "href": "./super-bomb-jump.md"}, {"name": "Super Fuse Overload", "abbr": "SFO", "date": "2025-12-06", "tags": ["weapon", "overload", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Aergyl", "Jordan", "MandelbrotChaylay"], "href": "./super-fuse-overload.md"}, {"name": "Surf storage", "abbr": "SSTR", "date": "2023-09-22", "tags": ["storage"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./surf-storage.md"}, {"name": "Swap Resync Zuggle", "abbr": "SRZ", "date": "2025-08-11", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry", "MandelbrotChaylay"], "href": "./swap-resync-zuggle-srz.md"}, {"name": "Swap Resync", "abbr": "SR", "date": "2025-08-10", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["MandelbrotChaylay"], "href": "./swap-resync.md"}, {"name": "Temporary Devices", "abbr": "TD", "date": "2024-11-30", "tags": ["fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./temporary-devices.md"}, {"name": "Texture Tearing", "abbr": "TT", "date": "2024-01-13", "tags": ["oob", "menu", "equipment", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./texture-tearing.md"}, {"name": "Throken", "abbr": "THK", "date": "2025-05-17", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikaboze"], "href": "./throken.md"}, {"name": "Throw Cancelling", "abbr": "TC", "date": "Unknown", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Quelfth"], "href": "./throw-cancelling.md"}, {"name": "Throw Tap Sprinting", "abbr": "TTS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer", "Tauktes"], "href": "./throw-tap-sprinting-tts.md"}, {"name": "Throwless Storage", "abbr": "THS", "date": "2023-06-19", "tags": ["storage", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["evilgabe", "NX721"], "href": "./throwless-storage-previously-known-as-beam-storage.md"}, {"name": "Time Bomb cancel", "abbr": "TBC", "date": "2023-11-04", "tags": ["animation", "equipment", "damage", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["tzakazuki"], "href": "./time-bomb-cancel.md"}, {"name": "Toti Saucery", "abbr": "TOTS", "date": "2024-08-17", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "Telkic"], "href": "./toti-saucery.md"}, {"name": "Travel Medallion storage", "abbr": "TMS", "date": "2023-06-16", "tags": ["storage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kirigaya"], "href": "./travel-medallion-storage-tms.md"}, {"name": "Tulin Pumping", "abbr": "TP", "date": "2023-05-14", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikkitrix"], "href": "./tulin-pumping.md"}, {"name": "Two Handed With Shield", "abbr": "THWS", "date": "2023-08-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Bucket_Sloe"], "href": "./two-handed-with-shield.md"}, {"name": "Ultimate Pocket Rocket", "abbr": "UPR", "date": "2025-05-20", "tags": ["launching", "warping", "ultrahand"], "versions": ["1.0.0"], "credits": ["Aergyl", "mulberry", "Ikaboze", "Jordan"], "href": "./ultimate-pocket-rocket.md"}, {"name": "Ultra Save Load Object Transfer", "abbr": "USLOT", "date": "2024-02-15", "tags": ["save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./ultra-save-load-object-transfer.md"}, {"name": "Ultrabroken Smuggling", "abbr": "UBS", "date": "2023-06-13", "tags": ["zuggling", "equipment", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["The_Andromeda"], "href": "./ultrabroken-smuggling-ubs.md"}, {"name": "Ultrabroken", "abbr": "UB", "date": "2023-05-29", "tags": ["item", "ultrahand", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Duncan"], "href": "./ultrabroken.md"}, {"name": "Unload Duping", "abbr": "UD", "date": "2023-05-31", "tags": ["duplication", "item", "culling", "fuse", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª", "ÕìâÕ╣┤ÞîÂÚÑ╝"], "href": "./unload-duping.md"}, {"name": "Unload WST", "abbr": "UWST", "date": "Unknown", "tags": ["item", "culling", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "Vee.Might.Exist", "Syb"], "href": "./unload-wst.md"}, {"name": "Unsheathed Mastersword", "abbr": "UMS", "date": "2023-07-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "DanielNeia"], "href": "./unsheathed-mastersword.md"}, {"name": "Vendor Scamming", "abbr": "VS", "date": "2023-07-03", "tags": ["zuggling", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "Mozz", "NaN Gogh"], "href": "./vendor-scamming.md"}, {"name": "Void Dipping", "abbr": "VD", "date": "2025-12-29", "tags": ["item", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Squidwest", "mulberry", "Aergyl"], "href": "./void-dipping.md"}, {"name": "Void Hold Storage", "abbr": "VHS", "date": "2023-07-22", "tags": ["storage", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "NX721"], "href": "./void-hold-storage.md"}, {"name": "Void Holding", "abbr": "VH", "date": "2023-06-10", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Lightos"], "href": "./void-holding.md"}, {"name": "Wacko Attacko", "abbr": "WATK", "date": "2024-01-21", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3", "WinnerBoi77"], "href": "./wacko-attacko.md"}, {"name": "Warp Bumping", "abbr": "WB", "date": "2023-06-07", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Mozz", "InAMuffinCup"], "href": "./warp-bumping.md"}, {"name": "Weapon Dash GAS", "abbr": "WDGAS", "date": "2025-11-28", "tags": ["gas", "weapon", "culling", "fuse", "zonai"], "versions": ["1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Toti Sauce"], "href": "./weapon-dash-gas.md"}, {"name": "Weapon Extensions", "abbr": "WEXT", "date": "2023-06-20", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deltenic", "Flash", "Zas"], "href": "./weapon-extensions.md"}, {"name": "Weapon Fuse Entangelemt", "abbr": "WFE", "date": "2023-06-01", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ROBUXY2ND", "Physioninja"], "href": "./weapon-fuse-entanglement.md"}, {"name": "Weapon Sheath Offset", "abbr": "WSO", "date": "2023-06-25", "tags": ["zuggling", "weapon", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["circyit", "dash"], "href": "./weapon-sheath-offset-wso.md"}, {"name": "Weapon Stacking Duplication", "abbr": "WSD", "date": "2023-05-16", "tags": ["duplication", "item", "weapon", "equipment", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ErlingÚÖäÞ║½"], "href": "./weapon-stacking-duplication-wsd.md"}, {"name": "Weapon Stand Dynamic Zuggle", "abbr": "WSDZ", "date": "2024-03-14", "tags": ["zuggling", "weapon", "item", "equipment"], "versions": ["1.0.0"], "credits": ["WinnerBoi77"], "href": "./weapon-stand-dynamic-zuggle.md"}, {"name": "Weapon State Transfer", "abbr": "WST", "date": "2023-05-19", "tags": ["weapon", "fuse", "entanglement", "equipment", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "kurocat471", "ElDuende", "Mentor_Kurt"], "href": "./weapon-state-transfer-wst.md"}, {"name": "Weather Amnesia", "abbr": "WA", "date": "2023-06-25", "tags": ["environment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk"], "href": "./weather-amnesia-wa.md"}, {"name": "Wheel Warping", "abbr": "WW", "date": "2023-06-18", "tags": ["launching", "warping", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk"], "href": "./wheel-warping.md"}, {"name": "Wheel Zoomy", "abbr": "WZ", "date": "2023-07-12", "tags": ["movement", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Solo_Turtle"], "href": "./wheel-zoomy-also-known-as-wheel-wacko-boingo.md"}, {"name": "Wireless Energy", "abbr": "WE", "date": "2023-07-11", "tags": ["equipment", "culling", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./wireless-energy.md"}, {"name": "Wuggle", "abbr": "WGL", "date": "2023-12-29", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "ROBUXY2ND"], "href": "./wuggle-weird-zuggle.md"}, {"name": "Yee Fuse Entanglement", "abbr": "YEEFE", "date": "2024-02-20", "tags": ["entanglement", "culling", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee", "mulberry"], "href": "./yee-fuse-entanglement.md"}, {"name": "Zapshield", "abbr": "ZAP", "date": "2024-09-16", "tags": ["equipment", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./zapshield.md"}, {"name": "ZL Animation Reset", "abbr": "ZLAR", "date": "2024-01-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./zl-animation-reset-zlar.md"}, {"name": "Zoggle", "abbr": "ZOG", "date": "2024-01-04", "tags": ["zuggling", "ultrahand", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ryan?", "Ock"], "href": "./zoggle.md"}, {"name": "Zonai Inventory Shift Dupe", "abbr": "ZISD", "date": "2023-07-10", "tags": ["duplication", "menu", "buff", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "quantim"], "href": "./zonai-inventory-shift-dupe-zisd.md"}, {"name": "Zonai Sort Duplication", "abbr": "ZSD", "date": "2023-05-22", "tags": ["duplication", "menu", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Quelfth", "Flash"], "href": "./zonai-sort-duplication-zsd.md"}, {"name": "Zonai Storage", "abbr": "ZS", "date": "2023-08-13", "tags": ["storage", "zonai"], "versions": ["1.0.0"], "credits": ["bebu0815"], "href": "./zonai-storage.md"}, {"name": "Zuggle Load Object Transfering", "abbr": "ZLOT", "date": "2023-06-07", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup", "ChargeVolt"], "href": "./zuggle-load-object-transfering-zlot.md"}, {"name": "Zuggle Overload Desync", "abbr": "ZOD", "date": "Unknown", "tags": ["zuggling", "desync", "menu", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./zuggle-overload-desync.md"}, {"name": "Zuggle Overload Out Of Bounds", "abbr": "ZOOB", "date": "2023-05-18", "tags": ["clipping", "oob", "zuggling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["AngryEgg"], "href": "./zuggle-overload-out-of-bounds.md"}, {"name": "Zuggle Overload", "abbr": "ZO", "date": "2023-05-17", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle-overload.md"}, {"name": "Zuggle", "abbr": "ZGL", "date": "2023-05-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle.md"}]
\ No newline at end of file
diff --git a/docs/wiki/entanglement/entanglement-library.md b/docs/wiki/entanglement/entanglement-library.md
index f3e89aa90..3ca98692c 100644
--- a/docs/wiki/entanglement/entanglement-library.md
+++ b/docs/wiki/entanglement/entanglement-library.md
@@ -10,15 +10,15 @@ This page complies Fuse Entanglement related glitches for quick reference.
 ---
 - [Fuse Entanglement](../glitchcraft/fuse-entanglement.md)
 - [Entanglement Height Glitch](../glitchcraft/entanglement-height-glitch.md)
-- [Fuse Entanglement Desync](../glitchcraft/fuse-entanglement-desync-fed.md)
-- [Fuse Entanglement Clipping](../glitchcraft/fuse-entanglement-clipping-fec.md)
-- [Fuse Storage Fuse Entanglement](../glitchcraft/fuse-storage-fuse-entanglement-fsfe.md)
+- [Fuse Entanglement Desync](../glitchcraft/fuse-entanglement-desync.md)
+- [Fuse Entanglement Clipping](../glitchcraft/fuse-entanglement-clipping.md)
+- [Fuse Storage Fuse Entanglement](../glitchcraft/fuse-storage-fuse-entanglement.md)
 - [Fuse Entanglement Drop Smuggling](../glitchcraft/fuse-entanglement-drop-smuggling.md)
 - [Detanglement](../glitchcraft/detanglement.md)
 - [Cull Fuse Entanglement](../glitchcraft/cull-fuse-entanglement-cull-fe.md)
 - [Mineru Fuse Entanglement](../glitchcraft/mineru-fuse-entanglement-mineru-fe.md)
 - [Resync Fuse Entanglement](../glitchcraft/resync-fuse-entanglement-resync-fe.md)
-- [Persistent Save Load Object Transfer](../glitchcraft/persistent-save-load-object-transfer-pslot.md)
+- [Persistent Save Load Object Transfer](../glitchcraft/persistent-save-load-object-transfer.md)
 - [Ultra Save Load Object Transfer](../glitchcraft/ultra-save-load-object-transfer.md)
 - [Double Shield Desync Clip Fuse Entanglement](../glitchcraft/double-shield-desync-clip-fuse-entanglement-double-sdc-fe.md)
 - [Construct Fuse Entanglement](../glitchcraft/construct-fuse-entanglement.md)
diff --git a/docs/wiki/glitchcraft/weapon-fe.md b/docs/wiki/glitchcraft/weapon-fuse-entanglement.md
similarity index 82%
rename from docs/wiki/glitchcraft/weapon-fe.md
rename to docs/wiki/glitchcraft/weapon-fuse-entanglement.md
index c3c35672a..572b1d5d9 100644
--- a/docs/wiki/glitchcraft/weapon-fe.md
+++ b/docs/wiki/glitchcraft/weapon-fuse-entanglement.md
@@ -1,15 +1,15 @@
 ---
-title: "Weapon FE"
+title: "Weapon Fuse Entangelemt"
 abbreviation: "WFE"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
 credits: ["ROBUXY2ND", "Physioninja"]
 date: "2023-06-01"
-description: "Allows for FE to weapons"
-aliases: ["weapon-fe"]
+description: "Allows for Fuse Entanglement to weapons"
+aliases: ["weapon-fe", "weapon fe"]
 tags: ["weapon"]
 ---
 
-# Weapon FE `WFE`
+# Weapon Fuse Entangelemt `WFE`
 `1.0.0` `1.1.0` `1.1.1` `1.1.2`
 
 ## Summary
diff --git a/docs/wiki/zuggling/zuggle-library.md b/docs/wiki/zuggling/zuggle-library.md
index b9b51ac21..be2ccc9c4 100644
--- a/docs/wiki/zuggling/zuggle-library.md
+++ b/docs/wiki/zuggling/zuggle-library.md
@@ -13,19 +13,19 @@ This page complies Smuggling and Zuggling related glitches for quick reference.
 - [Zuggle Overload](../glitchcraft/zuggle-overload.md)
 - [MNF Zuggle Fuse](../glitchcraft/mnf-zuggle-fuse.md)
 - [Zuggle Overload Out Of Bounds](../glitchcraft/zuggle-overload-out-of-bounds.md)
-- [Map Zuggling (MZ)](../glitchcraft/map-zuggling-mz.md)
-- [Save Load Zuggling (SLZ)](../glitchcraft/save-load-zuggling-slz.md)
+- [Map Zuggling (MZ)](../glitchcraft/map-zuggling.md)
+- [Save Load Zuggling (SLZ)](../glitchcraft/save-load-zuggling.md)
 - [Pickup Smuggling](../glitchcraft/pickup-smuggling.md)
 - [Drop Smuggling](../glitchcraft/drop-smuggling.md)
 - [Equipment Smuggle](../glitchcraft/equipment-smuggle.md)
 - [Shock Smuggle](../glitchcraft/shock-smuggle.md)
 - [Arrow Smuggling](../glitchcraft/arrow-smuggling.md)
-- [Smuggle Stacking Zuggle (SSZ)](../glitchcraft/smuggle-stacking-zuggle-ssz.md)
-- [Drop Delay Zuggle (DDZ)](../glitchcraft/drop-delay-zuggle-ddz.md)
-- [Force Equip Zuggling (FEZ)](../glitchcraft/force-equip-zuggling-fez.md)
-- [Zuggle Load Object Transfering (ZLOT)](../glitchcraft/zuggle-load-object-transfering-zlot.md)
+- [Smuggle Stacking Zuggle (SSZ)](../glitchcraft/smuggle-stacking-zuggle.md)
+- [Drop Delay Zuggle (DDZ)](../glitchcraft/drop-delay-zuggle.md)
+- [Force Equip Zuggling (FEZ)](../glitchcraft/force-equip-zuggling.md)
+- [Zuggle Load Object Transfering (ZLOT)](../glitchcraft/zuggle-load-object-transfering.md)
 - [Overload Drop Smuggling](../glitchcraft/overload-drop-smuggling.md)
-- [Ultrabroken Smuggling (UBS)](../glitchcraft/ultrabroken-smuggling-ubs.md)
+- [Ultrabroken Smuggling (UBS)](../glitchcraft/ultrabroken-smuggling.md)
 - [Like-Like Smuggling](../glitchcraft/like-like-smuggling.md)
 - [Like-Like Drop Smuggling](../glitchcraft/like-like-drop-smuggling.md)
 - [Like-Like Zuggling](../glitchcraft/like-like-zuggling.md)
@@ -34,22 +34,22 @@ This page complies Smuggling and Zuggling related glitches for quick reference.
 - [Cull Smuggle](../glitchcraft/cull-smuggle.md)
 - [Hold Smuggling](../glitchcraft/hold-smuggling.md)
 - [Quick Smuggling](../glitchcraft/quick-smuggling.md)
-- [Hand Locked Equipment Smuggling (HLES)](../glitchcraft/hand-locked-equipment-smuggling-hles.md)
+- [Hand Locked Equipment Smuggling (HLES)](../glitchcraft/hand-locked-equipment-smuggling.md)
 - [Dynamic Zuggle](../glitchcraft/dynamic-zuggle.md)
 - [LikeLike Stick Smuggling](../glitchcraft/likelike-stick-smuggling.md)
 - [Master Sword Zuggling](../glitchcraft/master-sword-zuggling-decayed-master-sword-zuggling.md)
-- [Mineru Hold Smuggle (MHS)](../glitchcraft/mineru-hold-smuggle-mhs.md)
+- [Mineru Hold Smuggle (MHS)](../glitchcraft/mineru-hold-smuggle.md)
 - [Wuggle (Weird Zuggle)](../glitchcraft/wuggle-weird-zuggle.md)
 - [Invizuggle](../glitchcraft/invizuggle.md)
-- [Persistent Save Load Object Transfer (PSLOT)](../glitchcraft/persistent-save-load-object-transfer-pslot.md)
+- [Persistent Save Load Object Transfer (PSLOT)](../glitchcraft/persistent-save-load-object-transfer.md)
 - [Lift Smuggle](../glitchcraft/lift-smuggle.md)
 - [Kilovictor's Quicksmuggle](../glitchcraft/kilovictor-s-quicksmuggle.md)
 - [Portacull Invismuggle](../glitchcraft/portacull-invismuggle.md)
 - [Weapon Stand Dynamic Zuggle](../glitchcraft/weapon-stand-dynamic-zuggle.md)
-- [Quick Drop Smuggle (QDS)](../glitchcraft/quick-drop-smuggle-qds.md)
-- [Chasm Delay Zuggle (CDZ)](../glitchcraft/chasm-delay-zuggle-cdz.md)
+- [Quick Drop Smuggle (QDS)](../glitchcraft/quick-drop-smuggle.md)
+- [Chasm Delay Zuggle (CDZ)](../glitchcraft/chasm-delay-zuggle.md)
 - [Dpadlock-less Invizuggle](../glitchcraft/dpadlock-less-invizuggle.md)
-- [Cull Storage Zuggle (CSZ)](../glitchcraft/cull-storage-zuggle-csz.md)
+- [Cull Storage Zuggle (CSZ)](../glitchcraft/cull-storage-zuggle.md)
 - [Overload Persistent Save Load Object Transfer](../glitchcraft/overload-persistent-save-load-object-transfer.md)
 - [Aeroculling](../glitchcraft/aeroculling.md)
 - [Zapshield](../glitchcraft/zapshield.md)
@@ -61,7 +61,7 @@ This page complies Smuggling and Zuggling related glitches for quick reference.
 - [Cull Pickup Dynamic Zuggle](../glitchcraft/cull-pickup-dynamic-zuggle.md)
 - [Overload Dynamic Zuggle](../glitchcraft/overload-dynamic-zuggle.md)
 - [Ultimate Pocket Rocket (uses zuggle/smuggle)](../glitchcraft/ultimate-pocket-rocket.md)
-- [Double Bypass Zuggle (DBZ)](../glitchcraft/double-bypass-zuggle-dbz.md)
+- [Double Bypass Zuggle (DBZ)](../glitchcraft/double-bypass-zuggle.md)
 - [Recall Sluggle](../glitchcraft/recall-sluggle.md)
 - [Swap Resync](../glitchcraft/swap-resync.md)
 - [Ocklusion Hovering (Pickup Smuggling)](../glitchcraft/ocklusion-hovering.md)
diff --git a/mkdocs.yml b/mkdocs.yml
index 6a3132024..e87cdf813 100644
--- a/mkdocs.yml
+++ b/mkdocs.yml
@@ -88,7 +88,7 @@ nav:
   - Entanglement:
     - Introduction: wiki/entanglement/index.md
     # - Fuse Entanglement: glitchcraft/fuse-entanglement.md
-    # - Fuse Storage Fuse Entanglement: glitchcraft/fuse-storage-fuse-entanglement-fsfe.md
+    # - Fuse Storage Fuse Entanglement: glitchcraft/fuse-storage-fuse-entanglement.md
     # - Cull Fuse Entanglement: glitchcraft/cull-fuse-entanglement-cull-fe.md
     # - Mineru Fuse Entanglement: glitchcraft/mineru-fuse-entanglement-mineru-fe.md
     # - Resync Fuse Entanglement: glitchcraft/resync-fuse-entanglement-resync-fe.md
@@ -96,24 +96,24 @@ nav:
     # - Construct Fuse Entanglement: glitchcraft/construct-fuse-entanglement.md
     # - Overload Fuse Entanglement: glitchcraft/overload-fuse-entanglement.md
     # - Replacement Actor Fuse Entanglement: glitchcraft/replacement-actor-fuse-entanglement.md
-    # - Fuse Overload Fuse Entanglement: glitchcraft/fuse-overload-fuse-entanglement-fofe.md
+    # - Fuse Overload Fuse Entanglement: glitchcraft/fuse-overload-fuse-entanglement.md
     # - Detanglement: glitchcraft/detanglement.md
     # - Collection: entanglement/entanglement-collection.md
   - Zuggling:
     - Introduction: wiki/zuggling/index.md
     # - Zuggle: glitchcraft/zuggle.md
     # - Equipment Collision Zuggle: glitchcraft/equipment-collision-zuggle.md
-    # - Map Zuggling: glitchcraft/map-zuggling-mz.md
-    # - Save Load Zuggling: glitchcraft/save-load-zuggling-slz.md
+    # - Map Zuggling: glitchcraft/map-zuggling.md
+    # - Save Load Zuggling: glitchcraft/save-load-zuggling.md
     # - Pickup Smuggling: glitchcraft/pickup-smuggling.md
     # - Drop Smuggling: glitchcraft/drop-smuggling.md
     # - Equipment Smuggle: glitchcraft/equipment-smuggle.md
     # - Shock Smuggle: glitchcraft/shock-smuggle.md
     # - Arrow Smuggling: glitchcraft/arrow-smuggling.md
-    # - Smuggle Stacking Zuggle: glitchcraft/smuggle-stacking-zuggle-ssz.md
-    # - Drop Delay Zuggle: glitchcraft/drop-delay-zuggle-ddz.md
-    # - Force Equip Zuggling: glitchcraft/force-equip-zuggling-fez.md
-    # - Zuggle Load Object Transfering: glitchcraft/zuggle-load-object-transfering-zlot.md
+    # - Smuggle Stacking Zuggle: glitchcraft/smuggle-stacking-zuggle.md
+    # - Drop Delay Zuggle: glitchcraft/drop-delay-zuggle.md
+    # - Force Equip Zuggling: glitchcraft/force-equip-zuggling.md
+    # - Zuggle Load Object Transfering: glitchcraft/zuggle-load-object-transfering.md
     # - Overload Drop Smuggling: glitchcraft/overload-drop-smuggling.md
     # - Like-Like Smuggling: glitchcraft/like-like-smuggling.md
     # - Like-Like Drop Smuggling: glitchcraft/like-like-drop-smuggling.md
@@ -122,26 +122,26 @@ nav:
     # - Cull Smuggle: glitchcraft/cull-smuggle.md
     # - Hold Smuggling: glitchcraft/hold-smuggling.md
     # - Quick Smuggling: glitchcraft/quick-smuggling.md
-    # - Hand Locked Equipment Smuggling: glitchcraft/hand-locked-equipment-smuggling-hles.md
+    # - Hand Locked Equipment Smuggling: glitchcraft/hand-locked-equipment-smuggling.md
     # - Dynamic Zuggle: glitchcraft/dynamic-zuggle.md
     # - LikeLike Stick Smuggling: glitchcraft/likelike-stick-smuggling.md
     # - Master Sword Zuggling: glitchcraft/master-sword-zuggling-decayed-master-sword-zuggling.md
-    # - Mineru Hold Smuggle: glitchcraft/mineru-hold-smuggle-mhs.md
+    # - Mineru Hold Smuggle: glitchcraft/mineru-hold-smuggle.md
     # - Wuggle: glitchcraft/wuggle-weird-zuggle.md
     # - Invizuggle: glitchcraft/invizuggle.md
     # - Lift Smuggle: glitchcraft/lift-smuggle.md
     # - Kilovictor's Quicksmuggle: glitchcraft/kilovictor-s-quicksmuggle.md
     # - Portacull Invismuggle: glitchcraft/portacull-invismuggle.md
     # - Weapon Stand Dynamic Zuggle: glitchcraft/weapon-stand-dynamic-zuggle.md
-    # - Quick Drop Smuggle: glitchcraft/quick-drop-smuggle-qds.md
-    # - Chasm Delay Zuggle: glitchcraft/chasm-delay-zuggle-cdz.md
+    # - Quick Drop Smuggle: glitchcraft/quick-drop-smuggle.md
+    # - Chasm Delay Zuggle: glitchcraft/chasm-delay-zuggle.md
     # - Dpadlock-less Invizuggle: glitchcraft/dpadlock-less-invizuggle.md
-    # - Cull Storage Zuggle: glitchcraft/cull-storage-zuggle-csz.md
+    # - Cull Storage Zuggle: glitchcraft/cull-storage-zuggle.md
     # - Smuggle Retrieval: glitchcraft/smuggle-retrieval.md
     # - Dynamic Purgatory Zuggle: glitchcraft/dynamic-purgatory-zuggle.md
     # - Cull Pickup Dynamic Zuggle: glitchcraft/cull-pickup-dynamic-zuggle.md
     # - Overload Dynamic Zuggle: glitchcraft/overload-dynamic-zuggle.md
-    # - Double Bypass Zuggle: glitchcraft/double-bypass-zuggle-dbz.md
+    # - Double Bypass Zuggle: glitchcraft/double-bypass-zuggle.md
     # - Zuggle Overload Desync: glitchcraft/zuggle-overload-desync.md
     # - Collection: zuggling/zuggle-collection.md
   - Desync: wiki/desync/index.md

----

*** COMMIT: 7b45d5e2ee185879ac4cd31f38678768b5ee6a0d
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 14:04:43 2026 +0100
Subject: fix: remove abbreviations from zuggling documentation for clarity

commit 7b45d5e2ee185879ac4cd31f38678768b5ee6a0d
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 14:04:43 2026 +0100

    fix: remove abbreviations from zuggling documentation for clarity

diff --git a/docs/wiki/zuggling/zuggle-library.md b/docs/wiki/zuggling/zuggle-library.md
index be2ccc9c4..fdcf6bc80 100644
--- a/docs/wiki/zuggling/zuggle-library.md
+++ b/docs/wiki/zuggling/zuggle-library.md
@@ -13,57 +13,57 @@ This page complies Smuggling and Zuggling related glitches for quick reference.
 - [Zuggle Overload](../glitchcraft/zuggle-overload.md)
 - [MNF Zuggle Fuse](../glitchcraft/mnf-zuggle-fuse.md)
 - [Zuggle Overload Out Of Bounds](../glitchcraft/zuggle-overload-out-of-bounds.md)
-- [Map Zuggling (MZ)](../glitchcraft/map-zuggling.md)
-- [Save Load Zuggling (SLZ)](../glitchcraft/save-load-zuggling.md)
+- [Map Zuggling](../glitchcraft/map-zuggling.md)
+- [Save Load Zuggling](../glitchcraft/save-load-zuggling.md)
 - [Pickup Smuggling](../glitchcraft/pickup-smuggling.md)
 - [Drop Smuggling](../glitchcraft/drop-smuggling.md)
 - [Equipment Smuggle](../glitchcraft/equipment-smuggle.md)
 - [Shock Smuggle](../glitchcraft/shock-smuggle.md)
 - [Arrow Smuggling](../glitchcraft/arrow-smuggling.md)
-- [Smuggle Stacking Zuggle (SSZ)](../glitchcraft/smuggle-stacking-zuggle.md)
-- [Drop Delay Zuggle (DDZ)](../glitchcraft/drop-delay-zuggle.md)
-- [Force Equip Zuggling (FEZ)](../glitchcraft/force-equip-zuggling.md)
-- [Zuggle Load Object Transfering (ZLOT)](../glitchcraft/zuggle-load-object-transfering.md)
+- [Smuggle Stacking Zuggle](../glitchcraft/smuggle-stacking-zuggle.md)
+- [Drop Delay Zuggle](../glitchcraft/drop-delay-zuggle.md)
+- [Force Equip Zuggling](../glitchcraft/force-equip-zuggling.md)
+- [Zuggle Load Object Transfering](../glitchcraft/zuggle-load-object-transfering.md)
 - [Overload Drop Smuggling](../glitchcraft/overload-drop-smuggling.md)
-- [Ultrabroken Smuggling (UBS)](../glitchcraft/ultrabroken-smuggling.md)
+- [Ultrabroken Smuggling](../glitchcraft/ultrabroken-smuggling.md)
 - [Like-Like Smuggling](../glitchcraft/like-like-smuggling.md)
 - [Like-Like Drop Smuggling](../glitchcraft/like-like-drop-smuggling.md)
 - [Like-Like Zuggling](../glitchcraft/like-like-zuggling.md)
-- [Like-Like Smuggle Desync (LSD)](../glitchcraft/like-like-smuggle-desync-lsd.md)
+- [Like-Like Smuggle Desync](../glitchcraft/like-like-smuggle-desync-lsd.md)
 - [Drop Zuggle](../glitchcraft/drop-zuggle.md)
 - [Cull Smuggle](../glitchcraft/cull-smuggle.md)
 - [Hold Smuggling](../glitchcraft/hold-smuggling.md)
 - [Quick Smuggling](../glitchcraft/quick-smuggling.md)
-- [Hand Locked Equipment Smuggling (HLES)](../glitchcraft/hand-locked-equipment-smuggling.md)
+- [Hand Locked Equipment Smuggling](../glitchcraft/hand-locked-equipment-smuggling.md)
 - [Dynamic Zuggle](../glitchcraft/dynamic-zuggle.md)
 - [LikeLike Stick Smuggling](../glitchcraft/likelike-stick-smuggling.md)
 - [Master Sword Zuggling](../glitchcraft/master-sword-zuggling-decayed-master-sword-zuggling.md)
-- [Mineru Hold Smuggle (MHS)](../glitchcraft/mineru-hold-smuggle.md)
-- [Wuggle (Weird Zuggle)](../glitchcraft/wuggle-weird-zuggle.md)
+- [Mineru Hold Smuggle](../glitchcraft/mineru-hold-smuggle.md)
+- [Wuggle](../glitchcraft/wuggle-weird-zuggle.md)
 - [Invizuggle](../glitchcraft/invizuggle.md)
-- [Persistent Save Load Object Transfer (PSLOT)](../glitchcraft/persistent-save-load-object-transfer.md)
+- [Persistent Save Load Object Transfer](../glitchcraft/persistent-save-load-object-transfer.md)
 - [Lift Smuggle](../glitchcraft/lift-smuggle.md)
 - [Kilovictor's Quicksmuggle](../glitchcraft/kilovictor-s-quicksmuggle.md)
 - [Portacull Invismuggle](../glitchcraft/portacull-invismuggle.md)
 - [Weapon Stand Dynamic Zuggle](../glitchcraft/weapon-stand-dynamic-zuggle.md)
-- [Quick Drop Smuggle (QDS)](../glitchcraft/quick-drop-smuggle.md)
-- [Chasm Delay Zuggle (CDZ)](../glitchcraft/chasm-delay-zuggle.md)
+- [Quick Drop Smuggle](../glitchcraft/quick-drop-smuggle.md)
+- [Chasm Delay Zuggle](../glitchcraft/chasm-delay-zuggle.md)
 - [Dpadlock-less Invizuggle](../glitchcraft/dpadlock-less-invizuggle.md)
-- [Cull Storage Zuggle (CSZ)](../glitchcraft/cull-storage-zuggle.md)
+- [Cull Storage Zuggle](../glitchcraft/cull-storage-zuggle.md)
 - [Overload Persistent Save Load Object Transfer](../glitchcraft/overload-persistent-save-load-object-transfer.md)
 - [Aeroculling](../glitchcraft/aeroculling.md)
 - [Zapshield](../glitchcraft/zapshield.md)
 - [Object MOE Enlargement](../glitchcraft/object-moe-enlargement.md)
-- [Temporary Devices (uses Quick Smuggled shields)](../glitchcraft/temporary-devices.md)
+- [Temporary Devices](../glitchcraft/temporary-devices.md)
 - [Smuggle Retrieval](../glitchcraft/smuggle-retrieval.md)
 - [Dynamic Purgatory Zuggle](../glitchcraft/dynamic-purgatory-zuggle.md)
 - [Sticky Dynamic Purgatory](../glitchcraft/sticky-dynamic-purgatory.md)
 - [Cull Pickup Dynamic Zuggle](../glitchcraft/cull-pickup-dynamic-zuggle.md)
 - [Overload Dynamic Zuggle](../glitchcraft/overload-dynamic-zuggle.md)
-- [Ultimate Pocket Rocket (uses zuggle/smuggle)](../glitchcraft/ultimate-pocket-rocket.md)
-- [Double Bypass Zuggle (DBZ)](../glitchcraft/double-bypass-zuggle.md)
+- [Ultimate Pocket Rocket](../glitchcraft/ultimate-pocket-rocket.md)
+- [Double Bypass Zuggle](../glitchcraft/double-bypass-zuggle.md)
 - [Recall Sluggle](../glitchcraft/recall-sluggle.md)
 - [Swap Resync](../glitchcraft/swap-resync.md)
-- [Ocklusion Hovering (Pickup Smuggling)](../glitchcraft/ocklusion-hovering.md)
-- [Void Dipping (effects mention smuggle/zuggle)](../glitchcraft/void-dipping.md)
+- [Ocklusion Hovering](../glitchcraft/ocklusion-hovering.md)
+- [Void Dipping](../glitchcraft/void-dipping.md)
 - [Zuggle Overload Desync](../glitchcraft/zuggle-overload-desync.md)

----

*** COMMIT: c92ea6c20b3028238df72b79939d1dc3bcd63320
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 14:26:45 2026 +0100
Subject: Remove leaderboard data file, add synonyms JSON, update build script to exclude correct grimoire page, and adjust import path for synonyms in worker script.

commit c92ea6c20b3028238df72b79939d1dc3bcd63320
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 14:26:45 2026 +0100

    Remove leaderboard data file, add synonyms JSON, update build script to exclude correct grimoire page, and adjust import path for synonyms in worker script.

diff --git a/.github/workflows/embeddings.yml b/.github/workflows/embeddings.yml
index c7d74f5e0..06b7b9d43 100644
--- a/.github/workflows/embeddings.yml
+++ b/.github/workflows/embeddings.yml
@@ -76,7 +76,12 @@ jobs:
       - name: Build BM25 index
         if: ${{ steps.docs_hash.outputs.skip == 'false' }}
         run: |
-          python docs/wiki/build_bm25_index.py --docs-dir docs/wiki --output site/wiki_index.json --gzip
+          python docs/wiki/build_bm25_index.py \
+            --docs-dir docs/wiki \
+            --output site/wiki_index.json \
+            --grimoire-output site/assets/data/grimoire-data.json \
+            --leaderboard-output site/assets/data/leaderboard-data.json \
+            --gzip
           echo "${{ hashFiles('docs/wiki/**') }}" > site/wiki_index.hash
 
       - name: Gzip index and size-check
diff --git a/docs/assets/data/grimoire-data.json b/docs/assets/data/grimoire-data.json
deleted file mode 100644
index 66ef83a26..000000000
--- a/docs/assets/data/grimoire-data.json
+++ /dev/null
@@ -1 +0,0 @@
-[{"name": "Grimoire of Glitchcraft", "abbr": "", "date": "", "tags": [], "versions": [], "credits": [], "href": "./_glitchcraft-grimoire.md"}, {"name": "Ability Wheel Loop", "abbr": "AWL", "date": "2024-03-11", "tags": ["menu", "ultrahand", "zonai"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./ability-wheel-loop.md"}, {"name": "Aeroculling", "abbr": "AC", "date": "2024-08-11", "tags": ["equipment", "culling", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./aeroculling.md"}, {"name": "Animation Swap", "abbr": "ASWP", "date": "2023-05-17", "tags": ["zuggling", "animation", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Swinginman"], "href": "./animation-swap.md"}, {"name": "Anti-gravity GAS", "abbr": "AGAS", "date": "2025-01-22", "tags": ["gas"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./anti-gravity-gas.md"}, {"name": "Anti-Gravity Glitch", "abbr": "AGG", "date": "2023-05-13", "tags": ["paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Kaldemar"], "href": "./anti-gravity-glitch.md"}, {"name": "Anti-Gravity Objects", "abbr": "AGO", "date": "Unknown", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./anti-gravity-objects.md"}, {"name": "AntiGrav Weapons", "abbr": "AGW", "date": "2023-05-28", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Blize"], "href": "./antigrav-weapons.md"}, {"name": "Arrow Prompt Storage", "abbr": "APS", "date": "2023-10-04", "tags": ["storage", "culling", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NghtmaR3"], "href": "./arrow-prompt-storage-aps.md"}, {"name": "Arrow Smuggling", "abbr": "ASMU", "date": "2023-06-04", "tags": ["zuggling", "equipment", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./arrow-smuggling.md"}, {"name": "Arrow Unlink", "abbr": "AUL", "date": "2023-10-26", "tags": ["fuse", "arrow"], "versions": ["1.0.0"], "credits": ["R4000"], "href": "./arrow-unlink.md"}, {"name": "Arrow Unloading", "abbr": "AU", "date": "2023-06-18", "tags": ["culling", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk", "Zas"], "href": "./arrow-unloading.md"}, {"name": "Ascend Camera Glitch", "abbr": "ACG", "date": "Unknown", "tags": ["ascend", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./ascend-camera-glitch.md"}, {"name": "Ascend Rushing", "abbr": "AR", "date": "2023-06-15", "tags": ["ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./ascend-rushing.md"}, {"name": "Ascend Storage", "abbr": "ASTR", "date": "2023-05-19", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Saria"], "href": "./ascend-storage.md"}, {"name": "Attached Rangeless Active Zonai", "abbr": "ARAZ", "date": "2023-06-16", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?", "NX721"], "href": "./attached-rangeless-active-zonai-araz.md"}, {"name": "Autobuild Cancel Slide", "abbr": "ABCS", "date": "2023-05-18", "tags": ["animation", "movement", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Takosensai1"], "href": "./autobuild-cancel-slide-abcs.md"}, {"name": "Autobuild Duplication", "abbr": "ABD", "date": "2023-06-11", "tags": ["duplication", "item", "ultrahand", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./autobuild-duplication-abd.md"}, {"name": "Autobuild Storage", "abbr": "ABST", "date": "2023-08-28", "tags": ["storage", "item", "autobuild"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "R4000"], "href": "./autobuild-storage.md"}, {"name": "Awakened Master Sword", "abbr": "AMS", "date": "2023-09-04", "tags": ["weapon", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tahata"], "href": "./awakened-master-sword-ams.md"}, {"name": "Back-in-Time Art", "abbr": "BIT", "date": "2023-06-18", "tags": ["save-load"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Zas"], "href": "./back-in-time-art.md"}, {"name": "Back to Back Bloodmoon", "abbr": "BTBB", "date": "2023-05-17", "tags": ["bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lopitty"], "href": "./back-to-back-bloodmoon.md"}, {"name": "Balloon Overload", "abbr": "BO", "date": "2025-03-08", "tags": ["menu", "equipment", "overload", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Jordan", "mulberry", "ofstrings2"], "href": "./balloon-overload.md"}, {"name": "Banc Storage", "abbr": "BANC", "date": "2024-10-01", "tags": ["storage", "warping", "save-load", "bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos", "mulberry", "Aergyl", "EOH_NS_SS"], "href": "./banc-storage.md"}, {"name": "Bomb Skew", "abbr": "BSK", "date": "2023-09-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl", "FerrusCube", "Mozz"], "href": "./bomb-skew.md"}, {"name": "Bow Attachment Desync", "abbr": "BAD", "date": "2023-07-11", "tags": ["desync", "item", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas", "Aeolian"], "href": "./bow-attachment-desync-bad-arrows.md"}, {"name": "Bow Attachment Storage", "abbr": "BAS", "date": "2023-12-03", "tags": ["storage", "item", "fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./bow-attachment-storage.md"}, {"name": "Bow Sprinting", "abbr": "BS", "date": "2023-05-14", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./bow-sprinting.md"}, {"name": "Breaking Awakened Master Sword", "abbr": "BAMS", "date": "2023-11-26", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Infrasolid"], "href": "./breaking-awakened-master-sword.md"}, {"name": "BThrow Sprinting", "abbr": "BTS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./bthrow-sprinting.md"}, {"name": "Bundled Item Duplication", "abbr": "BID", "date": "2023-12-12", "tags": ["duplication", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./bundled-item-duplication-bid.md"}, {"name": "Buoy Bouncing", "abbr": "BB", "date": "2023-05-25", "tags": ["equipment", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup"], "href": "./buoy-bouncing.md"}, {"name": "Camera CFW", "abbr": "CFW", "date": "2023-07-11", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh"], "href": "./camera-cfw.md"}, {"name": "Camera Pose Glitch", "abbr": "CPG", "date": "Unknown", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./camera-pose-glitch.md"}, {"name": "Capsule Cel Shader Removal", "abbr": "CCSR", "date": "2023-12-04", "tags": ["duplication", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./capsule-cel-shader-removal.md"}, {"name": "Cave Flag Culling", "abbr": "CFC", "date": "2023-11-24", "tags": ["duplication", "culling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Aergyl"], "href": "./cave-flag-culling.md"}, {"name": "Chasm Delay Zuggle", "abbr": "CDZ", "date": "2024-05-31", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock", "mulberry", "WinnerBoi77"], "href": "./chasm-delay-zuggle-cdz.md"}, {"name": "Chasm Device Dupe", "abbr": "CDD", "date": "2025-10-12", "tags": ["duplication", "item", "culling", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic", "mulberry"], "href": "./chasm-device-dupe.md"}, {"name": "Clear Camera/Scope", "abbr": "CCS", "date": "2023-07-03", "tags": ["bow", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./clear-camera-scope.md"}, {"name": "Cold Fuse Stick Desync Clip", "abbr": "CSSDC", "date": "2024-06-04", "tags": ["clipping", "desync", "weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "KiloVictor"], "href": "./cold-fuse-stick-desync-clip-cold-fuse-sdc.md"}, {"name": "Cold Fuse", "abbr": "CF", "date": "2023-07-23", "tags": ["weapon", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk", "Ryan?", "Zas"], "href": "./cold-fuse.md"}, {"name": "Construct Fuse Entanglement", "abbr": "CNFE", "date": "2024-06-30", "tags": ["equipment", "entanglement", "fuse", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./construct-fuse-entanglement.md"}, {"name": "Corrupt Meal", "abbr": "CM", "date": "2025-02-07", "tags": ["cooking"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Telkic"], "href": "./corrupt-meal.md"}, {"name": "Crouch Sprinting", "abbr": "CS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./crouch-sprinting.md"}, {"name": "Crouch Throw Tap Sprinting", "abbr": "CTTS", "date": "2023-05-15", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer"], "href": "./crouch-throw-tap-sprinting-ctts.md"}, {"name": "Cucco Warping", "abbr": "CW", "date": "2023-07-23", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi"], "href": "./cucco-warping.md"}, {"name": "Cull Cold Fuse", "abbr": "CCF", "date": "2024-02-01", "tags": ["weapon", "culling", "ultrahand", "fuse"], "versions": ["Unknown"], "credits": ["mulberry"], "href": "./cull-cold-fuse.md"}, {"name": "Cull Equipment Desync", "abbr": "CED", "date": "2023-10-10", "tags": ["desync", "menu", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blize", "Ock"], "href": "./cull-equipment-desync.md"}, {"name": "Cull Fuse Entanglement", "abbr": "CFE", "date": "2023-09-21", "tags": ["entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "suusi", "Ock", "SteFen45"], "href": "./cull-fuse-entanglement-cull-fe.md"}, {"name": "Cull Launching", "abbr": "CL", "date": "2023-07-01", "tags": ["launching", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Asgorne"], "href": "./cull-launching.md"}, {"name": "Cull Pickup Dynamic Zuggle", "abbr": "CPDZ", "date": "2025-05-18", "tags": ["zuggling", "item", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./cull-pickup-dynamic-zuggle.md"}, {"name": "Cull Smuggle", "abbr": "CSMU", "date": "2023-06-27", "tags": ["zuggling", "equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "ROBUXY2ND", "Ock"], "href": "./cull-smuggle.md"}, {"name": "Cull Storage Zuggle", "abbr": "CSZ", "date": "2024-07-18", "tags": ["zuggling", "storage", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars"], "href": "./cull-storage-zuggle-csz.md"}, {"name": "Cull Storage", "abbr": "CSTR", "date": "2024-01-20", "tags": ["storage", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./cull-storage.md"}, {"name": "Cull Zone Culling", "abbr": "CZC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./cull-zone-culling.md"}, {"name": "Culling Area Fuse Storage Fuse Entanglement", "abbr": "CFSFE", "date": "2024-02-25", "tags": ["storage", "entanglement", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee", "Zas"], "href": "./culling-area-fuse-storage-fuse-entanglement.md"}, {"name": "Culling Area Fuse Storage", "abbr": "CAFS", "date": "2023-06-30", "tags": ["storage", "culling", "fuse"], "versions": ["Unknown"], "credits": ["Mozz", "pyuk"], "href": "./culling-area-fuse-storage.md"}, {"name": "Cutscene Combo Amplifier", "abbr": "CCA", "date": "2023-12-22", "tags": ["item", "buff", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Lightos"], "href": "./cutscene-combo-amplifier.md"}, {"name": "Damage Amnesia", "abbr": "DA", "date": "2023-05-27", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./damage-amnesia.md"}, {"name": "Death Persistent Save Load Object Transfer", "abbr": "DPSLOT", "date": "2025-06-26", "tags": ["item", "save-load", "zuggling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./death-persistent-save-load-object-transfer.md"}, {"name": "Detached Rangeless Active Zonai", "abbr": "DRAZ", "date": "2023-06-15", "tags": ["zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Venaticus"], "href": "./detached-rangeless-active-zonai-draz.md"}, {"name": "Detanglement", "abbr": "DTG", "date": "2023-09-09", "tags": ["launching", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./detanglement.md"}, {"name": "Dialog Permacull", "abbr": "DPC", "date": "2025-11-28", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./dialog-permacull.md"}, {"name": "Disabled Enemy", "abbr": "DE", "date": "2023-06-27", "tags": ["enemy"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["shio_0725", "ralseidewitt"], "href": "./disabled-enemy.md"}, {"name": "Dispenser Storage", "abbr": "DISP", "date": "2023-07-02", "tags": ["storage", "item", "ultrahand", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./dispenser-storage.md"}, {"name": "Display Duping", "abbr": "DD", "date": "2023-05-27", "tags": ["duplication", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Pistonight"], "href": "./display-duping.md"}, {"name": "Display Master Sword", "abbr": "DMS", "date": "2023-06-08", "tags": ["weapon", "damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Zas"], "href": "./display-master-sword.md"}, {"name": "Dive Cancel Glide Boost", "abbr": "DCGB", "date": "2023-05-14", "tags": ["animation", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "Mety333"], "href": "./dive-cancel-glide-boost.md"}, {"name": "Double Bypass Zuggle", "abbr": "DBZ", "date": "2025-06-16", "tags": ["zuggling", "item", "culling", "ultrahand"], "versions": ["1.2.0"], "credits": ["mulberry", "dt13269"], "href": "./double-bypass-zuggle-dbz.md"}, {"name": "Double Shield Desync Clip Fuse Entanglement", "abbr": "DSDCFE", "date": "2024-06-06", "tags": ["duplication", "clipping", "desync", "equipment", "entanglement", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Yee"], "href": "./double-shield-desync-clip-fuse-entanglement-double-sdc-fe.md"}, {"name": "Double Tulin Boost", "abbr": "DTB", "date": "2023-05-17", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./double-tulin-boost.md"}, {"name": "Double Unfuse Duplicashen", "abbr": "DUD", "date": "2023-05-15", "tags": ["duplication", "item", "weapon", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Li Shen (Ú»ëþÑ×)"], "href": "./double-unfuse-duplicashen-dud.md"}, {"name": "Dpadlock-less Invizuggle", "abbr": "DLI", "date": "2024-07-17", "tags": ["zuggling", "culling", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry", "Blackmars", "NghtmaR3"], "href": "./dpadlock-less-invizuggle.md"}, {"name": "Drop Delay Zuggle", "abbr": "DDZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-delay-zuggle-ddz.md"}, {"name": "Drop Restriction", "abbr": "DR", "date": "2023-06-19", "tags": ["menu", "item", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["SCFD-GK2", "NicNac"], "href": "./drop-restriction.md"}, {"name": "Drop Smuggling", "abbr": "DSMU", "date": "2023-05-31", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./drop-smuggling.md"}, {"name": "Drop Zuggle", "abbr": "DZ", "date": "2023-06-15", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO"], "href": "./drop-zuggle.md"}, {"name": "Durability-", "abbr": "DUR", "date": "2023-09-11", "tags": ["item", "weapon", "bow"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./durability.md"}, {"name": "Dynamic Purgatory Zuggle", "abbr": "DPZ", "date": "2025-02-14", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./dynamic-purgatory-zuggle.md"}, {"name": "Dynamic Zuggle", "abbr": "DZG", "date": "2023-09-06", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "Zas", "mulberry", "WinnerBoi77", "Ryan?", "CS16"], "href": "./dynamic-zuggle.md"}, {"name": "Eaten Despawn Interrupt", "abbr": "EDI", "date": "2026-01-16", "tags": ["item", "zuggling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Squidwest"], "href": "./eaten-despawn-interrupt.md"}, {"name": "Enemy Pickpocketing", "abbr": "EP", "date": "2023-09-16", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KAIDUDE64"], "href": "./enemy-pickpocketing.md"}, {"name": "Entanglement Height Glitch", "abbr": "EHG", "date": "2023-05-24", "tags": ["equipment", "entanglement", "movement", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./entanglement-height-glitch.md"}, {"name": "Equipment Collision Zuggle", "abbr": "ECZ", "date": "2023-05-16", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zvleon"], "href": "./equipment-collision-zuggle.md"}, {"name": "Equipment Mitosis", "abbr": "EM", "date": "2023-09-05", "tags": ["duplication", "zuggling", "equipment", "overload"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./equipment-mitosis.md"}, {"name": "Equipment Shock Duping", "abbr": "ESD", "date": "2023-12-12", "tags": ["duplication", "item", "equipment"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./equipment-shock-duping.md"}, {"name": "Equipment Smuggle", "abbr": "ESMU", "date": "2023-06-01", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["sleepyppls", "Mozz", "mulberry", "NaN Gogh"], "href": "./equipment-smuggle.md"}, {"name": "Equipped Throken", "abbr": "ETHK", "date": "2025-05-20", "tags": ["weapon", "equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl", "mulberry"], "href": "./equipped-throken.md"}, {"name": "Extended Throw Sprinting", "abbr": "ETS", "date": "2023-05-12", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["briochoc"], "href": "./extended-throw-sprinting-ets.md"}, {"name": "Fall Damage Cancel", "abbr": "FDC", "date": "2023-05-23", "tags": ["animation", "damage", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter"], "href": "./fall-damage-cancel-fdc.md"}, {"name": "Floorping", "abbr": "FLP", "date": "2024-01-02", "tags": ["warping"], "versions": ["1.1.0", "1.1.1"], "credits": ["koreth"], "href": "./floorping.md"}, {"name": "Food Ability Buff Swap", "abbr": "FABS", "date": "2023-05-16", "tags": ["cooking", "item", "buff", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["fabs"], "href": "./food-ability-buff-swap-fabs.md"}, {"name": "Force Equip Zuggling", "abbr": "FEZ", "date": "2023-06-07", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "Mozz", "Rhkellz", "Syb", "NaN Gogh"], "href": "./force-equip-zuggling-fez.md"}, {"name": "Forced Blood Moon", "abbr": "FBM", "date": "2023-05-28", "tags": ["bloodmoon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["1789(@W0ERYySQgZyGOY3)", "Simonfirefighter", "Maxmasher", "Flash", "acaepius"], "href": "./forced-blood-moon.md"}, {"name": "Freecall", "abbr": "FC", "date": "2023-09-09", "tags": ["ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["suusi", "ROBUXY2ND"], "href": "./freecall.md"}, {"name": "Fuse Entangle Drop Zuggle", "abbr": "FEDZ", "date": "2023-06-17", "tags": ["zuggling", "item", "weapon", "equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-drop-zuggle-fedz.md"}, {"name": "Fuse Entangle Weapon Zuggle", "abbr": "FEWZ", "date": "2023-06-10", "tags": ["zuggling", "item", "weapon", "damage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./fuse-entangle-weapon-zuggle-fewz.md"}, {"name": "Fuse Entanglement Clipping", "abbr": "FEC", "date": "2023-06-16", "tags": ["clipping", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["circyit"], "href": "./fuse-entanglement-clipping-fec.md"}, {"name": "Fuse Entanglement Desync", "abbr": "FED", "date": "2023-05-26", "tags": ["duplication", "desync", "item", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement-desync-fed.md"}, {"name": "Fuse Entanglement Drop Smuggling", "abbr": "FEDS", "date": "2023-08-15", "tags": ["zuggling", "item", "equipment", "entanglement", "fuse"], "versions": ["1.2.0"], "credits": ["Blize", "Blackmars"], "href": "./fuse-entanglement-drop-smuggling.md"}, {"name": "Fuse Entanglement", "abbr": "FE", "date": "2023-05-24", "tags": ["equipment", "entanglement", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./fuse-entanglement.md"}, {"name": "Fuse Overload", "abbr": "FO", "date": "2023-11-03", "tags": ["weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ultrababouin", "NghtmaR3"], "href": "./fuse-overload-fo.md"}, {"name": "Fuse Overload Fuse Entanglement", "abbr": "FOFE", "date": "2025-05-26", "tags": ["entanglement", "overload", "ultrahand", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry"], "href": "./fuse-overload-fuse-entanglement-fofe.md"}, {"name": "Fuse Storage", "abbr": "FS", "date": "2023-06-18", "tags": ["storage", "item", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./fuse-storage-fs.md"}, {"name": "Fuse Storage Fuse Entanglement", "abbr": "FSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./fuse-storage-fuse-entanglement-fsfe.md"}, {"name": "GAS Launching", "abbr": "GASL", "date": "2023-06-25", "tags": ["gas", "launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "pyuk", "Flash", "Mozz", "Blize"], "href": "./gas-launching-previously-known-as-ascend-launching.md"}, {"name": "GAS Warping", "abbr": "GASW", "date": "2023-06-26", "tags": ["gas", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Flash", "pyuk"], "href": "./gas-warping.md"}, {"name": "Ghost Save Load Object Transfer", "abbr": "GSLOT", "date": "2024-03-08", "tags": ["save-load", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./ghost-save-load-object-transfer.md"}, {"name": "Ghost Stick Clipping", "abbr": "GSC", "date": "2023-05-28", "tags": ["clipping"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["rocomox"], "href": "./ghost-stick-clipping.md"}, {"name": "Glue Removal", "abbr": "GR", "date": "2023-10-05", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./glue-removal.md"}, {"name": "Guard-less Active Shield", "abbr": "GAS", "date": "2023-06-12", "tags": ["equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Venaticus"], "href": "./guard-less-active-shield-gas.md"}, {"name": "Hand Locked Equipment Smuggling", "abbr": "HLES", "date": "2023-07-11", "tags": ["zuggling", "equipment", "item", "shield"], "versions": ["1.0.0"], "credits": ["Aeolian"], "href": "./hand-locked-equipment-smuggling-hles.md"}, {"name": "Handy Job", "abbr": "HJ", "date": "2023-11-20", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./handy-job.md"}, {"name": "Hero Path Link Storage", "abbr": "HPLS", "date": "2023-06-20", "tags": ["storage"], "versions": ["1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./hero-path-link-storage-hpls.md"}, {"name": "Hestu Scamming", "abbr": "HSCA", "date": "2024-04-19", "tags": ["menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars", "Tahata", "EM"], "href": "./hestu-scamming.md"}, {"name": "Hold Smuggling", "abbr": "HSM", "date": "2023-07-04", "tags": ["zuggling", "menu", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "NaN Gogh"], "href": "./hold-smuggling.md"}, {"name": "Hold Storage Duplication", "abbr": "HSD", "date": "2023-07-03", "tags": ["duplication", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Mozz"], "href": "./hold-storage-duplication-also-known-as-minus-dupe.md"}, {"name": "Hold Storage", "abbr": "HS", "date": "2023-07-02", "tags": ["storage", "desync", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "NaN Gogh", "Mozz"], "href": "./hold-storage.md"}, {"name": "Horse Duping", "abbr": "HD", "date": "2024-03-22", "tags": ["duplication", "culling", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./horse-duping.md"}, {"name": "Hydro Clipping", "abbr": "HC", "date": "2023-06-15", "tags": ["clipping", "storage", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Simonfirefighter", "Maxmasher", "KnightPohtaytoh", "pyuk"], "href": "./hydro-clipping.md"}, {"name": "Infinite Balloon", "abbr": "IBAL", "date": "2024-06-13", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurone_yuu"], "href": "./infinite-balloon.md"}, {"name": "Infinite Bubbul Frog Gems", "abbr": "IBFG", "date": "2023-05-21", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Unknown"], "href": "./infinite-bubbul-frog-gems.md"}, {"name": "Infinite Damage 2.0", "abbr": "ID2", "date": "2024-01-21", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./infinite-damage-2-0.md"}, {"name": "Infinite Damage", "abbr": "IDMG", "date": "2023-05-13", "tags": ["damage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["GamSla341"], "href": "./infinite-damage.md"}, {"name": "Infinite Height", "abbr": "IH", "date": "2023-05-22", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "Physioninja"], "href": "./infinite-height.md"}, {"name": "Inventory Shift Duplication", "abbr": "ISD", "date": "2023-06-25", "tags": ["duplication", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Blizzard Blanc", "BigDUCCO", "Maxmasher", "pyuk", "Zas"], "href": "./inventory-shift-duplication-isd.md"}, {"name": "Invizuggle", "abbr": "IVZ", "date": "2024-01-03", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "Yee"], "href": "./invizuggle.md"}, {"name": "Item Save Load Transfer", "abbr": "ISLT", "date": "2023-12-22", "tags": ["item", "save-load", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Luckstyle"], "href": "./item-save-load-transfer-islt.md"}, {"name": "Item Throw Hitbox Disable", "abbr": "ITHD", "date": "2023-06-18", "tags": ["item", "recall", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Arfix", "Moonrise"], "href": "./item-throw-hitbox-disable.md"}, {"name": "Jumpslash Cancel Clipping", "abbr": "JCC", "date": "2023-06-16", "tags": ["clipping", "animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./jumpslash-cancel-clipping-jcc.md"}, {"name": "Jumpslash Canceling", "abbr": "JSC", "date": "2023-05-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Mozz"], "href": "./jumpslash-canceling.md"}, {"name": "Kilovictor's quicksmuggle", "abbr": "KQS", "date": "2024-02-23", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["KiloVictor"], "href": "./kilovictor-s-quicksmuggle.md"}, {"name": "L Sprinting", "abbr": "LS", "date": "2023-05-12", "tags": ["sprinting", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Tauktes"], "href": "./l-sprinting.md"}, {"name": "Lag Machines", "abbr": "LM", "date": "2023-10-05", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lag-machines.md"}, {"name": "Laser-OOB", "abbr": "LOOB", "date": "2023-05-13", "tags": ["duplication", "oob"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Xeryph"], "href": "./laser-oob.md"}, {"name": "Lift Fuse Interrupt", "abbr": "LFI", "date": "2025-04-22", "tags": ["weapon", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee"], "href": "./lift-fuse-interrupt.md"}, {"name": "Lift Smuggle", "abbr": "LSMU", "date": "2024-02-03", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Blackmars"], "href": "./lift-smuggle.md"}, {"name": "Lift Storage Warping", "abbr": "LSW", "date": "2024-01-08", "tags": ["storage", "item", "culling", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./lift-storage-warping-lsw.md"}, {"name": "Lift Warping", "abbr": "LW", "date": "2023-06-15", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./lift-warping.md"}, {"name": "Like-Like Culling", "abbr": "LLC", "date": "2023-06-13", "tags": ["culling", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-culling.md"}, {"name": "Like-Like Drop Smuggling", "abbr": "LLDS", "date": "2023-06-15", "tags": ["zuggling", "item", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-drop-smuggling.md"}, {"name": "Like-Like FSFE", "abbr": "LLFSFE", "date": "2023-06-18", "tags": ["storage", "entanglement", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "Mozz"], "href": "./like-like-fsfe.md"}, {"name": "Like-Like Fuse Storage", "abbr": "LLFS", "date": "2023-06-18", "tags": ["storage", "item", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Mozz"], "href": "./like-like-fuse-storage.md"}, {"name": "Like Like New Textbox Softlock", "abbr": "LLTS", "date": "2023-06-16", "tags": ["item", "like-like", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ryan?"], "href": "./like-like-new-textbox-softlock.md"}, {"name": "Like-Like Smuggle Desync", "abbr": "LLSD", "date": "2023-06-15", "tags": ["zuggling", "desync", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-smuggle-desync-lsd.md"}, {"name": "Like-Like Smuggling", "abbr": "LLS", "date": "2023-06-15", "tags": ["zuggling", "equipment", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "mulberry"], "href": "./like-like-smuggling.md"}, {"name": "Like-Like Warping", "abbr": "LLW", "date": "2023-06-15", "tags": ["warping", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./like-like-warping.md"}, {"name": "Like-Like Zuggling", "abbr": "LLZ", "date": "2023-06-15", "tags": ["zuggling", "like-like", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "Ryan?", "Blackmars"], "href": "./like-like-zuggling.md"}, {"name": "LikeLike Stick Smuggling", "abbr": "LLSS", "date": "Unknown", "tags": ["zuggling", "item", "equipment", "culling", "fuse", "like-like"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./likelike-stick-smuggling.md"}, {"name": "Long Jump", "abbr": "LJ", "date": "2023-05-18", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./long-jump.md"}, {"name": "Map Flickering", "abbr": "MF", "date": "Unknown", "tags": ["map"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Unknown"], "href": "./map-flickering.md"}, {"name": "Map Storage", "abbr": "MSTR", "date": "2023-05-29", "tags": ["storage", "map"], "versions": ["1.1.0", "1.1.1"], "credits": ["blueberryoats"], "href": "./map-storage.md"}, {"name": "Map Zuggling", "abbr": "MZ", "date": "2023-05-23", "tags": ["zuggling", "map", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["BigDUCCO"], "href": "./map-zuggling-mz.md"}, {"name": "Mass Amnesia", "abbr": "MA", "date": "2023-08-02", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./mass-amnesia.md"}, {"name": "Master Sword Liberation", "abbr": "MSL", "date": "2023-11-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./master-sword-liberation.md"}, {"name": "Master Sword Zuggling/ Decayed Master Sword Zuggling", "abbr": "MSZ", "date": "2023-11-06", "tags": ["zuggling", "desync", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zas"], "href": "./master-sword-zuggling-decayed-master-sword-zuggling.md"}, {"name": "Memory Buffering", "abbr": "MB", "date": "2023-05-29", "tags": ["menu", "buff"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./memory-buffering.md"}, {"name": "Memory Interrupt", "abbr": "MI", "date": "2024-10-01", "tags": ["Unknown"], "versions": ["1.0.0"], "credits": ["mulberry"], "href": "./memory-interrupt.md"}, {"name": "Menu Overload", "abbr": "MO", "date": "2024-01-11", "tags": ["oob", "menu", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./menu-overload.md"}, {"name": "Message Not Found", "abbr": "MNF", "date": "2023-05-17", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk", "Abahbob"], "href": "./message-not-found-mnf.md"}, {"name": "Midair Item Transmutation", "abbr": "MIT", "date": "2023-05-20", "tags": ["item", "paraglide", "zuggling"], "versions": ["1.1.0", "1.1.1"], "credits": ["eXe"], "href": "./midair-item-transmutation-mit.md"}, {"name": "Midair Sort Duplication", "abbr": "MSD", "date": "2023-05-21", "tags": ["duplication", "menu", "item", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Zas", "kurocat471"], "href": "./midair-sort-duplication-msd.md"}, {"name": "Midair Throw Duplication", "abbr": "MTD", "date": "2023-07-02", "tags": ["duplication", "item", "zonai", "paraglide"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["quantim"], "href": "./midair-throw-duplication-mtd.md"}, {"name": "Minecart Rail Collision Launching", "abbr": "MRCL", "date": "2023-05-18", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüØÒéë-ÒüòÒéô"], "href": "./minecart-rail-collision-launching-mrcl.md"}, {"name": "Mineru Ability Desync", "abbr": "MAD", "date": "2023-05-30", "tags": ["desync", "mineru"], "versions": ["1.1.0", "1.1.1"], "credits": ["Sillicat"], "href": "./mineru-ability-desync.md"}, {"name": "Mineru Aim Permanence", "abbr": "MAIP", "date": "Unknown", "tags": ["mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./mineru-aim-permanence.md"}, {"name": "Mineru Cull Storage", "abbr": "MCS", "date": "2025-11-09", "tags": ["zuggling", "storage", "culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["ofstrings2"], "href": "./mineru-cull-storage.md"}, {"name": "Mineru Culling", "abbr": "MC", "date": "2023-07-31", "tags": ["culling", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./mineru-culling.md"}, {"name": "Mineru Fuse Entanglement", "abbr": "MFE", "date": "2023-10-18", "tags": ["entanglement", "culling", "ultrahand", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "WinnerBoi77"], "href": "./mineru-fuse-entanglement-mineru-fe.md"}, {"name": "Mineru Hold Smuggle", "abbr": "MHS", "date": "2023-12-20", "tags": ["zuggling", "menu", "item", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["WinnerBoi77"], "href": "./mineru-hold-smuggle-mhs.md"}, {"name": "Mineru Persistent Save Load Object Transfer", "abbr": "MPSLOT", "date": "2024-07-27", "tags": ["equipment", "culling", "save-load", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["mulberry", "Armindo", "Emiya"], "href": "./mineru-persistent-save-load-object-transfer.md"}, {"name": "Mineru Text Storage", "abbr": "MTS", "date": "2024-07-11", "tags": ["storage", "mineru"], "versions": ["1.0.0"], "credits": ["CM30"], "href": "./mineru-text-storage.md"}, {"name": "MNF Fusing", "abbr": "MNFF", "date": "2023-06-05", "tags": ["fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["LegendofLinkk"], "href": "./mnf-fusing.md"}, {"name": "MNF Glow Overload", "abbr": "MGO", "date": "2025-01-03", "tags": ["item", "overload", "mnf"], "versions": ["1.0.0"], "credits": ["Toti Sauce"], "href": "./mnf-glow-overload.md"}, {"name": "MNF Zuggle Fuse", "abbr": "MZF", "date": "2023-05-18", "tags": ["zuggling", "weapon", "fuse", "mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./mnf-zuggle-fuse.md"}, {"name": "Model Teleport Desync", "abbr": "MTEL", "date": "2023-07-29", "tags": ["desync", "warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./model-teleport-desync.md"}, {"name": "Modifier Deletion Weapon State Transfer", "abbr": "MDWST", "date": "Unknown", "tags": ["duplication", "weapon"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md"}, {"name": "Modifier ONLY Transfer", "abbr": "MOT", "date": "2023-06-09", "tags": ["weapon"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kurocat471", "BigDUCCO"], "href": "./modifier-only-transfer.md"}, {"name": "Moobe Warping", "abbr": "MW", "date": "2024-01-12", "tags": ["oob", "warping", "movement", "horse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./moobe-warping.md"}, {"name": "Mount Lock", "abbr": "ML", "date": "2023-05-21", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Physioninja"], "href": "./mount-lock.md"}, {"name": "Mozdor Jumping/Slashing", "abbr": "MJS", "date": "2023-05-20", "tags": ["movement", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "AgdoR"], "href": "./mozdor-jumping-slashing.md"}, {"name": "MSNF glowing", "abbr": "MG", "date": "2023-08-02", "tags": ["mnf"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["evilgabe"], "href": "./msnf-glowing.md"}, {"name": "Mulberry's Out of Body Experience", "abbr": "MOOBE", "date": "2024-01-06", "tags": ["warping", "movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./mulberry-s-out-of-body-experience-moobe.md"}, {"name": "New Item Desync", "abbr": "NID", "date": "2023-05-12", "tags": ["duplication", "desync", "menu", "item", "equipment", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Modoki_returns"], "href": "./new-item-desync-equipment-duping.md"}, {"name": "No Bow Sprinting", "abbr": "NBS", "date": "2023-05-12", "tags": ["sprinting", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Steel"], "href": "./no-bow-sprinting-nbs.md"}, {"name": "Null Dropping", "abbr": "ND", "date": "2024-03-16", "tags": ["menu", "item", "zuggling"], "versions": ["1.0.0"], "credits": ["Aergyl"], "href": "./null-dropping.md"}, {"name": "Object Culling", "abbr": "OC", "date": "2023-06-27", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "tori", "mulberry", "Timber"], "href": "./object-culling.md"}, {"name": "Object (Moe) Enlargement", "abbr": "MOE", "date": "2024-10-30", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "PetitFrapo", "Jordan"], "href": "./object-moe-enlargement.md"}, {"name": "Ocklusion Hovering", "abbr": "OCKH", "date": "2025-10-12", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Telkic"], "href": "./ocklusion-hovering.md"}, {"name": "Ocklusion", "abbr": "OCKL", "date": "2024-05-29", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./ocklusion.md"}, {"name": "Octo-balloon Detanglement", "abbr": "OBD", "date": "2025-11-16", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["mulberry"], "href": "./octo-balloon-detanglement.md"}, {"name": "Octodupe", "abbr": "OD", "date": "2023-05-26", "tags": ["duplication", "item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Unknown"], "href": "./octodupe.md"}, {"name": "Overload at Home", "abbr": "OAH", "date": "2024-03-20", "tags": ["zuggling", "culling", "overload"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./overload-at-home-aka-pickup-overload.md"}, {"name": "Overload Cold Fuse", "abbr": "OCF", "date": "2023-07-23", "tags": ["item", "weapon", "overload", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["F. Buffalo"], "href": "./overload-cold-fuse.md"}, {"name": "Overload Drop Smuggling", "abbr": "ODS", "date": "2023-06-12", "tags": ["zuggling", "item", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ChargeVolt", "Windocks"], "href": "./overload-drop-smuggling.md"}, {"name": "Overload Dynamic Zuggle", "abbr": "ODZ", "date": "2025-05-19", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["mulberry"], "href": "./overload-dynamic-zuggle.md"}, {"name": "Overload Fuse Entanglement", "abbr": "OFE", "date": "2024-07-23", "tags": ["zuggling", "entanglement", "culling", "overload", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./overload-fuse-entanglement.md"}, {"name": "Overload Persistent Save Load Object Transfer", "abbr": "OPSLOT", "date": "2024-07-26", "tags": ["overload", "save-load"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./overload-persistent-save-load-object-transfer.md"}, {"name": "Pelison Duping", "abbr": "PD", "date": "2023-05-25", "tags": ["duplication", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["AngryEgg", "BigDUCCO"], "href": "./pelison-duping.md"}, {"name": "Persistent Save Load Object Transfer", "abbr": "PSLOT", "date": "2024-01-25", "tags": ["culling", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./persistent-save-load-object-transfer-pslot.md"}, {"name": "Pickup Smuggling", "abbr": "PSMU", "date": "2023-05-28", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ame"], "href": "./pickup-smuggling.md"}, {"name": "Pocket Rocket", "abbr": "PR", "date": "2023-06-15", "tags": ["launching", "equipment", "paraglide", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "SmallAnt"], "href": "./pocket-rocket.md"}, {"name": "Portable Cull Save Load Dupe", "abbr": "PSLD", "date": "2024-07-17", "tags": ["duplication", "culling", "save-load"], "versions": ["1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./portable-cull-save-load-dupe-portacull-sld.md"}, {"name": "Portable Culling", "abbr": "PCULL", "date": "2024-02-27", "tags": ["zuggling", "desync", "item", "culling", "fuse"], "versions": ["1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./portable-culling.md"}, {"name": "Portacull Invismuggle", "abbr": "PCI", "date": "2024-02-29", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry"], "href": "./portacull-invismuggle.md"}, {"name": "Weapon Despawn Prevention", "abbr": "WDP", "date": "2023-06-28", "tags": ["weapon", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721"], "href": "./prevent-weapon-despawn.md"}, {"name": "Prologue Escape", "abbr": "PE", "date": "2024-10-01", "tags": ["duplication", "storage"], "versions": ["1.0.0"], "credits": ["LegendofLinkk", "mulberry", "Aergyl", "Lightos", "EOH_NS_SS"], "href": "./prologue-escape.md"}, {"name": "Proxy Glitches", "abbr": "PG", "date": "Unknown", "tags": ["movement"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./proxy-glitches.md"}, {"name": "Purgatory Save Load Dupe", "abbr": "PGSLD", "date": "2024-02-11", "tags": ["duplication", "equipment", "save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./purgatory-save-load-dupe.md"}, {"name": "Pyroculling", "abbr": "PYR", "date": "2023-11-17", "tags": ["culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.2.0"], "credits": ["ROBUXY2ND"], "href": "./pyroculling.md"}, {"name": "Quantum Linking", "abbr": "QL", "date": "2023-08-30", "tags": ["culling", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "pyuk"], "href": "./quantum-linking-ql.md"}, {"name": "Quick Drop Smuggle", "abbr": "QDS", "date": "2024-03-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0"], "credits": ["mulberry", "Zas", "Aeolian", "WinnerBoi77", "Ryan?"], "href": "./quick-drop-smuggle-qds.md"}, {"name": "Quick Smuggling", "abbr": "QS", "date": "2023-07-10", "tags": ["zuggling", "equipment", "arrow"], "versions": ["1.2.0"], "credits": ["Suishi"], "href": "./quick-smuggling.md"}, {"name": "Reball", "abbr": "RBL", "date": "2023-07-06", "tags": ["movement", "recall", "zonai"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./reball.md"}, {"name": "Recall Cancel", "abbr": "RCC", "date": "2023-07-20", "tags": ["animation", "item", "recall"], "versions": ["1.2.0", "1.2.1"], "credits": ["R4000"], "href": "./recall-cancel.md"}, {"name": "Recall Clip", "abbr": "RC", "date": "2023-05-16", "tags": ["clipping", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ÒüôÒéôÒüØÒéü"], "href": "./recall-clip.md"}, {"name": "Recall Drop Stacking", "abbr": "RDS", "date": "2025-01-04", "tags": ["item", "recall", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Telkic", "mulberry"], "href": "./recall-drop-stacking.md"}, {"name": "Recall Launch", "abbr": "RL", "date": "2023-05-17", "tags": ["launching", "ultrahand", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deep"], "href": "./recall-launch.md"}, {"name": "Recall Locking", "abbr": "RLK", "date": "2023-06-11", "tags": ["recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?"], "href": "./recall-locking.md"}, {"name": "Recall Sluggle", "abbr": "RSL", "date": "2025-07-12", "tags": ["zuggling", "menu", "recall"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["WinnerBoi77"], "href": "./recall-sluggle.md"}, {"name": "Recipe Storage", "abbr": "RS", "date": "2024-09-14", "tags": ["storage", "menu"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "mulberry"], "href": "./recipe-storage.md"}, {"name": "Remote Arrow", "abbr": "RAT", "date": "2023-06-02", "tags": ["arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Flash", "ElDuende", "kirigaya"], "href": "./remote-arrow-trap.md"}, {"name": "Replacement Actor Fuse Entanglement", "abbr": "RAFE", "date": "2024-11-09", "tags": ["entanglement", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["dt13269", "mulberry"], "href": "./replacement-actor-fuse-entanglement.md"}, {"name": "Resync Fuse Entanglement", "abbr": "RFE", "date": "2023-12-18", "tags": ["item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./resync-fuse-entanglement-resync-fe.md"}, {"name": "Reverse Ascend Storage", "abbr": "RAS", "date": "2023-11-27", "tags": ["storage", "ascend"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Redrooey"], "href": "./reverse-ascend-storage.md"}, {"name": "Sage Madness", "abbr": "SM", "date": "2023-07-18", "tags": ["camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aci"], "href": "./sage-madness.md"}, {"name": "Sage Recycling", "abbr": "SRCY", "date": "2023-05-28", "tags": ["duplication", "tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Knight7108", "Candlelor"], "href": "./sage-recycling.md"}, {"name": "Save Load Dupe", "abbr": "SLD", "date": "2023-05-16", "tags": ["duplication", "equipment", "save-load", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ZombieBoy225", "ness", "ElDuende"], "href": "./save-load-dupe-sld.md"}, {"name": "Save Load Zuggling", "abbr": "SLZ", "date": "2023-05-23", "tags": ["zuggling", "save-load", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["NicNac", "Flash", "BigDUCCO", "Wip long sticks enjoyer"], "href": "./save-load-zuggling-slz.md"}, {"name": "Scope Render Cancel", "abbr": "SRC", "date": "2023-05-19", "tags": ["animation", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "eXe"], "href": "./scope-render-cancel.md"}, {"name": "Shadow/Void Icons", "abbr": "SVI", "date": "2024-10-16", "tags": ["equipment", "fuse", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["Lightos", "PetitFrapo"], "href": "./shadow-void-icons.md"}, {"name": "Shock Cold Fuse", "abbr": "SCF", "date": "2023-09-11", "tags": ["weapon", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-cold-fuse.md"}, {"name": "Shock Effect Overload", "abbr": "SEO", "date": "2023-07-26", "tags": ["overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NX721", "R4000"], "href": "./shock-effect-overload-seo.md"}, {"name": "Shock Fuse Entanglement", "abbr": "SFE", "date": "2023-09-12", "tags": ["zuggling", "item", "entanglement", "fuse"], "versions": ["1.0.0"], "credits": ["Zas"], "href": "./shock-fuse-entanglement.md"}, {"name": "Shock Smuggle", "abbr": "SSMU", "date": "2023-06-01", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["sleepyppls"], "href": "./shock-smuggle.md"}, {"name": "Shrunken Actors", "abbr": "SA", "date": "2025-10-26", "tags": ["ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["mulberry"], "href": "./shrunken-actors.md"}, {"name": "Slate Storage", "abbr": "SLST", "date": "2024-09-21", "tags": ["storage", "damage"], "versions": ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["LegendofLinkk"], "href": "./slate-storage.md"}, {"name": "Slugging", "abbr": "SLG", "date": "2023-06-15", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./slugging.md"}, {"name": "Smuggle Retrieval", "abbr": "SRET", "date": "2024-12-18", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["PetitFrapo"], "href": "./smuggle-retrieval.md"}, {"name": "Smuggle Stacking Zuggle", "abbr": "SSZ", "date": "2023-06-06", "tags": ["zuggling", "item", "equipment", "shield", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["BigDUCCO", "LegendofLinkk", "Mozz"], "href": "./smuggle-stacking-zuggle-ssz.md"}, {"name": "Split Item Duplication", "abbr": "SID", "date": "2025-06-19", "tags": ["duplication", "item", "zuggling"], "versions": ["1.2.0"], "credits": ["Telkic", "mulberry", "WinnerBoi77"], "href": "./split-item-duplication-sid.md"}, {"name": "Spring Fall Damage Cancel", "abbr": "SFDC", "date": "2023-05-15", "tags": ["animation", "damage", "movement", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./spring-fall-damage-cancel.md"}, {"name": "Spring Strangeness", "abbr": "STRS", "date": "2023-05-15", "tags": ["spring", "camera"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["orionsayshi", "Owen"], "href": "./spring-strangeness.md"}, {"name": "Springboard Clipping", "abbr": "SBC", "date": "2023-05-27", "tags": ["clipping", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["ab2x3z"], "href": "./springboard-clipping.md"}, {"name": "Springboarding", "abbr": "SBRD", "date": "2023-05-24", "tags": ["equipment", "shield", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springboarding.md"}, {"name": "Springdolling", "abbr": "SDOL", "date": "2023-05-15", "tags": ["launching", "spring"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz"], "href": "./springdolling.md"}, {"name": "Stack Splitting", "abbr": "SSPL", "date": "2024-12-31", "tags": ["item", "fuse", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["s0ft", "Telkic", "mulberry"], "href": "./stack-splitting.md"}, {"name": "Stamina Depletion Freeze", "abbr": "SDF", "date": "2023-05-20", "tags": ["Unknown"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos"], "href": "./stamina-depletion-freeze-sdf.md"}, {"name": "Stick Desync Clip", "abbr": "SDC", "date": "2023-07-01", "tags": ["clipping", "desync", "item", "equipment", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NaN Gogh", "DisguisedMoth"], "href": "./stick-desync-clip-sdc.md"}, {"name": "Sticky Dynamic Purgatory", "abbr": "SDP", "date": "2024-02-15", "tags": ["equipment", "culling", "fuse"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./sticky-dynamic-purgatory.md"}, {"name": "Super Bomb Jump", "abbr": "SBJ", "date": "2023-09-14", "tags": ["launching"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["FerrusCube", "Aergyl"], "href": "./super-bomb-jump.md"}, {"name": "Super Fuse Overload", "abbr": "SFO", "date": "2025-12-06", "tags": ["weapon", "overload", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry", "Aergyl", "Jordan", "MandelbrotChaylay"], "href": "./super-fuse-overload.md"}, {"name": "Surf storage", "abbr": "SSTR", "date": "2023-09-22", "tags": ["storage"], "versions": ["1.0.0"], "credits": ["Mozz"], "href": "./surf-storage.md"}, {"name": "Swap Resync Zuggle", "abbr": "SRZ", "date": "2025-08-11", "tags": ["zuggling", "equipment", "culling"], "versions": ["1.2.0"], "credits": ["mulberry", "MandelbrotChaylay"], "href": "./swap-resync-zuggle-srz.md"}, {"name": "Swap Resync", "abbr": "SR", "date": "2025-08-10", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["MandelbrotChaylay"], "href": "./swap-resync.md"}, {"name": "Temporary Devices", "abbr": "TD", "date": "2024-11-30", "tags": ["fuse", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./temporary-devices.md"}, {"name": "Texture Tearing", "abbr": "TT", "date": "2024-01-13", "tags": ["oob", "menu", "equipment", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock"], "href": "./texture-tearing.md"}, {"name": "Throken", "abbr": "THK", "date": "2025-05-17", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikaboze"], "href": "./throken.md"}, {"name": "Throw Cancelling", "abbr": "TC", "date": "Unknown", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Quelfth"], "href": "./throw-cancelling.md"}, {"name": "Throw Tap Sprinting", "abbr": "TTS", "date": "2023-05-14", "tags": ["sprinting"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deystroyer", "Tauktes"], "href": "./throw-tap-sprinting-tts.md"}, {"name": "Throwless Storage", "abbr": "THS", "date": "2023-06-19", "tags": ["storage", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["evilgabe", "NX721"], "href": "./throwless-storage-previously-known-as-beam-storage.md"}, {"name": "Time Bomb cancel", "abbr": "TBC", "date": "2023-11-04", "tags": ["animation", "equipment", "damage", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["tzakazuki"], "href": "./time-bomb-cancel.md"}, {"name": "Toti Saucery", "abbr": "TOTS", "date": "2024-08-17", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Toti Sauce", "Telkic"], "href": "./toti-saucery.md"}, {"name": "Travel Medallion storage", "abbr": "TMS", "date": "2023-06-16", "tags": ["storage"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["kirigaya"], "href": "./travel-medallion-storage-tms.md"}, {"name": "Tulin Pumping", "abbr": "TP", "date": "2023-05-14", "tags": ["tulin"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ikkitrix"], "href": "./tulin-pumping.md"}, {"name": "Two Handed With Shield", "abbr": "THWS", "date": "2023-08-21", "tags": ["equipment", "shield", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["R4000", "Bucket_Sloe"], "href": "./two-handed-with-shield.md"}, {"name": "Ultimate Pocket Rocket", "abbr": "UPR", "date": "2025-05-20", "tags": ["launching", "warping", "ultrahand"], "versions": ["1.0.0"], "credits": ["Aergyl", "mulberry", "Ikaboze", "Jordan"], "href": "./ultimate-pocket-rocket.md"}, {"name": "Ultra Save Load Object Transfer", "abbr": "USLOT", "date": "2024-02-15", "tags": ["save-load", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["mulberry"], "href": "./ultra-save-load-object-transfer.md"}, {"name": "Ultrabroken Smuggling", "abbr": "UBS", "date": "2023-06-13", "tags": ["zuggling", "equipment", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["The_Andromeda"], "href": "./ultrabroken-smuggling-ubs.md"}, {"name": "Ultrabroken", "abbr": "UB", "date": "2023-05-29", "tags": ["item", "ultrahand", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Duncan"], "href": "./ultrabroken.md"}, {"name": "Unload Duping", "abbr": "UD", "date": "2023-05-31", "tags": ["duplication", "item", "culling", "fuse", "bow", "arrow"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª", "ÕìâÕ╣┤ÞîÂÚÑ╝"], "href": "./unload-duping.md"}, {"name": "Unload WST", "abbr": "UWST", "date": "Unknown", "tags": ["item", "culling", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "Vee.Might.Exist", "Syb"], "href": "./unload-wst.md"}, {"name": "Unsheathed Mastersword", "abbr": "UMS", "date": "2023-07-11", "tags": ["duplication", "weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "DanielNeia"], "href": "./unsheathed-mastersword.md"}, {"name": "Vendor Scamming", "abbr": "VS", "date": "2023-07-03", "tags": ["zuggling", "storage", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"], "credits": ["NX721", "Mozz", "NaN Gogh"], "href": "./vendor-scamming.md"}, {"name": "Void Dipping", "abbr": "VD", "date": "2025-12-29", "tags": ["item", "equipment", "ultrahand"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Squidwest", "mulberry", "Aergyl"], "href": "./void-dipping.md"}, {"name": "Void Hold Storage", "abbr": "VHS", "date": "2023-07-22", "tags": ["storage", "menu", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Lightos", "NX721"], "href": "./void-hold-storage.md"}, {"name": "Void Holding", "abbr": "VH", "date": "2023-06-10", "tags": ["item", "zuggling"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Lightos"], "href": "./void-holding.md"}, {"name": "Wacko Attacko", "abbr": "WATK", "date": "2024-01-21", "tags": ["animation"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3", "WinnerBoi77"], "href": "./wacko-attacko.md"}, {"name": "Warp Bumping", "abbr": "WB", "date": "2023-06-07", "tags": ["warping"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["Mozz", "InAMuffinCup"], "href": "./warp-bumping.md"}, {"name": "Weapon Dash GAS", "abbr": "WDGAS", "date": "2025-11-28", "tags": ["gas", "weapon", "culling", "fuse", "zonai"], "versions": ["1.2.0", "1.2.1", "1.3.0", "1.4.0", "1.4.1", "1.4.2"], "credits": ["Toti Sauce"], "href": "./weapon-dash-gas.md"}, {"name": "Weapon Extensions", "abbr": "WEXT", "date": "2023-06-20", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Deltenic", "Flash", "Zas"], "href": "./weapon-extensions.md"}, {"name": "Weapon Fuse Entangelemt", "abbr": "WFE", "date": "2023-06-01", "tags": ["weapon"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["ROBUXY2ND", "Physioninja"], "href": "./weapon-fuse-entanglement.md"}, {"name": "Weapon Sheath Offset", "abbr": "WSO", "date": "2023-06-25", "tags": ["zuggling", "weapon", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["circyit", "dash"], "href": "./weapon-sheath-offset-wso.md"}, {"name": "Weapon Stacking Duplication", "abbr": "WSD", "date": "2023-05-16", "tags": ["duplication", "item", "weapon", "equipment", "bow"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["ErlingÚÖäÞ║½"], "href": "./weapon-stacking-duplication-wsd.md"}, {"name": "Weapon Stand Dynamic Zuggle", "abbr": "WSDZ", "date": "2024-03-14", "tags": ["zuggling", "weapon", "item", "equipment"], "versions": ["1.0.0"], "credits": ["WinnerBoi77"], "href": "./weapon-stand-dynamic-zuggle.md"}, {"name": "Weapon State Transfer", "abbr": "WST", "date": "2023-05-19", "tags": ["weapon", "fuse", "entanglement", "equipment", "item"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["BigDUCCO", "kurocat471", "ElDuende", "Mentor_Kurt"], "href": "./weapon-state-transfer-wst.md"}, {"name": "Weather Amnesia", "abbr": "WA", "date": "2023-06-25", "tags": ["environment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["pyuk"], "href": "./weather-amnesia-wa.md"}, {"name": "Wheel Warping", "abbr": "WW", "date": "2023-06-18", "tags": ["launching", "warping", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Mozz", "pyuk"], "href": "./wheel-warping.md"}, {"name": "Wheel Zoomy", "abbr": "WZ", "date": "2023-07-12", "tags": ["movement", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Solo_Turtle"], "href": "./wheel-zoomy-also-known-as-wheel-wacko-boingo.md"}, {"name": "Wireless Energy", "abbr": "WE", "date": "2023-07-11", "tags": ["equipment", "culling", "ultrahand", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["NaN Gogh"], "href": "./wireless-energy.md"}, {"name": "Wuggle", "abbr": "WGL", "date": "2023-12-29", "tags": ["zuggling", "item", "equipment", "culling"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ock", "ROBUXY2ND"], "href": "./wuggle-weird-zuggle.md"}, {"name": "Yee Fuse Entanglement", "abbr": "YEEFE", "date": "2024-02-20", "tags": ["entanglement", "culling", "fuse", "mineru"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Yee", "mulberry"], "href": "./yee-fuse-entanglement.md"}, {"name": "Zapshield", "abbr": "ZAP", "date": "2024-09-16", "tags": ["equipment", "culling", "fuse", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Aergyl"], "href": "./zapshield.md"}, {"name": "ZL Animation Reset", "abbr": "ZLAR", "date": "2024-01-21", "tags": ["animation", "equipment", "shield"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["NghtmaR3"], "href": "./zl-animation-reset-zlar.md"}, {"name": "Zoggle", "abbr": "ZOG", "date": "2024-01-04", "tags": ["zuggling", "ultrahand", "item", "equipment"], "versions": ["1.2.0", "1.2.1"], "credits": ["Ryan?", "Ock"], "href": "./zoggle.md"}, {"name": "Zonai Inventory Shift Dupe", "abbr": "ZISD", "date": "2023-07-10", "tags": ["duplication", "menu", "buff", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Ryan?", "quantim"], "href": "./zonai-inventory-shift-dupe-zisd.md"}, {"name": "Zonai Sort Duplication", "abbr": "ZSD", "date": "2023-05-22", "tags": ["duplication", "menu", "zonai"], "versions": ["1.0.0", "1.1.0", "1.1.1"], "credits": ["Quelfth", "Flash"], "href": "./zonai-sort-duplication-zsd.md"}, {"name": "Zonai Storage", "abbr": "ZS", "date": "2023-08-13", "tags": ["storage", "zonai"], "versions": ["1.0.0"], "credits": ["bebu0815"], "href": "./zonai-storage.md"}, {"name": "Zuggle Load Object Transfering", "abbr": "ZLOT", "date": "2023-06-07", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["InAMuffinCup", "ChargeVolt"], "href": "./zuggle-load-object-transfering-zlot.md"}, {"name": "Zuggle Overload Desync", "abbr": "ZOD", "date": "Unknown", "tags": ["zuggling", "desync", "menu", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Unknown"], "href": "./zuggle-overload-desync.md"}, {"name": "Zuggle Overload Out Of Bounds", "abbr": "ZOOB", "date": "2023-05-18", "tags": ["clipping", "oob", "zuggling", "overload"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2"], "credits": ["AngryEgg"], "href": "./zuggle-overload-out-of-bounds.md"}, {"name": "Zuggle Overload", "abbr": "ZO", "date": "2023-05-17", "tags": ["zuggling", "overload", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle-overload.md"}, {"name": "Zuggle", "abbr": "ZGL", "date": "2023-05-16", "tags": ["zuggling", "item", "equipment"], "versions": ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"], "credits": ["Zvleon"], "href": "./zuggle.md"}]
\ No newline at end of file
diff --git a/docs/assets/data/leaderboard-data.json b/docs/assets/data/leaderboard-data.json
deleted file mode 100644
index b424f9e55..000000000
--- a/docs/assets/data/leaderboard-data.json
+++ /dev/null
@@ -1,822 +0,0 @@
-{
-  "total": 136,
-  "updated": "2026-02-24",
-  "entries": [
-    {
-      "rank": 1,
-      "name": "mulberry",
-      "url": null,
-      "count": 57
-    },
-    {
-      "rank": 2,
-      "name": "Mozz",
-      "url": "https://www.youtube.com/@M0zzed",
-      "count": 47
-    },
-    {
-      "rank": 3,
-      "name": "Zas",
-      "url": null,
-      "count": 21
-    },
-    {
-      "rank": 4,
-      "name": "Ock",
-      "url": null,
-      "count": 17
-    },
-    {
-      "rank": 5,
-      "name": "Ryan?",
-      "url": null,
-      "count": 16
-    },
-    {
-      "rank": 6,
-      "name": "Aergyl",
-      "url": null,
-      "count": 13
-    },
-    {
-      "rank": 6,
-      "name": "Unknown",
-      "url": null,
-      "count": 13
-    },
-    {
-      "rank": 7,
-      "name": "NaN Gogh",
-      "url": "https://x.com/_nan_gogh",
-      "count": 12
-    },
-    {
-      "rank": 7,
-      "name": "NX721",
-      "url": null,
-      "count": 12
-    },
-    {
-      "rank": 8,
-      "name": "BigDUCCO",
-      "url": null,
-      "count": 10
-    },
-    {
-      "rank": 8,
-      "name": "Lightos",
-      "url": "https://www.youtube.com/@lightos_",
-      "count": 10
-    },
-    {
-      "rank": 8,
-      "name": "pyuk",
-      "url": null,
-      "count": 10
-    },
-    {
-      "rank": 8,
-      "name": "WinnerBoi77",
-      "url": null,
-      "count": 10
-    },
-    {
-      "rank": 9,
-      "name": "LegendofLinkk",
-      "url": null,
-      "count": 8
-    },
-    {
-      "rank": 9,
-      "name": "R4000",
-      "url": null,
-      "count": 8
-    },
-    {
-      "rank": 10,
-      "name": "Blackmars",
-      "url": null,
-      "count": 7
-    },
-    {
-      "rank": 10,
-      "name": "Flash",
-      "url": null,
-      "count": 7
-    },
-    {
-      "rank": 10,
-      "name": "NghtmaR3",
-      "url": null,
-      "count": 7
-    },
-    {
-      "rank": 10,
-      "name": "Telkic",
-      "url": null,
-      "count": 7
-    },
-    {
-      "rank": 11,
-      "name": "Physioninja",
-      "url": null,
-      "count": 5
-    },
-    {
-      "rank": 11,
-      "name": "ROBUXY2ND",
-      "url": null,
-      "count": 5
-    },
-    {
-      "rank": 11,
-      "name": "Yee",
-      "url": null,
-      "count": 5
-    },
-    {
-      "rank": 12,
-      "name": "Blize",
-      "url": "https://www.youtube.com/@blizegaming",
-      "count": 4
-    },
-    {
-      "rank": 12,
-      "name": "Jordan",
-      "url": null,
-      "count": 4
-    },
-    {
-      "rank": 12,
-      "name": "kurocat471",
-      "url": null,
-      "count": 4
-    },
-    {
-      "rank": 12,
-      "name": "Toti Sauce",
-      "url": null,
-      "count": 4
-    },
-    {
-      "rank": 12,
-      "name": "Zvleon",
-      "url": null,
-      "count": 4
-    },
-    {
-      "rank": 13,
-      "name": "Aeolian",
-      "url": null,
-      "count": 3
-    },
-    {
-      "rank": 13,
-      "name": "ElDuende",
-      "url": null,
-      "count": 3
-    },
-    {
-      "rank": 13,
-      "name": "InAMuffinCup",
-      "url": null,
-      "count": 3
-    },
-    {
-      "rank": 13,
-      "name": "MandelbrotChaylay",
-      "url": null,
-      "count": 3
-    },
-    {
-      "rank": 13,
-      "name": "Maxmasher",
-      "url": null,
-      "count": 3
-    },
-    {
-      "rank": 13,
-      "name": "PetitFrapo",
-      "url": null,
-      "count": 3
-    },
-    {
-      "rank": 13,
-      "name": "Simonfirefighter",
-      "url": null,
-      "count": 3
-    },
-    {
-      "rank": 14,
-      "name": "AngryEgg",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "ChargeVolt",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "circyit",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "Deystroyer",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "dt13269",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "EOH_NS_SS",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "evilgabe",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "eXe",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "FerrusCube",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "Ikaboze",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "KiloVictor",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "kirigaya",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "NicNac",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "ofstrings2",
-      "url": "https://www.youtube.com/channel/UCdJgWquwZxJlfc8rDMmmilA",
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "orionsayshi",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "quantim",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "Quelfth",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "sleepyppls",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "Squidwest",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "Steel",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "suusi",
-      "url": "https://www.youtube.com/channel/UCbUwlQ_88XfXD2bfU_4kxYg",
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "Syb",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "Tahata",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "Tauktes",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "ultrababouin",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 14,
-      "name": "Venaticus",
-      "url": null,
-      "count": 2
-    },
-    {
-      "rank": 15,
-      "name": "1789(@W0ERYySQgZyGOY3)",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "ab2x3z",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Abahbob",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "acaepius",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Aci",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "AgdoR",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Ame",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Arfix",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Armindo",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Asgorne",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "bebu0815",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Blizzard Blanc",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "blueberryoats",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "briochoc",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Bucket_Sloe",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Candlelor",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "CM30",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "CS16",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "DanielNeia",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "dash",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Deep",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Deltenic",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "DisguisedMoth",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Duncan",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "EM",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Emiya",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "ErlingÚÖäÞ║½",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "F. Buffalo",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "fabs",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "GamSla341",
-      "url": "https://www.youtube.com/@gamsla3413",
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Ikkitrix",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Infrasolid",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "KAIDUDE64",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Kaldemar",
-      "url": "https://www.youtube.com/@Kaldemar",
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Knight7108",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "KnightPohtaytoh",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "koreth",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "kurone_yuu",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Li Shen (Ú»ëþÑ×)",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Lopitty",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Luckstyle",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Mentor_Kurt",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Mety333",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Modoki_returns",
-      "url": "https://twitter.com/Modoki_returns",
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Moonrise",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "ness",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Owen",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Pistonight",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "ralseidewitt",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Redrooey",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Rhkellz",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "rocomox",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "s0ft",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Saria",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "SCFD-GK2",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "shio_0725",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Sillicat",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "SmallAnt",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Solo_Turtle",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "SteFen45",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Suishi",
-      "url": "https://www.youtube.com/@SuishiYT",
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Swinginman",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Takosensai1",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "The_Andromeda",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Timber",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "tori",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "tzakazuki",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Vee.Might.Exist",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Windocks",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Wip long sticks enjoyer",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Xeryph",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "ZombieBoy225",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "ÒüôÒéôÒüØÒéü",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "ÒüØÒéë-ÒüòÒéô",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "ÕìâÕ╣┤ÞîÂÚÑ╝",
-      "url": null,
-      "count": 1
-    },
-    {
-      "rank": 15,
-      "name": "Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª",
-      "url": null,
-      "count": 1
-    }
-  ]
-}
\ No newline at end of file
diff --git a/docs/worker/synonyms.json b/docs/assets/data/synonyms.json
similarity index 100%
rename from docs/worker/synonyms.json
rename to docs/assets/data/synonyms.json
diff --git a/docs/wiki/build_bm25_index.py b/docs/wiki/build_bm25_index.py
index 238704def..631552618 100644
--- a/docs/wiki/build_bm25_index.py
+++ b/docs/wiki/build_bm25_index.py
@@ -307,7 +307,7 @@ def build_grimoire_data(output: str):
       credits   ÔÇô frontmatter credits list
       href      ÔÇô relative link to the .md file, e.g. "./l-sprinting.md"
     """
-    _SKIP = {'glitchcraft-grimoire'}  # non-entry pages to exclude
+    _SKIP = {'_glitchcraft-grimoire'}  # non-entry pages to exclude
 
     glitchcraft_dir = ROOT / 'docs' / 'wiki' / 'glitchcraft'
     entries = []
diff --git a/docs/worker/worker.js b/docs/worker/worker.js
index 4627c821b..ddefe0c11 100644
--- a/docs/worker/worker.js
+++ b/docs/worker/worker.js
@@ -3,7 +3,7 @@
  */
 
 // Synonym sets extracted to JSON for easier editing and reuse
-import RAW_SYNONYM_SETS from './synonyms.json' assert { type: 'json' };
+import RAW_SYNONYM_SETS from '../assets/data/synonyms.json' assert { type: 'json' };
 
 // Increase TOP_K to collect more candidates (we'll deduplicate by path for evidence)
 const TOP_K = 12;

----

*** COMMIT: 7233852cdd66e89f67b45ec9f7e069c0f66dcca1
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 15:04:17 2026 +0100
Subject: fix: remove Cache-Control header from response in worker script

commit 7233852cdd66e89f67b45ec9f7e069c0f66dcca1
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 15:04:17 2026 +0100

    fix: remove Cache-Control header from response in worker script

diff --git a/docs/worker/worker.js b/docs/worker/worker.js
index ddefe0c11..1beecd1ca 100644
--- a/docs/worker/worker.js
+++ b/docs/worker/worker.js
@@ -112,7 +112,6 @@ export default {
         index = await fetchIndex(indexUrl);
         try{
           const resp = new Response(JSON.stringify(index), { headers: {'Content-Type':'application/json'} });
-          resp.headers.set('Cache-Control', 'public, max-age=3600');
           await caches.default.put(cacheKey, resp.clone());
         }catch(e){ /* ignore cache put failures */ }
       }

----

*** COMMIT: 787f078d3f63c69778d07e666231e030d4ee8538
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 15:08:10 2026 +0100
Subject: fix: set Cache-Control header for cached responses in worker script

commit 787f078d3f63c69778d07e666231e030d4ee8538
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 15:08:10 2026 +0100

    fix: set Cache-Control header for cached responses in worker script

diff --git a/docs/worker/worker.js b/docs/worker/worker.js
index 1beecd1ca..143f9b0d5 100644
--- a/docs/worker/worker.js
+++ b/docs/worker/worker.js
@@ -112,6 +112,7 @@ export default {
         index = await fetchIndex(indexUrl);
         try{
           const resp = new Response(JSON.stringify(index), { headers: {'Content-Type':'application/json'} });
+          resp.headers.set('Cache-Control', 'public, max-age=60');
           await caches.default.put(cacheKey, resp.clone());
         }catch(e){ /* ignore cache put failures */ }
       }

----

*** COMMIT: f93af1607f6760824ae38f7427380eb1ff5a0131
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 15:12:17 2026 +0100
Subject: feat: add video demonstration to Laser-OOB and image demonstration to Zuggle Overload OOB

commit f93af1607f6760824ae38f7427380eb1ff5a0131
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 15:12:17 2026 +0100

    feat: add video demonstration to Laser-OOB and image demonstration to Zuggle Overload OOB

diff --git a/docs/wiki/glitchcraft/laser-oob.md b/docs/wiki/glitchcraft/laser-oob.md
index 8577cc1c8..99b4f95ad 100644
--- a/docs/wiki/glitchcraft/laser-oob.md
+++ b/docs/wiki/glitchcraft/laser-oob.md
@@ -30,3 +30,5 @@ You need a laser nearby.
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1107045488454279188)
 - [YouTube](https://www.youtube.com/watch?v=oBYBi8dqflI)
+
+<video controls><source src="https://cdn.discordapp.com/attachments/1105598687167664239/1107045487787380836/clip.mp4?ex=699eb634&is=699d64b4&hm=a77d6181588a1da01d24bbb68e75005afed94e9b36eb6024049bc834f837cb0d&" type="video/mp4"></video>
diff --git a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
index 4e1497c62..b6ce78600 100644
--- a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
+++ b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
@@ -33,6 +33,8 @@ _AngryEgg - 18 May 2023_
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108780208137437314)
 - [YouTube](https://www.youtube.com/watch?v=w1fI3QYrerQ)
 
+![ZOOB demonstration](https://cdn.discordapp.com/attachments/1105598687167664239/1108780207827079218/image.png?ex=699e6e49&is=699d1cc9&hm=ff5b33c53a5d61adb428f0b0c72460e41afb947cbb691fb5791783506d4b3fdd&)
+
 ## Related
 ---
 - [Zuggle Overload](search:Zuggle Overload)

----

*** COMMIT: 50f3117b65b0aed71ec5f4c3025092033da7074d
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 15:20:22 2026 +0100
Subject: Update glitchcraft documentation with new sections and formatting improvements

commit 50f3117b65b0aed71ec5f4c3025092033da7074d
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 15:20:22 2026 +0100

    Update glitchcraft documentation with new sections and formatting improvements
    
    - Added "Related" sections to multiple pages for better navigation.
    - Standardized front matter formatting across various markdown files.
    - Corrected encoding issues in author names and other text.
    - Enhanced resource links and descriptions for clarity.
    - Improved overall consistency in documentation structure.

diff --git a/docs/wiki/glitchcraft/ability-wheel-loop.md b/docs/wiki/glitchcraft/ability-wheel-loop.md
index b6bf390e7..1f38de0c8 100644
--- a/docs/wiki/glitchcraft/ability-wheel-loop.md
+++ b/docs/wiki/glitchcraft/ability-wheel-loop.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Ability Wheel Loop"
 abbreviation: "AWL"
 versions: ["1.0.0"]
@@ -28,8 +28,12 @@ if the timing was right the ability wheel will come up right after the dpad menu
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1216873236248395896)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/aeroculling.md b/docs/wiki/glitchcraft/aeroculling.md
index 00a4c9191..c8bc61513 100644
--- a/docs/wiki/glitchcraft/aeroculling.md
+++ b/docs/wiki/glitchcraft/aeroculling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Aeroculling"
 abbreviation: "AC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -49,3 +49,7 @@ Once AC is set up, in order to Physical AC, put a SDC in the wind and the base o
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1283455775976718346)
 - [YouTube](https://www.youtube.com/watch?v=o-9HO3NbfPU)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/anti-gravity-glitch.md b/docs/wiki/glitchcraft/anti-gravity-glitch.md
index 50f73c511..73466bb4b 100644
--- a/docs/wiki/glitchcraft/anti-gravity-glitch.md
+++ b/docs/wiki/glitchcraft/anti-gravity-glitch.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Anti-Gravity Glitch"
 abbreviation: "AGG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -29,3 +29,7 @@ Todo: Find other places where this glitch could be replicated (maybe on the Grea
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=109kaxFj8FQ)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/anti-gravity-objects.md b/docs/wiki/glitchcraft/anti-gravity-objects.md
index fbcb8ba29..f389b15b8 100644
--- a/docs/wiki/glitchcraft/anti-gravity-objects.md
+++ b/docs/wiki/glitchcraft/anti-gravity-objects.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Anti-Gravity Objects"
 abbreviation: "AGO"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -26,8 +26,12 @@ _?_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1113306645854945303)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/antigrav-weapons.md b/docs/wiki/glitchcraft/antigrav-weapons.md
index 0fdd2570d..6cc9c4c57 100644
--- a/docs/wiki/glitchcraft/antigrav-weapons.md
+++ b/docs/wiki/glitchcraft/antigrav-weapons.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "AntiGrav Weapons"
 abbreviation: "AGW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -42,3 +42,7 @@ It will obtain the property of anti-gravity unless you un-equip it or throw it.
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1112349555606966292)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1112355745321713754)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/arrow-smuggling.md b/docs/wiki/glitchcraft/arrow-smuggling.md
index 7cd7967a8..d29979fcb 100644
--- a/docs/wiki/glitchcraft/arrow-smuggling.md
+++ b/docs/wiki/glitchcraft/arrow-smuggling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Arrow Smuggling"
 abbreviation: "ASMU"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -42,3 +42,7 @@ Update this entry
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1116843954126737461)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1114980377514217482)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1114982170310754345)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/arrow-unloading.md b/docs/wiki/glitchcraft/arrow-unloading.md
index 4c61bd8da..b1a47d271 100644
--- a/docs/wiki/glitchcraft/arrow-unloading.md
+++ b/docs/wiki/glitchcraft/arrow-unloading.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Arrow Unloading"
 abbreviation: "AU"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -42,3 +42,7 @@ Arrows fired from a multi-shot bow are warped to 0,0,0.
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1118827552497217576)
 - [YouTube](https://www.youtube.com/watch?v=MDNuNpKpi9U)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/ascend-camera-glitch.md b/docs/wiki/glitchcraft/ascend-camera-glitch.md
index 1e0aa0afc..4e47d219a 100644
--- a/docs/wiki/glitchcraft/ascend-camera-glitch.md
+++ b/docs/wiki/glitchcraft/ascend-camera-glitch.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Ascend Camera Glitch"
 abbreviation: "ACG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -26,8 +26,12 @@ _?_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
+├óÔé¼ÔÇØ
+
+## Related
+---
 ÔÇö
diff --git a/docs/wiki/glitchcraft/ascend-rushing.md b/docs/wiki/glitchcraft/ascend-rushing.md
index 2bc64651c..d1bf52abb 100644
--- a/docs/wiki/glitchcraft/ascend-rushing.md
+++ b/docs/wiki/glitchcraft/ascend-rushing.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Ascend Rushing"
 abbreviation: "AR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -25,9 +25,13 @@ _R4000 - 15 June 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1119057121611362317)
 - [YouTube](https://www.youtube.com/watch?v=jEkCy9NzbBk)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/ascend-storage.md b/docs/wiki/glitchcraft/ascend-storage.md
index 928a2a2c2..4798cca19 100644
--- a/docs/wiki/glitchcraft/ascend-storage.md
+++ b/docs/wiki/glitchcraft/ascend-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Ascend Storage"
 abbreviation: "ASTR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -35,3 +35,7 @@ _Saria - 19 May 2023_
 ## Resources
 ---
 - [Twitter](https://twitter.com/reaperhide/status/1659593296774299648)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/autobuild-cancel-slide.md b/docs/wiki/glitchcraft/autobuild-cancel-slide.md
index 8c41f6073..9943efd50 100644
--- a/docs/wiki/glitchcraft/autobuild-cancel-slide.md
+++ b/docs/wiki/glitchcraft/autobuild-cancel-slide.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Autobuild Cancel Slide"
 abbreviation: "ABCS"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
@@ -43,3 +43,7 @@ On 1.0.0, the speed that can be achieved is much slower than what is seen on 1.1
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108851384239009912)
 - [YouTube](https://www.youtube.com/watch?v=3DHEaqoDl1M)
 - [Twitter](https://twitter.com/PowerGaymerKai/status/1659292261572829184)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/autobuild-duplication.md b/docs/wiki/glitchcraft/autobuild-duplication.md
index 8177d3190..7d69a3225 100644
--- a/docs/wiki/glitchcraft/autobuild-duplication.md
+++ b/docs/wiki/glitchcraft/autobuild-duplication.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Autobuild Duplication"
 abbreviation: "ABD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -31,8 +31,12 @@ This only works with items that change into other items in another temperature.
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=IfRlldenZNc)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/autobuild-storage.md b/docs/wiki/glitchcraft/autobuild-storage.md
index eb0222a4a..a7c1d9b3b 100644
--- a/docs/wiki/glitchcraft/autobuild-storage.md
+++ b/docs/wiki/glitchcraft/autobuild-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Autobuild Storage"
 abbreviation: "ABST"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -34,3 +34,7 @@ Can do launches with Octo Balloons and pulling items towards the Like Like's loc
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1145897049963892797)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1147602597168029728)
 - [YouTube](https://www.youtube.com/watch?v=u3ke0m3VNFA)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/back-in-time-art.md b/docs/wiki/glitchcraft/back-in-time-art.md
index bcd0e07e3..eaf81b425 100644
--- a/docs/wiki/glitchcraft/back-in-time-art.md
+++ b/docs/wiki/glitchcraft/back-in-time-art.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Back-in-Time Art"
 abbreviation: "BIT"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -32,9 +32,13 @@ Compendium pictures (Zas):
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=DWA_cTNykyo)
 - [Twitter](https://vxtwitter.com/zasbotw/status/1692295854173167930)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/back-to-back-bloodmoon.md b/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
index 8d7346e0d..857b14472 100644
--- a/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
+++ b/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Back to Back Bloodmoon"
 abbreviation: "BTBB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -20,12 +20,16 @@ _Lopitty - 17 May 2023_
 
 ## Instructions
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=60mI9DLo_vw)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/banc-storage.md b/docs/wiki/glitchcraft/banc-storage.md
index 29b44479c..20080faae 100644
--- a/docs/wiki/glitchcraft/banc-storage.md
+++ b/docs/wiki/glitchcraft/banc-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Banc Storage"
 abbreviation: "BANC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1",]
@@ -52,10 +52,14 @@ Instructions for 1.1+:
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1290703223467937898)
 - [Video guide to the 1.0 method](https://www.youtube.com/watch?v=RmjZKVGvstE)
 - [Demonstration of the 1.4.2 method](https://www.youtube.com/watch?v=EP8FkHYkqks)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/bomb-skew.md b/docs/wiki/glitchcraft/bomb-skew.md
index 0b1332fb9..c23bb9109 100644
--- a/docs/wiki/glitchcraft/bomb-skew.md
+++ b/docs/wiki/glitchcraft/bomb-skew.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Bomb Skew"
 abbreviation: "BSK"
 versions: ["1.0.0"]
@@ -25,9 +25,13 @@ _Aergyl, FerrusCube, Mozz - 21 September 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598254198050947/1154554443644293171)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598254198050947/1154555245830086706)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/bow-attachment-desync-bad-arrows.md b/docs/wiki/glitchcraft/bow-attachment-desync-bad-arrows.md
index 8fbac757a..ec9651dfc 100644
--- a/docs/wiki/glitchcraft/bow-attachment-desync-bad-arrows.md
+++ b/docs/wiki/glitchcraft/bow-attachment-desync-bad-arrows.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Bow Attachment Desync"
 abbreviation: "BAD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -43,3 +43,7 @@ On 1.1.0-1.1.2 only the last material is consumed.
 - [Twitter](https://twitter.com/zasoot/status/1678779155310338053)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1128344687825133649)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1128344687825133649%20(Aeolian%20with%201.0.0%20item%20drop))
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/bow-attachment-storage.md b/docs/wiki/glitchcraft/bow-attachment-storage.md
index e952946f4..e316b162b 100644
--- a/docs/wiki/glitchcraft/bow-attachment-storage.md
+++ b/docs/wiki/glitchcraft/bow-attachment-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Bow Attachment Storage"
 abbreviation: "BAS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -48,3 +48,7 @@ A variant of this glitch can be done using zuggle overload (has been known for a
 - [Discord](https://discord.com/channels/1086729144307564648/1109838351596527726/1180885814230655017)
 - [Discord](https://discord.com/channels/1086729144307564648/1109838351596527726/1180883442636955718)
 - [Twitter](https://vxtwitter.com/zasbotw/status/1731339526008963191)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/buoy-bouncing.md b/docs/wiki/glitchcraft/buoy-bouncing.md
index f8e7c723d..7c5fae265 100644
--- a/docs/wiki/glitchcraft/buoy-bouncing.md
+++ b/docs/wiki/glitchcraft/buoy-bouncing.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Buoy Bouncing"
 abbreviation: "BB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -30,3 +30,7 @@ Initial velocity seems to play an effect when buoy bouncing, such as when fallin
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1106412847359082506/1111400160879194165)
 - [Discord](https://discord.com/channels/1086729144307564648/1106412847359082506/1111400160879194165)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/camera-cfw.md b/docs/wiki/glitchcraft/camera-cfw.md
index 37eaa50c0..6dda48215 100644
--- a/docs/wiki/glitchcraft/camera-cfw.md
+++ b/docs/wiki/glitchcraft/camera-cfw.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Camera CFW"
 abbreviation: "CFW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -42,8 +42,12 @@ no camera ui
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Twitter](https://vxtwitter.com/_nan_gogh/status/1678749376833781763?s=46)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/camera-pose-glitch.md b/docs/wiki/glitchcraft/camera-pose-glitch.md
index 528251e9a..a3ff9f691 100644
--- a/docs/wiki/glitchcraft/camera-pose-glitch.md
+++ b/docs/wiki/glitchcraft/camera-pose-glitch.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Camera Pose Glitch"
 abbreviation: "CPG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -27,8 +27,12 @@ _?_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1196121825160212571)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/capsule-cel-shader-removal.md b/docs/wiki/glitchcraft/capsule-cel-shader-removal.md
index ed3f85478..b88bf3ddb 100644
--- a/docs/wiki/glitchcraft/capsule-cel-shader-removal.md
+++ b/docs/wiki/glitchcraft/capsule-cel-shader-removal.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Capsule Cel Shader Removal"
 abbreviation: "CCSR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -32,3 +32,7 @@ And one black layer that shows the base model
 ## Resources
 ---
 - [Twitter](https://x.com/NX721_/status/1731784487636443229?s=20)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/chasm-delay-zuggle.md b/docs/wiki/glitchcraft/chasm-delay-zuggle.md
index 691ab7950..090176518 100644
--- a/docs/wiki/glitchcraft/chasm-delay-zuggle.md
+++ b/docs/wiki/glitchcraft/chasm-delay-zuggle.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Chasm Delay Zuggle"
 abbreviation: "CDZ"
 versions: ["1.2.0", "1.2.1"]
@@ -48,3 +48,7 @@ Mastersword zuggle (Ock)
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1246004390062587944)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/clear-camera-scope.md b/docs/wiki/glitchcraft/clear-camera-scope.md
index c93d3b41f..5664df19e 100644
--- a/docs/wiki/glitchcraft/clear-camera-scope.md
+++ b/docs/wiki/glitchcraft/clear-camera-scope.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Clear Camera/Scope"
 abbreviation: "CCS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,3 +33,7 @@ how was this not found
 ---
 - [Twitter](https://twitter.com/NX721_/status/1681732748476596344)
 - [Twitter](https://twitter.com/NX721_/status/1681732748476596344)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/corrupt-meal.md b/docs/wiki/glitchcraft/corrupt-meal.md
index 3626a7212..b5a9cb365 100644
--- a/docs/wiki/glitchcraft/corrupt-meal.md
+++ b/docs/wiki/glitchcraft/corrupt-meal.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Corrupt Meal"
 abbreviation: "CM"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,3 +33,7 @@ If no other foods have been cooked since last boot, nothing will be cooked and t
 - [Discord](https://discordapp.com/channels/1086729144307564648/1110956205624532993/1337566200418537554)
 - [Discord](https://discordapp.com/channels/1086729144307564648/1110956205624532993/1337605400777719931)
 - [Discord](https://discordapp.com/channels/1086729144307564648/1110956205624532993/1337612908300865617)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/cucco-warping.md b/docs/wiki/glitchcraft/cucco-warping.md
index 907cb7788..9a0180f49 100644
--- a/docs/wiki/glitchcraft/cucco-warping.md
+++ b/docs/wiki/glitchcraft/cucco-warping.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Cucco Warping"
 abbreviation: "CW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -25,8 +25,12 @@ _onion - 23 July 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1132767408696852541)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/cull-zone-culling.md b/docs/wiki/glitchcraft/cull-zone-culling.md
index 77376cc86..15d0a124e 100644
--- a/docs/wiki/glitchcraft/cull-zone-culling.md
+++ b/docs/wiki/glitchcraft/cull-zone-culling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Cull Zone Culling"
 abbreviation: "CZC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -34,3 +34,7 @@ Certain sub-areas such as caves can also act as cull zones.
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1123379490408636507)
 - [TotK Object Map](https://objmap-totk.zeldamods.org/#/map/z3,0,0,Surface)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/dispenser-storage.md b/docs/wiki/glitchcraft/dispenser-storage.md
index b45499503..e53516c0a 100644
--- a/docs/wiki/glitchcraft/dispenser-storage.md
+++ b/docs/wiki/glitchcraft/dispenser-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Dispenser Storage"
 abbreviation: "DISP"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -20,7 +20,7 @@ _Mozz - 2 July 2023_
 
 ## Instructions
 ---
-1. Put a heavy item that doesnÔÇÖt slide much into a Zonai dispenser. 
+1. Put a heavy item that doesn├óÔé¼Ôäót slide much into a Zonai dispenser. 
 2. The dispenser hatch should remain open, otherwise try again.
 3. Take out a stabilizer and activate it.
 4. Using Ultrahand, place the stabilizer into the hatch opening, this should keep it open indefinetley
@@ -38,3 +38,7 @@ Two Fans fused at a 45 degree angle can be used to block the Dispenser, avoiding
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1125043115397484596)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1125069475541164032)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/display-duping.md b/docs/wiki/glitchcraft/display-duping.md
index 1002e999c..dfcde1066 100644
--- a/docs/wiki/glitchcraft/display-duping.md
+++ b/docs/wiki/glitchcraft/display-duping.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Display Duping"
 abbreviation: "DD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -30,3 +30,7 @@ Since this deletes the last equipment, consider placing the desired equipment la
 ---
 - [Twitter](https://twitter.com/i_piston/status/1662365886525870080)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1112078050000117900)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/display-master-sword.md b/docs/wiki/glitchcraft/display-master-sword.md
index 5a6188e3a..1d43a503b 100644
--- a/docs/wiki/glitchcraft/display-master-sword.md
+++ b/docs/wiki/glitchcraft/display-master-sword.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Display Master Sword"
 abbreviation: "DMS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -33,3 +33,7 @@ For MsgNotFound you don't need to drop it out of recall
 ---
 - [Twitter](https://twitter.com/zasbotw/status/1666751564743315456)
 - [Twitter](https://twitter.com/zasbotw/status/1666751564743315456)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/dive-cancel-glide-boost.md b/docs/wiki/glitchcraft/dive-cancel-glide-boost.md
index a7aaef15c..cd8f5720a 100644
--- a/docs/wiki/glitchcraft/dive-cancel-glide-boost.md
+++ b/docs/wiki/glitchcraft/dive-cancel-glide-boost.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Dive Cancel Glide Boost"
 abbreviation: "DCGB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -35,3 +35,7 @@ Doesn't stack well with Tulin's ability. Can be maintained with Infinite Height.
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=oIzJKQAWPdI)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/double-tulin-boost.md b/docs/wiki/glitchcraft/double-tulin-boost.md
index e524f51f9..b9e99872a 100644
--- a/docs/wiki/glitchcraft/double-tulin-boost.md
+++ b/docs/wiki/glitchcraft/double-tulin-boost.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Double Tulin Boost"
 abbreviation: "DTB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -29,3 +29,7 @@ This glitch may be removed from the spreasheet in the future, it is just tulin p
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108375175222796348)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/double-unfuse-duplicashen.md b/docs/wiki/glitchcraft/double-unfuse-duplicashen.md
index fa11b3cf5..fcda9e96c 100644
--- a/docs/wiki/glitchcraft/double-unfuse-duplicashen.md
+++ b/docs/wiki/glitchcraft/double-unfuse-duplicashen.md
@@ -1,8 +1,8 @@
----
+´╗┐---
 title: "Double Unfuse Duplicashen"
 abbreviation: "DUD"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
-credits: ["Li Shen (Ú»ëþÑ×)"]
+credits: ["Li Shen (├®┬»ÔÇ░├º┬Ñ┼¥)"]
 date: "2023-05-15"
 description: "Allows you to duplicate any material that can be fused to an arrow"
 aliases: ["double unfuse", "double unfuse duplicashen", "dupe unfuse"]
@@ -16,7 +16,7 @@ tags: ["duplication", "item", "weapon", "fuse", "arrow"]
 ---
 allows you to duplicate any material that can be fused to an arrow
 
-_Li Shen (Ú»ëþÑ×) - 15 May 2023_
+_Li Shen (├®┬»ÔÇ░├º┬Ñ┼¥) - 15 May 2023_
 
 ## Instructions
 ---
@@ -38,3 +38,7 @@ Stops working if cooked meals page is full
 ---
 - [Bilibili](https://www.bilibili.com/video/BV19h4y147iR/)
 - [YouTube](https://www.youtube.com/watch?v=0sRvQzU2j5w)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md b/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md
index 987d66577..d011cdc5a 100644
--- a/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md
+++ b/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Dpadlock-less Invizuggle"
 abbreviation: "DLI"
 versions: ["1.2.0", "1.2.1"]
@@ -46,9 +46,13 @@ If you want to zlot an item with invizuggle, you can do the following:
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1262927638683582505)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1263286685198712883)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/drop-restriction.md b/docs/wiki/glitchcraft/drop-restriction.md
index 69aa25aa8..8a751b4e5 100644
--- a/docs/wiki/glitchcraft/drop-restriction.md
+++ b/docs/wiki/glitchcraft/drop-restriction.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Drop Restriction"
 abbreviation: "DR"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
@@ -35,3 +35,7 @@ Only way to cancel it is by closing the game.
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1120378339442556990)
 - [YouTube](https://www.youtube.com/watch?v=V6ZeZmfpvEI)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/drop-smuggling.md b/docs/wiki/glitchcraft/drop-smuggling.md
index 6aef103a6..cee3f390c 100644
--- a/docs/wiki/glitchcraft/drop-smuggling.md
+++ b/docs/wiki/glitchcraft/drop-smuggling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Drop Smuggling"
 abbreviation: "DSMU"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -36,3 +36,7 @@ The weapons hitbox remains constantly active, while being maintained at Links fe
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1113469513011310716)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1113455975039512626)
 - [YouTube](https://www.youtube.com/watch?v=LWPbxaZcpCo)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/durability.md b/docs/wiki/glitchcraft/durability.md
index 1c39f4f8d..c2cbc5049 100644
--- a/docs/wiki/glitchcraft/durability.md
+++ b/docs/wiki/glitchcraft/durability.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Durability-"
 abbreviation: "DUR"
 versions: ["1.0.0"]
@@ -29,3 +29,7 @@ For some reason, the game only removes durability if it's considered a cold drop
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1150849925140197517)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/dynamic-zuggle.md b/docs/wiki/glitchcraft/dynamic-zuggle.md
index f9a7eaf24..f9fe95ea8 100644
--- a/docs/wiki/glitchcraft/dynamic-zuggle.md
+++ b/docs/wiki/glitchcraft/dynamic-zuggle.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Dynamic Zuggle"
 abbreviation: "DZG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -66,3 +66,7 @@ Method 3 (WinnerBoi77 & Ryan):
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1149037981181689936)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1218667308671832134)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1218672345749913642)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/enemy-pickpocketing.md b/docs/wiki/glitchcraft/enemy-pickpocketing.md
index 2e9b6d0ad..64878977a 100644
--- a/docs/wiki/glitchcraft/enemy-pickpocketing.md
+++ b/docs/wiki/glitchcraft/enemy-pickpocketing.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Enemy Pickpocketing"
 abbreviation: "EP"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -27,10 +27,14 @@ _KAIDUDE64 - 16 September 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1152798657419157626)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1152799909666377808)
 - [YouTube](https://www.youtube.com/watch?v=nmFfZ_MZ34M)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/equipment-smuggle.md b/docs/wiki/glitchcraft/equipment-smuggle.md
index c35ed4b41..f67081577 100644
--- a/docs/wiki/glitchcraft/equipment-smuggle.md
+++ b/docs/wiki/glitchcraft/equipment-smuggle.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Equipment Smuggle"
 abbreviation: "ESMU"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -36,3 +36,7 @@ On 1.2.0 and 1.2.1, equipping an item of the same type as a smuggle causes the s
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1113917918422511776)
 - [Twitter](https://twitter.com/goghnan/status/1664921192527020033?s=46)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/extended-throw-sprinting.md b/docs/wiki/glitchcraft/extended-throw-sprinting.md
index 1ef0920d3..92f55f141 100644
--- a/docs/wiki/glitchcraft/extended-throw-sprinting.md
+++ b/docs/wiki/glitchcraft/extended-throw-sprinting.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Extended Throw Sprinting"
 abbreviation: "ETS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -22,9 +22,13 @@ Hold B, tap R, repeat
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1106610982379323492)
 - [YouTube](https://www.youtube.com/watch?v=uM4o7rmSbwc)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/floorping.md b/docs/wiki/glitchcraft/floorping.md
index aeae8ade3..cd2e48f7f 100644
--- a/docs/wiki/glitchcraft/floorping.md
+++ b/docs/wiki/glitchcraft/floorping.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Floorping"
 abbreviation: "FLP"
 versions: ["1.1.0", "1.1.1"]
@@ -30,3 +30,7 @@ Test on more versions
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1191838704646488145)
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1193252888064040981)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/food-ability-buff-swap.md b/docs/wiki/glitchcraft/food-ability-buff-swap.md
index ca0de1fea..b9007af5f 100644
--- a/docs/wiki/glitchcraft/food-ability-buff-swap.md
+++ b/docs/wiki/glitchcraft/food-ability-buff-swap.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Food Ability Buff Swap"
 abbreviation: "FABS"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
@@ -40,3 +40,7 @@ These are all the places you can obtain cooked food to perform with FABS:
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108032859811348631)
 - [YouTube](https://www.youtube.com/watch?v=UurzVka6G9M)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/forced-blood-moon.md b/docs/wiki/glitchcraft/forced-blood-moon.md
index 2120be149..613c76539 100644
--- a/docs/wiki/glitchcraft/forced-blood-moon.md
+++ b/docs/wiki/glitchcraft/forced-blood-moon.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Forced Blood Moon"
 abbreviation: "FBM"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -40,3 +40,7 @@ Bullet time is not always needed and other gems could work too. There are many w
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1134025370279104532)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1119272037215649872)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1119307782433280110)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/fuse-entanglement.md b/docs/wiki/glitchcraft/fuse-entanglement.md
index 889006862..08a98eec3 100644
--- a/docs/wiki/glitchcraft/fuse-entanglement.md
+++ b/docs/wiki/glitchcraft/fuse-entanglement.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Fuse Entanglement"
 abbreviation: "FE"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -59,3 +59,7 @@ Recall a thrown object (needs to by thrown by an enemy), then fuse it
 - [Twitter](https://vxtwitter.com/_nan_gogh/status/1668449729305296899?s=46(Antighost)
 - [Twitter](https://vxtwitter.com/_nan_gogh/status/1677819049235951617?s=46)
 - [Discord](https://discord.com/channels/1086729144307564648/1128894970653327401/1148262809277313035)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/glue-removal.md b/docs/wiki/glitchcraft/glue-removal.md
index c7cafd48f..31e460f4c 100644
--- a/docs/wiki/glitchcraft/glue-removal.md
+++ b/docs/wiki/glitchcraft/glue-removal.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Glue Removal"
 abbreviation: "GR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -34,3 +34,7 @@ Doesn't work with every object
 ---
 - [Google Drive](https://drive.google.com/file/d/1XP7dg6aCd-34AH5v-_AsbVoz2oDoo5vJ/view?usp=drive_link)
 - [Google Drive](https://drive.google.com/drive/folders/15l1DDx1-64bO43FeUr2-2NtpeY58a79A?usp=sharing)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/guard-less-active-shield.md b/docs/wiki/glitchcraft/guard-less-active-shield.md
index ae680e342..435caaf3c 100644
--- a/docs/wiki/glitchcraft/guard-less-active-shield.md
+++ b/docs/wiki/glitchcraft/guard-less-active-shield.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Guard-less Active Shield"
 abbreviation: "GAS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -41,3 +41,7 @@ Can be achieved via Fuse Entanglement Drop Smuggling either a shield or a weapon
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1118279347325894746)
 - [Discord](https://discordapp.com/channels/1086729144307564648/1105598687167664239/1149978844573487156)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md b/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
index 2522feba0..e55ad309b 100644
--- a/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
+++ b/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Hand Locked Equipment Smuggling"
 abbreviation: "HLES"
 versions: ["1.0.0"]
@@ -33,4 +33,8 @@ Hand locked smuggling can also be performed using runes, two handed weapon and h
 
 ## Resources
 ---
+├óÔé¼ÔÇØ
+
+## Related
+---
 ÔÇö
diff --git a/docs/wiki/glitchcraft/handy-job.md b/docs/wiki/glitchcraft/handy-job.md
index 0e021c546..7e7043637 100644
--- a/docs/wiki/glitchcraft/handy-job.md
+++ b/docs/wiki/glitchcraft/handy-job.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Handy Job"
 abbreviation: "HJ"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -32,3 +32,7 @@ Does not repair a weapon's fuse durability if an item has been fused to it previ
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1176267847220076595)
 - [YouTube](https://www.youtube.com/watch?v=a0slhXe6jzU)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/hero-path-link-storage.md b/docs/wiki/glitchcraft/hero-path-link-storage.md
index b0a77d935..307f605e9 100644
--- a/docs/wiki/glitchcraft/hero-path-link-storage.md
+++ b/docs/wiki/glitchcraft/hero-path-link-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Hero Path Link Storage"
 abbreviation: "HPLS"
 versions: ["1.1.0", "1.1.1", "1.1.2"]
@@ -32,3 +32,7 @@ Persists through file loads and warps but opening the hero path or return to tit
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1120781144976261210)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1120786260483641414)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/hestu-scamming.md b/docs/wiki/glitchcraft/hestu-scamming.md
index ef303bba4..09133908b 100644
--- a/docs/wiki/glitchcraft/hestu-scamming.md
+++ b/docs/wiki/glitchcraft/hestu-scamming.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Hestu Scamming"
 abbreviation: "HSCA"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -35,10 +35,14 @@ Prerequisites:
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1230669568066846741)
 - [YouTube](https://www.youtube.com/watch?v=oRo_1R9d_-w)
 - [YouTube](https://www.youtube.com/watch?v=sJdmYu9j1FI)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/hold-smuggling.md b/docs/wiki/glitchcraft/hold-smuggling.md
index 8b345ec91..e14209da1 100644
--- a/docs/wiki/glitchcraft/hold-smuggling.md
+++ b/docs/wiki/glitchcraft/hold-smuggling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Hold Smuggling"
 abbreviation: "HSM"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -36,3 +36,7 @@ Also removes HUD from Sheikah Scope
 ## Resources
 ---
 - [Twitter](https://twitter.com/_nan_gogh/status/1676384792818995200)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/infinite-balloon.md b/docs/wiki/glitchcraft/infinite-balloon.md
index 2dc4f0eaa..4202f2a7f 100644
--- a/docs/wiki/glitchcraft/infinite-balloon.md
+++ b/docs/wiki/glitchcraft/infinite-balloon.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Infinite Balloon"
 abbreviation: "IBAL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,3 +33,7 @@ There are many NPCs that can be put into this weird rolling state.
 ## Resources
 ---
 - [Twitter](https://x.com/kurone_yuu/status/1801239224378900947?s=46&t=DdtmlnCQqIbD5irw-jnKbQ)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/infinite-bubbul-frog-gems.md b/docs/wiki/glitchcraft/infinite-bubbul-frog-gems.md
index f3e7db99a..ff7a8e41d 100644
--- a/docs/wiki/glitchcraft/infinite-bubbul-frog-gems.md
+++ b/docs/wiki/glitchcraft/infinite-bubbul-frog-gems.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Infinite Bubbul Frog Gems"
 abbreviation: "IBFG"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
@@ -38,3 +38,7 @@ Needs to be tested more, and see if it can be consistently replicated.
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=c9TDP4qdAUY)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/infinite-damage.md b/docs/wiki/glitchcraft/infinite-damage.md
index 4f8092845..d0bc7649c 100644
--- a/docs/wiki/glitchcraft/infinite-damage.md
+++ b/docs/wiki/glitchcraft/infinite-damage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Infinite Damage"
 abbreviation: "IDMG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -31,3 +31,7 @@ Todo: Replicate in TotK, test in BotW.
 - [YouTube](https://www.youtube.com/watch?v=Q1aWa0Kg-8Y)
 - [Reddit](https://www.reddit.com/r/TOTK/comments/13tho3e)
 - [Twitter](https://twitter.com/ThatOneNerd0329/status/1662590423582535680)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/inventory-shift-duplication.md b/docs/wiki/glitchcraft/inventory-shift-duplication.md
index ee51a9ab1..43e07fff2 100644
--- a/docs/wiki/glitchcraft/inventory-shift-duplication.md
+++ b/docs/wiki/glitchcraft/inventory-shift-duplication.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Inventory Shift Duplication"
 abbreviation: "ISD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -33,3 +33,7 @@ The item that gets duplicated will always be to the right of the item you are ho
 ---
 - [Twitter](https://vxtwitter.com/zb_yuhudaddy/status/1673184858628296704?s=20)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1122835952423944282)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/invizuggle.md b/docs/wiki/glitchcraft/invizuggle.md
index 26d4af412..1182dea45 100644
--- a/docs/wiki/glitchcraft/invizuggle.md
+++ b/docs/wiki/glitchcraft/invizuggle.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Invizuggle"
 abbreviation: "IVZ"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -78,3 +78,7 @@ Add Method 5
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1192403098753310770)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1195821216326488264)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/item-throw-hitbox-disable.md b/docs/wiki/glitchcraft/item-throw-hitbox-disable.md
index 3219ddcc4..79e5bd94c 100644
--- a/docs/wiki/glitchcraft/item-throw-hitbox-disable.md
+++ b/docs/wiki/glitchcraft/item-throw-hitbox-disable.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Item Throw Hitbox Disable"
 abbreviation: "ITHD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -26,4 +26,8 @@ Impact triggered items can still go off if hit by an explosion. For Bomb Flowers
 
 ## Resources
 ---
+├óÔé¼ÔÇØ
+
+## Related
+---
 ÔÇö
diff --git a/docs/wiki/glitchcraft/jumpslash-canceling.md b/docs/wiki/glitchcraft/jumpslash-canceling.md
index 599eaa38c..eab22450f 100644
--- a/docs/wiki/glitchcraft/jumpslash-canceling.md
+++ b/docs/wiki/glitchcraft/jumpslash-canceling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Jumpslash Canceling"
 abbreviation: "JSC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,3 +33,7 @@ Jumpslash Cancel Clipping
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1110002512074907740)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1110004852823703552)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/laser-oob.md b/docs/wiki/glitchcraft/laser-oob.md
index 99b4f95ad..d34599d8e 100644
--- a/docs/wiki/glitchcraft/laser-oob.md
+++ b/docs/wiki/glitchcraft/laser-oob.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Laser-OOB"
 abbreviation: "LOOB"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
@@ -32,3 +32,7 @@ You need a laser nearby.
 - [YouTube](https://www.youtube.com/watch?v=oBYBi8dqflI)
 
 <video controls><source src="https://cdn.discordapp.com/attachments/1105598687167664239/1107045487787380836/clip.mp4?ex=699eb634&is=699d64b4&hm=a77d6181588a1da01d24bbb68e75005afed94e9b36eb6024049bc834f837cb0d&" type="video/mp4"></video>
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/lift-fuse-interrupt.md b/docs/wiki/glitchcraft/lift-fuse-interrupt.md
index 95d84b324..7829094c0 100644
--- a/docs/wiki/glitchcraft/lift-fuse-interrupt.md
+++ b/docs/wiki/glitchcraft/lift-fuse-interrupt.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Lift Fuse Interrupt"
 abbreviation: "LFI"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -34,3 +34,7 @@ It is not yet understood what causes this glitch.
 - [Discord](https://discord.com/channels/1086729144307564648/1109838351596527726/1364240647736791071)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1367499196676051034)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1366561351069077616)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/lift-warping.md b/docs/wiki/glitchcraft/lift-warping.md
index a22d23db8..4a8d316c8 100644
--- a/docs/wiki/glitchcraft/lift-warping.md
+++ b/docs/wiki/glitchcraft/lift-warping.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Lift Warping"
 abbreviation: "LW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -31,3 +31,7 @@ Can also be achieved with object culling (steps/examples needed.)
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1118758645111468042)
 - [YouTube](https://www.youtube.com/watch?v=AAMX8LRxSK0)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/like-like-culling.md b/docs/wiki/glitchcraft/like-like-culling.md
index 05ee229f1..cafe05352 100644
--- a/docs/wiki/glitchcraft/like-like-culling.md
+++ b/docs/wiki/glitchcraft/like-like-culling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Like-Like Culling"
 abbreviation: "LLC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -25,8 +25,12 @@ _Mozz - 13 June 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1118369148439904276)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md b/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md
index e94e1998f..9c0d6b405 100644
--- a/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md
+++ b/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Like Like New Textbox Softlock"
 abbreviation: "LLTS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -20,7 +20,7 @@ _Ryan? - 16 June 2023_
 
 ## Instructions
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Notes
 ---
@@ -30,3 +30,7 @@ Test for 1.2.0/1.2.1
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1119086382565048421)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1169727626353577984)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/like-like-warping.md b/docs/wiki/glitchcraft/like-like-warping.md
index 36ffe63eb..5d65b6cb7 100644
--- a/docs/wiki/glitchcraft/like-like-warping.md
+++ b/docs/wiki/glitchcraft/like-like-warping.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Like-Like Warping"
 abbreviation: "LLW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -24,8 +24,12 @@ _Mozz - 15 June 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1118758645111468042)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/likelike-stick-smuggling.md b/docs/wiki/glitchcraft/likelike-stick-smuggling.md
index 0cc28dfe6..f639a6f1f 100644
--- a/docs/wiki/glitchcraft/likelike-stick-smuggling.md
+++ b/docs/wiki/glitchcraft/likelike-stick-smuggling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "LikeLike Stick Smuggling"
 abbreviation: "LLSS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -31,8 +31,12 @@ _?_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
+├óÔé¼ÔÇØ
+
+## Related
+---
 ÔÇö
diff --git a/docs/wiki/glitchcraft/long-jump.md b/docs/wiki/glitchcraft/long-jump.md
index 84bbe5e33..d48baf9f1 100644
--- a/docs/wiki/glitchcraft/long-jump.md
+++ b/docs/wiki/glitchcraft/long-jump.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Long Jump"
 abbreviation: "LJ"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -24,10 +24,14 @@ While facing sideways (any angle that is more than or equal to 90 degrees from t
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108911864710185041)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108911864710185041)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1109098133100703774)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/map-flickering.md b/docs/wiki/glitchcraft/map-flickering.md
index 35953dbbd..ff9598daf 100644
--- a/docs/wiki/glitchcraft/map-flickering.md
+++ b/docs/wiki/glitchcraft/map-flickering.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Map Flickering"
 abbreviation: "MF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
@@ -30,3 +30,7 @@ Do not do this if you suffer from epilepsy, or are prone to seizures
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=RjSKbESuVHo)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/map-storage.md b/docs/wiki/glitchcraft/map-storage.md
index b6f5212c4..42f79ac9e 100644
--- a/docs/wiki/glitchcraft/map-storage.md
+++ b/docs/wiki/glitchcraft/map-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Map Storage"
 abbreviation: "MSTR"
 versions: ["1.1.0", "1.1.1"]
@@ -33,3 +33,7 @@ effects can range from softlocks to crashes
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1112660897891102740)
 - [YouTube](https://www.youtube.com/watch?v=cZZ-enDJ6jY)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/master-sword-liberation.md b/docs/wiki/glitchcraft/master-sword-liberation.md
index 29694a3d3..d37564fbe 100644
--- a/docs/wiki/glitchcraft/master-sword-liberation.md
+++ b/docs/wiki/glitchcraft/master-sword-liberation.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Master Sword Liberation"
 abbreviation: "MSL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -67,3 +67,7 @@ This can be combined with decayed zuggle to transfer it through files.
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1191987058412101725)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1191987058412101725)
 - [DIscord](https://discord.com/channels/1086729144307564648/1105598687167664239/1178791475216134194)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/memory-buffering.md b/docs/wiki/glitchcraft/memory-buffering.md
index 37fbf43e5..de7cbd691 100644
--- a/docs/wiki/glitchcraft/memory-buffering.md
+++ b/docs/wiki/glitchcraft/memory-buffering.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Memory Buffering"
 abbreviation: "MB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -24,8 +24,12 @@ Skip a playing memory during an animation.
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
+├óÔé¼ÔÇØ
+
+## Related
+---
 ÔÇö
diff --git a/docs/wiki/glitchcraft/memory-interrupt.md b/docs/wiki/glitchcraft/memory-interrupt.md
index a1f084deb..2c894f6e2 100644
--- a/docs/wiki/glitchcraft/memory-interrupt.md
+++ b/docs/wiki/glitchcraft/memory-interrupt.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Memory Interrupt"
 abbreviation: "MI"
 versions: ["1.0.0"]
@@ -30,9 +30,13 @@ The main use for this is Banc Storage, check the next row
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1290665812855885846)
 - [YouTube](https://www.youtube.com/watch?v=RmjZKVGvstE)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/message-not-found.md b/docs/wiki/glitchcraft/message-not-found.md
index 8b9e860d6..f4488820d 100644
--- a/docs/wiki/glitchcraft/message-not-found.md
+++ b/docs/wiki/glitchcraft/message-not-found.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Message Not Found"
 abbreviation: "MNF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -55,3 +55,7 @@ This MNF can be powered up further! See WST or Unload WST for the method
 - [YouTube](https://www.youtube.com/watch?v=EAthghngbKs)
 - [YouTube](https://www.youtube.com/watch?v=TKSQJ23ES_c)
 - [Zocument](https://docs.google.com/document/d/1-BeufJtao2cG5ABG0ZDEUX1SbgQwc_89n7C0VZjPAdI/edit?usp=sharing)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/midair-item-transmutation.md b/docs/wiki/glitchcraft/midair-item-transmutation.md
index 9f1281857..daa5683c7 100644
--- a/docs/wiki/glitchcraft/midair-item-transmutation.md
+++ b/docs/wiki/glitchcraft/midair-item-transmutation.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Midair Item Transmutation"
 abbreviation: "MIT"
 versions: ["1.1.0", "1.1.1"]
@@ -43,3 +43,7 @@ You can chain this many times during 1 shield jump by repeating steps 2-5. It do
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1109456967480647710)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1109460329966092319)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1109456967480647710)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/midair-sort-duplication.md b/docs/wiki/glitchcraft/midair-sort-duplication.md
index baa33d3a3..741f881fd 100644
--- a/docs/wiki/glitchcraft/midair-sort-duplication.md
+++ b/docs/wiki/glitchcraft/midair-sort-duplication.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Midair Sort Duplication"
 abbreviation: "MSD"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
@@ -33,3 +33,7 @@ Y and exit must be pressed on the same frame.
 ## Resources
 ---
 - [Twitter](https://twitter.com/zasoot/status/1660458317934915584)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/midair-throw-duplication.md b/docs/wiki/glitchcraft/midair-throw-duplication.md
index 76b8e62ec..1720aa7f6 100644
--- a/docs/wiki/glitchcraft/midair-throw-duplication.md
+++ b/docs/wiki/glitchcraft/midair-throw-duplication.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Midair Throw Duplication"
 abbreviation: "MTD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -27,9 +27,13 @@ _quantim - 2 July 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1125201209310068766)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1125201792096030811)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/minecart-rail-collision-launching.md b/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
index 99e6f6f85..8dcd6333c 100644
--- a/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
+++ b/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
@@ -1,8 +1,8 @@
----
+´╗┐---
 title: "Minecart Rail Collision Launching"
 abbreviation: "MRCL"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
-credits: ["ÒüØÒéë-ÒüòÒéô"]
+credits: ["├ú┬ü┬Ø├úÔÇÜÔÇ░-├ú┬üÔÇó├úÔÇÜÔÇ£"]
 date: "2023-05-18"
 description: "Allows the usage of minecarts to be launched from awkward collision grabbing on rails."
 aliases: ["minecart collision", "minecart rail collision", "rail collision launching", "collision launch", "collision launching"]
@@ -16,11 +16,11 @@ tags: ["launching"]
 ---
 Allows the usage of minecarts to be launched from awkward collision grabbing on rails.
 
-_ÒüØÒéë-ÒüòÒéô - 18 May 2023_
+_├ú┬ü┬Ø├úÔÇÜÔÇ░-├ú┬üÔÇó├úÔÇÜÔÇ£ - 18 May 2023_
 
 ## Instructions
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Notes
 ---
@@ -31,3 +31,7 @@ Still needs to be experimented with more.
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108547906698485852)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108547906698485852)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1112410236356145182)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/mineru-ability-desync.md b/docs/wiki/glitchcraft/mineru-ability-desync.md
index fa5ad6981..77ce40c37 100644
--- a/docs/wiki/glitchcraft/mineru-ability-desync.md
+++ b/docs/wiki/glitchcraft/mineru-ability-desync.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Mineru Ability Desync"
 abbreviation: "MAD"
 versions: ["1.1.0", "1.1.1"]
@@ -32,3 +32,7 @@ To do: test on other versions and with more emitters Seems similar to ARAZ
 ---
 - [Twitter](https://twitter.com/SilicatYT/status/1663658677302353920)
 - [Twitter](https://twitter.com/SilicatYT/status/1663846017060700161)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/mineru-aim-permanence.md b/docs/wiki/glitchcraft/mineru-aim-permanence.md
index 6b09af83f..3fa3a9c7c 100644
--- a/docs/wiki/glitchcraft/mineru-aim-permanence.md
+++ b/docs/wiki/glitchcraft/mineru-aim-permanence.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Mineru Aim Permanence"
 abbreviation: "MAIP"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -30,8 +30,12 @@ The Construct will stick around despite the other sage avatars going away
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Youtube](https://www.youtube.com/shorts/LnB58_FgDFM)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/mineru-text-storage.md b/docs/wiki/glitchcraft/mineru-text-storage.md
index b5715a52b..c0613b090 100644
--- a/docs/wiki/glitchcraft/mineru-text-storage.md
+++ b/docs/wiki/glitchcraft/mineru-text-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Mineru Text Storage"
 abbreviation: "MTS"
 versions: ["1.0.0"]
@@ -34,3 +34,7 @@ Only tested on 1.0.0, probably works on all versions
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1128894970653327401/1261062222306869268)
 - [YouTube](https://www.youtube.com/watch?v=W0bNi0q7A6Q)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/mnf-fusing.md b/docs/wiki/glitchcraft/mnf-fusing.md
index 0b33930cc..ea399a7b0 100644
--- a/docs/wiki/glitchcraft/mnf-fusing.md
+++ b/docs/wiki/glitchcraft/mnf-fusing.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "MNF Fusing"
 abbreviation: "MNFF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -28,8 +28,12 @@ _LegendofLinkk - 5 June 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=n2nP6FNjEPI)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/mnf-zuggle-fuse.md b/docs/wiki/glitchcraft/mnf-zuggle-fuse.md
index 5af5a6fd4..931032360 100644
--- a/docs/wiki/glitchcraft/mnf-zuggle-fuse.md
+++ b/docs/wiki/glitchcraft/mnf-zuggle-fuse.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "MNF Zuggle Fuse"
 abbreviation: "MZF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -36,3 +36,7 @@ Can also be done with other weapons and already fused weapons. This just replace
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1108141837954330686/1108621041527427144)
 - [Discord](https://discord.com/channels/1086729144307564648/1108141837954330686/1108622215672496138)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md b/docs/wiki/glitchcraft/modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md
index aacf17bc2..d0c754e2b 100644
--- a/docs/wiki/glitchcraft/modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md
+++ b/docs/wiki/glitchcraft/modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Modifier Deletion Weapon State Transfer"
 abbreviation: "MDWST"
 versions: ["1.0.0"]
@@ -52,3 +52,7 @@ Variant 2 can be used to infinitely re-use items on shields that break on impact
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1155267014848430111)
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1180149524874940498)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/modifier-only-transfer.md b/docs/wiki/glitchcraft/modifier-only-transfer.md
index 574a3f364..3b3d1477a 100644
--- a/docs/wiki/glitchcraft/modifier-only-transfer.md
+++ b/docs/wiki/glitchcraft/modifier-only-transfer.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Modifier ONLY Transfer"
 abbreviation: "MOT"
 versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,3 +33,7 @@ _kurocat471, BigDUCCO - 9 June 2023_
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=ycKeFgsb7gs)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/mount-lock.md b/docs/wiki/glitchcraft/mount-lock.md
index 7aac3b870..ab7dfb4ce 100644
--- a/docs/wiki/glitchcraft/mount-lock.md
+++ b/docs/wiki/glitchcraft/mount-lock.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Mount Lock"
 abbreviation: "ML"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -34,3 +34,7 @@ Grabbing the steering stick with Ultrahand after mount lock causes Link to disco
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1342646563184312432)
 - [Discord](https://discordapp.com/channels/1086729144307564648/1110956205624532993/1342580552447950961)
 - [YouTube](https://www.youtube.com/watch?v=E2Qp3Zj15fo)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/mozdor-jumping-slashing.md b/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
index 592971dad..8eab29b82 100644
--- a/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
+++ b/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Mozdor Jumping/Slashing"
 abbreviation: "MJS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -26,8 +26,12 @@ _Mozz, AgdoR - 20 May 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1106412847359082506/1109296265847640094)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/msnf-glowing.md b/docs/wiki/glitchcraft/msnf-glowing.md
index e19563f09..e856accac 100644
--- a/docs/wiki/glitchcraft/msnf-glowing.md
+++ b/docs/wiki/glitchcraft/msnf-glowing.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "MSNF glowing"
 abbreviation: "MG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -31,3 +31,7 @@ Gloom hands only work on 1.0.0 while phantom ganon works on all versions
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=x71Zp-zBbEE)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/new-item-desync-equipment-duping.md b/docs/wiki/glitchcraft/new-item-desync-equipment-duping.md
index b60940fb7..c588379c4 100644
--- a/docs/wiki/glitchcraft/new-item-desync-equipment-duping.md
+++ b/docs/wiki/glitchcraft/new-item-desync-equipment-duping.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "New Item Desync"
 abbreviation: "NID"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -32,9 +32,13 @@ The new item must change positions when you sort your inventory. So for shields
 
 In addition to desyncing your inventory, it will also transfer any fused objects from the new item to the item you equip in the menu.
 
-Can only be done with new items once. Must meet sorting requirements listed under ÔÇ£InstructionsÔÇØ.
+Can only be done with new items once. Must meet sorting requirements listed under ├óÔé¼┼ôInstructions├óÔé¼┬Ø.
 
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=7_1fwTUz0A4)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1107447184745582662)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/null-dropping.md b/docs/wiki/glitchcraft/null-dropping.md
index ee7cfd6bd..7a7e4e295 100644
--- a/docs/wiki/glitchcraft/null-dropping.md
+++ b/docs/wiki/glitchcraft/null-dropping.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Null Dropping"
 abbreviation: "ND"
 versions: ["1.0.0"]
@@ -25,8 +25,12 @@ _Aergyl - 16 March 2024_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1218578523690897458)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/object-moe-enlargement.md b/docs/wiki/glitchcraft/object-moe-enlargement.md
index 2f6913fae..0ffcbaad0 100644
--- a/docs/wiki/glitchcraft/object-moe-enlargement.md
+++ b/docs/wiki/glitchcraft/object-moe-enlargement.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Object (Moe) Enlargement"
 abbreviation: "MOE"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -46,8 +46,12 @@ In order to make it rangeless, you need to PSLOT the target.
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1301144333499760670)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/ocklusion.md b/docs/wiki/glitchcraft/ocklusion.md
index 9c52518fb..65b0c0410 100644
--- a/docs/wiki/glitchcraft/ocklusion.md
+++ b/docs/wiki/glitchcraft/ocklusion.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Ocklusion"
 abbreviation: "OCKL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -41,3 +41,7 @@ By going into the room of the secret stone in Lightning Temple, going up and dow
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1245447960658051184)
 - [YouTube](https://www.youtube.com/watch?v=krR0oUnjauw)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/octodupe.md b/docs/wiki/glitchcraft/octodupe.md
index aae39d840..56061b4ca 100644
--- a/docs/wiki/glitchcraft/octodupe.md
+++ b/docs/wiki/glitchcraft/octodupe.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Octodupe"
 abbreviation: "OD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -38,3 +38,7 @@ This does not work on items that cannot be modified or octoroks that have alread
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1111702277451960370)
 - [YouTube](https://www.youtube.com/watch?v=oXzMRPK2sRM)
 - [YouTube](https://www.youtube.com/watch?v=FSxiPP-SDtM)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/prologue-escape.md b/docs/wiki/glitchcraft/prologue-escape.md
index 6e839a2a5..00f0c9458 100644
--- a/docs/wiki/glitchcraft/prologue-escape.md
+++ b/docs/wiki/glitchcraft/prologue-escape.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Prologue Escape"
 abbreviation: "PE"
 versions: ["1.0.0"]
@@ -49,4 +49,8 @@ Check the Resources section for more specific effects, such as Awakened Master S
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1290703223467937898)
 - [YouTube](https://www.youtube.com/watch?v=RmjZKVGvstE)
-ÔÇö [Banc Storage](./banc-storage.md)
+├óÔé¼ÔÇØ [Banc Storage](./banc-storage.md)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/proxy-glitches.md b/docs/wiki/glitchcraft/proxy-glitches.md
index 5d1381d84..db1269763 100644
--- a/docs/wiki/glitchcraft/proxy-glitches.md
+++ b/docs/wiki/glitchcraft/proxy-glitches.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Proxy Glitches"
 abbreviation: "PG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -34,3 +34,7 @@ Testing is still being done. As more is discovered, this section will be updated
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1107369279747260666)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1107214237174071347)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1112189474911297668)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/quick-smuggling.md b/docs/wiki/glitchcraft/quick-smuggling.md
index 60a7762d2..cab0cbfa6 100644
--- a/docs/wiki/glitchcraft/quick-smuggling.md
+++ b/docs/wiki/glitchcraft/quick-smuggling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Quick Smuggling"
 abbreviation: "QS"
 versions: ["1.2.0"]
@@ -34,3 +34,7 @@ Allows for infinite springboarding if you quick smuggle with a spring shield. Th
 - [YouTube](https://www.youtube.com/watch?v=emvoQHVRaCE)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1128052108109811784)
 - [YouTube](https://www.youtube.com/watch?v=Tw3sjs0ftyk)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/reball.md b/docs/wiki/glitchcraft/reball.md
index 492241386..72a9f8727 100644
--- a/docs/wiki/glitchcraft/reball.md
+++ b/docs/wiki/glitchcraft/reball.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Reball"
 abbreviation: "RBL"
 versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -30,4 +30,8 @@ Can be combined with arrow smuggle for momentum preservation.
 
 ## Resources
 ---
+├óÔé¼ÔÇØ
+
+## Related
+---
 ÔÇö
diff --git a/docs/wiki/glitchcraft/recall-cancel.md b/docs/wiki/glitchcraft/recall-cancel.md
index e48b837f3..180e4ba46 100644
--- a/docs/wiki/glitchcraft/recall-cancel.md
+++ b/docs/wiki/glitchcraft/recall-cancel.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Recall Cancel"
 abbreviation: "RCC"
 versions: ["1.2.0", "1.2.1"]
@@ -32,3 +32,7 @@ Jumpslash cancel
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1131627625991905432)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1153447778240974908)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1153822693880238171)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/recall-clip.md b/docs/wiki/glitchcraft/recall-clip.md
index 0c9034b8c..2b396f6c2 100644
--- a/docs/wiki/glitchcraft/recall-clip.md
+++ b/docs/wiki/glitchcraft/recall-clip.md
@@ -1,8 +1,8 @@
----
+´╗┐---
 title: "Recall Clip"
 abbreviation: "RC"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
-credits: ["ÒüôÒéôÒüØÒéü"]
+credits: ["├ú┬üÔÇ£├úÔÇÜÔÇ£├ú┬ü┬Ø├úÔÇÜ┬ü"]
 date: "2023-05-16"
 description: "Allows you to clip through things using a large object and recall"
 aliases: ["recall clip", "recall-clip glitch", "recall-clip", "recallclip"]
@@ -16,7 +16,7 @@ tags: ["clipping", "ultrahand", "recall"]
 ---
 Allows you to clip through things using a large object and recall
 
-_ÒüôÒéôÒüØÒéü - 16 May 2023_
+_├ú┬üÔÇ£├úÔÇÜÔÇ£├ú┬ü┬Ø├úÔÇÜ┬ü - 16 May 2023_
 
 ## Instructions
 ---
@@ -33,3 +33,7 @@ This can be done with a spring, making the entire trick much more portable
 ---
 - [Twitter](https://vxtwitter.com/tsu509359170830/status/1657767717796208640?s=20)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108100337254023168)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/recall-drop-stacking.md b/docs/wiki/glitchcraft/recall-drop-stacking.md
index e9dc8b615..b67cd0415 100644
--- a/docs/wiki/glitchcraft/recall-drop-stacking.md
+++ b/docs/wiki/glitchcraft/recall-drop-stacking.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Recall Drop Stacking"
 abbreviation: "RDS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -36,3 +36,7 @@ Can be done on 1.2.0+ with materials only
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1325262259152486432)
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1325264364013355152)
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1325266809590517782)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/recall-launch.md b/docs/wiki/glitchcraft/recall-launch.md
index f6a14587a..9bf339469 100644
--- a/docs/wiki/glitchcraft/recall-launch.md
+++ b/docs/wiki/glitchcraft/recall-launch.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Recall Launch"
 abbreviation: "RL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,3 +33,7 @@ This works very good with boomerangs. It also works with anything Link can pick
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108497033951719517)
 - [Twitter](https://twitter.com/iLegendofLinkk/status/1659100053535965185?t=tWBb41YeFveu5NycFpue5w&s=19)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/recipe-storage.md b/docs/wiki/glitchcraft/recipe-storage.md
index fcc779535..d3e8c0acf 100644
--- a/docs/wiki/glitchcraft/recipe-storage.md
+++ b/docs/wiki/glitchcraft/recipe-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Recipe Storage"
 abbreviation: "RS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -45,7 +45,7 @@ Recipe Hold Storage:
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
@@ -53,3 +53,7 @@ Recipe Hold Storage:
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1305180152325738589)
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1305204895602704534)
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1305205208665821186)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/remote-arrow-trap.md b/docs/wiki/glitchcraft/remote-arrow-trap.md
index b2da243ac..8a3db46be 100644
--- a/docs/wiki/glitchcraft/remote-arrow-trap.md
+++ b/docs/wiki/glitchcraft/remote-arrow-trap.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Remote Arrow"
 abbreviation: "RAT"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
@@ -35,3 +35,7 @@ Firing from any other bow with this glitch active, will allow it to shoot from t
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1114292162268499979)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1114294468363960490)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1114313664535732315)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/replacement-actor-fuse-entanglement.md b/docs/wiki/glitchcraft/replacement-actor-fuse-entanglement.md
index 7b9ad4657..016d0f53e 100644
--- a/docs/wiki/glitchcraft/replacement-actor-fuse-entanglement.md
+++ b/docs/wiki/glitchcraft/replacement-actor-fuse-entanglement.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Replacement Actor Fuse Entanglement"
 abbreviation: "RAFE"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -36,3 +36,7 @@ Objects which do not have a replacement actor as listed on the AttachmentParam s
 - [YouTube](https://www.youtube.com/watch?v=WR_ByU-_0ic)
 - [AttachmentParam list](https://docs.google.com/spreadsheets/d/13_I_wPuG6AvFm02qgtIBDamQrrb6x4a8--UouZYKOsc/)
 - [Replacement Actors](https://discord.com/channels/1086729144307564648/1113557914444111873/1463729861683056732)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md b/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md
index 9b24a8c66..e9af0aea8 100644
--- a/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md
+++ b/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Resync Fuse Entanglement"
 abbreviation: "RFE"
 versions: ["1.0.0"]
@@ -53,8 +53,12 @@ This method uses recall for a makeshift wall:
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Twitter](https://vxtwitter.com/zasbotw/status/1736818709677977998)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/reverse-ascend-storage.md b/docs/wiki/glitchcraft/reverse-ascend-storage.md
index 3a85ab0f4..68efb9be3 100644
--- a/docs/wiki/glitchcraft/reverse-ascend-storage.md
+++ b/docs/wiki/glitchcraft/reverse-ascend-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Reverse Ascend Storage"
 abbreviation: "RAS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -24,10 +24,14 @@ _Redrooey - 27 November 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1128894970653327401/1178472338778493029)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1178478433160929301)
 - [Discord](https://discord.com/channels/1086729144307564648/1128894970653327401/1178476023818494044)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/sage-madness.md b/docs/wiki/glitchcraft/sage-madness.md
index ed9b26ae2..28677a4d4 100644
--- a/docs/wiki/glitchcraft/sage-madness.md
+++ b/docs/wiki/glitchcraft/sage-madness.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Sage Madness"
 abbreviation: "SM"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -24,8 +24,12 @@ Activate the text box you get after obtaining a sage while the sage falls down a
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
+├óÔé¼ÔÇØ
+
+## Related
+---
 ÔÇö
diff --git a/docs/wiki/glitchcraft/sage-recycling.md b/docs/wiki/glitchcraft/sage-recycling.md
index ad50b70ac..56355648f 100644
--- a/docs/wiki/glitchcraft/sage-recycling.md
+++ b/docs/wiki/glitchcraft/sage-recycling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Sage Recycling"
 abbreviation: "SRCY"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -30,3 +30,7 @@ SRC with tulin might be frame perfect
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1128385969620533329)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/save-load-dupe.md b/docs/wiki/glitchcraft/save-load-dupe.md
index d17d67d56..a503d2b5e 100644
--- a/docs/wiki/glitchcraft/save-load-dupe.md
+++ b/docs/wiki/glitchcraft/save-load-dupe.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Save Load Dupe"
 abbreviation: "SLD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -40,3 +40,7 @@ Requires Portable culling to be performed on 1.2.0/1.2.1
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108041163170128022)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/scope-render-cancel.md b/docs/wiki/glitchcraft/scope-render-cancel.md
index 9e275396c..0ee2285f4 100644
--- a/docs/wiki/glitchcraft/scope-render-cancel.md
+++ b/docs/wiki/glitchcraft/scope-render-cancel.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Scope Render Cancel"
 abbreviation: "SRC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -44,3 +44,7 @@ This glitch cancels any time you open any type of menu, any NPC or prompt intera
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1109188178008621147)
 - [Twitter](https://twitter.com/NX721_/status/1678077674349121536)
 - [Twitter](https://twitter.com/NX721_/status/1678114915293491200?s=20)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/shadow-void-icons.md b/docs/wiki/glitchcraft/shadow-void-icons.md
index 8c267f2e1..45e16ed76 100644
--- a/docs/wiki/glitchcraft/shadow-void-icons.md
+++ b/docs/wiki/glitchcraft/shadow-void-icons.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Shadow/Void Icons"
 abbreviation: "SVI"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
@@ -37,3 +37,7 @@ tighter.
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1296080453413109830)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/shock-cold-fuse.md b/docs/wiki/glitchcraft/shock-cold-fuse.md
index cb4382492..d820aefe8 100644
--- a/docs/wiki/glitchcraft/shock-cold-fuse.md
+++ b/docs/wiki/glitchcraft/shock-cold-fuse.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Shock Cold Fuse"
 abbreviation: "SCF"
 versions: ["1.0.0"]
@@ -26,9 +26,13 @@ _Zas - 11 September 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1150759871520710666)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1151265557295923220)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/slate-storage.md b/docs/wiki/glitchcraft/slate-storage.md
index 9b314c58f..2b42b5c07 100644
--- a/docs/wiki/glitchcraft/slate-storage.md
+++ b/docs/wiki/glitchcraft/slate-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Slate Storage"
 abbreviation: "SLST"
 versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -40,9 +40,13 @@ The Fall Damage should be cancelled if you dived quick enough
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1287107041877299374)
 - [YouTube](https://www.youtube.com/watch?v=S_zTJymG-s0)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/spring-fall-damage-cancel.md b/docs/wiki/glitchcraft/spring-fall-damage-cancel.md
index 3f0c19eca..262e0b621 100644
--- a/docs/wiki/glitchcraft/spring-fall-damage-cancel.md
+++ b/docs/wiki/glitchcraft/spring-fall-damage-cancel.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Spring Fall Damage Cancel"
 abbreviation: "SFDC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -31,3 +31,7 @@ Glitchless Fall Damage Cancel
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1107739989544009828)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/spring-strangeness.md b/docs/wiki/glitchcraft/spring-strangeness.md
index b97f532e1..ff13b8497 100644
--- a/docs/wiki/glitchcraft/spring-strangeness.md
+++ b/docs/wiki/glitchcraft/spring-strangeness.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Spring Strangeness"
 abbreviation: "STRS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,4 +33,8 @@ Method 1 is reliablely strange, while Method 2 has only been performed once thus
 
 ## Resources
 ---
+├óÔé¼ÔÇØ
+
+## Related
+---
 ÔÇö
diff --git a/docs/wiki/glitchcraft/springdolling.md b/docs/wiki/glitchcraft/springdolling.md
index 6997c248d..0a5f57d5f 100644
--- a/docs/wiki/glitchcraft/springdolling.md
+++ b/docs/wiki/glitchcraft/springdolling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Springdolling"
 abbreviation: "SDOL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,3 +33,7 @@ Can chain more springs to make the horizontal launch more powerful
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1107794101111377920)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1112137651743637584)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/stack-splitting.md b/docs/wiki/glitchcraft/stack-splitting.md
index 86bb4b5eb..b42de96c2 100644
--- a/docs/wiki/glitchcraft/stack-splitting.md
+++ b/docs/wiki/glitchcraft/stack-splitting.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Stack Splitting"
 abbreviation: "SSPL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
@@ -44,3 +44,7 @@ Can lead to Split Item Duplication, a material duplication glitch
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1323483601756622899)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/stamina-depletion-freeze.md b/docs/wiki/glitchcraft/stamina-depletion-freeze.md
index f6b6e703b..3bdc69143 100644
--- a/docs/wiki/glitchcraft/stamina-depletion-freeze.md
+++ b/docs/wiki/glitchcraft/stamina-depletion-freeze.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Stamina Depletion Freeze"
 abbreviation: "SDF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -29,9 +29,13 @@ Letting go of B or stopping running cancels it
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1109478155409965076)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1148688838198304779)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/surf-storage.md b/docs/wiki/glitchcraft/surf-storage.md
index cacde78ee..89c617267 100644
--- a/docs/wiki/glitchcraft/surf-storage.md
+++ b/docs/wiki/glitchcraft/surf-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Surf storage"
 abbreviation: "SSTR"
 versions: ["1.0.0"]
@@ -25,9 +25,13 @@ Shield surf against a slope
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598254198050947/1154554443644293171)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1155495303642882099)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/swap-resync.md b/docs/wiki/glitchcraft/swap-resync.md
index 87cbb9e1c..48b8e2354 100644
--- a/docs/wiki/glitchcraft/swap-resync.md
+++ b/docs/wiki/glitchcraft/swap-resync.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Swap Resync"
 abbreviation: "SR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
@@ -40,3 +40,7 @@ Swap Resync Zuggle: see next row
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1404329328220704779)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/temporary-devices.md b/docs/wiki/glitchcraft/temporary-devices.md
index 76efa2611..7d989aac7 100644
--- a/docs/wiki/glitchcraft/temporary-devices.md
+++ b/docs/wiki/glitchcraft/temporary-devices.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Temporary Devices"
 abbreviation: "TD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -37,3 +37,7 @@ On 1.0, Link can stand on it, allowing to jump off it, and get more height off t
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1312200159345643722)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/throken.md b/docs/wiki/glitchcraft/throken.md
index df73ee5e7..2a56a8d4d 100644
--- a/docs/wiki/glitchcraft/throken.md
+++ b/docs/wiki/glitchcraft/throken.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Throken"
 abbreviation: "THK"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -32,3 +32,7 @@ Throken weapons have no despawn radius, and can never be unloaded from distance
 ---
 - [Discord](https://discordapp.com/channels/1086729144307564648/1113557914444111873/1373320909842288870)
 - [Discord](https://discordapp.com/channels/1086729144307564648/1113557914444111873/1373347636647825481)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/throw-cancelling.md b/docs/wiki/glitchcraft/throw-cancelling.md
index 8f1b20241..7de957d98 100644
--- a/docs/wiki/glitchcraft/throw-cancelling.md
+++ b/docs/wiki/glitchcraft/throw-cancelling.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Throw Cancelling"
 abbreviation: "TC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -26,8 +26,12 @@ _Quelfth_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
+├óÔé¼ÔÇØ
+
+## Related
+---
 ÔÇö
diff --git a/docs/wiki/glitchcraft/time-bomb-cancel.md b/docs/wiki/glitchcraft/time-bomb-cancel.md
index b0259b67a..1a389decf 100644
--- a/docs/wiki/glitchcraft/time-bomb-cancel.md
+++ b/docs/wiki/glitchcraft/time-bomb-cancel.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Time Bomb cancel"
 abbreviation: "TBC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -30,3 +30,7 @@ Also works with the msgnotfound
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1170334121910882366)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/travel-medallion-storage.md b/docs/wiki/glitchcraft/travel-medallion-storage.md
index fe4a802a6..a2bf61ca5 100644
--- a/docs/wiki/glitchcraft/travel-medallion-storage.md
+++ b/docs/wiki/glitchcraft/travel-medallion-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Travel Medallion storage"
 abbreviation: "TMS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -29,8 +29,12 @@ _kirigaya - 16 June 2023_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1119636429933387826)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/two-handed-with-shield.md b/docs/wiki/glitchcraft/two-handed-with-shield.md
index 593a704d9..6076b6818 100644
--- a/docs/wiki/glitchcraft/two-handed-with-shield.md
+++ b/docs/wiki/glitchcraft/two-handed-with-shield.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Two Handed With Shield"
 abbreviation: "THWS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -32,3 +32,7 @@ Disable the earthwake ability or press "R" instead of "Y".
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1143287784589770933)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/ultrabroken.md b/docs/wiki/glitchcraft/ultrabroken.md
index 00e19299f..94b92b9d4 100644
--- a/docs/wiki/glitchcraft/ultrabroken.md
+++ b/docs/wiki/glitchcraft/ultrabroken.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Ultrabroken"
 abbreviation: "UB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
@@ -36,3 +36,7 @@ During flying with Ultrabroken, it can be very easily for the game to cancel out
 - [YouTube](https://www.youtube.com/watch?v=Ik5oJdPI-WA&t=10)
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1116453456572588105)
 - [Ultrabroken Guide](https://docs.google.com/document/d/1Q0RxFCc_-Sr08y0SHZqTPxkdoUFZ__pI_ojA86CUidw)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/unload-duping.md b/docs/wiki/glitchcraft/unload-duping.md
index 20b8915a1..72436784e 100644
--- a/docs/wiki/glitchcraft/unload-duping.md
+++ b/docs/wiki/glitchcraft/unload-duping.md
@@ -1,8 +1,8 @@
----
+´╗┐---
 title: "Unload Duping"
 abbreviation: "UD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
-credits: ["Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª", "ÕìâÕ╣┤ÞîÂÚÑ╝"]
+credits: ["├®┬¡ÔÇØ├ª┬│ÔÇó├ª┼ô┬¼├Ñ┬░┬▒├ñ┬©┬ì├º┬ºÔÇÿ├Ñ┬¡┬ª", "├Ñ┬ìãÆ├Ñ┬╣┬┤├¿┼Æ┬Â├®┬Ñ┬╝"]
 date: "2023-05-31"
 description: "By firing arrows between load triggers, items fused to the arrows get dropped. Allowing you to dupe items with multi-shot bows."
 aliases: ["unload-duping"]
@@ -16,7 +16,7 @@ tags: ["duplication", "item", "culling", "fuse", "bow", "arrow"]
 ---
 By firing arrows between load triggers, items fused to the arrows get dropped. Allowing you to dupe items with multi-shot bows.
 
-_Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª (magic is not science), ÕìâÕ╣┤ÞîÂÚÑ╝ (Thousand Year Tea) - 31 May 2023_
+_├®┬¡ÔÇØ├ª┬│ÔÇó├ª┼ô┬¼├Ñ┬░┬▒├ñ┬©┬ì├º┬ºÔÇÿ├Ñ┬¡┬ª (magic is not science), ├Ñ┬ìãÆ├Ñ┬╣┬┤├¿┼Æ┬Â├®┬Ñ┬╝ (Thousand Year Tea) - 31 May 2023_
 
 ## Instructions
 ---
@@ -35,3 +35,7 @@ This also works in any other chasm in which you have enough room to shoot your a
 - [Bilibili](https://www.bilibili.com/video/BV1QL411q742)
 - [YouTube](https://www.youtube.com/watch?v=69IW7x_JFeU)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1113480578583511122)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/void-holding.md b/docs/wiki/glitchcraft/void-holding.md
index faada116c..f72beb78d 100644
--- a/docs/wiki/glitchcraft/void-holding.md
+++ b/docs/wiki/glitchcraft/void-holding.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Void Holding"
 abbreviation: "VH"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
@@ -32,3 +32,7 @@ Needs more testing.
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1117164294505779244)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1117479024063684660)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/wacko-attacko.md b/docs/wiki/glitchcraft/wacko-attacko.md
index fa1128a13..75da211b3 100644
--- a/docs/wiki/glitchcraft/wacko-attacko.md
+++ b/docs/wiki/glitchcraft/wacko-attacko.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Wacko Attacko"
 abbreviation: "WATK"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -26,9 +26,13 @@ _NghtmaR3, WinnerBoi77 - 21 January 2024_
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1198765751578939482)
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1198792795616464989)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/weapon-extensions.md b/docs/wiki/glitchcraft/weapon-extensions.md
index 1dc026cb8..f8e3ac5fc 100644
--- a/docs/wiki/glitchcraft/weapon-extensions.md
+++ b/docs/wiki/glitchcraft/weapon-extensions.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Weapon Extensions"
 abbreviation: "WEXT"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -35,3 +35,7 @@ Has yet to be seen if this can work on 2H weapons. Also works on fused 1H/Spear
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1121798115595403375)
 - [Twitter](https://vxtwitter.com/zasbotw/status/1672240465985323011)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/weapon-sheath-offset.md b/docs/wiki/glitchcraft/weapon-sheath-offset.md
index cf3a487dc..ccd9dad71 100644
--- a/docs/wiki/glitchcraft/weapon-sheath-offset.md
+++ b/docs/wiki/glitchcraft/weapon-sheath-offset.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Weapon Sheath Offset"
 abbreviation: "WSO"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -35,3 +35,7 @@ This works for ALL weapons not just the .
 ## Resources
 ---
 - [YouTube](https://www.youtube.com/watch?v=E9yKzddgre4)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/weapon-stacking-duplication.md b/docs/wiki/glitchcraft/weapon-stacking-duplication.md
index 4a3fee2f6..ce7b042d1 100644
--- a/docs/wiki/glitchcraft/weapon-stacking-duplication.md
+++ b/docs/wiki/glitchcraft/weapon-stacking-duplication.md
@@ -1,8 +1,8 @@
----
+´╗┐---
 title: "Weapon Stacking Duplication"
 abbreviation: "WSD"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
-credits: ["ErlingÚÖäÞ║½"]
+credits: ["Erling├®ÔäóÔÇ×├¿┬║┬½"]
 date: "2023-05-16"
 description: "Allows for a quick dupe of any weapon, bow or shield"
 aliases: ["weapon stacking", "stacking weapons", "weapon stacking dupe", "weapon-stacking-duplication"]
@@ -16,7 +16,7 @@ tags: ["duplication", "item", "weapon", "equipment", "bow"]
 ---
 Allows for a quick dupe of any weapon, bow or shield
 
-_ErlingÚÖäÞ║½ - 16 May 2023_
+_Erling├®ÔäóÔÇ×├¿┬║┬½ - 16 May 2023_
 
 ## Instructions
 ---
@@ -31,3 +31,7 @@ This is just zuggling, but you drop your equipped weapon at the end, that being
 ## Resources
 ---
 - [Bilibili](http://www.bilibili.com/video/BV1qT411t7Kv/)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/weapon-state-transfer.md b/docs/wiki/glitchcraft/weapon-state-transfer.md
index 5113ffa37..075e45803 100644
--- a/docs/wiki/glitchcraft/weapon-state-transfer.md
+++ b/docs/wiki/glitchcraft/weapon-state-transfer.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Weapon State Transfer"
 abbreviation: "WST"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -66,3 +66,7 @@ Depending on the bow you use (ex. Phrenic Bow), you'll still be able to perform
 - [YouTube](https://www.youtube.com/watch?v=NRZpPp1vVsQ)
 - [YouTube](https://www.youtube.com/watch?v=Kzf_uJBvRjI)
 - [YouTube](https://www.youtube.com/watch?v=1gWV6p814F8)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/wheel-zoomy-also-known-as-wheel-wacko-boingo.md b/docs/wiki/glitchcraft/wheel-zoomy-also-known-as-wheel-wacko-boingo.md
index feb2a9981..422fc00a5 100644
--- a/docs/wiki/glitchcraft/wheel-zoomy-also-known-as-wheel-wacko-boingo.md
+++ b/docs/wiki/glitchcraft/wheel-zoomy-also-known-as-wheel-wacko-boingo.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Wheel Zoomy"
 abbreviation: "WZ"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,3 +33,7 @@ Also possible with two wheels.
 ## Resources
 ---
 - [Twitter](https://twitter.com/NX721_/status/1679259808757870592?t=O2gULUcC_CmV0isS44RMEg&s=19)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md b/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
index c44a02054..b2c44199a 100644
--- a/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
+++ b/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Zonai Inventory Shift Dupe"
 abbreviation: "ZISD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -33,8 +33,12 @@ Steps:
 
 ## Notes
 ---
-ÔÇö
+├óÔé¼ÔÇØ
 
 ## Resources
 ---
 - [Twitter](https://twitter.com/quantim/status/1678509305044115458?s=46)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/zonai-sort-duplication.md b/docs/wiki/glitchcraft/zonai-sort-duplication.md
index bf376626f..49d864953 100644
--- a/docs/wiki/glitchcraft/zonai-sort-duplication.md
+++ b/docs/wiki/glitchcraft/zonai-sort-duplication.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Zonai Sort Duplication"
 abbreviation: "ZSD"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
@@ -34,3 +34,7 @@ For a more consistent method, 3 shield parries away should work on most walls if
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1110075304338260059)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1110075304338260059)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/zonai-storage.md b/docs/wiki/glitchcraft/zonai-storage.md
index 59165840f..f97e5193c 100644
--- a/docs/wiki/glitchcraft/zonai-storage.md
+++ b/docs/wiki/glitchcraft/zonai-storage.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Zonai Storage"
 abbreviation: "ZS"
 versions: ["1.0.0"]
@@ -33,3 +33,7 @@ Activating zonai storage, dying and opening the inventory may crash the game
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1140347990368854047)
 - [YouTube](https://www.youtube.com/watch?v=6plkkvYGW74)
+
+## Related
+---
+ÔÇö
diff --git a/docs/wiki/glitchcraft/zuggle.md b/docs/wiki/glitchcraft/zuggle.md
index 5fe218c85..27ce9647f 100644
--- a/docs/wiki/glitchcraft/zuggle.md
+++ b/docs/wiki/glitchcraft/zuggle.md
@@ -1,4 +1,4 @@
----
+´╗┐---
 title: "Zuggle"
 abbreviation: "ZGL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
@@ -43,3 +43,7 @@ zuggle discussion in the zuggle- thread on the discord please
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108101391983067216)
 - [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1110408813116407859)
 - [Zocument](https://docs.google.com/document/d/1-BeufJtao2cG5ABG0ZDEUX1SbgQwc_89n7C0VZjPAdI/edit?usp=sharing)
+
+## Related
+---
+ÔÇö

----

*** COMMIT: 0cad9df5a90ed8790cf81903ac5e6fc153cf5645
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 16:08:44 2026 +0100
Subject: refactor: rename 'Memorial' to 'Memorandum' and update related documentation

commit 0cad9df5a90ed8790cf81903ac5e6fc153cf5645
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 16:08:44 2026 +0100

    refactor: rename 'Memorial' to 'Memorandum' and update related documentation

diff --git a/docs/assets/scripts/ai-worker-client.js b/docs/assets/scripts/ai-worker-client.js
index 717c08895..1e0276f8a 100644
--- a/docs/assets/scripts/ai-worker-client.js
+++ b/docs/assets/scripts/ai-worker-client.js
@@ -153,7 +153,7 @@
     // Output area (answer + evidence). `out` holds the model answer; `evidenceWrap` holds clickable evidence links returned by the Worker.
     // Starts blank; the typewriter callback populates it after the first cycle.
     const out = el('div', { class: 'ub-ai-out' }, '');
-    const evidenceWrap = el('div', { class: 'ub-ai-evidence' }, '');
+    const evidenceWrap = el('div', { class: 'ub-ai-evidence md-typeset' }, '');
     inputWrap.appendChild(input);
     row.appendChild(inputWrap);
     row.appendChild(askBtn);
@@ -295,7 +295,7 @@
         try{
           const ev = r.evidence || [];
           if (Array.isArray(ev) && ev.length && w.evidence){
-            const heading = el('h2', { class: 'ub-ai-resources md-typeset' }, 'Resources');
+            const heading = el('h2', { class: 'ub-ai-resources' }, 'Resources');
             w.evidence.appendChild(heading);
             const sep = el('hr', { class: 'ub-ai-resources-sep' }, '');
             w.evidence.appendChild(sep);
@@ -304,7 +304,7 @@
             ev.forEach(item => {
               const id = item.id || item.path || '';
               const titleText = item.title || '';
-              let slug = String(id).replace(/\.md$/,'').replace(/^\/+|\/+$/g, '');
+              let slug = String(id).replace(/\.md$/,'').replace(/^\/+|\/+$/g, '').replace(/\/index$/, '');
               const text = titleText || slug || id;
               if (!text.trim()) return;
               // Build direct wiki link
@@ -326,7 +326,7 @@
         try{
           const modelSources = Array.isArray(r.sources) ? r.sources : [];
           if (SHOW_MODEL_SOURCES && modelSources.length && w.evidence){
-            const heading = el('h2', { class: 'ub-ai-related md-typeset' }, 'Related');
+            const heading = el('h2', { class: 'ub-ai-related' }, 'Related');
             w.evidence.appendChild(heading);
             const sep = el('hr', { class: 'ub-ai-related-sep' }, '');
             w.evidence.appendChild(sep);
diff --git a/docs/assets/stylesheets/glow.css b/docs/assets/stylesheets/glow.css
index 002e98925..0d9d0e4be 100644
--- a/docs/assets/stylesheets/glow.css
+++ b/docs/assets/stylesheets/glow.css
@@ -922,6 +922,10 @@ li.task-list-item a, li.task-list a {
   font-family: 'New Rocker', 'Texturina', Georgia, 'Times New Roman', serif !important;
 }
 
+/* Suppress Material permalink anchor injection on evidence/related headings */
+.ub-ai-evidence h2 { cursor: default !important; }
+.ub-ai-evidence h2 .headerlink { display: none !important; }
+
 /* ================================================================
    Grimoire of Glitchcraft ÔÇô Filter & Sort UI
    ================================================================ */
diff --git a/docs/wiki/build_bm25_index.py b/docs/wiki/build_bm25_index.py
index 631552618..264e0a47e 100644
--- a/docs/wiki/build_bm25_index.py
+++ b/docs/wiki/build_bm25_index.py
@@ -342,7 +342,7 @@ def build_leaderboard(json_path: str):
 
     Scans docs/wiki/glitchcraft/ for all credit entries, tallies per name,
     and writes a JSON file consumed by leaderboard.js to render the table
-    client-side in memorial.md.
+    client-side in memorandum.md.
 
     Contributor profile URLs are read from contributors.json (manually maintained).
     """
diff --git a/docs/wiki/index.md b/docs/wiki/index.md
index 958dcef1f..4ac8d0ff5 100644
--- a/docs/wiki/index.md
+++ b/docs/wiki/index.md
@@ -20,4 +20,4 @@ This site is a community-driven encyclopedia of glitches, techniques, and invest
 - **[Out of Bounds section](oob/)** - Glitches and strats that get you Out of Bounds
 - **[Message Not Found](mnf/)** - Explore the powers of MessageNotFound items in this section
 - **[Overload section](overload/)** - Detailed setups and techniques for reaching Overload states
-- **[Memorial](memorial/)** - Leaderboard for glitch hunters and hall of fame for archivists
\ No newline at end of file
+- **[Memorandum](memorandum/)** - Leaderboard for glitch hunters and hall of fame for archivists
\ No newline at end of file
diff --git a/docs/wiki/memorial.md b/docs/wiki/memorandum.md
similarity index 98%
rename from docs/wiki/memorial.md
rename to docs/wiki/memorandum.md
index 39a361d6e..6d777431d 100644
--- a/docs/wiki/memorial.md
+++ b/docs/wiki/memorandum.md
@@ -1,8 +1,8 @@
 ---
-title: Memorial
+title: Memorandum
 ---
 
-# Memorial
+# Memorandum
 
 ## Archivists
 ---
diff --git a/mkdocs.yml b/mkdocs.yml
index e87cdf813..9461d40e4 100644
--- a/mkdocs.yml
+++ b/mkdocs.yml
@@ -148,7 +148,7 @@ nav:
   - OOB: wiki/oob/index.md
   - MNF: wiki/mnf/index.md
   - Overload: wiki/overload/index.md
-  - Memorial: wiki/memorial.md
+  - Memorandum: wiki/memorandum.md
 
 hooks:
   - docs/assets/hooks/youtube_embed.py

----

*** COMMIT: 1a8d1d6e771f716d9519b689688080427cd3cb85
Author: NaN Gogh <igor@torbas.net>
Date: Tue Feb 24 17:10:56 2026 +0100
Subject: Fix encoding issues in markdown files and update metadata

commit 1a8d1d6e771f716d9519b689688080427cd3cb85
Author: NaN Gogh <igor@torbas.net>
Date:   Tue Feb 24 17:10:56 2026 +0100

    Fix encoding issues in markdown files and update metadata
    
    - Corrected the front matter in multiple markdown files to ensure proper encoding and formatting.
    - Updated credits and dates in specific markdown files to reflect accurate information.
    - Added a script to fix double-encoded UTF-8 files caused by PowerShell handling.

diff --git a/.fix_encoding.py b/.fix_encoding.py
new file mode 100644
index 000000000..c457e8260
--- /dev/null
+++ b/.fix_encoding.py
@@ -0,0 +1,64 @@
+"""
+Fix double-encoded UTF-8 files.
+
+PowerShell Get-Content -Raw read UTF-8 files as Windows cp1252,
+then WriteAllText re-encoded as UTF-8-with-BOM, corrupting non-ASCII chars.
+
+Recovery: for each Unicode char in the corrupted text:
+  - Try cp1252 encode -> get original byte
+  - If cp1252 undefined, use latin-1 -> get original byte
+  - Then decode the reassembled bytes as UTF-8
+"""
+import pathlib
+
+ROOT = pathlib.Path('d:/Fragments/Zelda/Ultrabroken Documentation/ultrabroken-documentation')
+
+def degrade_char(c):
+    n = ord(c)
+    if n < 0x80:
+        return bytes([n])
+    try:
+        return c.encode('cp1252')
+    except (UnicodeEncodeError, LookupError):
+        try:
+            return c.encode('latin-1')
+        except (UnicodeEncodeError, LookupError):
+            return c.encode('utf-8')
+
+def fix_encoding(text):
+    raw = bytearray()
+    for c in text:
+        raw.extend(degrade_char(c))
+    return raw.decode('utf-8')
+
+glitchcraft = ROOT / 'docs/wiki/glitchcraft'
+fixed_count = 0
+bom_stripped = 0
+
+for md in sorted(glitchcraft.glob('*.md')):
+    raw = md.read_bytes()
+    if not raw.startswith(b'\xef\xbb\xbf'):
+        continue  # wasn't touched by the PowerShell script
+
+    text = raw[3:].decode('utf-8')
+
+    try:
+        fixed = fix_encoding(text)
+    except UnicodeDecodeError as e:
+        print(f'DECODE ERROR {md.name}: {e}')
+        continue
+
+    if fixed != text:
+        for i, (ol, fl) in enumerate(zip(text.splitlines(), fixed.splitlines())):
+            if ol != fl:
+                print(f'{md.name}:{i+1}')
+                print(f'  WAS: {ol}')
+                print(f'  NOW: {fl}')
+        fixed_count += 1
+        md.write_text(fixed, encoding='utf-8')
+    else:
+        # Same content but BOM stripped
+        bom_stripped += 1
+        md.write_text(text, encoding='utf-8')
+
+print(f'\nEncoding-fixed: {fixed_count}, BOM-only stripped: {bom_stripped}')
diff --git a/docs/wiki/glitchcraft/ability-wheel-loop.md b/docs/wiki/glitchcraft/ability-wheel-loop.md
index 1f38de0c8..7b84b3400 100644
--- a/docs/wiki/glitchcraft/ability-wheel-loop.md
+++ b/docs/wiki/glitchcraft/ability-wheel-loop.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Ability Wheel Loop"
 abbreviation: "AWL"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/aeroculling.md b/docs/wiki/glitchcraft/aeroculling.md
index c8bc61513..59d580411 100644
--- a/docs/wiki/glitchcraft/aeroculling.md
+++ b/docs/wiki/glitchcraft/aeroculling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Aeroculling"
 abbreviation: "AC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/anti-gravity-glitch.md b/docs/wiki/glitchcraft/anti-gravity-glitch.md
index 73466bb4b..d1631774c 100644
--- a/docs/wiki/glitchcraft/anti-gravity-glitch.md
+++ b/docs/wiki/glitchcraft/anti-gravity-glitch.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Anti-Gravity Glitch"
 abbreviation: "AGG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/anti-gravity-objects.md b/docs/wiki/glitchcraft/anti-gravity-objects.md
index f389b15b8..7b4149ebb 100644
--- a/docs/wiki/glitchcraft/anti-gravity-objects.md
+++ b/docs/wiki/glitchcraft/anti-gravity-objects.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Anti-Gravity Objects"
 abbreviation: "AGO"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/antigrav-weapons.md b/docs/wiki/glitchcraft/antigrav-weapons.md
index 6cc9c4c57..75a24cc27 100644
--- a/docs/wiki/glitchcraft/antigrav-weapons.md
+++ b/docs/wiki/glitchcraft/antigrav-weapons.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "AntiGrav Weapons"
 abbreviation: "AGW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/arrow-smuggling.md b/docs/wiki/glitchcraft/arrow-smuggling.md
index d29979fcb..ac37dc1a5 100644
--- a/docs/wiki/glitchcraft/arrow-smuggling.md
+++ b/docs/wiki/glitchcraft/arrow-smuggling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Arrow Smuggling"
 abbreviation: "ASMU"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/arrow-unloading.md b/docs/wiki/glitchcraft/arrow-unloading.md
index b1a47d271..87b52a187 100644
--- a/docs/wiki/glitchcraft/arrow-unloading.md
+++ b/docs/wiki/glitchcraft/arrow-unloading.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Arrow Unloading"
 abbreviation: "AU"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/ascend-camera-glitch.md b/docs/wiki/glitchcraft/ascend-camera-glitch.md
index 4e47d219a..212776ff7 100644
--- a/docs/wiki/glitchcraft/ascend-camera-glitch.md
+++ b/docs/wiki/glitchcraft/ascend-camera-glitch.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Ascend Camera Glitch"
 abbreviation: "ACG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/ascend-rushing.md b/docs/wiki/glitchcraft/ascend-rushing.md
index d1bf52abb..8eae26a21 100644
--- a/docs/wiki/glitchcraft/ascend-rushing.md
+++ b/docs/wiki/glitchcraft/ascend-rushing.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Ascend Rushing"
 abbreviation: "AR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/ascend-storage.md b/docs/wiki/glitchcraft/ascend-storage.md
index 4798cca19..5afe0b76d 100644
--- a/docs/wiki/glitchcraft/ascend-storage.md
+++ b/docs/wiki/glitchcraft/ascend-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Ascend Storage"
 abbreviation: "ASTR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/autobuild-cancel-slide.md b/docs/wiki/glitchcraft/autobuild-cancel-slide.md
index 9943efd50..67bd56242 100644
--- a/docs/wiki/glitchcraft/autobuild-cancel-slide.md
+++ b/docs/wiki/glitchcraft/autobuild-cancel-slide.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Autobuild Cancel Slide"
 abbreviation: "ABCS"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/autobuild-duplication.md b/docs/wiki/glitchcraft/autobuild-duplication.md
index 7d69a3225..82db4825a 100644
--- a/docs/wiki/glitchcraft/autobuild-duplication.md
+++ b/docs/wiki/glitchcraft/autobuild-duplication.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Autobuild Duplication"
 abbreviation: "ABD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/autobuild-storage.md b/docs/wiki/glitchcraft/autobuild-storage.md
index a7c1d9b3b..cbecbfdc2 100644
--- a/docs/wiki/glitchcraft/autobuild-storage.md
+++ b/docs/wiki/glitchcraft/autobuild-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Autobuild Storage"
 abbreviation: "ABST"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/back-in-time-art.md b/docs/wiki/glitchcraft/back-in-time-art.md
index eaf81b425..662fafffd 100644
--- a/docs/wiki/glitchcraft/back-in-time-art.md
+++ b/docs/wiki/glitchcraft/back-in-time-art.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Back-in-Time Art"
 abbreviation: "BIT"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/back-to-back-bloodmoon.md b/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
index 857b14472..908c2797a 100644
--- a/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
+++ b/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Back to Back Bloodmoon"
 abbreviation: "BTBB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/banc-storage.md b/docs/wiki/glitchcraft/banc-storage.md
index 20080faae..9140708b0 100644
--- a/docs/wiki/glitchcraft/banc-storage.md
+++ b/docs/wiki/glitchcraft/banc-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Banc Storage"
 abbreviation: "BANC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1",]
diff --git a/docs/wiki/glitchcraft/bomb-skew.md b/docs/wiki/glitchcraft/bomb-skew.md
index c23bb9109..de32c8a65 100644
--- a/docs/wiki/glitchcraft/bomb-skew.md
+++ b/docs/wiki/glitchcraft/bomb-skew.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Bomb Skew"
 abbreviation: "BSK"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/bow-attachment-desync-bad-arrows.md b/docs/wiki/glitchcraft/bow-attachment-desync-bad-arrows.md
index ec9651dfc..cca7926de 100644
--- a/docs/wiki/glitchcraft/bow-attachment-desync-bad-arrows.md
+++ b/docs/wiki/glitchcraft/bow-attachment-desync-bad-arrows.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Bow Attachment Desync"
 abbreviation: "BAD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/bow-attachment-storage.md b/docs/wiki/glitchcraft/bow-attachment-storage.md
index e316b162b..0bbfdf335 100644
--- a/docs/wiki/glitchcraft/bow-attachment-storage.md
+++ b/docs/wiki/glitchcraft/bow-attachment-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Bow Attachment Storage"
 abbreviation: "BAS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/buoy-bouncing.md b/docs/wiki/glitchcraft/buoy-bouncing.md
index 7c5fae265..009f3062c 100644
--- a/docs/wiki/glitchcraft/buoy-bouncing.md
+++ b/docs/wiki/glitchcraft/buoy-bouncing.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Buoy Bouncing"
 abbreviation: "BB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/camera-cfw.md b/docs/wiki/glitchcraft/camera-cfw.md
index 6dda48215..6926236bf 100644
--- a/docs/wiki/glitchcraft/camera-cfw.md
+++ b/docs/wiki/glitchcraft/camera-cfw.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Camera CFW"
 abbreviation: "CFW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/camera-pose-glitch.md b/docs/wiki/glitchcraft/camera-pose-glitch.md
index a3ff9f691..4512da2f8 100644
--- a/docs/wiki/glitchcraft/camera-pose-glitch.md
+++ b/docs/wiki/glitchcraft/camera-pose-glitch.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Camera Pose Glitch"
 abbreviation: "CPG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/capsule-cel-shader-removal.md b/docs/wiki/glitchcraft/capsule-cel-shader-removal.md
index b88bf3ddb..f0af59b23 100644
--- a/docs/wiki/glitchcraft/capsule-cel-shader-removal.md
+++ b/docs/wiki/glitchcraft/capsule-cel-shader-removal.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Capsule Cel Shader Removal"
 abbreviation: "CCSR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/chasm-delay-zuggle.md b/docs/wiki/glitchcraft/chasm-delay-zuggle.md
index 090176518..8e3c30359 100644
--- a/docs/wiki/glitchcraft/chasm-delay-zuggle.md
+++ b/docs/wiki/glitchcraft/chasm-delay-zuggle.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Chasm Delay Zuggle"
 abbreviation: "CDZ"
 versions: ["1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/clear-camera-scope.md b/docs/wiki/glitchcraft/clear-camera-scope.md
index 5664df19e..d3b3dd88a 100644
--- a/docs/wiki/glitchcraft/clear-camera-scope.md
+++ b/docs/wiki/glitchcraft/clear-camera-scope.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Clear Camera/Scope"
 abbreviation: "CCS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/corrupt-meal.md b/docs/wiki/glitchcraft/corrupt-meal.md
index b5a9cb365..d7fd3633f 100644
--- a/docs/wiki/glitchcraft/corrupt-meal.md
+++ b/docs/wiki/glitchcraft/corrupt-meal.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Corrupt Meal"
 abbreviation: "CM"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/cucco-warping.md b/docs/wiki/glitchcraft/cucco-warping.md
index 9a0180f49..6fb8d4241 100644
--- a/docs/wiki/glitchcraft/cucco-warping.md
+++ b/docs/wiki/glitchcraft/cucco-warping.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Cucco Warping"
 abbreviation: "CW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/cull-zone-culling.md b/docs/wiki/glitchcraft/cull-zone-culling.md
index 15d0a124e..c9712d3d7 100644
--- a/docs/wiki/glitchcraft/cull-zone-culling.md
+++ b/docs/wiki/glitchcraft/cull-zone-culling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Cull Zone Culling"
 abbreviation: "CZC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/dispenser-storage.md b/docs/wiki/glitchcraft/dispenser-storage.md
index e53516c0a..f3eb296b9 100644
--- a/docs/wiki/glitchcraft/dispenser-storage.md
+++ b/docs/wiki/glitchcraft/dispenser-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Dispenser Storage"
 abbreviation: "DISP"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/display-duping.md b/docs/wiki/glitchcraft/display-duping.md
index dfcde1066..9ccc3aa69 100644
--- a/docs/wiki/glitchcraft/display-duping.md
+++ b/docs/wiki/glitchcraft/display-duping.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Display Duping"
 abbreviation: "DD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/display-master-sword.md b/docs/wiki/glitchcraft/display-master-sword.md
index 1d43a503b..efdb4d5e1 100644
--- a/docs/wiki/glitchcraft/display-master-sword.md
+++ b/docs/wiki/glitchcraft/display-master-sword.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Display Master Sword"
 abbreviation: "DMS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/dive-cancel-glide-boost.md b/docs/wiki/glitchcraft/dive-cancel-glide-boost.md
index cd8f5720a..8715db12e 100644
--- a/docs/wiki/glitchcraft/dive-cancel-glide-boost.md
+++ b/docs/wiki/glitchcraft/dive-cancel-glide-boost.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Dive Cancel Glide Boost"
 abbreviation: "DCGB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/double-tulin-boost.md b/docs/wiki/glitchcraft/double-tulin-boost.md
index b9e99872a..b7b8c402b 100644
--- a/docs/wiki/glitchcraft/double-tulin-boost.md
+++ b/docs/wiki/glitchcraft/double-tulin-boost.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Double Tulin Boost"
 abbreviation: "DTB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/double-unfuse-duplicashen.md b/docs/wiki/glitchcraft/double-unfuse-duplicashen.md
index fcda9e96c..2de590ddc 100644
--- a/docs/wiki/glitchcraft/double-unfuse-duplicashen.md
+++ b/docs/wiki/glitchcraft/double-unfuse-duplicashen.md
@@ -1,8 +1,8 @@
-´╗┐---
+---
 title: "Double Unfuse Duplicashen"
 abbreviation: "DUD"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
-credits: ["Li Shen (├®┬»ÔÇ░├º┬Ñ┼¥)"]
+credits: ["Ú»ëþÑ× (Li Shen)"]
 date: "2023-05-15"
 description: "Allows you to duplicate any material that can be fused to an arrow"
 aliases: ["double unfuse", "double unfuse duplicashen", "dupe unfuse"]
@@ -16,7 +16,7 @@ tags: ["duplication", "item", "weapon", "fuse", "arrow"]
 ---
 allows you to duplicate any material that can be fused to an arrow
 
-_Li Shen (├®┬»ÔÇ░├º┬Ñ┼¥) - 15 May 2023_
+_Ú»ëþÑ× (Li Shen) - 15 May 2023_
 
 ## Instructions
 ---
diff --git a/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md b/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md
index d011cdc5a..0bf22b669 100644
--- a/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md
+++ b/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Dpadlock-less Invizuggle"
 abbreviation: "DLI"
 versions: ["1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/drop-restriction.md b/docs/wiki/glitchcraft/drop-restriction.md
index 8a751b4e5..ed0056e15 100644
--- a/docs/wiki/glitchcraft/drop-restriction.md
+++ b/docs/wiki/glitchcraft/drop-restriction.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Drop Restriction"
 abbreviation: "DR"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/drop-smuggling.md b/docs/wiki/glitchcraft/drop-smuggling.md
index cee3f390c..5fe6ffb0c 100644
--- a/docs/wiki/glitchcraft/drop-smuggling.md
+++ b/docs/wiki/glitchcraft/drop-smuggling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Drop Smuggling"
 abbreviation: "DSMU"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/durability.md b/docs/wiki/glitchcraft/durability.md
index c2cbc5049..228619be5 100644
--- a/docs/wiki/glitchcraft/durability.md
+++ b/docs/wiki/glitchcraft/durability.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Durability-"
 abbreviation: "DUR"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/dynamic-zuggle.md b/docs/wiki/glitchcraft/dynamic-zuggle.md
index f9fe95ea8..96af24081 100644
--- a/docs/wiki/glitchcraft/dynamic-zuggle.md
+++ b/docs/wiki/glitchcraft/dynamic-zuggle.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Dynamic Zuggle"
 abbreviation: "DZG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/enemy-pickpocketing.md b/docs/wiki/glitchcraft/enemy-pickpocketing.md
index 64878977a..ec22ea12f 100644
--- a/docs/wiki/glitchcraft/enemy-pickpocketing.md
+++ b/docs/wiki/glitchcraft/enemy-pickpocketing.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Enemy Pickpocketing"
 abbreviation: "EP"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/equipment-smuggle.md b/docs/wiki/glitchcraft/equipment-smuggle.md
index f67081577..7fc7cff7f 100644
--- a/docs/wiki/glitchcraft/equipment-smuggle.md
+++ b/docs/wiki/glitchcraft/equipment-smuggle.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Equipment Smuggle"
 abbreviation: "ESMU"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/extended-throw-sprinting.md b/docs/wiki/glitchcraft/extended-throw-sprinting.md
index 92f55f141..cbf02143f 100644
--- a/docs/wiki/glitchcraft/extended-throw-sprinting.md
+++ b/docs/wiki/glitchcraft/extended-throw-sprinting.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Extended Throw Sprinting"
 abbreviation: "ETS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/floorping.md b/docs/wiki/glitchcraft/floorping.md
index cd2e48f7f..b27336bf2 100644
--- a/docs/wiki/glitchcraft/floorping.md
+++ b/docs/wiki/glitchcraft/floorping.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Floorping"
 abbreviation: "FLP"
 versions: ["1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/food-ability-buff-swap.md b/docs/wiki/glitchcraft/food-ability-buff-swap.md
index b9007af5f..4ca2b1159 100644
--- a/docs/wiki/glitchcraft/food-ability-buff-swap.md
+++ b/docs/wiki/glitchcraft/food-ability-buff-swap.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Food Ability Buff Swap"
 abbreviation: "FABS"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/forced-blood-moon.md b/docs/wiki/glitchcraft/forced-blood-moon.md
index 613c76539..7de2b0e07 100644
--- a/docs/wiki/glitchcraft/forced-blood-moon.md
+++ b/docs/wiki/glitchcraft/forced-blood-moon.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Forced Blood Moon"
 abbreviation: "FBM"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/fuse-entanglement.md b/docs/wiki/glitchcraft/fuse-entanglement.md
index 08a98eec3..7768a5c6e 100644
--- a/docs/wiki/glitchcraft/fuse-entanglement.md
+++ b/docs/wiki/glitchcraft/fuse-entanglement.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Fuse Entanglement"
 abbreviation: "FE"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/glue-removal.md b/docs/wiki/glitchcraft/glue-removal.md
index 31e460f4c..0dff7f802 100644
--- a/docs/wiki/glitchcraft/glue-removal.md
+++ b/docs/wiki/glitchcraft/glue-removal.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Glue Removal"
 abbreviation: "GR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/guard-less-active-shield.md b/docs/wiki/glitchcraft/guard-less-active-shield.md
index 435caaf3c..35b7e1d61 100644
--- a/docs/wiki/glitchcraft/guard-less-active-shield.md
+++ b/docs/wiki/glitchcraft/guard-less-active-shield.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Guard-less Active Shield"
 abbreviation: "GAS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md b/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
index e55ad309b..993e15b53 100644
--- a/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
+++ b/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Hand Locked Equipment Smuggling"
 abbreviation: "HLES"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/handy-job.md b/docs/wiki/glitchcraft/handy-job.md
index 7e7043637..4ff7c0812 100644
--- a/docs/wiki/glitchcraft/handy-job.md
+++ b/docs/wiki/glitchcraft/handy-job.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Handy Job"
 abbreviation: "HJ"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/hero-path-link-storage.md b/docs/wiki/glitchcraft/hero-path-link-storage.md
index 307f605e9..63e836619 100644
--- a/docs/wiki/glitchcraft/hero-path-link-storage.md
+++ b/docs/wiki/glitchcraft/hero-path-link-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Hero Path Link Storage"
 abbreviation: "HPLS"
 versions: ["1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/hestu-scamming.md b/docs/wiki/glitchcraft/hestu-scamming.md
index 09133908b..36195aa7a 100644
--- a/docs/wiki/glitchcraft/hestu-scamming.md
+++ b/docs/wiki/glitchcraft/hestu-scamming.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Hestu Scamming"
 abbreviation: "HSCA"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/hold-smuggling.md b/docs/wiki/glitchcraft/hold-smuggling.md
index e14209da1..0cccd5de1 100644
--- a/docs/wiki/glitchcraft/hold-smuggling.md
+++ b/docs/wiki/glitchcraft/hold-smuggling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Hold Smuggling"
 abbreviation: "HSM"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/infinite-balloon.md b/docs/wiki/glitchcraft/infinite-balloon.md
index 4202f2a7f..f27b35376 100644
--- a/docs/wiki/glitchcraft/infinite-balloon.md
+++ b/docs/wiki/glitchcraft/infinite-balloon.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Infinite Balloon"
 abbreviation: "IBAL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/infinite-bubbul-frog-gems.md b/docs/wiki/glitchcraft/infinite-bubbul-frog-gems.md
index ff7a8e41d..8c4193dba 100644
--- a/docs/wiki/glitchcraft/infinite-bubbul-frog-gems.md
+++ b/docs/wiki/glitchcraft/infinite-bubbul-frog-gems.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Infinite Bubbul Frog Gems"
 abbreviation: "IBFG"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/infinite-damage.md b/docs/wiki/glitchcraft/infinite-damage.md
index d0bc7649c..fb0e784cc 100644
--- a/docs/wiki/glitchcraft/infinite-damage.md
+++ b/docs/wiki/glitchcraft/infinite-damage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Infinite Damage"
 abbreviation: "IDMG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/inventory-shift-duplication.md b/docs/wiki/glitchcraft/inventory-shift-duplication.md
index 43e07fff2..62a5201f6 100644
--- a/docs/wiki/glitchcraft/inventory-shift-duplication.md
+++ b/docs/wiki/glitchcraft/inventory-shift-duplication.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Inventory Shift Duplication"
 abbreviation: "ISD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/invizuggle.md b/docs/wiki/glitchcraft/invizuggle.md
index 1182dea45..dbd579568 100644
--- a/docs/wiki/glitchcraft/invizuggle.md
+++ b/docs/wiki/glitchcraft/invizuggle.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Invizuggle"
 abbreviation: "IVZ"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/item-throw-hitbox-disable.md b/docs/wiki/glitchcraft/item-throw-hitbox-disable.md
index 79e5bd94c..7ce6a436d 100644
--- a/docs/wiki/glitchcraft/item-throw-hitbox-disable.md
+++ b/docs/wiki/glitchcraft/item-throw-hitbox-disable.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Item Throw Hitbox Disable"
 abbreviation: "ITHD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/jumpslash-canceling.md b/docs/wiki/glitchcraft/jumpslash-canceling.md
index eab22450f..8685edf2e 100644
--- a/docs/wiki/glitchcraft/jumpslash-canceling.md
+++ b/docs/wiki/glitchcraft/jumpslash-canceling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Jumpslash Canceling"
 abbreviation: "JSC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/laser-oob.md b/docs/wiki/glitchcraft/laser-oob.md
index d34599d8e..6a1e70125 100644
--- a/docs/wiki/glitchcraft/laser-oob.md
+++ b/docs/wiki/glitchcraft/laser-oob.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Laser-OOB"
 abbreviation: "LOOB"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/lift-fuse-interrupt.md b/docs/wiki/glitchcraft/lift-fuse-interrupt.md
index 7829094c0..cdf94d8f3 100644
--- a/docs/wiki/glitchcraft/lift-fuse-interrupt.md
+++ b/docs/wiki/glitchcraft/lift-fuse-interrupt.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Lift Fuse Interrupt"
 abbreviation: "LFI"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/lift-warping.md b/docs/wiki/glitchcraft/lift-warping.md
index 4a8d316c8..87b8dfb1e 100644
--- a/docs/wiki/glitchcraft/lift-warping.md
+++ b/docs/wiki/glitchcraft/lift-warping.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Lift Warping"
 abbreviation: "LW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/like-like-culling.md b/docs/wiki/glitchcraft/like-like-culling.md
index cafe05352..9214748a0 100644
--- a/docs/wiki/glitchcraft/like-like-culling.md
+++ b/docs/wiki/glitchcraft/like-like-culling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Like-Like Culling"
 abbreviation: "LLC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md b/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md
index 9c0d6b405..7c3bd22b5 100644
--- a/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md
+++ b/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Like Like New Textbox Softlock"
 abbreviation: "LLTS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/like-like-warping.md b/docs/wiki/glitchcraft/like-like-warping.md
index 5d65b6cb7..7a13cbbd3 100644
--- a/docs/wiki/glitchcraft/like-like-warping.md
+++ b/docs/wiki/glitchcraft/like-like-warping.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Like-Like Warping"
 abbreviation: "LLW"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/likelike-stick-smuggling.md b/docs/wiki/glitchcraft/likelike-stick-smuggling.md
index f639a6f1f..247538483 100644
--- a/docs/wiki/glitchcraft/likelike-stick-smuggling.md
+++ b/docs/wiki/glitchcraft/likelike-stick-smuggling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "LikeLike Stick Smuggling"
 abbreviation: "LLSS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/long-jump.md b/docs/wiki/glitchcraft/long-jump.md
index d48baf9f1..d4b13367c 100644
--- a/docs/wiki/glitchcraft/long-jump.md
+++ b/docs/wiki/glitchcraft/long-jump.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Long Jump"
 abbreviation: "LJ"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/map-flickering.md b/docs/wiki/glitchcraft/map-flickering.md
index ff9598daf..9e6185f4f 100644
--- a/docs/wiki/glitchcraft/map-flickering.md
+++ b/docs/wiki/glitchcraft/map-flickering.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Map Flickering"
 abbreviation: "MF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
diff --git a/docs/wiki/glitchcraft/map-storage.md b/docs/wiki/glitchcraft/map-storage.md
index 42f79ac9e..4819b13ce 100644
--- a/docs/wiki/glitchcraft/map-storage.md
+++ b/docs/wiki/glitchcraft/map-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Map Storage"
 abbreviation: "MSTR"
 versions: ["1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/master-sword-liberation.md b/docs/wiki/glitchcraft/master-sword-liberation.md
index d37564fbe..4c2c96399 100644
--- a/docs/wiki/glitchcraft/master-sword-liberation.md
+++ b/docs/wiki/glitchcraft/master-sword-liberation.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Master Sword Liberation"
 abbreviation: "MSL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/memory-buffering.md b/docs/wiki/glitchcraft/memory-buffering.md
index de7cbd691..7dbc6bbca 100644
--- a/docs/wiki/glitchcraft/memory-buffering.md
+++ b/docs/wiki/glitchcraft/memory-buffering.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Memory Buffering"
 abbreviation: "MB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/memory-interrupt.md b/docs/wiki/glitchcraft/memory-interrupt.md
index 2c894f6e2..ede879827 100644
--- a/docs/wiki/glitchcraft/memory-interrupt.md
+++ b/docs/wiki/glitchcraft/memory-interrupt.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Memory Interrupt"
 abbreviation: "MI"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/message-not-found.md b/docs/wiki/glitchcraft/message-not-found.md
index f4488820d..5ca150bd5 100644
--- a/docs/wiki/glitchcraft/message-not-found.md
+++ b/docs/wiki/glitchcraft/message-not-found.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Message Not Found"
 abbreviation: "MNF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/midair-item-transmutation.md b/docs/wiki/glitchcraft/midair-item-transmutation.md
index daa5683c7..8cc820fa6 100644
--- a/docs/wiki/glitchcraft/midair-item-transmutation.md
+++ b/docs/wiki/glitchcraft/midair-item-transmutation.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Midair Item Transmutation"
 abbreviation: "MIT"
 versions: ["1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/midair-sort-duplication.md b/docs/wiki/glitchcraft/midair-sort-duplication.md
index 741f881fd..f577a8f59 100644
--- a/docs/wiki/glitchcraft/midair-sort-duplication.md
+++ b/docs/wiki/glitchcraft/midair-sort-duplication.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Midair Sort Duplication"
 abbreviation: "MSD"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/midair-throw-duplication.md b/docs/wiki/glitchcraft/midair-throw-duplication.md
index 1720aa7f6..758a2a8f6 100644
--- a/docs/wiki/glitchcraft/midair-throw-duplication.md
+++ b/docs/wiki/glitchcraft/midair-throw-duplication.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Midair Throw Duplication"
 abbreviation: "MTD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/minecart-rail-collision-launching.md b/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
index 8dcd6333c..cdcaa3c93 100644
--- a/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
+++ b/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
@@ -1,8 +1,8 @@
-´╗┐---
+---
 title: "Minecart Rail Collision Launching"
 abbreviation: "MRCL"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
-credits: ["├ú┬ü┬Ø├úÔÇÜÔÇ░-├ú┬üÔÇó├úÔÇÜÔÇ£"]
+credits: ["ÒüØÒéë-ÒüòÒéô"]
 date: "2023-05-18"
 description: "Allows the usage of minecarts to be launched from awkward collision grabbing on rails."
 aliases: ["minecart collision", "minecart rail collision", "rail collision launching", "collision launch", "collision launching"]
@@ -16,7 +16,7 @@ tags: ["launching"]
 ---
 Allows the usage of minecarts to be launched from awkward collision grabbing on rails.
 
-_├ú┬ü┬Ø├úÔÇÜÔÇ░-├ú┬üÔÇó├úÔÇÜÔÇ£ - 18 May 2023_
+_ÒüØÒéë-ÒüòÒéô - 18 May 2023_
 
 ## Instructions
 ---
diff --git a/docs/wiki/glitchcraft/mineru-ability-desync.md b/docs/wiki/glitchcraft/mineru-ability-desync.md
index 77ce40c37..5ee1c8770 100644
--- a/docs/wiki/glitchcraft/mineru-ability-desync.md
+++ b/docs/wiki/glitchcraft/mineru-ability-desync.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Mineru Ability Desync"
 abbreviation: "MAD"
 versions: ["1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/mineru-aim-permanence.md b/docs/wiki/glitchcraft/mineru-aim-permanence.md
index 3fa3a9c7c..a557d62d8 100644
--- a/docs/wiki/glitchcraft/mineru-aim-permanence.md
+++ b/docs/wiki/glitchcraft/mineru-aim-permanence.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Mineru Aim Permanence"
 abbreviation: "MAIP"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/mineru-text-storage.md b/docs/wiki/glitchcraft/mineru-text-storage.md
index c0613b090..52b2e9594 100644
--- a/docs/wiki/glitchcraft/mineru-text-storage.md
+++ b/docs/wiki/glitchcraft/mineru-text-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Mineru Text Storage"
 abbreviation: "MTS"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/mnf-fusing.md b/docs/wiki/glitchcraft/mnf-fusing.md
index ea399a7b0..35ad52fa7 100644
--- a/docs/wiki/glitchcraft/mnf-fusing.md
+++ b/docs/wiki/glitchcraft/mnf-fusing.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "MNF Fusing"
 abbreviation: "MNFF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/mnf-zuggle-fuse.md b/docs/wiki/glitchcraft/mnf-zuggle-fuse.md
index 931032360..313e06fac 100644
--- a/docs/wiki/glitchcraft/mnf-zuggle-fuse.md
+++ b/docs/wiki/glitchcraft/mnf-zuggle-fuse.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "MNF Zuggle Fuse"
 abbreviation: "MZF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md b/docs/wiki/glitchcraft/modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md
index d0c754e2b..db89075bc 100644
--- a/docs/wiki/glitchcraft/modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md
+++ b/docs/wiki/glitchcraft/modifier-deletion-weapon-state-transfer-modifier-deletion-wst.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Modifier Deletion Weapon State Transfer"
 abbreviation: "MDWST"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/modifier-only-transfer.md b/docs/wiki/glitchcraft/modifier-only-transfer.md
index 3b3d1477a..4b30fdf00 100644
--- a/docs/wiki/glitchcraft/modifier-only-transfer.md
+++ b/docs/wiki/glitchcraft/modifier-only-transfer.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Modifier ONLY Transfer"
 abbreviation: "MOT"
 versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/mount-lock.md b/docs/wiki/glitchcraft/mount-lock.md
index ab7dfb4ce..b74523392 100644
--- a/docs/wiki/glitchcraft/mount-lock.md
+++ b/docs/wiki/glitchcraft/mount-lock.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Mount Lock"
 abbreviation: "ML"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/mozdor-jumping-slashing.md b/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
index 8eab29b82..c94edc8a7 100644
--- a/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
+++ b/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Mozdor Jumping/Slashing"
 abbreviation: "MJS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/msnf-glowing.md b/docs/wiki/glitchcraft/msnf-glowing.md
index e856accac..c66baf801 100644
--- a/docs/wiki/glitchcraft/msnf-glowing.md
+++ b/docs/wiki/glitchcraft/msnf-glowing.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "MSNF glowing"
 abbreviation: "MG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/new-item-desync-equipment-duping.md b/docs/wiki/glitchcraft/new-item-desync-equipment-duping.md
index c588379c4..da6d319ed 100644
--- a/docs/wiki/glitchcraft/new-item-desync-equipment-duping.md
+++ b/docs/wiki/glitchcraft/new-item-desync-equipment-duping.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "New Item Desync"
 abbreviation: "NID"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/null-dropping.md b/docs/wiki/glitchcraft/null-dropping.md
index 7a7e4e295..0ad3be6b7 100644
--- a/docs/wiki/glitchcraft/null-dropping.md
+++ b/docs/wiki/glitchcraft/null-dropping.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Null Dropping"
 abbreviation: "ND"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/object-moe-enlargement.md b/docs/wiki/glitchcraft/object-moe-enlargement.md
index 0ffcbaad0..b4cbecd0c 100644
--- a/docs/wiki/glitchcraft/object-moe-enlargement.md
+++ b/docs/wiki/glitchcraft/object-moe-enlargement.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Object (Moe) Enlargement"
 abbreviation: "MOE"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/ocklusion.md b/docs/wiki/glitchcraft/ocklusion.md
index 65b0c0410..c457b4f01 100644
--- a/docs/wiki/glitchcraft/ocklusion.md
+++ b/docs/wiki/glitchcraft/ocklusion.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Ocklusion"
 abbreviation: "OCKL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/octodupe.md b/docs/wiki/glitchcraft/octodupe.md
index 56061b4ca..15fb97bdc 100644
--- a/docs/wiki/glitchcraft/octodupe.md
+++ b/docs/wiki/glitchcraft/octodupe.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Octodupe"
 abbreviation: "OD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/prologue-escape.md b/docs/wiki/glitchcraft/prologue-escape.md
index 00f0c9458..fc320a0a5 100644
--- a/docs/wiki/glitchcraft/prologue-escape.md
+++ b/docs/wiki/glitchcraft/prologue-escape.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Prologue Escape"
 abbreviation: "PE"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/proxy-glitches.md b/docs/wiki/glitchcraft/proxy-glitches.md
index db1269763..cd5d19658 100644
--- a/docs/wiki/glitchcraft/proxy-glitches.md
+++ b/docs/wiki/glitchcraft/proxy-glitches.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Proxy Glitches"
 abbreviation: "PG"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/quick-smuggling.md b/docs/wiki/glitchcraft/quick-smuggling.md
index cab0cbfa6..b755f5a84 100644
--- a/docs/wiki/glitchcraft/quick-smuggling.md
+++ b/docs/wiki/glitchcraft/quick-smuggling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Quick Smuggling"
 abbreviation: "QS"
 versions: ["1.2.0"]
diff --git a/docs/wiki/glitchcraft/reball.md b/docs/wiki/glitchcraft/reball.md
index 72a9f8727..fb190df7e 100644
--- a/docs/wiki/glitchcraft/reball.md
+++ b/docs/wiki/glitchcraft/reball.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Reball"
 abbreviation: "RBL"
 versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/recall-cancel.md b/docs/wiki/glitchcraft/recall-cancel.md
index 180e4ba46..011acb3ee 100644
--- a/docs/wiki/glitchcraft/recall-cancel.md
+++ b/docs/wiki/glitchcraft/recall-cancel.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Recall Cancel"
 abbreviation: "RCC"
 versions: ["1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/recall-clip.md b/docs/wiki/glitchcraft/recall-clip.md
index 2b396f6c2..4e462b391 100644
--- a/docs/wiki/glitchcraft/recall-clip.md
+++ b/docs/wiki/glitchcraft/recall-clip.md
@@ -1,8 +1,8 @@
-´╗┐---
+---
 title: "Recall Clip"
 abbreviation: "RC"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
-credits: ["├ú┬üÔÇ£├úÔÇÜÔÇ£├ú┬ü┬Ø├úÔÇÜ┬ü"]
+credits: ["ÒüôÒéôÒüØÒéü"]
 date: "2023-05-16"
 description: "Allows you to clip through things using a large object and recall"
 aliases: ["recall clip", "recall-clip glitch", "recall-clip", "recallclip"]
@@ -16,7 +16,7 @@ tags: ["clipping", "ultrahand", "recall"]
 ---
 Allows you to clip through things using a large object and recall
 
-_├ú┬üÔÇ£├úÔÇÜÔÇ£├ú┬ü┬Ø├úÔÇÜ┬ü - 16 May 2023_
+_ÒüôÒéôÒüØÒéü - 16 May 2023_
 
 ## Instructions
 ---
diff --git a/docs/wiki/glitchcraft/recall-drop-stacking.md b/docs/wiki/glitchcraft/recall-drop-stacking.md
index b67cd0415..56c510125 100644
--- a/docs/wiki/glitchcraft/recall-drop-stacking.md
+++ b/docs/wiki/glitchcraft/recall-drop-stacking.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Recall Drop Stacking"
 abbreviation: "RDS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/recall-launch.md b/docs/wiki/glitchcraft/recall-launch.md
index 9bf339469..746dfc1b2 100644
--- a/docs/wiki/glitchcraft/recall-launch.md
+++ b/docs/wiki/glitchcraft/recall-launch.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Recall Launch"
 abbreviation: "RL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/recipe-storage.md b/docs/wiki/glitchcraft/recipe-storage.md
index d3e8c0acf..9120f25ec 100644
--- a/docs/wiki/glitchcraft/recipe-storage.md
+++ b/docs/wiki/glitchcraft/recipe-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Recipe Storage"
 abbreviation: "RS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/remote-arrow-trap.md b/docs/wiki/glitchcraft/remote-arrow-trap.md
index 8a3db46be..2d2ebf512 100644
--- a/docs/wiki/glitchcraft/remote-arrow-trap.md
+++ b/docs/wiki/glitchcraft/remote-arrow-trap.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Remote Arrow"
 abbreviation: "RAT"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
diff --git a/docs/wiki/glitchcraft/replacement-actor-fuse-entanglement.md b/docs/wiki/glitchcraft/replacement-actor-fuse-entanglement.md
index 016d0f53e..3289e3112 100644
--- a/docs/wiki/glitchcraft/replacement-actor-fuse-entanglement.md
+++ b/docs/wiki/glitchcraft/replacement-actor-fuse-entanglement.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Replacement Actor Fuse Entanglement"
 abbreviation: "RAFE"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md b/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md
index e9af0aea8..57817c8d8 100644
--- a/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md
+++ b/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Resync Fuse Entanglement"
 abbreviation: "RFE"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/reverse-ascend-storage.md b/docs/wiki/glitchcraft/reverse-ascend-storage.md
index 68efb9be3..5b54dbb55 100644
--- a/docs/wiki/glitchcraft/reverse-ascend-storage.md
+++ b/docs/wiki/glitchcraft/reverse-ascend-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Reverse Ascend Storage"
 abbreviation: "RAS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/sage-madness.md b/docs/wiki/glitchcraft/sage-madness.md
index 28677a4d4..afa114901 100644
--- a/docs/wiki/glitchcraft/sage-madness.md
+++ b/docs/wiki/glitchcraft/sage-madness.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Sage Madness"
 abbreviation: "SM"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/sage-recycling.md b/docs/wiki/glitchcraft/sage-recycling.md
index 56355648f..a9eb41d3b 100644
--- a/docs/wiki/glitchcraft/sage-recycling.md
+++ b/docs/wiki/glitchcraft/sage-recycling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Sage Recycling"
 abbreviation: "SRCY"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/save-load-dupe.md b/docs/wiki/glitchcraft/save-load-dupe.md
index a503d2b5e..433745b36 100644
--- a/docs/wiki/glitchcraft/save-load-dupe.md
+++ b/docs/wiki/glitchcraft/save-load-dupe.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Save Load Dupe"
 abbreviation: "SLD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/scope-render-cancel.md b/docs/wiki/glitchcraft/scope-render-cancel.md
index 0ee2285f4..79f227049 100644
--- a/docs/wiki/glitchcraft/scope-render-cancel.md
+++ b/docs/wiki/glitchcraft/scope-render-cancel.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Scope Render Cancel"
 abbreviation: "SRC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/shadow-void-icons.md b/docs/wiki/glitchcraft/shadow-void-icons.md
index 45e16ed76..849aeef87 100644
--- a/docs/wiki/glitchcraft/shadow-void-icons.md
+++ b/docs/wiki/glitchcraft/shadow-void-icons.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Shadow/Void Icons"
 abbreviation: "SVI"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
diff --git a/docs/wiki/glitchcraft/shock-cold-fuse.md b/docs/wiki/glitchcraft/shock-cold-fuse.md
index d820aefe8..3e26a72ec 100644
--- a/docs/wiki/glitchcraft/shock-cold-fuse.md
+++ b/docs/wiki/glitchcraft/shock-cold-fuse.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Shock Cold Fuse"
 abbreviation: "SCF"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/slate-storage.md b/docs/wiki/glitchcraft/slate-storage.md
index 2b42b5c07..409758f5f 100644
--- a/docs/wiki/glitchcraft/slate-storage.md
+++ b/docs/wiki/glitchcraft/slate-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Slate Storage"
 abbreviation: "SLST"
 versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/spring-fall-damage-cancel.md b/docs/wiki/glitchcraft/spring-fall-damage-cancel.md
index 262e0b621..15daf42a2 100644
--- a/docs/wiki/glitchcraft/spring-fall-damage-cancel.md
+++ b/docs/wiki/glitchcraft/spring-fall-damage-cancel.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Spring Fall Damage Cancel"
 abbreviation: "SFDC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/spring-strangeness.md b/docs/wiki/glitchcraft/spring-strangeness.md
index ff13b8497..61540b85f 100644
--- a/docs/wiki/glitchcraft/spring-strangeness.md
+++ b/docs/wiki/glitchcraft/spring-strangeness.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Spring Strangeness"
 abbreviation: "STRS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/springdolling.md b/docs/wiki/glitchcraft/springdolling.md
index 0a5f57d5f..f8487ccd4 100644
--- a/docs/wiki/glitchcraft/springdolling.md
+++ b/docs/wiki/glitchcraft/springdolling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Springdolling"
 abbreviation: "SDOL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/stack-splitting.md b/docs/wiki/glitchcraft/stack-splitting.md
index b42de96c2..c2201dd2e 100644
--- a/docs/wiki/glitchcraft/stack-splitting.md
+++ b/docs/wiki/glitchcraft/stack-splitting.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Stack Splitting"
 abbreviation: "SSPL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
diff --git a/docs/wiki/glitchcraft/stamina-depletion-freeze.md b/docs/wiki/glitchcraft/stamina-depletion-freeze.md
index 3bdc69143..5e5089fa4 100644
--- a/docs/wiki/glitchcraft/stamina-depletion-freeze.md
+++ b/docs/wiki/glitchcraft/stamina-depletion-freeze.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Stamina Depletion Freeze"
 abbreviation: "SDF"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/surf-storage.md b/docs/wiki/glitchcraft/surf-storage.md
index 89c617267..540c9ed02 100644
--- a/docs/wiki/glitchcraft/surf-storage.md
+++ b/docs/wiki/glitchcraft/surf-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Surf storage"
 abbreviation: "SSTR"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/swap-resync.md b/docs/wiki/glitchcraft/swap-resync.md
index 48b8e2354..64621949f 100644
--- a/docs/wiki/glitchcraft/swap-resync.md
+++ b/docs/wiki/glitchcraft/swap-resync.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Swap Resync"
 abbreviation: "SR"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0"]
diff --git a/docs/wiki/glitchcraft/temporary-devices.md b/docs/wiki/glitchcraft/temporary-devices.md
index 7d989aac7..3621ac7ac 100644
--- a/docs/wiki/glitchcraft/temporary-devices.md
+++ b/docs/wiki/glitchcraft/temporary-devices.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Temporary Devices"
 abbreviation: "TD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/throken.md b/docs/wiki/glitchcraft/throken.md
index 2a56a8d4d..0e455c0b4 100644
--- a/docs/wiki/glitchcraft/throken.md
+++ b/docs/wiki/glitchcraft/throken.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Throken"
 abbreviation: "THK"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/throw-cancelling.md b/docs/wiki/glitchcraft/throw-cancelling.md
index 7de957d98..82275c35a 100644
--- a/docs/wiki/glitchcraft/throw-cancelling.md
+++ b/docs/wiki/glitchcraft/throw-cancelling.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Throw Cancelling"
 abbreviation: "TC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/time-bomb-cancel.md b/docs/wiki/glitchcraft/time-bomb-cancel.md
index 1a389decf..5ac13f274 100644
--- a/docs/wiki/glitchcraft/time-bomb-cancel.md
+++ b/docs/wiki/glitchcraft/time-bomb-cancel.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Time Bomb cancel"
 abbreviation: "TBC"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/travel-medallion-storage.md b/docs/wiki/glitchcraft/travel-medallion-storage.md
index a2bf61ca5..d3629fa4a 100644
--- a/docs/wiki/glitchcraft/travel-medallion-storage.md
+++ b/docs/wiki/glitchcraft/travel-medallion-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Travel Medallion storage"
 abbreviation: "TMS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/two-handed-with-shield.md b/docs/wiki/glitchcraft/two-handed-with-shield.md
index 6076b6818..89e6c5077 100644
--- a/docs/wiki/glitchcraft/two-handed-with-shield.md
+++ b/docs/wiki/glitchcraft/two-handed-with-shield.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Two Handed With Shield"
 abbreviation: "THWS"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/ultrabroken.md b/docs/wiki/glitchcraft/ultrabroken.md
index 94b92b9d4..dcc606fd4 100644
--- a/docs/wiki/glitchcraft/ultrabroken.md
+++ b/docs/wiki/glitchcraft/ultrabroken.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Ultrabroken"
 abbreviation: "UB"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
diff --git a/docs/wiki/glitchcraft/unload-duping.md b/docs/wiki/glitchcraft/unload-duping.md
index 72436784e..00fe8d7b6 100644
--- a/docs/wiki/glitchcraft/unload-duping.md
+++ b/docs/wiki/glitchcraft/unload-duping.md
@@ -1,8 +1,8 @@
-´╗┐---
+---
 title: "Unload Duping"
 abbreviation: "UD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
-credits: ["├®┬¡ÔÇØ├ª┬│ÔÇó├ª┼ô┬¼├Ñ┬░┬▒├ñ┬©┬ì├º┬ºÔÇÿ├Ñ┬¡┬ª", "├Ñ┬ìãÆ├Ñ┬╣┬┤├¿┼Æ┬Â├®┬Ñ┬╝"]
+credits: ["Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª (magic is not science)", "ÕìâÕ╣┤ÞîÂÚÑ╝ (Thousand Year Tea)"]
 date: "2023-05-31"
 description: "By firing arrows between load triggers, items fused to the arrows get dropped. Allowing you to dupe items with multi-shot bows."
 aliases: ["unload-duping"]
@@ -16,7 +16,7 @@ tags: ["duplication", "item", "culling", "fuse", "bow", "arrow"]
 ---
 By firing arrows between load triggers, items fused to the arrows get dropped. Allowing you to dupe items with multi-shot bows.
 
-_├®┬¡ÔÇØ├ª┬│ÔÇó├ª┼ô┬¼├Ñ┬░┬▒├ñ┬©┬ì├º┬ºÔÇÿ├Ñ┬¡┬ª (magic is not science), ├Ñ┬ìãÆ├Ñ┬╣┬┤├¿┼Æ┬Â├®┬Ñ┬╝ (Thousand Year Tea) - 31 May 2023_
+_Ú¡öµ│òµ£¼Õ░▒õ©ìþºæÕ¡ª (magic is not science), ÕìâÕ╣┤ÞîÂÚÑ╝ (Thousand Year Tea) - 31 May 2023_
 
 ## Instructions
 ---
diff --git a/docs/wiki/glitchcraft/void-holding.md b/docs/wiki/glitchcraft/void-holding.md
index f72beb78d..77f92bcfb 100644
--- a/docs/wiki/glitchcraft/void-holding.md
+++ b/docs/wiki/glitchcraft/void-holding.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Void Holding"
 abbreviation: "VH"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/wacko-attacko.md b/docs/wiki/glitchcraft/wacko-attacko.md
index 75da211b3..b1c31c506 100644
--- a/docs/wiki/glitchcraft/wacko-attacko.md
+++ b/docs/wiki/glitchcraft/wacko-attacko.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Wacko Attacko"
 abbreviation: "WATK"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/weapon-extensions.md b/docs/wiki/glitchcraft/weapon-extensions.md
index f8e3ac5fc..fb765b229 100644
--- a/docs/wiki/glitchcraft/weapon-extensions.md
+++ b/docs/wiki/glitchcraft/weapon-extensions.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Weapon Extensions"
 abbreviation: "WEXT"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/weapon-sheath-offset.md b/docs/wiki/glitchcraft/weapon-sheath-offset.md
index ccd9dad71..02e7f9a27 100644
--- a/docs/wiki/glitchcraft/weapon-sheath-offset.md
+++ b/docs/wiki/glitchcraft/weapon-sheath-offset.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Weapon Sheath Offset"
 abbreviation: "WSO"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/weapon-stacking-duplication.md b/docs/wiki/glitchcraft/weapon-stacking-duplication.md
index ce7b042d1..88b872059 100644
--- a/docs/wiki/glitchcraft/weapon-stacking-duplication.md
+++ b/docs/wiki/glitchcraft/weapon-stacking-duplication.md
@@ -1,8 +1,8 @@
-´╗┐---
+---
 title: "Weapon Stacking Duplication"
 abbreviation: "WSD"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
-credits: ["Erling├®ÔäóÔÇ×├¿┬║┬½"]
+credits: ["ErlingÚÖäÞ║½"]
 date: "2023-05-16"
 description: "Allows for a quick dupe of any weapon, bow or shield"
 aliases: ["weapon stacking", "stacking weapons", "weapon stacking dupe", "weapon-stacking-duplication"]
@@ -16,7 +16,7 @@ tags: ["duplication", "item", "weapon", "equipment", "bow"]
 ---
 Allows for a quick dupe of any weapon, bow or shield
 
-_Erling├®ÔäóÔÇ×├¿┬║┬½ - 16 May 2023_
+_ErlingÚÖäÞ║½ - 16 May 2023_
 
 ## Instructions
 ---
diff --git a/docs/wiki/glitchcraft/weapon-state-transfer.md b/docs/wiki/glitchcraft/weapon-state-transfer.md
index 075e45803..7111d5904 100644
--- a/docs/wiki/glitchcraft/weapon-state-transfer.md
+++ b/docs/wiki/glitchcraft/weapon-state-transfer.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Weapon State Transfer"
 abbreviation: "WST"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/wheel-zoomy-also-known-as-wheel-wacko-boingo.md b/docs/wiki/glitchcraft/wheel-zoomy-also-known-as-wheel-wacko-boingo.md
index 422fc00a5..458353328 100644
--- a/docs/wiki/glitchcraft/wheel-zoomy-also-known-as-wheel-wacko-boingo.md
+++ b/docs/wiki/glitchcraft/wheel-zoomy-also-known-as-wheel-wacko-boingo.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Wheel Zoomy"
 abbreviation: "WZ"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md b/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
index b2c44199a..b58c7df34 100644
--- a/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
+++ b/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Zonai Inventory Shift Dupe"
 abbreviation: "ZISD"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
diff --git a/docs/wiki/glitchcraft/zonai-sort-duplication.md b/docs/wiki/glitchcraft/zonai-sort-duplication.md
index 49d864953..624b0168e 100644
--- a/docs/wiki/glitchcraft/zonai-sort-duplication.md
+++ b/docs/wiki/glitchcraft/zonai-sort-duplication.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Zonai Sort Duplication"
 abbreviation: "ZSD"
 versions: ["1.0.0", "1.1.0", "1.1.1"]
diff --git a/docs/wiki/glitchcraft/zonai-storage.md b/docs/wiki/glitchcraft/zonai-storage.md
index f97e5193c..4699b9588 100644
--- a/docs/wiki/glitchcraft/zonai-storage.md
+++ b/docs/wiki/glitchcraft/zonai-storage.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Zonai Storage"
 abbreviation: "ZS"
 versions: ["1.0.0"]
diff --git a/docs/wiki/glitchcraft/zuggle.md b/docs/wiki/glitchcraft/zuggle.md
index 27ce9647f..378a69647 100644
--- a/docs/wiki/glitchcraft/zuggle.md
+++ b/docs/wiki/glitchcraft/zuggle.md
@@ -1,4 +1,4 @@
-´╗┐---
+---
 title: "Zuggle"
 abbreviation: "ZGL"
 versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]

----

*** COMMIT: 76f8d8820bfe936b5cfd3defff337e4d065d59e1
Author: MandelbrotChay <mandelbrotchaylay@gmail.com>
Date: Tue Feb 24 23:25:01 2026 -0800
Subject: Update zuggle-overload-out-of-bounds.md

commit 76f8d8820bfe936b5cfd3defff337e4d065d59e1
Author: MandelbrotChay <mandelbrotchaylay@gmail.com>
Date:   Tue Feb 24 23:25:01 2026 -0800

    Update zuggle-overload-out-of-bounds.md

diff --git a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
index b6ce78600..bd72ec17d 100644
--- a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
+++ b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
@@ -1,8 +1,8 @@
 ---
 title: "Zuggle Overload Out Of Bounds"
 abbreviation: "ZOOB"
-versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
-credits: ["AngryEgg"]
+versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2" "1.2.0" "1.2.1"]
+credits: ["AngryEgg" "Dark" "Toti Sauce"]
 date: "2023-05-18"
 description: "Allows you to clip OOB using zuggle overload"
 aliases: ["zuggle-overload-oob", "zuggle overload oob", "zo oob"]
@@ -16,21 +16,29 @@ tags: ["clipping", "oob", "zuggling", "overload"]
 ---
 Allows you to clip OOB using zuggle overload
 
-_AngryEgg - 18 May 2023_
+_AngryEgg (1.0 - 1.1.2)  - 18 May 2023_
 
 ## Instructions
 ---
+For versions 1.0 - 1.1.2:
 1. Zuggle Overload
 2. Mount anything (Zonai control stick, Lynel, horse)
 3. You now clip into the floor!
 
+For versions 1.2.0 - 1.2.1+:
+1. Zuggle overload such that with your bow drawn you are overloaded, but with it sheathed you are not
+2. Aim with a multishot bow
+3. Shoot an arrow and quickly mount what you want to clip with (timing varies from
+4. 
 ## Notes
 ---
 ÔÇö
 
 ## Resources
 ---
-- [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108780208137437314)
+- [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108780208137437314)[
+- [Discovery for 1.2.0+] (https://discordapp.com/channels/1086729144307564648/1113557914444111873/1394979337253687377)
+- [Discovery of arrow SDC] (https://discordapp.com/channels/1086729144307564648/1105598687167664239/1399016292882714747)
 - [YouTube](https://www.youtube.com/watch?v=w1fI3QYrerQ)
 
 ![ZOOB demonstration](https://cdn.discordapp.com/attachments/1105598687167664239/1108780207827079218/image.png?ex=699e6e49&is=699d1cc9&hm=ff5b33c53a5d61adb428f0b0c72460e41afb947cbb691fb5791783506d4b3fdd&)

----

*** COMMIT: 36d6d6b21d647f3ef9e028688cd03efb04858f51
Author: NaN Gogh <igor@torbas.net>
Date: Wed Feb 25 08:59:26 2026 +0100
Subject: fix: replace invalid character encoding in markdown files

commit 36d6d6b21d647f3ef9e028688cd03efb04858f51
Author: NaN Gogh <igor@torbas.net>
Date:   Wed Feb 25 08:59:26 2026 +0100

    fix: replace invalid character encoding in markdown files

diff --git a/docs/wiki/glitchcraft/ability-wheel-loop.md b/docs/wiki/glitchcraft/ability-wheel-loop.md
index 7b84b3400..9be014fa3 100644
--- a/docs/wiki/glitchcraft/ability-wheel-loop.md
+++ b/docs/wiki/glitchcraft/ability-wheel-loop.md
@@ -28,7 +28,7 @@ if the timing was right the ability wheel will come up right after the dpad menu
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/anti-gravity-objects.md b/docs/wiki/glitchcraft/anti-gravity-objects.md
index 7b4149ebb..519fa7ced 100644
--- a/docs/wiki/glitchcraft/anti-gravity-objects.md
+++ b/docs/wiki/glitchcraft/anti-gravity-objects.md
@@ -26,7 +26,7 @@ _?_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/ascend-camera-glitch.md b/docs/wiki/glitchcraft/ascend-camera-glitch.md
index 212776ff7..21fcd52e3 100644
--- a/docs/wiki/glitchcraft/ascend-camera-glitch.md
+++ b/docs/wiki/glitchcraft/ascend-camera-glitch.md
@@ -26,11 +26,11 @@ _?_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/ascend-rushing.md b/docs/wiki/glitchcraft/ascend-rushing.md
index 8eae26a21..9d7c86443 100644
--- a/docs/wiki/glitchcraft/ascend-rushing.md
+++ b/docs/wiki/glitchcraft/ascend-rushing.md
@@ -25,7 +25,7 @@ _R4000 - 15 June 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/autobuild-duplication.md b/docs/wiki/glitchcraft/autobuild-duplication.md
index 82db4825a..3165be33d 100644
--- a/docs/wiki/glitchcraft/autobuild-duplication.md
+++ b/docs/wiki/glitchcraft/autobuild-duplication.md
@@ -31,7 +31,7 @@ This only works with items that change into other items in another temperature.
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/back-in-time-art.md b/docs/wiki/glitchcraft/back-in-time-art.md
index 662fafffd..53f36218b 100644
--- a/docs/wiki/glitchcraft/back-in-time-art.md
+++ b/docs/wiki/glitchcraft/back-in-time-art.md
@@ -32,7 +32,7 @@ Compendium pictures (Zas):
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/back-to-back-bloodmoon.md b/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
index 908c2797a..b9047dbac 100644
--- a/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
+++ b/docs/wiki/glitchcraft/back-to-back-bloodmoon.md
@@ -20,11 +20,11 @@ _Lopitty - 17 May 2023_
 
 ## Instructions
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/banc-storage.md b/docs/wiki/glitchcraft/banc-storage.md
index 9140708b0..8bf6422dd 100644
--- a/docs/wiki/glitchcraft/banc-storage.md
+++ b/docs/wiki/glitchcraft/banc-storage.md
@@ -52,7 +52,7 @@ Instructions for 1.1+:
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/bomb-skew.md b/docs/wiki/glitchcraft/bomb-skew.md
index de32c8a65..e96f0a9e5 100644
--- a/docs/wiki/glitchcraft/bomb-skew.md
+++ b/docs/wiki/glitchcraft/bomb-skew.md
@@ -25,7 +25,7 @@ _Aergyl, FerrusCube, Mozz - 21 September 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/camera-cfw.md b/docs/wiki/glitchcraft/camera-cfw.md
index 6926236bf..20296e962 100644
--- a/docs/wiki/glitchcraft/camera-cfw.md
+++ b/docs/wiki/glitchcraft/camera-cfw.md
@@ -42,7 +42,7 @@ no camera ui
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/camera-pose-glitch.md b/docs/wiki/glitchcraft/camera-pose-glitch.md
index 4512da2f8..ecb07e24c 100644
--- a/docs/wiki/glitchcraft/camera-pose-glitch.md
+++ b/docs/wiki/glitchcraft/camera-pose-glitch.md
@@ -27,7 +27,7 @@ _?_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/cucco-warping.md b/docs/wiki/glitchcraft/cucco-warping.md
index 6fb8d4241..9c534aa56 100644
--- a/docs/wiki/glitchcraft/cucco-warping.md
+++ b/docs/wiki/glitchcraft/cucco-warping.md
@@ -25,7 +25,7 @@ _onion - 23 July 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md b/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md
index 0bf22b669..6c8079fe2 100644
--- a/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md
+++ b/docs/wiki/glitchcraft/dpadlock-less-invizuggle.md
@@ -46,7 +46,7 @@ If you want to zlot an item with invizuggle, you can do the following:
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/enemy-pickpocketing.md b/docs/wiki/glitchcraft/enemy-pickpocketing.md
index ec22ea12f..b29e2a7aa 100644
--- a/docs/wiki/glitchcraft/enemy-pickpocketing.md
+++ b/docs/wiki/glitchcraft/enemy-pickpocketing.md
@@ -27,7 +27,7 @@ _KAIDUDE64 - 16 September 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/extended-throw-sprinting.md b/docs/wiki/glitchcraft/extended-throw-sprinting.md
index cbf02143f..c4e15afc7 100644
--- a/docs/wiki/glitchcraft/extended-throw-sprinting.md
+++ b/docs/wiki/glitchcraft/extended-throw-sprinting.md
@@ -22,7 +22,7 @@ Hold B, tap R, repeat
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md b/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
index 993e15b53..5159e78e0 100644
--- a/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
+++ b/docs/wiki/glitchcraft/hand-locked-equipment-smuggling.md
@@ -33,7 +33,7 @@ Hand locked smuggling can also be performed using runes, two handed weapon and h
 
 ## Resources
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/hestu-scamming.md b/docs/wiki/glitchcraft/hestu-scamming.md
index 36195aa7a..b30365a12 100644
--- a/docs/wiki/glitchcraft/hestu-scamming.md
+++ b/docs/wiki/glitchcraft/hestu-scamming.md
@@ -35,7 +35,7 @@ Prerequisites:
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/item-throw-hitbox-disable.md b/docs/wiki/glitchcraft/item-throw-hitbox-disable.md
index 7ce6a436d..3fb58c108 100644
--- a/docs/wiki/glitchcraft/item-throw-hitbox-disable.md
+++ b/docs/wiki/glitchcraft/item-throw-hitbox-disable.md
@@ -26,7 +26,7 @@ Impact triggered items can still go off if hit by an explosion. For Bomb Flowers
 
 ## Resources
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/like-like-culling.md b/docs/wiki/glitchcraft/like-like-culling.md
index 9214748a0..14a0c6fda 100644
--- a/docs/wiki/glitchcraft/like-like-culling.md
+++ b/docs/wiki/glitchcraft/like-like-culling.md
@@ -25,7 +25,7 @@ _Mozz - 13 June 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md b/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md
index 7c3bd22b5..c346b1334 100644
--- a/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md
+++ b/docs/wiki/glitchcraft/like-like-new-textbox-softlock.md
@@ -20,7 +20,7 @@ _Ryan? - 16 June 2023_
 
 ## Instructions
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Notes
 ---
diff --git a/docs/wiki/glitchcraft/like-like-warping.md b/docs/wiki/glitchcraft/like-like-warping.md
index 7a13cbbd3..b67d8f11e 100644
--- a/docs/wiki/glitchcraft/like-like-warping.md
+++ b/docs/wiki/glitchcraft/like-like-warping.md
@@ -24,7 +24,7 @@ _Mozz - 15 June 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/likelike-stick-smuggling.md b/docs/wiki/glitchcraft/likelike-stick-smuggling.md
index 247538483..4bd0aaab0 100644
--- a/docs/wiki/glitchcraft/likelike-stick-smuggling.md
+++ b/docs/wiki/glitchcraft/likelike-stick-smuggling.md
@@ -31,11 +31,11 @@ _?_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/long-jump.md b/docs/wiki/glitchcraft/long-jump.md
index d4b13367c..e70912d90 100644
--- a/docs/wiki/glitchcraft/long-jump.md
+++ b/docs/wiki/glitchcraft/long-jump.md
@@ -24,7 +24,7 @@ While facing sideways (any angle that is more than or equal to 90 degrees from t
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/memory-buffering.md b/docs/wiki/glitchcraft/memory-buffering.md
index 7dbc6bbca..64cb1af1c 100644
--- a/docs/wiki/glitchcraft/memory-buffering.md
+++ b/docs/wiki/glitchcraft/memory-buffering.md
@@ -24,11 +24,11 @@ Skip a playing memory during an animation.
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/memory-interrupt.md b/docs/wiki/glitchcraft/memory-interrupt.md
index ede879827..9a6e336c9 100644
--- a/docs/wiki/glitchcraft/memory-interrupt.md
+++ b/docs/wiki/glitchcraft/memory-interrupt.md
@@ -30,7 +30,7 @@ The main use for this is Banc Storage, check the next row
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/midair-throw-duplication.md b/docs/wiki/glitchcraft/midair-throw-duplication.md
index 758a2a8f6..d6aa9884d 100644
--- a/docs/wiki/glitchcraft/midair-throw-duplication.md
+++ b/docs/wiki/glitchcraft/midair-throw-duplication.md
@@ -27,7 +27,7 @@ _quantim - 2 July 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/minecart-rail-collision-launching.md b/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
index cdcaa3c93..050013c43 100644
--- a/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
+++ b/docs/wiki/glitchcraft/minecart-rail-collision-launching.md
@@ -20,7 +20,7 @@ _ÒüØÒéë-ÒüòÒéô - 18 May 2023_
 
 ## Instructions
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Notes
 ---
diff --git a/docs/wiki/glitchcraft/mineru-aim-permanence.md b/docs/wiki/glitchcraft/mineru-aim-permanence.md
index a557d62d8..5549343d1 100644
--- a/docs/wiki/glitchcraft/mineru-aim-permanence.md
+++ b/docs/wiki/glitchcraft/mineru-aim-permanence.md
@@ -30,7 +30,7 @@ The Construct will stick around despite the other sage avatars going away
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/mnf-fusing.md b/docs/wiki/glitchcraft/mnf-fusing.md
index 35ad52fa7..4b4aa48dc 100644
--- a/docs/wiki/glitchcraft/mnf-fusing.md
+++ b/docs/wiki/glitchcraft/mnf-fusing.md
@@ -28,7 +28,7 @@ _LegendofLinkk - 5 June 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/mozdor-jumping-slashing.md b/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
index c94edc8a7..e7769ed14 100644
--- a/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
+++ b/docs/wiki/glitchcraft/mozdor-jumping-slashing.md
@@ -26,7 +26,7 @@ _Mozz, AgdoR - 20 May 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/null-dropping.md b/docs/wiki/glitchcraft/null-dropping.md
index 0ad3be6b7..819bd6a16 100644
--- a/docs/wiki/glitchcraft/null-dropping.md
+++ b/docs/wiki/glitchcraft/null-dropping.md
@@ -25,7 +25,7 @@ _Aergyl - 16 March 2024_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/object-moe-enlargement.md b/docs/wiki/glitchcraft/object-moe-enlargement.md
index b4cbecd0c..92d52214b 100644
--- a/docs/wiki/glitchcraft/object-moe-enlargement.md
+++ b/docs/wiki/glitchcraft/object-moe-enlargement.md
@@ -46,7 +46,7 @@ In order to make it rangeless, you need to PSLOT the target.
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/prologue-escape.md b/docs/wiki/glitchcraft/prologue-escape.md
index fc320a0a5..d9b0c3b37 100644
--- a/docs/wiki/glitchcraft/prologue-escape.md
+++ b/docs/wiki/glitchcraft/prologue-escape.md
@@ -49,7 +49,7 @@ Check the Resources section for more specific effects, such as Awakened Master S
 ---
 - [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1290703223467937898)
 - [YouTube](https://www.youtube.com/watch?v=RmjZKVGvstE)
-├óÔé¼ÔÇØ [Banc Storage](./banc-storage.md)
+ÔÇö [Banc Storage](./banc-storage.md)
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/reball.md b/docs/wiki/glitchcraft/reball.md
index fb190df7e..a815b72e6 100644
--- a/docs/wiki/glitchcraft/reball.md
+++ b/docs/wiki/glitchcraft/reball.md
@@ -30,7 +30,7 @@ Can be combined with arrow smuggle for momentum preservation.
 
 ## Resources
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/recipe-storage.md b/docs/wiki/glitchcraft/recipe-storage.md
index 9120f25ec..293c18279 100644
--- a/docs/wiki/glitchcraft/recipe-storage.md
+++ b/docs/wiki/glitchcraft/recipe-storage.md
@@ -45,7 +45,7 @@ Recipe Hold Storage:
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md b/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md
index 57817c8d8..053e12665 100644
--- a/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md
+++ b/docs/wiki/glitchcraft/resync-fuse-entanglement-resync-fe.md
@@ -53,7 +53,7 @@ This method uses recall for a makeshift wall:
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/reverse-ascend-storage.md b/docs/wiki/glitchcraft/reverse-ascend-storage.md
index 5b54dbb55..127b0f11e 100644
--- a/docs/wiki/glitchcraft/reverse-ascend-storage.md
+++ b/docs/wiki/glitchcraft/reverse-ascend-storage.md
@@ -24,7 +24,7 @@ _Redrooey - 27 November 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/sage-madness.md b/docs/wiki/glitchcraft/sage-madness.md
index afa114901..4a05d2efe 100644
--- a/docs/wiki/glitchcraft/sage-madness.md
+++ b/docs/wiki/glitchcraft/sage-madness.md
@@ -24,11 +24,11 @@ Activate the text box you get after obtaining a sage while the sage falls down a
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/shock-cold-fuse.md b/docs/wiki/glitchcraft/shock-cold-fuse.md
index 3e26a72ec..fcb8d730f 100644
--- a/docs/wiki/glitchcraft/shock-cold-fuse.md
+++ b/docs/wiki/glitchcraft/shock-cold-fuse.md
@@ -26,7 +26,7 @@ _Zas - 11 September 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/slate-storage.md b/docs/wiki/glitchcraft/slate-storage.md
index 409758f5f..8c56109f0 100644
--- a/docs/wiki/glitchcraft/slate-storage.md
+++ b/docs/wiki/glitchcraft/slate-storage.md
@@ -40,7 +40,7 @@ The Fall Damage should be cancelled if you dived quick enough
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/spring-strangeness.md b/docs/wiki/glitchcraft/spring-strangeness.md
index 61540b85f..a225da6f7 100644
--- a/docs/wiki/glitchcraft/spring-strangeness.md
+++ b/docs/wiki/glitchcraft/spring-strangeness.md
@@ -33,7 +33,7 @@ Method 1 is reliablely strange, while Method 2 has only been performed once thus
 
 ## Resources
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/stamina-depletion-freeze.md b/docs/wiki/glitchcraft/stamina-depletion-freeze.md
index 5e5089fa4..2b040622b 100644
--- a/docs/wiki/glitchcraft/stamina-depletion-freeze.md
+++ b/docs/wiki/glitchcraft/stamina-depletion-freeze.md
@@ -29,7 +29,7 @@ Letting go of B or stopping running cancels it
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/surf-storage.md b/docs/wiki/glitchcraft/surf-storage.md
index 540c9ed02..53324df5b 100644
--- a/docs/wiki/glitchcraft/surf-storage.md
+++ b/docs/wiki/glitchcraft/surf-storage.md
@@ -25,7 +25,7 @@ Shield surf against a slope
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/throw-cancelling.md b/docs/wiki/glitchcraft/throw-cancelling.md
index 82275c35a..be73efae0 100644
--- a/docs/wiki/glitchcraft/throw-cancelling.md
+++ b/docs/wiki/glitchcraft/throw-cancelling.md
@@ -26,11 +26,11 @@ _Quelfth_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Related
 ---
diff --git a/docs/wiki/glitchcraft/travel-medallion-storage.md b/docs/wiki/glitchcraft/travel-medallion-storage.md
index d3629fa4a..82f79898b 100644
--- a/docs/wiki/glitchcraft/travel-medallion-storage.md
+++ b/docs/wiki/glitchcraft/travel-medallion-storage.md
@@ -29,7 +29,7 @@ _kirigaya - 16 June 2023_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/wacko-attacko.md b/docs/wiki/glitchcraft/wacko-attacko.md
index b1c31c506..7f721afe0 100644
--- a/docs/wiki/glitchcraft/wacko-attacko.md
+++ b/docs/wiki/glitchcraft/wacko-attacko.md
@@ -26,7 +26,7 @@ _NghtmaR3, WinnerBoi77 - 21 January 2024_
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---
diff --git a/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md b/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
index b58c7df34..3afe2e55c 100644
--- a/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
+++ b/docs/wiki/glitchcraft/zonai-inventory-shift-dupe.md
@@ -33,7 +33,7 @@ Steps:
 
 ## Notes
 ---
-├óÔé¼ÔÇØ
+ÔÇö
 
 ## Resources
 ---

----

*** COMMIT: 75a5a54a9403f34860e221b3ab473d41831cfe31
Author: NaN Gogh <igor@torbas.net>
Date: Wed Feb 25 08:59:28 2026 +0100
Subject: Merge branch 'main' of https://github.com/nan-gogh/ultrabroken-documentation

commit 75a5a54a9403f34860e221b3ab473d41831cfe31
Merge: 36d6d6b21 76f8d8820
Author: NaN Gogh <igor@torbas.net>
Date:   Wed Feb 25 08:59:28 2026 +0100

    Merge branch 'main' of https://github.com/nan-gogh/ultrabroken-documentation


----

*** COMMIT: a94b95c3b6099d6c4728a669796d5e02c75a81fc
Author: NaN Gogh <igor@torbas.net>
Date: Wed Feb 25 09:01:28 2026 +0100
Subject: fix: correct formatting of resource links in zuggle-overload-out-of-bounds.md

commit a94b95c3b6099d6c4728a669796d5e02c75a81fc
Author: NaN Gogh <igor@torbas.net>
Date:   Wed Feb 25 09:01:28 2026 +0100

    fix: correct formatting of resource links in zuggle-overload-out-of-bounds.md

diff --git a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
index bd72ec17d..1aae77bbd 100644
--- a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
+++ b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
@@ -36,12 +36,12 @@ For versions 1.2.0 - 1.2.1+:
 
 ## Resources
 ---
-- [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108780208137437314)[
-- [Discovery for 1.2.0+] (https://discordapp.com/channels/1086729144307564648/1113557914444111873/1394979337253687377)
-- [Discovery of arrow SDC] (https://discordapp.com/channels/1086729144307564648/1105598687167664239/1399016292882714747)
+- [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1108780208137437314)
+- [Discovery for 1.2.0+](https://discordapp.com/channels/1086729144307564648/1113557914444111873/1394979337253687377)
+- [Discovery of arrow SDC](https://discordapp.com/channels/1086729144307564648/1105598687167664239/1399016292882714747)
 - [YouTube](https://www.youtube.com/watch?v=w1fI3QYrerQ)
 
-![ZOOB demonstration](https://cdn.discordapp.com/attachments/1105598687167664239/1108780207827079218/image.png?ex=699e6e49&is=699d1cc9&hm=ff5b33c53a5d61adb428f0b0c72460e41afb947cbb691fb5791783506d4b3fdd&)
+- ![ZOOB demonstration](https://cdn.discordapp.com/attachments/1105598687167664239/1108780207827079218/image.png?ex=699e6e49&is=699d1cc9&hm=ff5b33c53a5d61adb428f0b0c72460e41afb947cbb691fb5791783506d4b3fdd&)
 
 ## Related
 ---

----

*** COMMIT: 26d5fa82a882fce603ee445d9dd7e5d66fc3e0d9
Author: NaN Gogh <igor@torbas.net>
Date: Wed Feb 25 09:04:52 2026 +0100
Subject: fix: correct image formatting in zuggle-overload-out-of-bounds.md

commit 26d5fa82a882fce603ee445d9dd7e5d66fc3e0d9
Author: NaN Gogh <igor@torbas.net>
Date:   Wed Feb 25 09:04:52 2026 +0100

    fix: correct image formatting in zuggle-overload-out-of-bounds.md

diff --git a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
index 1aae77bbd..89a82fb61 100644
--- a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
+++ b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
@@ -41,7 +41,7 @@ For versions 1.2.0 - 1.2.1+:
 - [Discovery of arrow SDC](https://discordapp.com/channels/1086729144307564648/1105598687167664239/1399016292882714747)
 - [YouTube](https://www.youtube.com/watch?v=w1fI3QYrerQ)
 
-- ![ZOOB demonstration](https://cdn.discordapp.com/attachments/1105598687167664239/1108780207827079218/image.png?ex=699e6e49&is=699d1cc9&hm=ff5b33c53a5d61adb428f0b0c72460e41afb947cbb691fb5791783506d4b3fdd&)
+![ZOOB demonstration](https://cdn.discordapp.com/attachments/1105598687167664239/1108780207827079218/image.png?ex=699e6e49&is=699d1cc9&hm=ff5b33c53a5d61adb428f0b0c72460e41afb947cbb691fb5791783506d4b3fdd&)
 
 ## Related
 ---

----

*** COMMIT: 56bd7aadc54bc4784294a53829e7dc32eee1ff4f
Author: NaN Gogh <igor@torbas.net>
Date: Wed Feb 25 09:12:20 2026 +0100
Subject: fix: correct syntax errors in versions and credits fields in zuggle-overload-out-of-bounds.md

commit 56bd7aadc54bc4784294a53829e7dc32eee1ff4f
Author: NaN Gogh <igor@torbas.net>
Date:   Wed Feb 25 09:12:20 2026 +0100

    fix: correct syntax errors in versions and credits fields in zuggle-overload-out-of-bounds.md

diff --git a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
index 89a82fb61..a7bb4e875 100644
--- a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
+++ b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
@@ -1,8 +1,8 @@
 ---
 title: "Zuggle Overload Out Of Bounds"
 abbreviation: "ZOOB"
-versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2" "1.2.0" "1.2.1"]
-credits: ["AngryEgg" "Dark" "Toti Sauce"]
+versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1"]
+credits: ["AngryEgg", "Dark", "Toti Sauce"]
 date: "2023-05-18"
 description: "Allows you to clip OOB using zuggle overload"
 aliases: ["zuggle-overload-oob", "zuggle overload oob", "zo oob"]

----

*** COMMIT: d6f37f396ca632956efa45007cd288b2bd974735
Author: NaN Gogh <igor@torbas.net>
Date: Wed Feb 25 09:22:56 2026 +0100
Subject: fix: update image URL for ZOOB demonstration in zuggle-overload-out-of-bounds.md

commit d6f37f396ca632956efa45007cd288b2bd974735
Author: NaN Gogh <igor@torbas.net>
Date:   Wed Feb 25 09:22:56 2026 +0100

    fix: update image URL for ZOOB demonstration in zuggle-overload-out-of-bounds.md

diff --git a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
index a7bb4e875..17e628206 100644
--- a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
+++ b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
@@ -41,7 +41,7 @@ For versions 1.2.0 - 1.2.1+:
 - [Discovery of arrow SDC](https://discordapp.com/channels/1086729144307564648/1105598687167664239/1399016292882714747)
 - [YouTube](https://www.youtube.com/watch?v=w1fI3QYrerQ)
 
-![ZOOB demonstration](https://cdn.discordapp.com/attachments/1105598687167664239/1108780207827079218/image.png?ex=699e6e49&is=699d1cc9&hm=ff5b33c53a5d61adb428f0b0c72460e41afb947cbb691fb5791783506d4b3fdd&)
+![ZOOB demonstration](https://cdn.discordapp.com/attachments/1105598687167664239/1108780207827079218/image.png?ex=699fbfc9&is=699e6e49&hm=8d5c9b3681c297aa2f28caeb12874f6e62043810c53015b73688d2d84db49be6&)
 
 ## Related
 ---

----

*** COMMIT: 370841c2d0ecf213c0d28ee18c3ba9a851666601
Author: NaN Gogh <igor@torbas.net>
Date: Wed Feb 25 09:26:59 2026 +0100
Subject: fix: add spacing for better readability in zuggle-overload-out-of-bounds.md

commit 370841c2d0ecf213c0d28ee18c3ba9a851666601
Author: NaN Gogh <igor@torbas.net>
Date:   Wed Feb 25 09:26:59 2026 +0100

    fix: add spacing for better readability in zuggle-overload-out-of-bounds.md

diff --git a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
index 17e628206..f80d0463d 100644
--- a/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
+++ b/docs/wiki/glitchcraft/zuggle-overload-out-of-bounds.md
@@ -21,11 +21,13 @@ _AngryEgg (1.0 - 1.1.2)  - 18 May 2023_
 ## Instructions
 ---
 For versions 1.0 - 1.1.2:
+
 1. Zuggle Overload
 2. Mount anything (Zonai control stick, Lynel, horse)
 3. You now clip into the floor!
 
 For versions 1.2.0 - 1.2.1+:
+
 1. Zuggle overload such that with your bow drawn you are overloaded, but with it sheathed you are not
 2. Aim with a multishot bow
 3. Shoot an arrow and quickly mount what you want to clip with (timing varies from

----

