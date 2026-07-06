---
title: "Mineru Cull Storage"
uid: "7ZD"
label: "MCS"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["ofstrings2", "Squidwest"]
date: "2025-11-09"
description: "Stores the callback of Mineru while mounted on her. Primarily useful for swap resync zuggle setups."
aliases: ["mineru-cull-storage"]
tags: ["zuggling", "storage", "culling", "mineru"]
---

# Mineru Cull Storage

## Summary
Stores the culling animation (and forced dismount) of Mineru while mounted on her. Primarily useful for Swap Resync Zuggle setups, _especially_ for self-zuggling sdc items (portaculls/vortaculls).

This can be performed with Mineru's cull, as well as her dismissal. Each has similar behavior and uses, with slightly distinct pros and cons.

_Mineru Cull Storage discovered by ofstrings2 - Nov 9th, 2025_

_Mineru Dismissal Storage SRZ developed by ofstrings2, Squidwest - June 6th, 2026_

## Instructions

=== "Cull Storage" ###
    
    #### Device Deployment ?

    By deploying a device onto Mineru's position and mounting her before the deployment occurs, her attempt to cull will be stored. The steps below are very reliable and fully portable.

    1. Drop a zonai wing or hoverstone on the ground
    2. Walk Mineru onto wing/hoverstone and dismount her
    3. Drop a small device (like a battery) and quickly mount her
    4. Cull will be stored until taking one of the actions below

    #### Town/Stable "No-Sage Zones" ?

    Certain animation types store the forced cull that occurs towns and other inhabited places. The steps below are 100% consistent.

    1. Fuse a rocket to one of Mineru's arms
    2. Ride Mineru to the edge of the town's limits (or any other location which forcibly culls sages)
    3. Begin to shoot the rocket, walk into the sage-culling area, and stop walking before the rocket detaches from her arm
    4. Cull will be stored until taking one of the actions below

    #### Releasing a Stored Cull ?

    The following actions will cause a stored cull to immediately activate:

    - Pressing ZL to guard
    - Pressing a movement direction
    - Pressing L/R with an aimable arm fuse
    - Pressing Y with a usable back fuse

    The following actions _also_ release a stored cull. However, unlike the above, they cannot be buffered while the D-Pad Menu is closing, making them mostly useless for Swap Resync Zuggling:

    - Pressing L/R without an aimable arm fuse
    - Pressing Y without a usable back fuse
    - Pressing B to dismount Mineru
    - Pressing ZR to draw bow (can be buffered, but even with the bow pre-unsheathed there is a 1 frame delay)

=== "Dismissal Storage" ###

    #### Low Ceilings ?

    If a low ceiling is overhead, such that dismounting Mineru requires the full animation to play out, dismissal will automatically be stored. This has easier timing than the option below, but can occasionally not force a faildrop when released.

    1. Mount Mineru and stand underneath a low ceiling (making one with a Hover Stone or other object is fine)
    2. Pause the game and dismiss Mineru via her sage vow
    3. Unpause. Dismissal will be stored until there is no longer a low ceiling overhead, or until pressing Y with one of the back fuses below

    #### Parry Animation ?

    Mineru's guard parry animation stores dismissal until it completes. This places a time constraint on beginning the resync zuggle, but is faster, waste-free, and fully portable.

    1. Mount Mineru and guard with ZL
    2. Press A to parry and **Pause** (+/-) at the same time, then dismiss Mineru via her sage vow
    3. Unpause. Dismissal will be stored until the parry animation ends, or until pressing Y with one of the back fuses below

    #### Releasing a Stored Dismissal ?

    Attempting to activate any of the following Zonai Devices, fused to Mineru's back part, will immediately activate a stored dismissal.

    - Fan
    - Wing
    - Balloon
    - Rocket (see below)
    - Flame/Frost/Shock/Beam Emitter
    - Hydrant
    - Big/Small Wheel
    - Spring
    - Cannon
    - Hover Stone
    - Light
    - Mirror
    - Homing Cart

    All of these, with the notable exception of the Rocket, can have their activation buffered while the D-Pad Menu is closing.

    #### Other Animations ?

    These other animations store a dismissal as well, but have no known way to release the stored dismissal on command:

    - Activating Mineru's back part without a usable device fused
    - Taking strong knockback
    - Being frozen
    - Being shocked
    - Aiming or swinging an arm

    Additionally, aiming an arm fuse can interrupt a Parry, but doesn't release a stored dismissal (due to also storing it).

### Using Cull/Dismissal Release to SRZ

The forced dismount of the cull/dismissal animation causes all pending equipment drops to faildrop. This essentially allows one to choose whether or not to faildrop at the _end_ of a setup instead of the start, preventing important items from being sent into the inventory and destroyed.

#### Zuggling an SDC item: ?
1. Equip the SDC item and perform a Mineru Cull/Dismissal Storage
2. Use the D-Pad Menu to Drop-Swap the SDC, keeping the menu open
3. D-Pad buffer one frame, so that Mineru+Link are culled (release the D-pad for gradually longer times until it fully closes for one frame)
4. Swap any other equipment type besides the SDC's type to resync
5. Drop the SDC's type
6. Allow the D-Pad Menu to fully close while holding a button that will release the stored dismount
7. If any step is failed, the SDC will simply be dropped

#### Zuggling something else: ?
1. Equip an SDC item of a different type to the target
2. Perform Mineru Cull/Dismissal Storage
3. Use the D-Pad Menu to Drop-Swap the SDC item, then the target, without allowing the menu to close
4. D-Pad buffer one frame, so that Mineru+Link are culled
5. Swap the third equipment type to resync the target and SDC types
6. Unequip the SDC's type and drop the target type (in either order)
7. Allow the D-Pad Menu to fully close while holding a button that will release the stored dismount
8. If any step is failed, the target and the SDC will simply be dropped

#### Zuggling both: ?
1. Equip an SDC item of a different type to the target
2. Perform Mineru Cull/Dismissal Storage
3. Use the D-Pad Menu to Drop-Swap the SDC item, then the target, without allowing the menu to close
4. D-Pad buffer one frame, so that Mineru+Link are culled
5. Swap the third equipment type to resync the target and SDC types
6. Drop the target and SDC's types in either order
7. Allow the D-Pad Menu to fully close while holding a button that will release the stored dismount
8. If any step is failed, the target and the SDC will simply be dropped

## Notes
Mineru Cull/Dismissal Storage SRZ neither requires frame–perfect pausing (like non-stored Mineru Dismissal SRZ) nor the risk of losing your portacull/vortacull (like Mineru Wall SRZ).

## Resources
- [Discord](https://discord.com/channels/1111875355758837830/1247621060657025197/1438180015635304529)
- [Discord](https://discord.com/channels/1086729144307564648/1110956205624532993/1439720452325900411)

## Related
- [Portable Culling](search:Portable Culling)
- [Swap Resync Zuggle](search:Swap Resync Zuggle)
