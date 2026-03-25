---
title: "DI Cloning"
draft: true
label: "DIC"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "Switch 2"]
credits: ["Aergyl", "mulberry", "Squidwest"]
date: "2026-01-16"
description: "Eaten DI passes a despawn attempt down to newly-fused main children, which can itself be interrupted to cause the "Ghost DI" state."
aliases: ["Ghost DI", "Ghost-DI"]
tags: ["item", "despawn", "fuse", "culling"]
---

# DI Cloning

## Summary
---

Eaten DI equipment passes an Eaten death down to newly-fused children (_if_ the main parent is DI), which can itself be interrupted. This causes the "Ghost DI" state, which has additional properties over the standard Eaten DI state.

_Discovered by mulberry; Properties, methods, and optimizations found by Aergyl, mulberry, Squidwest - Jan 16, 2026_

## Instructions
---

=== "Full Fuse Methods"

    These methods fully fuse the target to a normal parent and FE it to a DI parent; the former will need to be detangled/despawned to make the target persistent.

    ??? "Method 1: Fuse + Drop-Swap"

        1. Smuggle or Zuggle a DI weapon or shield
        2. Equip a normal item of the same type
        3. Fuse the target to the normal item; It will immediately begin despawning
        4. **Pause** a few frames after fusing. One way is to hold L at the same time as the fuse button, then selecting the Map Rune
        5. **Drop** the normal parent and **swap** to another item of the same type
        6. Optionally, **unequip** the item that was swapped to
        7. **Unpause** the game; The target will be DI'd and remain attached to the normal parent
        8. **Pick up** the target off of the normal parent and set it aside
        9. Delete the normal parent by "FarDelete"; this can be done by sending it away with a rocket, dropping it down a chasm, or simply moving about 60m away
        10. Detangle the DI parent; The fastest way to do this is to just use it again (DI objects with DI parents are protected from "Fuse-over" deletion)

    ??? "Method 2: Turbo Replication"

        1. Prepare an Octo Balloon Shield
        2. Smuggle or Zuggle a DI Shield
        3. Equip a normal shield and any 1-handed weapon
        4. Unsheathe the weapon; this will also unsheathe the shield
        5. **Hold** ZL to fuse the target and pause a few frames later; One way is to also hold L at the same time, and select the Map Rune
        6. **Drop** the equipped shield and **swap** to the Octo Balloon Shield
        7. **Unpause** the game and press B within a couple frames of the game actually unpausing
        8. Done correctly, the target will detangle from both the DI parent and the normal parent, and its pickup prompt will be displaced from its visual model

    ??? "Method 3: Mineru FE Target + Fuse"

        1. Mineru FE the target; This will cause it to cull with Mineru
        2. Smuggle or Zuggle a DI weapon or shield
        3. Equip a normal item of the same type
        4. Induce Mineru to cull and **fuse** the target a few frames before it culls with her; It will immediately begin despawning
        5. When Mineru culls the target, it will DI and remain attached to the normal parent
        7. **Pick up** the target off of the normal parent and set it aside
        8. Detangle the target from Mineru by fusing something else to the slot the target is on
        9. Delete the normal parent by "FarDelete"; this can be done by sending it away with a rocket, dropping it down a chasm, or simply moving about 60m away
        10. Detangle the target from the DI parent; The fastest way to do this is to just use it again (DI objects with DI parents are protected from "Fuse-over" deletion)

    ??? "Method 4: Mineru FE Parent + Fuse"

        1. Mineru FE a normal weapon or shield
        2. Smuggle a DI item of the same type
        3. Induce Mineru to cull and **fuse** the target a few frames before she culls
        4. The target will immediately begin despawning, then be culled with the normal parent, resulting in DI
        5. **Pick up** the target off of the normal parent and set it aside
        6. Delete the normal parent by "FarDelete"; this can be done by sending it away with a rocket, dropping it down a chasm, or simply moving about 60m away
        7. Detangle the target from the DI parent; The fastest way to do this is to just use it again (DI objects with DI parents are protected from "fuse-over" deletion)

    ??? "Method 5: Mineru DI + Fuse"

        1. DI a weapon or shield (A) with Method 2 and _do not_ detangle it from Mineru
        2. Smuggle or Zuggle A and equip a normal item over it
        3. Induce Mineru to cull and **fuse** the target a few frames before she culls
        4. The target will immediately begin despawning, then be culled with the DI parent, resulting in DI
        5. **Pick up** the target off the normal parent and set it aside
        6. Delete the normal parent by "FarDelete"; this can be done by sending it away with a rocket, dropping it down a chasm, or simply moving about 60m away
        7. Detangle the target from the DI parent; the fastest way to do this is to just use it again (DI objects with DI parents are protected from "fuse-over" deletion)

=== "Pseudo Fuse Methods"

    These methods FE the target to a DI parent and CF the target to a normal parent, resulting in PF; this removes the need to detangle it from the normal parent.

    ooohg i need a break

## Properties

- Retains all(?) properties of non-ghost DI
- Has no collision, gravity, or ability to move on its own once detached from its "model-bind" parent
- So long as it does not have non-persistent parents, it is "Auto-slotted" and will travel through warps and loads when dropped in the world
- Passes this persistence down to FE children
- Can be made persistently invisible with certain processes and passes this invisibility down to anything that attempts to fuse to it

!!! warning "Take care!"

    Warping causes a "sleep" on equipped items, which will undo this state! You can zuggle it to take it with you safely.

## Notes
---
### Remarks
Remarks

### Additions
Additions

### Extensions
Extensions

## Resources
---
- [Link Title](Link URL)

## Related
---
- [Searchbar Query](search:Searchbar Query)
