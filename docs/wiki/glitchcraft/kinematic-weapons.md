---
title: "Kinematic Weapons"
uid: "OO2"
label: "KW"
versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["mulberry", "dt13269", "Squidwest"]
date: "2026-02-25"
description: "Allows weapons with the 'kinematic' motion type to be obtained, which don't react to outside forces (making them movable only by certain techniques)."
aliases: ["kinematic equipment","unmovable equipment"]
tags: ["equipment"]
---

# Kinematic Weapons `KW`
`1.1.0` `1.1.1` `1.1.2` `1.2.0` `1.2.1` `1.3.0/1.4.0` `1.4.1` `1.4.2` `1.4.3` `Switch 2`

## Summary
---
Allows weapons with the 'kinematic' motion type to be obtained, which don't react to outside forces (making them movable only by certain techniques).

_mulberry, dt13269; Optimizations by mulberry, Squidwest - 25 February 2026_

## Instructions
---

All methods require a weapon currently held by a Depths Ghost, which will be referred to as the "target weapon" or "target".

=== "Pause-Cancel FE Methods"

    These Methods pause the game while performing FE on the target, preventing the ghost from detecting it being tampered with.

    ??? abstract "Method 1: Pause-Cancel Overload FE + Load Null Fuse"
    
        1. Zuggle any shield
        2. Overload drop another shield and fuse it to a weapon
        3. Highlight the target weapon with fuse
        4. Press ZL and pause the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
        5. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
        6. Highlight the target weapon with fuse again
        7. Press ZL and +/- on the same frame, then load a save. The target should be where it was, but not uninteractible.
        8. Move away from the target weapon and use a Rocket Shield to detangle it from the zuggled shield
        9. The target weapon should regain interaction and remain floating

    ??? abstract "Method 2: Pause-Cancel Mineru FE + Load Null Fuse"

        1. Find a large weapon cairn, with 3 ghosts atop it. These are large enough for Mineru to spawn atop them.
        2. Zuggle any shield
        3. Mineru FE another shield
        4. Highlight the target weapon with fuse
        5. Induce Mineru to cull, and perform "Animated" Mineru Cold Fuse on the target weapon (the frame which causes the visual and sound effects to play)
        6. On the frame you press ZL, pause the game. This can be done by opening a menu, or by performing this method on an unobtained weapon (??? prompt)
        7. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
        8. Highlight the target weapon with fuse again
        9. Press ZL and +/- on the same frame, then load a save. The target should be where it was, but now uninteractible.
        10. Move away from the target weapon and use a Rocket Shield to detangle it from teh zuggled shield
        11. The target weapon should regain interaction and remain floating

    ??? abstract "Method 3: Pause-Cancel Overload FE + Warp Fuse"

        1. Zuggle any non-DI shield
        2. Overload drop another shield and fuse it to a weapon
        3. Highlight the target weapon with fuse
        4. Press ZL and pause the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
        5. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
        6. Highlight the target weapon with fuse again.
        7. Press ZL and +/- on the same frame, then warp to your destination
        8. Use Octo Detanglement on the _equipped_ shield. This will detangle from the _zuggled_ parent shield without having to time the cancel
        9. The target weapon should regain interaction and remain floating

    ??? tip "Pause-Cancel???"

        Instead of pausing during the FE, any method requiring it can alternatively be performed with Overload Pickup:

        1. Overload Pickup the target weapon
        2. Move out of the ghost's update range, but stay within its spawn range
        3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
        4. Fail-drop the target, then drop it once it returns
        5. Proceed with a given Pause-Cancel method; The ghost will not despawn even without performing Wheel-Cancel.

