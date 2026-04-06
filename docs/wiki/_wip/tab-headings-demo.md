---
title: "Tab Headings Demo"
uid: "P4X"
draft: true
---

# Tab Headings Demo

This page showcases the tab heading feature and nested tab layouts.

## Basic Tab Headings

Tabs with `###` marks appear as h3 entries in the TOC and are sized accordingly.

=== "Pause-Cancel" ###

    Pause-cancel is the most common setup method.

    1. Open the menu
    2. Navigate to the item
    3. Press cancel at the right frame

=== "Menu Overload" ###

    Menu overload works by flooding the input buffer.

    1. Mash inputs during the load
    2. Wait for the desync
    3. Confirm the overload state

=== "Plain Tab"

    This tab has no `#` marks — it does **not** appear in the TOC and renders at the default size.

## Deeper Heading Levels

Tabs with `####` marks appear as h4 entries and render at a smaller size.

### Setup Variants

=== "Quick Setup" ####

    A fast variant that skips the initial positioning step.

    1. Zuggle directly from inventory
    2. Confirm the clone

=== "Safe Setup" ####

    A slower but more reliable variant.

    1. Save before attempting
    2. Position Link carefully
    3. Zuggle from inventory
    4. Verify the result

## Nested Tabs

Tabs can be nested by indenting the inner tab set by 4 additional spaces inside the outer tab's content. Inner tabs with `#` marks get their own heading size; inner tabs without `#` marks render at the default size.

=== "Version 1.0" ###

    Techniques available on the original release.

    === "Method A" ####

        The original discovery. Simple but slow.

        1. Open inventory
        2. Select the weapon
        3. Trigger the glitch

    === "Method B" ####

        An optimized variant found later.

        1. Skip the inventory step
        2. Use the shortcut input
        3. Confirm the result

=== "Version 1.2" ###

    These inner tabs have no `#` marks, so they render at the default size and don't appear in the TOC.

    === "Method A"

        Adapted from the 1.0 method with timing adjustments.

        1. Open inventory (timing changed)
        2. Wait two extra frames
        3. Trigger the glitch

    === "Method B"

        A completely new approach only possible on 1.2+.

        1. Use the new menu path
        2. Exploit the added delay
        3. Confirm the clone

## Mixed Nesting with Collapsible Sections

=== "Exploration Route" ###

    #### Shrine Skip ?

    1. Approach the shrine from the east
    2. Clip through the wall using a shield surf
    3. Land inside the shrine

    #### Boss Strategy ?

    1. Equip a fused weapon
    2. Use the zuggle state to bypass the first phase
    3. Finish with a flurry rush

=== "Combat Route" ###

    #### Hinox Skip ?

    1. Use a tree launch to fly over the arena
    2. Land on the far side

    #### Lynel Strategy !

    1. Mount the Lynel immediately
    2. Use the infinite mount glitch
    3. Repeat until defeated

## Autolink Throttle Demo

This section tests section-based throttling, the `!` escape prefix, and
existing-link deduplication.

### Section Throttling (headings)

Anti-Gravity Glitch is mentioned here — this first occurrence should be
autolinked. Anti-Gravity Glitch appears again in the same section and
should **not** be linked a second time. AGG (the label) should also be
suppressed since the UID is already covered.

### Section Reset

Anti-Gravity Glitch in a new section — should get a fresh autolink
because each heading resets the per-section budget.

Autobuild Duplication also appears here (first link) and then
Autobuild Duplication again (no link).

### Escape Prefix

!Anti-Gravity Glitch is prefixed with `!` — it should render as plain
"Anti-Gravity Glitch" with no link and no `!` marker visible. Because
the escaped mention consumed the only occurrence so far, the next
Anti-Gravity Glitch in this section should still get autolinked.

Conversely, !AGG suppresses the label, and AGG after it should link.

### Existing Link Awareness

This section contains a manual link to [Anti-Gravity Glitch](uid:PEY).
Because that UID is already linked, the autolinker should skip all
subsequent mentions of Anti-Gravity Glitch, AGG, anti gravity, and
any other alias for that page within this section.

Arrow Smuggling is not manually linked so it should still autolink once.
Arrow Smuggling again — no second link.

### Tabs as Sections

=== "Tab A" ###

    Anti-Gravity Glitch in Tab A — own section, should get one autolink.

    Anti-Gravity Glitch again in the same tab — should NOT be linked.

=== "Tab B" ###

    Anti-Gravity Glitch in Tab B — separate tab, separate section,
    so this should also get its own autolink.

    Arrow Smuggling also gets linked independently per tab.

### Collapsibles as Sections

Anti-Gravity Glitch appears above the collapsible — autolinked here.

??? example "Collapsible Test"

    Anti-Gravity Glitch inside a collapsible block. This is an
    independent section, so it should get its own autolink.

    Anti-Gravity Glitch again inside the same collapsible — no link.

After the collapsible, we are back in the parent section.
Anti-Gravity Glitch here should NOT be linked (already linked before
the collapsible in this same section fragment).

### Nested: Collapsible Inside Tab

=== "Outer Tab" ###

    Arrow Prompt Storage in the tab body — autolinked.

    ??? tip "Nested Collapsible"

        Arrow Prompt Storage inside the collapsible — separate section,
        gets its own link.

        Arrow Prompt Storage again — no second link.

    Arrow Prompt Storage after the collapsible — same tab section as
    above, already linked, so no second link.
