---
uid: editor-guide
label: Editor Guide
title: Editor Guide & Markdown Reference
aliases: ["markdown-extensions"]
---

# Editor Guide & Markdown Reference

This page provides a comprehensive guide for editors contributing to the Ultrabroken Archives written in Markdown and published with MkDocs + Material. It covers contribution workflows, conventions, custom site features, and all active Markdown extensions.

## How GitHub collaborators should contribute
- Use the GitHub web editor or your normal GitHub workflow to edit Markdown files in the [`docs/`](https://github.com/nan-gogh/ultrabroken-documentation/tree/main/docs) folder.
- Make small, focused commits and include a clear title/description for the change.
- When ready, commit changes.
- Keep changes scoped to documentation content: avoid editing [`mkdocs.yml`](https://github.com/nan-gogh/ultrabroken-documentation/blob/main/mkdocs.yml) or continuous integration (CI) workflows in [`github/workflows`](https://github.com/nan-gogh/ultrabroken-documentation/tree/main/.github/workflows) unless requested by maintainers.

### Quick tips for the GitHub editor
1. Navigate to the file you want to change (for example [`docs/effects/wacko-boingo.md`](https://github.com/nan-gogh/ultrabroken-documentation/blob/main/docs/wiki/ultrabroken/effects/wacko-boingo.md)).
2. Click the pencil ✏️ icon to edit the file in your browser or use the menu in the GitHub app.
3. Make your edits, add a concise commit message, and commit directly to "main".
4. Open a pull request if you used a different branch than "main".

## Recommended editing guidelines
- Write in present tense and keep instructions concise.
- Use clear section headings and include example commands or code where useful.
- Keep the steps of your instructions as granular as possible. Try to extract pausing / unpausing into dedicated steps with bold styling for clarity.
- Avoid abbreviations in titles or filenames for easy parsing.
- Prefer relative links for cross-references inside the wiki (for example `../wiki/effects/index.md`).
- For images, put files in [`docs/assets/images/`](https://github.com/nan-gogh/ultrabroken-documentation/tree/main/docs/assets/images) and reference them with relative paths.
- Put your WIPs into the dedicated [`docs/wiki/wip/`](https://github.com/nan-gogh/ultrabroken-documentation/tree/main/docs/wiki/_wip) folder.
- UIDs for files are generated automatically. Don't manually add UID fields to the frontmatter.
- After you have committed changes to the wiki, is takes around two minutes until those are reflected on the page. Wait until the page build finishes before making the next commit.

## Frontmatter Reference
---

Every wiki page begins with YAML frontmatter between `---` delimiters. Here are all available fields:

### title

The display title for the page. Required.

```yaml
title: "Zuggle Overload"
```

### label

A short abbreviation displayed alongside the title (e.g., "ZO" for "Zuggle Overload").

```yaml
label: "ZO"
```

### versions

List of game versions where the glitch/technique works.

```yaml
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
```

### credits

Contributors who discovered or documented the technique. Names must match [credits.json](../assets/data/credits.json) exactly for leaderboard aggregation.

```yaml
credits: ["Zvleon", "Mozz"]
```

### date

Discovery or documentation date in `YYYY-MM-DD` format.

```yaml
date: "2023-05-16"
```

### description

A brief summary used for search results and SEO.

```yaml
description: "Zuggling allows you to stack weapons to get more attack power by cloning equipment onto Link."
```

### tags

Categorization tags. Auto-indexed into [tags.json](../assets/data/tags.json) during build.

```yaml
tags: ["zuggling", "overload", "item", "equipment"]
```

### aliases

Alternative names for search discovery. Case-insensitive.

```yaml
aliases: ["zuggo", "overloaded zuggle"]
```

### uid

Auto-generated unique identifier. **Do not add manually.**

### Complete Example

```yaml
---
title: "Zuggle Overload"
label: "ZO"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0"]
credits: ["Zvleon"]
date: "2023-05-16"
description: "Zuggling allows you to stack weapons by cloning equipment onto Link."
aliases: ["zuggo", "ZO"]
tags: ["zuggling", "overload"]
---
```

## Custom Site Features
---

These are site-specific enhancements beyond standard Markdown.

### Search links

Links prefixed with `search:` open the site search overlay instead of navigating.

```markdown
[Slugging](search:Slugging)
```

### Map embeds

Embed interactive [TotK Object Map](https://objmap-totk.zeldamods.org/) previews using coordinate shorthand.

**Format:** `[Label](zoom, x:x_coord, z:z_coord[, layer])`

| Parameter | Required | Description |
|-----------|----------|-------------|
| zoom | Yes | Initial zoom level (e.g., 8, 10) |
| x:x_coord | Yes | X coordinate (decimals OK) |
| z:z_coord | Yes | Z coordinate (decimals OK) |
| layer | No | Surface, Sky, or Depths (default: Surface) |

```markdown
[Fire Temple VD location](8, x:1321.68, z:-2823.71, Depths)
```

### Social links and leaderboard

Credit names in frontmatter are aggregated into the leaderboard. Names link to social profiles when mapped in [credits.json](../assets/data/credits.json).

```json
{
    "Mozz": "https://www.youtube.com/@M0zzed"
}
```

**Names must match exactly** — mismatched capitalization or spelling prevents linking and splits leaderboard entries.

### Level-2 section separators

Place `---` after `##` headings for visual consistency:

```markdown
## Instructions
---
```

## Markdown Extensions
---

This site uses customized extensions to enhance standard Markdown. Each extension includes syntax and a rendered example.

### Admonition

Displays highlighted blocks for notes, tips, warnings, and other callouts.

#### Syntax

```markdown
!!! note "Optional Title"
    This is a note. The title is optional.

!!! tip
    Pro tip for readers.

!!! warning
    Pay attention to this warning.

!!! danger
    Critical danger notice.
```

#### Example

!!! note "Example Note"
    Admonitions draw attention to important content with a colored border and background.

!!! tip
    Use admonitions sparingly to maintain visual hierarchy.

---

### Details (Collapsible Blocks)

Creates expandable/collapsible sections of content.

#### Syntax

```markdown
??? note "Click to expand"
    Hidden content appears when you click the title.

???+ tip "Expanded by default"
    The + makes it expand automatically on page load.
```

#### Example

??? note "Hidden Content Example"
    This content is collapsed by default. Click the title to expand it.

???+ tip "Expanded by Default"
    Use the `+` prefix to show collapsed blocks expanded initially.

---

### Superfences (Code Blocks)

Enables advanced code block features including syntax highlighting, line numbers, and custom attributes.

#### Syntax

````markdown
```python
def hello_world():
    print("Hello, World!")
```

```javascript title="filename.js" linenums="1"
console.log("Line numbers and titles work!");
```
````

**Options:** `linenums="1"` for line numbers, `title="name"` for titles, `hl_lines="1 2 3"` to highlight lines.

#### Example

```python title="example.py" linenums="1"
def hello_world():
    print("Hello, World!")
```

---

### Highlight

Provides syntax highlighting for code blocks. Works transparently with Superfences to color-code code blocks based on language.

#### Syntax

Simply specify the language after the opening triple backticks:

````markdown
```python
print("Highlighted automatically")
```
````

#### Example

```python
print("Highlighted automatically")
```

---

### InlineHilite

Highlights inline code snippets with syntax coloring.

#### Syntax

```markdown
Use `#!python print("inline")` for inline highlighting.
```

#### Example

Use `#!python print("inline")` for inline highlighting or `#!javascript const x = 42;` for JavaScript.

---

### Tasklist

Renders interactive checkboxes for task lists.

#### Syntax

```markdown
- [x] Completed task
- [ ] Incomplete task
```

#### Example

- [x] Study Ultrabroken mechanics
- [ ] Master zuggling techniques
- [x] Document discoveries

---

### TOC (Table of Contents)

Automatically generates a table of contents from headings in the sidebar. Supports custom heading IDs via the Attr List extension.

#### Syntax

```markdown
## My Section {#custom-anchor}

Link to it with [jump to section](#custom-anchor).
```

#### Example

The sidebar navigation on this page is automatically generated from headings.

---

### Attr List

Adds support for custom attributes (IDs, classes) on elements.

#### Syntax

```markdown
# Heading with Custom ID {#custom-id}

Paragraph with a class.
{: .custom-class }

[Link text](#custom-id){ .button }
```

#### Example

This paragraph has custom styling applied.
{: .md-typeset }

---

### Md in HTML

Allows Markdown to be written inside HTML blocks.

#### Syntax

```html
<div markdown="1">

**Markdown** inside an HTML div.

- List item 1
- List item 2

</div>
```

#### Example

<div markdown="1">

**Markdown** renders correctly inside HTML containers.

</div>

---

### Def List (Definition Lists)

Creates structured definition/term pairs useful for glossaries.

#### Syntax

```markdown
Term
:   Definition of the term.

Another Term
:   Another definition.
```

#### Example

Zuggle
:   A glitch technique where Link's equipment state becomes desynchronized with the inventory display.

OOB (Out of Bounds)
:   Exploiting collision detection to move Link outside the intended playable area.

---

### Tabbed (Tabbed Content)

Creates tabs for organizing related content groups.

#### Syntax

```markdown
=== "Tab 1"

    Content for tab 1.

=== "Tab 2"

    Content for tab 2.
```

#### Example

=== "Method A"

    This is approach A.

=== "Method B"

    This is alternative approach B.

---

## Extension Configuration
---

All extensions are defined in `mkdocs.yml`:

```yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.tasklist:
      clickable_checkbox: true
  - toc:
      permalink: false
  - attr_list
  - md_in_html
  - def_list
  - pymdownx.tabbed:
      alternate_style: true
```

---

## Quick Reference
---

| Extension | Purpose | Key Syntax |
|---|---|---|
| **Admonition** | Callout blocks | !!! type "Title" |
| **Details** | Collapsible sections | ??? note "Title" |
| **Superfences** | Advanced code blocks |  `python title="..." `  |
| **Highlight** | Syntax coloring | (Automatic with Superfences) |
| **InlineHilite** | Inline code highlighting | `#!python code` |
| **Tasklist** | Interactive checkboxes | - [x] Task |
| **TOC** | Auto table of contents | (Automatic from headings) |
| **Attr List** | Custom attributes | {#id .class} |
| **Md in HTML** | Markdown in HTML blocks | <div markdown="1"> |
| **Def List** | Glossaries | Term\n:   Definition |
| **Tabbed** | Organized content groups | === "Tab Name" |

---

## Best Practices
---

1. **Use Admonitions** for important callouts (notes, warnings, tips)
2. **Prefer collapsible Details** only when content is optional or supplementary
3. **Leverage code block titles** to label examples
4. **Apply custom IDs** with Attr List for deep-linking to specific sections
5. **Use Def Lists** for glossaries and terminology sections
6. **Tab related content** to keep pages more scannable
7. **Nest extensions** appropriately (e.g., code blocks inside admonitions)

---

## Navigation and where to edit
---

Top-level docs live in `docs/wiki/`. Edit pages directly; to reorganize navigation, ask a maintainer or update `mkdocs.yml`.

## Community and contribution
---

This is a community project — everyone is welcome to contribute even without a GitHub account. Join the discussion:

- Download [blank.md](_wip/blank.md) as a starting point and post your discoveries in our **[dedicated Encyclopedia thread](https://discord.com/channels/1086729144307564648/1471224902890684557)** on the **[TotK Speedrunning Discord](https://discord.gg/xM8NnTetb2)**

## See Also
---

- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Python-Markdown Extensions](https://python-markdown.github.io/extensions/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)

## Appendix: Markdown Basics
---

Standard Markdown syntax reference:

```markdown
# Heading 1
## Heading 2
### Heading 3

**bold** and _italic_

`inline code`

[Link text](path/to/file.md)
![Alt text](assets/images/example.png)

- Unordered item
1. Ordered item

> Blockquote

| Column A | Column B |
|----------|----------|
| Value 1  | Value 2  |
```