=== "Overload Pickup Methods"

    These Methods use Overload Pickup to move the target to a distance where the ghost can't detect it being tampered with.

    ??? abstract "Method 4: Basic Loadless"

        1. Overload Pickup the target weapon
        2. Move out of the ghost's update range, but stay within its spawn range
        3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
        4. Fail-drop the target, then drop it once it returns. It should remain floating and interactible
        5. Overload Pickup the target again and fuse it to a shield
        6. Move out of the spawn range of the ghost
        7. Fail-drop the target, then drop it once it moves from the shield
        8. Move out of update range of the target and use Octo Detanglement on the parent shield
        9. The target weapon should regain interaction and remain floating

        This method relies on the ability to detach a fully-fused and ghosted weapon from its parent via Overload Pickup, allowing Octo Detanglement to be done out of update range.

    ??? abstract "Method 5: Minimalist Loadless"

        1. Overload Pickup the target weapon
        2. Move to the edge of the ghost's spawn range. Face away from the ghost to prevent it from updating
        3. Fail-drop the target, then drop it once it returns. It should remain floating and interactible
        4. Overload drop a shield and fuse it to a weapon
        5. Overload Cold Fuse the target to the shield on the frame Link exits the ghost's spawn range
        6. The target weapon should remain floating and interactible

        This method relies on the fact that an Overload Cold Fuse causes the target to be considered "Fused" for a single frame.

    ??? abstract "Method 6: Temporary Ghosting"

        1. Overload Pickup the target weapon
        2. Move out of the ghost's update range, but stay within its spawn range
        3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
        4. Fail-drop the target, then drop it once it returns. It should remain floating and interactible
        5. Overload drop a shield (A) and fuse it to a weapon
        6. Overload Cold Fuse a shield (B) to A
        7. Fail-drop and drop A, then Overload Pickup B
        8. Move B to the edge of Ultrahand range
        9. Highlight the target weapon with fuse
        10. Press ZL and pause the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
        11. The target weapon should become uninteractible, without appearing fused to the equipped shield
        12. Exit the ghost's spawn range, then return to the target weapon; it should regain interation and remain floating

=== "Legacy Methods"

    These original methods are retained here for archival purposes, but are surpassed by the other given methods.

    ??? "Basic Setup"

        1. Overload pickup weapon held by depths ghost
        2. Go out of range - this varies between ghosts
        3. While looking away from the ghost fail drop weapon
        4. Wait until Link holds it
        5. Drop it - it should be stuck in mid-air
        6. Keep looking away and resync zuggle a shield unless you already have one zuggled
        7. Overload CF the weapon twice to a random shield to PF it
        8. Load a save
        9. Either detangle out of weapon range or drop the zuggle and octo detangle it

    ??? "DI PSLOT Kinematic Weapon Setup"

        1. Zuggle a DI ghost shield
        2. Overload pick up a kinematic weapon held by ghost
        3. Fail drop and drop the kinematic weapon out of range
        4. Overload FE the weapon (using the shield zuggle) and load null fuse it (= overload cold fuse to your shield + pause on the FE frame -> load)
        5. Detangle out of range
        6. Overload FE the kinematic weapon and unzuggle parent


## Ways to move Kinematic Weapons
---

### Pickup-related Actions

- Carrying it around; Drop Smuggle-like states retain collision and are notably more forceful than normal
- Dropping it while moving, which directly adds Link's velocity
- Throwing it, which directly adds throw velocity; Boomerangs will follow a return arc

### Recall-related Actions

Kinematic Weapons obey the "position lock" and "velocity reset" of recall, so the following will work to move/stop it:

- Recalling an attached object; May break the glue sometimes
- Recalling the kw along a return path
- Recall-locking it and dropping it somewhere else

### Others

- Attaching an upside-down wing; Seems to directly add velocity to build instead of applying a force
- The "gravitational" force of attaching with Ultrahand can affect the velocity

## Other properties
---

- Doesn't collide with objects with Kinematic or Static motion types (npcs, terrain, other KWs, etc)
- Cannot be glued "from" (holding it or something attached to it), only "to" (holding something unattached to it)

!!! warning "Take care!"

    Warping causes a "sleep" on equipped items, which will undo this state! You can zuggle it to take it with you safely.

## Notes
---

Version `1.0.0` lacks a check for whether the weapon is fused, making it impossible to take the weapon in a way that preserves the motion type.

## Resources
---
- [Original discovery](https://discordapp.com/channels/1086729144307564648/1110956205624532993/1476367185642520639)
- [Original Load Null Fuse Method](https://discord.com/channels/1086729144307564648/1110956205624532993/1476693921533923390)
- [Pause-Cancel Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1481259601495195739)
- [Mineru Pause-Cancel Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1481251852237672609)
- [Pause-Cancel Warp Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1481411419093340222)
- [Basic Loadless Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1481190445135691836)
- [Minimalist Loadless Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1481347605215580363)
- [Temporary Ghosting Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1481367458517487877)

## Related
---
- [Zuggle Overload](search:Zuggle Overload)
- [Mineru FE](search:Mineru Fuse Entanglement)
