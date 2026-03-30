---
title: "Ghost Despawn Interrupt"
draft: true
label: "GDI"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["Aergyl", "mulberry", "Squidwest"]
date: "2026-01-16"
description: "Eaten DI passes a despawn attempt down to newly-fused children, which can itself be interrupted to cause the Ghost DI state."
aliases: ["Ghost DI", "Ghost-DI", "Ghost Frox"]
tags: ["item", "despawn", "fuse", "culling"]
---

# Ghost Despawn Interrupt

## Summary

Eaten DI equipment passes an Eaten death down to newly-fused children (_if_ the main parent is DI), which can itself be interrupted. This causes the "Ghost DI" state, which has additional properties over the standard Eaten DI state.

_Discovered by mulberry; methods, optimizations, and properties found by Aergyl, mulberry, Squidwest - Jan 16, 2026_

## Instructions

All methods follow the same general pattern:

1. FE the target to a DI weapon or shield (must be the "main" parent, which is usually automatically true but can be deliberately controlled)
2. Put the target in the "Ghost" state (aka fused state; often happens with the same Fuse input as step 1, but is always at least a frame later)
3. Cull the target to interrupt the resulting fadeout despawn, locking in the state
4. (usually) Detangle the target from its parent(s) to make it independent

=== "Full Fuse Methods"

    These methods FE the target to a DI parent and fully fuse the target to a normal parent; the latter will need to be detangled/despawned to make the target persistent.

    #### Method 1: Fuse + Drop-Swap { .collapse }
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This is the simplest method, and the easiest to understand. It uses drop-swap culling as the DI method, making it exclusive to newer patches.

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

    #### Method 2: Turbo Replication { .collapse }
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This method builds on Method 1, incorporating Octo Detanglement to instantly detangle both parents.

    1. Prepare an Octo Balloon Shield
    2. Smuggle or Zuggle a DI Shield
    3. Equip a normal shield and any 1-handed weapon
    4. Unsheathe the weapon; this will also unsheathe the shield
    5. **Hold** ZL to fuse the target and pause a few frames later; One way is to also hold L at the same time, and select the Map Rune
    6. **Drop** the equipped shield and **swap** to the Octo Balloon Shield
    7. **Unpause** the game and press B within a couple frames of the game actually unpausing
    8. Done correctly, the target will detangle from both the DI parent and the normal parent, and its pickup prompt will be displaced from its visual model

    #### Method 3: Mineru FE Target + Fuse { .collapse }
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This method entangles the target to Mineru, allowing her to be used as the culling source to DI that target. The target will continue culling with Mineru afterwards.

    1. Mineru FE the target; This will cause it to cull with Mineru
    2. Smuggle or Zuggle a DI weapon or shield
    3. Equip a normal item of the same type
    4. Induce Mineru to cull and **fuse** the target a few frames before it culls with her; It will immediately begin despawning
    5. When Mineru culls the target, it will DI and remain attached to the normal parent
    7. **Pick up** the target off of the normal parent and set it aside
    8. If desired, detangle the target from Mineru by fusing something else to the slot the target is on
    9. Delete the normal parent by "FarDelete"; this can be done by sending it away with a rocket, dropping it down a chasm, or simply moving about 60m away
    10. Detangle the target from the DI parent; The fastest way to do this is to just use it again (DI objects with DI parents are protected from "Fuse-over" deletion)

    #### Method 4: Mineru FE Parent + Fuse { .collapse }
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This method entangles the "normal parent" to Mineru, allowing her to be used as the culling source to make one DI Ghost.

    1. Mineru FE a normal weapon or shield
    2. Smuggle a DI item of the same type
    3. Induce Mineru to cull and **fuse** the target a few frames before she culls
    4. The target will immediately begin despawning, then be culled with the normal parent, resulting in DI
    5. **Pick up** the target off of the normal parent and set it aside
    6. Delete the normal parent by "FarDelete"; this can be done by sending it away with a rocket, dropping it down a chasm, or simply moving about 60m away
    7. Detangle the target from the DI parent; The fastest way to do this is to just use it again (DI objects with DI parents are protected from "fuse-over" deletion)

    #### Method 5: Mineru DI + Fuse { .collapse }
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This method entangles the DI parent to Mineru, allowing her to be used as the culling source to make many ghosts.

    1. Prepare a DI weapon or shield (A) which is entangled to Mineru (for example, with Method 3)
    2. Smuggle or Zuggle A and equip a normal item over it
    3. Induce Mineru to cull and **fuse** the target a few frames before she culls
    4. The target will immediately begin despawning, then be culled with the DI parent, resulting in DI
    5. **Pick up** the target off the normal parent and set it aside
    6. Delete the normal parent by "FarDelete"; this can be done by sending it away with a rocket, dropping it down a chasm, or simply moving about 60m away
    7. Detangle the target from the DI parent; the fastest way to do this is to just use it again (DI objects with DI parents are protected from "fuse-over" deletion)

