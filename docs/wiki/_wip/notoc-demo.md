---
title: "No-TOC Demo"
uid: "N0T"
draft: true
---

# No-TOC Demo

This page tests the `notoc: true` metadata field across all section types.
Headings marked with `notoc` — and all their children — should be absent from
the sidebar TOC and invisible to the scroll spy (no URL hash updates, no active
highlight).

## Visible Section

This heading and everything below it should appear in the TOC normally.

### Visible Child

Still visible — no `notoc` in scope yet.

## Hidden Regular Section
---
notoc: true
---

This entire section is excluded from the TOC.  Neither this heading nor any of
its children should appear in the sidebar or be tracked by the scroll spy.

### Hidden Child (auto-suppressed)

This child heading carries no `notoc` marker itself, but it is excluded
automatically because its parent (`## Hidden Regular Section`) has
`notoc: true`.

#### Deeply Nested (also suppressed)

Three levels deep — still excluded because the root ancestor is notoc.

## Visible Again

Back to a normal visible heading.  The notoc scope ended when this `##`
boundary was reached.  This section and its children should appear in the TOC.

### Visible Child Under "Visible Again"

Confirms the scope reset correctly.

---

## Collapsible: All Visible ?

This collapsible section and its children are fully visible in the TOC.

### Visible Collapsible Child

Should appear in the TOC as a child of the section above.

## Hidden Collapsible Section ?
---
notoc: true
---

This collapsed section is excluded from the TOC.  Expanding it reveals content
but still no TOC entry.

### Hidden Collapsible Child (auto-suppressed)

Not in the TOC.  Only reachable by scrolling or direct hash navigation.

## Partially Visible Collapsible ?

This section itself is visible in the TOC.

### Visible Child Inside Collapsible

This child appears normally.

### Hidden Sub-Section ?
---
notoc: true
---

This specific sub-section is excluded even though its parent is visible.
The TOC shows the parent but not this sub-section or anything below it.

#### Auto-Suppressed Grandchild

Hidden because the `##` above has `notoc: true`.

### Visible Sibling After Hidden Sub-Section

This `###` sibling is back at the same level as the hidden sub-section, so
the notoc scope ends here.  This heading should appear in the TOC.

---

## Tabbed Sections

=== "Fully Visible Tab" ###

    This tab and its child headings are all visible.

    #### Visible Tab Child

    Appears in the TOC nested under the tab heading.

=== "Fully Hidden Tab" ###
    ---
    notoc: true
    ---

    The entire tab is excluded from the TOC.  No entry for the tab heading
    or any heading inside it.

    #### Hidden Tab Child (auto-suppressed)

    Not in the TOC.

=== "Partially Hidden Tab" ###

    This tab heading itself is visible in the TOC.

    #### Visible Heading Inside Tab

    This child appears in the TOC.

    #### Hidden Heading Inside Tab ?
    ---
    notoc: true
    ---

    This collapsible sub-heading inside a tab is excluded from the TOC.

    ##### Auto-Suppressed Child of Hidden Tab Sub-Heading

    Not in the TOC.

    #### Another Visible Heading Inside Tab

    Back in scope — the notoc boundary ended at the `####` level.

---

## Nested Tabs

=== "Outer Tab A" ###

    Outer tab A is visible in the TOC.

    === "Inner Tab: Visible" ####

        Inner tab visible — should appear in TOC as an h4.

    === "Inner Tab: Hidden" ####
        ---
        notoc: true
        ---

        This inner tab is excluded from the TOC along with any headings
        inside it.

        ##### Hidden Inner Content (auto-suppressed)

        Not in the TOC.

    === "Inner Tab: Visible Again" ####

        Back to visible — the notoc scope does not bleed to sibling tabs.

=== "Outer Tab B" ###
    ---
    notoc: true
    ---

    The whole outer tab is excluded.

    === "Inner Tab inside Hidden Outer" ####

        Even though this inner tab has no `notoc`, it is inside the body
        of a hidden outer tab.  Because the outer tab heading's notoc scope
        includes everything nested within it, this inner tab heading should
        also be suppressed.

---

## Summary

| Section type | Marker | Expected TOC behaviour |
|---|---|---|
| Regular heading | `notoc: true` | Excluded, children auto-excluded |
| Regular child | _(none, parent notoc)_ | Auto-excluded |
| Collapsible heading | `notoc: true` | Excluded, children auto-excluded |
| Tab heading | `notoc: true` | Excluded, children auto-excluded |
| Sibling after notoc | _(none)_ | Visible — scope reset at same level |
