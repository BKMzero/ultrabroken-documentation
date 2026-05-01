---
title: "Nesting Aggregation Demo"
uid: "H3N"
draft: true
---

# Nesting Aggregation Demo

This page tests version badge aggregation for collapsible headings nested
inside tabs. Each combination below should produce the correct range badge on
the collapsible heading and in the TOC — with no bleed from sibling or parent
tabs.

## Flat: no tabs

Baseline. A collapsible heading with one method directly inside.

### Flat method { .collapse }
---
versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
obsolete: false
---

Should show `1.2.0+` on the heading above.

## Tabs with collapsible children

Two tabs, each containing a collapsible heading. The badges on the collapsible
headings should reflect only their own tab's versions, not bleed across.

=== "Tab A" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
    obsolete: false
    ---

    #### Tab A section { .collapse }

    ##### Only method in Tab A { .collapse }
    ---
    versions: ["1.0.0", "1.1.0"]
    obsolete: false
    ---

    Step one. Should show `1.0.0-1.1.0` on the heading above.
    `#### Tab A section` above should show `1.0.0-1.1.0` (child only, not Tab B).

=== "Tab B" ###
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0"]
    obsolete: false
    ---

    #### Tab B section { .collapse }

    ##### Only method in Tab B { .collapse }
    ---
    versions: ["1.2.0", "1.2.1"]
    obsolete: false
    ---

    Step one. Should show `1.2.0-1.2.1` on the heading above.
    `#### Tab B section` above should show `1.2.0-1.2.1` (child only, not Tab A).

## Tabs with multiple methods per collapsible heading

A single collapsible heading contains two methods. The badge should be the
union of both.

=== "Tab C" ###

    #### Multi-method section { .collapse }

    ##### Method C1 { .collapse }
    ---
    versions: ["1.0.0", "1.1.0"]
    obsolete: false
    ---

    ##### Method C2 { .collapse }
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    `#### Multi-method section` above should show `All versions` (union of C1 + C2).

=== "Tab D" ###

    #### Tab D section { .collapse }

    ##### Only method in Tab D { .collapse }
    ---
    versions: ["1.4.3", "Switch 2"]
    obsolete: false
    ---

    Should show `1.4.3` and `Switch 2` badges above.
    No bleed from Tab C's `All versions`.

## notoc: true on a collapsible heading inside a tab

The notoc heading should be absent from the TOC; adjacent headings should be
unaffected.

=== "Tab E" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    #### Visible section { .collapse }

    ##### Method visible { .collapse }
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    #### Hidden section { .collapse }
    ---
    notoc: true
    ---

    ##### Method hidden { .collapse }
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    `#### Hidden section` above should be absent from the TOC.
    `#### Visible section` above should be present with `All versions`.
