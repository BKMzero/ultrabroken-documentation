---
uid: markdown-extensions
label: Markdown Extensions
title: Markdown Extensions Reference
---

# Markdown Extensions Reference

This page documents all active Markdown extensions configured for the Ultrabroken Archives site. These extensions enhance the Markdown syntax to support rich formatting, interactive elements, and improved readability.

## Active Extensions

### 1. **Admonition**
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

#### Examples
!!! note "Example Note"
    Admonitions draw attention to important content with a colored border and background.

!!! tip
    Use admonitions sparingly to maintain visual hierarchy.

---

### 2. **Pymdownx Details** (Collapsible Blocks)
Creates expandable/collapsible sections of content.

#### Syntax
```markdown
??? note "Click to expand"
    Hidden content appears when you click the title.

??? warning "Collapsible warning"
    This section is hidden by default.

???+ tip "Expanded by default"
    The `+` makes it expand automatically on page load.
```

#### Examples
??? note "Hidden Content Example"
    This content is collapsed by default. Click the title to expand it.

???+ tip "Expanded by Default"
    Use the `+` prefix to show collapsed blocks expanded initially.

---

### 3. **Pymdownx Superfences**
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

#### Features
- **Syntax highlighting** for 100+ languages
- **Line numbers** with `linenums="1"`
- **Titles** with `title="your_title"`
- **Callout lines** with `hl_lines="1 2 3"`

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
```markdown
:::python print("inline code with highlighting")

:::javascript const x = 42;
```

---

### 6. **Pymdownx Tasklist**
Renders interactive checkboxes for task lists.

#### Syntax
```markdown
- [x] Completed task
- [ ] Incomplete task
- [x] Another completed task
```

#### Example
- [x] Study Ultrabroken mechanics
- [ ] Master zuggling techniques
- [x] Document discoveries

**Features:** Clickable checkboxes (when enabled) allow tasks to be marked complete.

---

### 7. **TOC (Table of Contents)**
Automatically generates a table of contents from headings. Includes **permalink support** for linking directly to sections.

#### Current Config
- `permalink: false` — Permalinks are disabled in the extension config
- Material Theme provides native styling and sidebar integration
- Use heading anchors like `[Link](#section-title)` to reference sections

#### Features
- Automatically detects heading hierarchy (h1, h2, h3, etc.)
- Integrated into Material theme sidebar
- Supports custom IDs with `attr_list` extension

---

### 8. **Attr List**
Adds support for custom attributes (IDs, classes) on elements.

#### Syntax
```markdown
# Heading with Custom ID {#custom-id}

Paragraph with a class.
{: .custom-class }

[Link text](#custom-id){ .button }
```

#### Use Cases
- Custom IDs for deep linking: `{#section-name}`
- CSS class application: `{: .highlight }`
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
```markdown
Term 1
:   Definition of term 1 with full support for **bold**, *italic*, and [links](/).

Term 2
:   Multi-paragraph definitions.
:   Supported by adding multiple `: ` entries.

Zuggle
:   A complex glitch involving equipment state manipulation.
```

#### Example
Zuggle
:   A glitch technique where Link's equipment state becomes desynchronized with the inventory display, allowing impossible item combinations.

OOB (Out of Bounds)
:   Exploiting collision detection to move Link outside the intended playable area.

---

### 11. **Pymdownx Tabbed** (Tabbed Content)
Creates tabs for organizing related content groups.

#### Syntax
```markdown
=== "Tab 1: Python"

    ```python
    print("Python code here")
    ```

=== "Tab 2: JavaScript"

    ```javascript
    console.log("JavaScript");
    ```

=== "Tab 3: Notes"

    Regular content here.
```

#### Features
- Multiple tabs within a single block
- Support for arbitrary content (code, text, lists)
- `alternate_style: true` enabled for modern Material theme styling
- Improves readability when comparing related content

#### Example
=== "Method A"

    This is approach A.

=== "Method B"

    This is alternative approach B.

---

## Extension Configuration

All extensions are defined in `mkdocs.yml` under the `markdown_extensions` section:

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

## Quick Reference Cheat Sheet

| Extension | Purpose | Key Syntax |
|---|---|---|
| **Admonition** | Callout blocks | `!!! type "Title"` |
| **Details** | Collapsible sections | `??? note "Title"` |
| **Superfences** | Advanced code blocks | ` ```python title="..." ``` ` |
| **Highlight** | Syntax coloring | (Automatic with Superfences) |
| **InlineHilite** | Inline code highlighting | `:::python code` |
| **Tasklist** | Interactive checkboxes | `- [x] Task` |
| **TOC** | Auto table of contents | (Automatic from headings) |
| **Attr List** | Custom attributes | `{#id .class}` |
| **Md in HTML** | Markdown in HTML blocks | `<div markdown="1">` |
| **Def List** | Glossaries | `Term\n:   Definition` |
| **Tabbed** | Organized content groups | `=== "Tab Name"` |

---

## Best Practices

1. **Use Admonitions** for important callouts (notes, warnings, tips)
2. **Prefer collapsible Details** only when content is optional or supplementary
3. **Leverage code block titles** to label examples
4. **Apply custom IDs** with `attr_list` for deep-linking to specific sections
5. **Use Def Lists** for glossaries and terminology sections
6. **Tab related content** to keep pages more scannable
7. **Nest extensions** appropriately (e.g., code blocks inside admonitions)

---

## See Also

- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Python-Markdown Extensions](https://python-markdown.github.io/extensions/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
