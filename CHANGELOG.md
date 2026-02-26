# Changelog 2026-02-25

Range: from commit `1e0a6934b4d5a929724e9c68e7ea36c7ee804b98` to commit `370841c2d0ecf213c0d28ee18c3ba9a851666601`

**Overview:**
- Project maintenance, data reorganization, search quality improvements, AI evidence UI refactor, and a large batch of content updates across the `glitchcraft` docs. Several generated JSON data files were moved to `docs/assets/data` and supporting scripts updated to match. A small number of content regressions (encoding issues) were later fixed.

**Key changes (grouped):**
- **Data & Assets:** Updated and moved several data files into a central directory for the build pipeline.
  - Moved grimoire and leaderboard data into `docs/assets/data` and updated consumers accordingly.
  - Migrated `credits.json` into `docs/assets/data` and adjusted hooks that read it (`docs/assets/hooks/contributor_links.py`).
  - Updated `docs/wiki/build_bm25_index.py` to read/write into `docs/assets/data` by default.

- **Leaderboard / Socials:**
  - Added/updated entries in the leaderboard data (e.g., adding `Suishi`, adjusting totals and ranks).
  - Added social links and improved contributor link lookup.

- **Search & Worker Improvements:**
  - Improved the ranking/scoring algorithm in `docs/worker/worker.js`:
    - Added abbreviation exact-match boosts so short codes (e.g., `SDC`) reliably surface matching pages.
    - Added alias/phrase boosts to favor pages whose aliases appear as phrase matches in the query.
  - Synonyms adjusted in `docs/worker/synonyms.json` (added and removed some synonym groups to refine search behavior).
  - Increased the number of evidence items returned/displayed from 3 → 6 in the worker/evidence pipeline.

- **AI Client / Evidence UI:**
  - Major refactor of `docs/assets/scripts/ai-worker-client.js`:
    - Separates `Resources` (worker-provided evidence; direct wiki links) from `Related` (model-provided sources rendered as search links).
    - Renders Resource links as direct clickable wiki URLs, and Related items as `search:` links to the site search.
    - Improves copy-to-clipboard content to include `Resources`, `Related`, and a short disclaimer.
    - Standardizes headings to `## Resources` and `## Related`.

- **Frontend script fixes:**
  - Updated `grimoire-filter.js` and `leaderboard.js` to fetch from `docs/assets/data` paths.
  - `docs/assets/hooks/contributor_links.py` updated to point to the new `credits.json` path.

- **Documentation content:**
  - Large batch of edits to `docs/wiki/glitchcraft/*.md` (aliases, tags, related sections, and small content fixes). Many pages had a `## Related` section added or standardized.
  - Alias/tag cleanup across many glitch pages to improve searchability and consistency.

- **Build & Indexing:**
  - `docs/wiki/build_bm25_index.py` updated to write grimoire/leaderboard outputs into `docs/assets/data` (matching the new asset layout).
  - Various workflow adjustments made so generated JSON files are placed into `site/` during CI correctly.

- **Bug fixes & editorial changes:**
  - Clarified wording in the Memorial/index headings.
  - Minor content edits across the wiki (typos, formatting, and heading consistency).

- **Encoding incident & repair (notable):**
  - A batch edit that appended `## Related` to many files was performed using a PowerShell workflow that unintentionally re-encoded some UTF-8 files with a Windows code page; this caused some Japanese/Unicode contributor names to be corrupted and BOMs to be added.
  - The corrupted `credits:` lines were restored from git for the affected files, and BOMs were removed where necessary — those fixes are now in the working tree.

**Representative files changed (non-exhaustive):**
- `docs/assets/data/grimoire-data.json` (moved/rewritten)
- `docs/assets/data/leaderboard-data.json` (rebuilt / data tweaks)
- `docs/assets/data/credits.json`
- `docs/worker/worker.js` (scoring, evidence handling)
- `docs/worker/synonyms.json` (synonym list adjustments)
- `docs/assets/scripts/ai-worker-client.js` (evidence UI refactor)
- `docs/assets/scripts/grimoire-filter.js`, `docs/assets/scripts/leaderboard.js` (path fixes)
- `docs/wiki/build_bm25_index.py` (output path fixes)
- Many `docs/wiki/glitchcraft/*.md` files (Related sections, aliases, tags)

**Notes & recommendations:**
- The canonical place for generated JSON is now `docs/assets/data/`. If you have build scripts or CI steps relying on the old paths, update them (most were already updated in these commits).
- The AI evidence UI changes alter how Resources/Related are presented; check `docs/assets/scripts/ai-worker-client.js` if you want the old behavior restored or further tweaks.
- Rehost any externally-hosted media (Discord CDN links) used in docs to a stable location inside the repo (`docs/assets/images/`) to avoid ephemeral CDN tokens causing broken images.
