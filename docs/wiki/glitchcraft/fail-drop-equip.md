---
title: "Fail Drop Equip"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
description: "Attaches equipment to Link's back/hand with the pickup prompt still accessible."
aliases: ["fde", "fds", "fdz", "fail drop smuggle", "fail drop zuggle"]
tags: ["overload"]
---

# Fail Drop Equip

## Summary
Lets you equip something that has its pickup prompt still attached. Formerly known as _fail drop smuggle_.

## Instructions

=== "Method 1 (`1.0`)" ###
    ---
    versions: ["1.0.0"]
    ---

    _Setup by mulberry, this writeup by Pearfalse (untested)_

    1. Put Link's back to a wall with something of the same type as your target equipped
    1. Pause, swap to your target item, and drop it
    1. Pause buffer
    1. Drop the re-equipped item, then equip and unequip something else in the same tab
    1. Pause buffer
    1. Drop something unequipped in that tab
    1. Unpause to fail drop

=== "Method 2 (Overload-based, all versions)" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    ---

    1. Fill the inventory for the type of equipment you want to fail drop equip
    1. Position Link with his back to a wall
    1. Overload drop the equipment you want to fail drop equip

## Notes

If you zuggle FDE equipment, it becomes a Fail Drop Zuggle.

For the overload method:

    - The timing for the X press is very tight, possibly frame-perfect.
    - A success requires the message "You can't carry any more \[equipment type\].", and not "You can't take that out here." (although there is at last one frame that gives you the correct message, but fail drops normally).

## Resources
- [Discord: video of 1.0 method](https://discord.com/channels/1086729144307564648/1105598687167664239/1251550527175786716)

## Related
[Equipment States: Fail Drop Equip](../_wip/equipment-states/fail-drop-equip)
