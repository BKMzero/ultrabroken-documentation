---
title: "Autolink Throttle Demo"
uid: "D9K"
draft: true
---

# Autolink Throttle Demo

This page tests section-based throttling, the `!` escape prefix, and
existing-link deduplication in the glitch autolinker.

## Section Throttling (headings)

Anti-Gravity Glitch is mentioned here — this first occurrence should be
autolinked. Anti-Gravity Glitch appears again in the same section and
should **not** be linked a second time. AGG (the label) should also be
suppressed since the UID is already covered.

## Section Reset

Anti-Gravity Glitch in a new section — should get a fresh autolink
because each heading resets the per-section budget.

Autobuild Duplication also appears here (first link) and then
Autobuild Duplication again (no link).

## Escape Prefix

!Anti-Gravity Glitch is prefixed with `!` — it should render as plain
`Anti-Gravity Glitch` with no link and with no `!` marker visible. Because
the escaped mention consumed the only occurrence so far, the next
Anti-Gravity Glitch in this section should still get autolinked.

Conversely, !AGG suppresses the label, and AGG after it should not be linked even without `!` marker.

## Existing Link Awareness

This section contains a manual link to [Anti-Gravity Glitch](uid:PEY).
Because that UID is already linked, the autolinker should skip all
subsequent mentions of Anti-Gravity Glitch, AGG, anti gravity, and
any other alias for that page within this section.

Arrow Smuggling is not manually linked so it should still autolink once.
Arrow Smuggling again — no second link.

## Tabs as Sections

=== "Tab A" ###

    Anti-Gravity Glitch in Tab A — own section, should get one autolink.

    Anti-Gravity Glitch again in the same tab — should NOT be linked.

=== "Tab B" ###

    Anti-Gravity Glitch in Tab B — separate tab, separate section,
    so this should also get its own autolink.

    Arrow Smuggling also gets linked independently per tab.

## Collapsible Headings (section boundaries) ?

Anti-Gravity Glitch in a collapsible heading section — autolinked.
Anti-Gravity Glitch again — same section, no second link.

### Nested Collapsible Heading ?

Anti-Gravity Glitch under a nested collapsible heading — this is a
new section (h3 boundary), so it gets its own autolink.

Arrow Prompt Storage also appears here — autolinked independently.
Arrow Prompt Storage again — no second link.

#### Deep Nested Collapsible !

Autobuild Duplication appears here — own h4 section, gets autolinked.
Autobuild Duplication mentioned again — same section, no second link.

Arrow Unloading also shows up (first mention in this section, autolinked).
Arrow Unloading repeated — no second link in this section.
