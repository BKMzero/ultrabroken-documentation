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

Conversely, `!` suppresses the !AGG label, and AGG after it should not be linked either even without `!` marker because of the spent contingent.

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

## Multi-Word Aliases

This section tests that multi-word aliases link correctly and that
position-based matching links the **earliest** occurrence in the text.

**Mineru FE** (the alias) should link here — the first occurrence in the
sentence.

**anti gravity** (lowercase alias) should link to Anti-Gravity Glitch.
The alias anti gravity again should not link in this section.

**crouch sprint** should link to Crouch Sprinting. Another mention of
crouch sprint stays plain text.

**Batch DI** should link here — the alias appears first. Then
Batch Despawn Interrupt later stays plain (budget spent).

**dive cancel** should link to Dive Cancel Glide Boost. And dive cancel
again is plain text due to section throttling.

## Single-Word Aliases Still Work

FE should link to Fuse Entanglement — a different UID than "Mineru FE"
so it gets its own budget. Then Mineru FE links to its page too.

DI should link to Despawn Interrupt.

AGG should link to Anti-Gravity Glitch.
