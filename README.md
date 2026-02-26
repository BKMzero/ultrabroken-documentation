# Ultrabroken Archives — Editor Guide

This repository holds the Ultrabroken Archives written in Markdown and published with MkDocs + Material.

This README is focused on editors who will make content changes directly on GitHub. Editors typically do not need to run or build the site locally — just edit and commit. If you wish to build the site locally, ask the admin to receive a guide.

## How GitHub collaborators should contribute

- Use the GitHub web editor or your normal GitHub workflow to edit Markdown files in the `docs/` folder.
- Make small, focused commits and include a clear title/description for the change.
- When ready, commit changes.
- Keep changes scoped to documentation content: avoid editing `mkdocs.yml` or continuous integration (CI) workflows unless requested by maintainers.

### Quick tips for the GitHub editor

1. Navigate to the file you want to change (for example `docs/effects/wacko-boingo.md`).
2. Click the pencil ✏️ icon to edit the file in your browser or use the menu in the GitHub app.
3. Make your edits, add a concise commit message, and commit directly to `main`.
4. Open a pull request if you used a different branch than `main`.

## Recommended editing conventions

- Write in present tense and keep instructions concise.
- Use clear section headings and include example commands or code where useful.
- Prefer relative links for cross-references inside the docs (for example `../effects/index.md`).
- For images, put files in `docs/assets/images/` and reference them with relative paths.

### Additional editor conveniences

#### Search links

Write Markdown links that start with `search:` to create an editor-friendly trigger for the site's search overlay.

```markdown
[Slugging](search:Slugging)
```

These links are intercepted client-side and open the Material theme search with the provided query instead of navigating away. They are safe to edit in GitHub and make finding related content easier.

#### Level-2 section separators

To keep `##` sections visually consistent, place a horizontal rule immediately after the level-2 heading by adding a line with three dashes on the next line.

```markdown
## Instructions
---
```

#### Social links and leaderboard

Contributor credit names are automatically aggregated into the leaderboard and converted into clickable social media links on the site using [`docs/assets/data/credits.json`](docs/assets/data/credits.json). The build system automatically adds newly credited names with an empty URL (`""`) as a pending placeholder. These names render as plain text in the docs and on the leaderboard until a social URL is manually filled in. To enable linking, open `credits.json` and replace the empty string with the contributor's profile URL.

Each entry maps a name to a URL:

```json
{
    "Mozz": "https://www.youtube.com/@M0zzed",
}
```

**Credit names must match exactly** the names in `credits.json` to work correctly.

Mismatched names (different capitalization, spacing, or spelling) will:

- Create separate leaderboard entries instead of aggregating contributions
- Prevent social media links from appearing
- Give inaccurate credit attribution

**Always check the exact spelling and capitalization** in `credits.json` before adding a credit.

#### Tagging

To see all available tags, check [`docs/assets/data/tags.json`](docs/assets/data/tags.json). Glitch and content tags are automatically aggregated into `tags.json` during the build process. When you add a new tag to a glitch's frontmatter (in the `tags:` field), the build system automatically discovers it and adds it to the tags file if it's not already present sorting it alphabetically.

## Markdown quick reference

### Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
```

### Emphasis

```markdown
**bold**
_italic_
`inline code`
```

### Code blocks

````markdown
```bash
echo "example"
```
````

### Links and images

```markdown
[Link text](path/to/file.md)
![Alt text](assets/images/example.png)
```

### Lists

```markdown
- Unordered item
- Another item

1. First item
2. Second item
```

### Blockquotes

```markdown
> This is a quote
```

### Tables

```markdown
| Column A | Column B |
|---|---|
| Value 1  | Value 2  |
```

### Task lists

Useful in pull requests:

```markdown
- [ ] Open review
- [x] Addressed comments
```

### Admonitions

Supported by MkDocs Material:

```markdown
!!! note
    This is a helpful note.
```

## Navigation and where to edit

- Top-level docs live in `docs/`.
- Edit pages directly; to reorganize navigation, ask a maintainer or update `mkdocs.yml`.

## Community and contribution

This is a community project — everyone is welcome to contribute even without a GitHub account. Join the discussion and show us what you got:

- Download [`docs/wiki/blank.md`](docs/wiki/blank.md) if you need a starting point, write down your intel and post it in our **[dedicated Encyclopedia thread](https://discord.com/channels/1086729144307564648/1471224902890684557)** in the **[Zelda: Tears of the Kingdom Speedrunning Discord server](https://discord.gg/xM8NnTetb2)**

---

Thanks for contributing — keep changes focused, documented, and easy to review.

