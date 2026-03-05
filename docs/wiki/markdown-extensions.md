---
uid: editor-guide
label: Editor Guide
title: Editor Guide & Markdown Reference
aliases: ["markdown-extensions"]
---

# Editor Guide & Markdown Reference

This page provides a comprehensive guide for editors contributing to the Ultrabroken Archives written in Markdown and published with MkDocs + Material. It covers contribution workflows, conventions, custom site features, and all active Markdown extensions.

## How GitHub collaborators should contribute
- Use the GitHub web editor or your normal GitHub workflow to edit Markdown files in the [docs/](https://github.com/nan-gogh/ultrabroken-documentation/tree/main/docs) folder.
- Make small, focused commits and include a clear title/description for the change.
- When ready, commit changes.
- Keep changes scoped to documentation content: avoid editing [mkdocs.yml](https://github.com/nan-gogh/ultrabroken-documentation/blob/main/mkdocs.yml) or [continuous integration (CI) workflows](https://github.com/nan-gogh/ultrabroken-documentation/tree/main/.github/workflows) unless requested by maintainers.

### Quick tips for the GitHub editor
1. Navigate to the file you want to change (for example "docs/effects/wacko-boingo.md").
2. Click the pencil ✏️ icon to edit the file in your browser or use the menu in the GitHub app.
3. Make your edits, add a concise commit message, and commit directly to "main".
4. Open a pull request if you used a different branch than "main".

## Recommended editing guidelines
- Write in present tense and keep instructions concise.
- Use clear section headings and include example commands or code where useful.
- Keep the steps of your instructions as granular as possible. Try to extract pausing / unpausing into dedicated steps with bold styling for clarity.
- Avoid abbreviations in titles or filenames for easy parsing.
- Prefer relative links for cross-references inside the wiki (for example `../wiki/effects/index.md`).
- For images, put files in `docs/assets/images/` and reference them with relative paths.
- Put your WIPs into the dedicated [`docs/wiki/wip/`](docs/wiki/wip/) folder.
- UIDs for files are generated automatically. Don't manually add UID fields to the frontmatter.
- After you have committed changes to the wiki, is takes around two minutes until those are reflected on the page. Wait until the page build finishes before making the next commit.

## Additional editor conventions

### Search links
Write Markdown links that start with "search:" to create an editor-friendly trigger for the site's search overlay.

`markdown
[Slugging](search:Slugging)
`

These links are intercepted client-side and open the Material theme search with the provided query instead of navigating away. They are safe to edit in GitHub and make finding related content easier.

### Map embeds
Embed interactive map previews from the [TotK Object Map](https://objmap-totk.zeldamods.org/) using shorthand coordinate syntax:

`markdown
[Fire Temple VD location](8, x:1321.68, z:-2823.71, Depths)
`

Format: [Label](zoom, x:x_coord, z:z_coord[, layer])

- **zoom**: Required — initial zoom level (e.g., 8, 10)
- **x:x_coord**: Required — X coordinate (supports decimals)
- **z:z_coord**: Required — Z coordinate (supports decimals)
- **layer**: Optional — map layer (Surface, Sky, Depths; defaults to Surface)

The embed automatically generates two versions: desktop at the specified zoom, and mobile at zoom -1 for better mobile viewing. Desktop shows at full size (500px), while mobile portrait shows at 300px height and mobile landscape at 55vh.


### Social links and leaderboard
Contributor credit names are automatically aggregated into the leaderboard and converted into clickable social media links on the site using [docs/assets/data/credits.json](docs/assets/data/credits.json). The build system automatically adds newly credited names with an empty URL ("") as a pending placeholder. These names render as plain text in the docs and on the leaderboard until a social URL is manually filled in. To enable linking, open credits.json and replace the empty string with the contributor's profile URL. Do not manually add or remove entries.

Each entry maps a name to a URL:

`json
{
    "Mozz": "https://www.youtube.com/@M0zzed",
}
`

**Credit names must match exactly** the names in credits.json to work correctly.

Mismatched names (different capitalization, spacing, or spelling) will:

- Create separate leaderboard entries instead of aggregating contributions
- Prevent social media links from appearing
- Give inaccurate credit attribution

**Always check the exact spelling and capitalization** in credits.json before adding a credit.

### Tagging
To see all available tags, check [docs/assets/data/tags.json](docs/assets/data/tags.json). Glitch and content tags are automatically aggregated into tags.json during the build process. When you add a new tag to a glitch's frontmatter (in the tags: field), the build system automatically discovers it and adds it to the tags file if it's not already present sorting it alphabetically. Do not edit tags.json manually.

### Aliases
Aliases make pages discoverable under alternative names. Add them to a page's frontmatter using the `aliases` field:

```yaml
---
title: "Zuggle Overload"
aliases: ["zuggle-o", "ZO", "overload-zuggle"]
---
```

When a reader searches for any of these alias names (e.g., "ZO" or "overload-zuggle"), the search system will find and suggest this page. Use aliases for:

- **Abbreviations**: Common shorthand references (e.g., "VD" for "Void Dipping")
- **Alternative names**: Common alternate names or spellings
- **Old page names**: If you rename a page, keep the old name as an alias so old links still work

Aliases are case-insensitive and automatically indexed during the build process.

### Level-2 section separators
To keep `##` sections visually consistent, place a horizontal rule immediately after the level-2 heading by adding a line with three dashes on the next line.

```markdown
## Instructions
---
```

## Markdown Quick Reference

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
inline code
```

### Links and images

```markdown
[Link text](path/to/file.md)
![Alt text](assets/images/example.png)
```

### Lists
*Leave a blank line between regular text and lists!*
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

## Active Markdown Extensions

This site uses customized extensions to enhance standard Markdown formatting.

### 1. **Admonition**
Displays highlighted blocks for notes, tips, warnings, and other callouts.

#### Syntax
`markdown
!!! note "Optional Title"
    This is a note. The title is optional.

!!! tip
    Pro tip for readers.

!!! warning
    Pay attention to this warning.

!!! danger
    Critical danger notice.
`

#### Examples
!!! note "Example Note"
    Admonitions draw attention to important content with a colored border and background.

!!! tip
    Use admonitions sparingly to maintain visual hierarchy.

---

### 2. **Pymdownx Details** (Collapsible Blocks)
Creates expandable/collapsible sections of content.

#### Syntax
`markdown
??? note "Click to expand"
    Hidden content appears when you click the title.

??? warning "Collapsible warning"
    This section is hidden by default.

???+ tip "Expanded by default"
    The + makes it expand automatically on page load.
`

#### Examples
??? note "Hidden Content Example"
    This content is collapsed by default. Click the title to expand it.

???+ tip "Expanded by Default"
    Use the + prefix to show collapsed blocks expanded initially.

---

### 3. **Pymdownx Superfences**
Enables advanced code block features including syntax highlighting, line numbers, and custom attributes.

#### Syntax
``markdown
`python
def hello_world():
    print("Hello, World!")
`

`javascript title="filename.js" linenums="1"
console.log("Line numbers and titles work!");
`
``

#### Features
- **Syntax highlighting** for 100+ languages
- **Line numbers** with linenums="1"
- **Titles** with 	itle="your_title"
- **Callout lines** with hl_lines="1 2 3"

---

### 4. **Pymdownx Highlight**
Provides syntax highlighting for code blocks with customizable themes and styles.

Works transparently with **Superfences** to color-code code blocks based on language.

#### Supported Languages
Python, JavaScript, TypeScript, Java, C++, CSS, HTML, Bash, JSON, YAML, Markdown, Regex, and 100+ more.

---

### 5. **Pymdownx InlineHilite**
Highlights inline code snippets with syntax coloring (without backticks).

#### Syntax
`markdown
:::python print("inline code with highlighting")

:::javascript const x = 42;
`

---

### 6. **Pymdownx Tasklist**
Renders interactive checkboxes for task lists.

#### Syntax
`markdown
- [x] Completed task
- [ ] Incomplete task
- [x] Another completed task
`

#### Example
- [x] Study Ultrabroken mechanics
- [ ] Master zuggling techniques
- [x] Document discoveries

**Features:** Clickable checkboxes (when enabled) allow tasks to be marked complete.

---

### 7. **TOC (Table of Contents)**
Automatically generates a table of contents from headings. Includes **permalink support** for linking directly to sections.

#### Current Config
- permalink: false — Permalinks are disabled in the extension config
- Material Theme provides native styling and sidebar integration
- Use heading anchors like [Link](#section-title) to reference sections

#### Features
- Automatically detects heading hierarchy (h1, h2, h3, etc.)
- Integrated into Material theme sidebar
- Supports custom IDs with ttr_list extension

---

### 8. **Attr List**
Adds support for custom attributes (IDs, classes) on elements.

#### Syntax
`markdown
# Heading with Custom ID {#custom-id}

Paragraph with a class.
{: .custom-class }

[Link text](#custom-id){ .button }
`

#### Use Cases
- Custom IDs for deep linking: {#section-name}
- CSS class application: {: .highlight }
- Custom styling on images, lists, and blocks

---

### 9. **Md in HTML**
Allows Markdown to be written inside HTML blocks.

#### Syntax
```html
<div markdown="1">

# Markdown in HTML
This paragraph uses **Markdown formatting** inside an HTML div.

- List item 1
- List item 2

</div>
```

#### Use Cases
- Complex layouts requiring HTML structure with Markdown flexibility
- Custom containers with Markdown content inside
- Preserve Markdown rendering within semantic HTML

---

### 10. **Def List** (Definition Lists)
Creates structured definition/term pairs useful for glossaries and terminology.

#### Syntax
`markdown
Term 1
:   Definition of term 1 with full support for **bold**, *italic*, and [links](/).

Term 2
:   Multi-paragraph definitions.
:   Supported by adding multiple :  entries.

Zuggle
:   A complex glitch involving equipment state manipulation.
`

#### Example
Zuggle
:   A glitch technique where Link's equipment state becomes desynchronized with the inventory display, allowing impossible item combinations.

OOB (Out of Bounds)
:   Exploiting collision detection to move Link outside the intended playable area.

---

### 11. **Pymdownx Tabbed** (Tabbed Content)
Creates tabs for organizing related content groups.

#### Syntax
`markdown
=== "Tab 1: Python"

    `python
    print("Python code here")
    `

=== "Tab 2: JavaScript"

    `javascript
    console.log("JavaScript");
    `

=== "Tab 3: Notes"

    Regular content here.
`

#### Features
- Multiple tabs within a single block
- Support for arbitrary content (code, text, lists)
- lternate_style: true enabled for modern Material theme styling
- Improves readability when comparing related content

#### Example
=== "Method A"

    This is approach A.

=== "Method B"

    This is alternative approach B.

---

## Extension Configuration

All extensions are defined in mkdocs.yml under the markdown_extensions section:

`yaml
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
`

---

## Quick Reference Cheat Sheet

| Extension | Purpose | Key Syntax |
|---|---|---|
| **Admonition** | Callout blocks | !!! type "Title" |
| **Details** | Collapsible sections | ??? note "Title" |
| **Superfences** | Advanced code blocks |  `python title="..." `  |
| **Highlight** | Syntax coloring | (Automatic with Superfences) |
| **InlineHilite** | Inline code highlighting | :::python code |
| **Tasklist** | Interactive checkboxes | - [x] Task |
| **TOC** | Auto table of contents | (Automatic from headings) |
| **Attr List** | Custom attributes | {#id .class} |
| **Md in HTML** | Markdown in HTML blocks | <div markdown="1"> |
| **Def List** | Glossaries | Term\n:   Definition |
| **Tabbed** | Organized content groups | === "Tab Name" |

---

## Best Practices

1. **Use Admonitions** for important callouts (notes, warnings, tips)
2. **Prefer collapsible Details** only when content is optional or supplementary
3. **Leverage code block titles** to label examples
4. **Apply custom IDs** with ttr_list for deep-linking to specific sections
5. **Use Def Lists** for glossaries and terminology sections
6. **Tab related content** to keep pages more scannable
7. **Nest extensions** appropriately (e.g., code blocks inside admonitions)

---

## Navigation and where to edit

- Top-level docs live in "docs/wiki/".
- Edit pages directly; to reorganize navigation, ask a maintainer or update "mkdocs.yml".

## Community and contribution

This is a community project — everyone is welcome to contribute even without a GitHub account. Join the discussion and show us what you got:

- Download [docs/wiki/_wip/blank.md](docs/wiki/_wip/blank.md) if you need a starting point, write down your intel and post it in our **[dedicated Encyclopedia thread](https://discord.com/channels/1086729144307564648/1471224902890684557)** in the **[Zelda: Tears of the Kingdom Speedrunning Discord server](https://discord.gg/xM8NnTetb2)**

---

Thanks for contributing — keep changes focused, documented, and easy to review.

## See Also

- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Python-Markdown Extensions](https://python-markdown.github.io/extensions/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