=== "Pseudo Fuse Methods"

    These methods FE the target to a DI parent and CF the target to a normal parent, resulting in PF; this removes the need to detangle it from the normal parent.

    #### Method 6: Overload Pseudo Fuse { .collapse }
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This method uses overload to Pseudo-Fuse the target, and then literally idk how it culls the target

    (normal overload pfdi without any batching considerations)
    (I don't actually know what's minimal, so I'm coming back to this one later)

    #### Method 7<br/>Culling Area Distant Pseudo Fuse { .collapse }
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This method uses a culling area to Pseudo-Fuse the target, and a portacull to perform the DI.

    Prepare a DI weapon or shield, another item of that type, and a portacull of the opposite type

    1. Use a small culling area to store fuse on the target with a normal parent
    2. Move into and quickly back out of the culling margin to uncull the target for 1 frame
    3. Drop the normal parent and move it out of update range (the far end of the platform at Akkala Citadel Ruins' small culling area is enough)
    4. Pick up the DI item and move into the culling margin
    5. A few frames after the target unculls, pause the game
    6. Use the portacull to cull the DI parent and the target
    7. The target, now DI'd, will be attached to the normal parent, but not fused

    #### Method 8<br/>Culling Area Recull Pseudo Fuse { .collapse }
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: true
    ---

    This method uses a culling area to Pseudo-Fuse the target, and a portacull to perform the DI. It's more difficult than Method 7, for no benefit. Don't do it.

    Prepare a DI weapon or shield, another item of that type, and a portacull of the opposite type

    1. Use a small culling area to store fuse on the target with a normal parent
    2. Move into and quickly back out of the culling margin to uncull the target for 1 frame
    3. Drop the normal parent and move it out of update range (the far end of the platform at Akkala Citadel Ruins' small culling area is enough)
    4. Pick up the DI item
    5. Move into and quickly back out of the culling margin again to uncull the target for 1 frame, again
    6. Shortly after the target unculls, pause the game (timing is frame perfect)
    6. Use the portacull to cull the DI parent and the target
    7. The target, now DI'd, will be attached to the normal parent, but not fused

    Don't.

## Properties

- Retains all(?) properties of non-ghost DI
- Can be picked up off its "model-bind" parent, permanently detaching it (and turning the connection into plain FE/CF)
- Has no collision, gravity, or ability to move on its own once detached from its "model-bind" parent
- Its FE connection to its DI parent can be "fused over", reducing it to a CF connection
- So long as it does not have non-persistent parents, it is "Auto-slotted" and will travel through warps and loads when dropped in the world
- Passes this persistence down to FE children
- Can be made persistently invisible with certain processes and passes this invisibility down to anything that attempts to fuse to it

!!! warning "Take care!"

    Warping causes a "sleep" on equipped items, which will undo this state! You can zuggle it to take it with you safely.

## Notes

- Due to the requirement that the _Main_ parent of the target be DI, the despawn can be prevented by fusing it in a way that makes another item the main parent
- In addition, it can be _delayed_ by providing the target with additional CF parent(s) before performing most methods; the despawn can be triggered **at will** by deleting these additional parents

!!! failure "Pre-fused Ghosts"

    If a non-ghost DI equipment is created with a fuse already attached, the fuse (if it survives at all) will _seem_ to be in the Ghost DI state, but is in fact missing any form of persistence (even warping with it zuggled will delete it).

    This is due to a property of the DI state: it stops updating various flags and variables, including whether it is a "resident" (aka persistent) actor. DI Ghosts which are attached to Link on creation (like fusing to a zuggled equipment) keep their resident state even when dropped, and DI Ghosts created while unattached (such as being fused to a detached piece of equipment) fail to gain the resident state even when attached.

!!! warning "Fuse Overload"

    If a piece of equipment has 30 direct child dependencies, it will become "Fuse Overloaded". Further fuse attempts will fail, producing a "reference FE" connection, which will usually **crash the game** if the "failed parent" is dropped. Because "fusing over" a DI ghost leaves a CF connection to that parent, a DI parent can only be used 30 times unless full detanglement is used or some children are destroyed.

### Remarks
Remarks

### Additions
Additions

### Extensions
Extensions

## Resources
- [Link Title](Link URL)

## Related
- [Searchbar Query](search:Searchbar Query)
