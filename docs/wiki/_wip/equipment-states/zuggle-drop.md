---
title: "Zuggle Drop"
uid: "L84"
tags: ["zuggle", "overload"]
aliases: ["zd", "local overload"]
---

# Zuggle Drop

Undone zuggles don't immediately go back to normal.

## Description

When equipment that was zuggled is released from its zuggle status, it loses most of those properties. It won't persist across loading screens, and won't interfere with fusing to equipment. However, it is still connected to Link.

Zuggle Drop is not to be confused with [Drop Zuggle](search:Drop Zuggle).

## Effects

The lingering connection to Link makes zuggle dropped equipment behave slightly different to normal equipment:

- It still contributes to [Zuggle Overload](search:Zuggle Overload), like zuggles and invizuggles do, but with some benefits:
    - Unlike zuggles, zuggle drops don't become FE parents of anything newly fused to a weapon or shield.
    - Unlike invizuggles, individually detaching zuggle drops from Link is easy, and doesn't require a game close.
            - This trick is sometimes called _local overload_.
- Zuggle dropped equipment will continue to have its physics updated during some cutscenes and dialog text.
- Ascending while a zuggle drop is being recalled will immediately cancel the recall. This is a way to test if some dropped equipment is a zuggle drop or not.

## Direct construction

You don't need to go through the whole zuggle state to make a zuggle drop. You can also make one by slightly modifying a zuggle method:

=== "Map" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1"]
    ---

    !!!info
        This method works on any version with DI equipment.

    Perform the inputs to Map Zuggling as described, but not with your back to a wall, so that both items can drop. The first item initially equipped will be a zuggle drop.

=== "Drop Delay" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2"]
    ---

    Perform the inputs of Drop Delay Zuggle as described, but not near a wall, so that everything has room to drop. The first item that was dropped while equipped will be a zuggle drop.

=== "Portacull" ###
    ---
    versions: ["1.2.0", "1.2.1", 1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    ---

    1. Drop swap your target item, then a portacull weapon/shield of the opposite kind.
    1. Pause buffer.
    1. Drop the swapped-to item of the original target kind.
    1. Unpause, and the first dropped item will be a zuggle drop.

## Undoing

You can undo zuggle drop status by picking the equipment up and dropping it again, or grabbing it with Ultrahand.
