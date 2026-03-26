---
title: "Kinematic Weapons (Collapsible Sections Demo)"
uid: "OO2"
label: "KW"
versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["mulberry", "dt13269", "Squidwest"]
date: "2026-02-25"
description: "Allows weapons with the 'kinematic' motion type to be obtained, which don't react to outside forces (making them movable only by certain techniques)."
aliases: ["kinematic equipment","unmovable equipment"]
tags: ["equipment"]
---

# Kinematic Weapons

## Summary
---
Allows weapons with the 'kinematic' motion type to be obtained, which don't react to outside forces (making them movable only by certain techniques).

_mulberry, dt13269; Optimizations by mulberry, Squidwest - 25 February 2026_

## Instructions
---

All methods require a weapon currently held by a Depths Ghost, which will be referred to as the "target weapon" or "target".

=== "Pause-Cancel FE Methods"

    These Methods pause the game while performing FE on the target, preventing the ghost from detecting it being tampered with.

    #### Method 1: Pause-Cancel Overload FE + Load Null Fuse ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: true
    ---

    1. Zuggle any shield
    2. Overload Drop another shield and fuse it to a weapon
    3. Highlight the target weapon with Fuse
    4. Press ZL and **pause** the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
    5. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
    6. Highlight the target weapon with Fuse again
    7. Press ZL and +/- on the same frame, then load a save. The target should be where it was, but uninteractible
    8. Move away from the target weapon and use a Rocket Shield to detangle it from the zuggled shield
    9. The target weapon should regain interaction and remain floating

    #### Method 2: Pause-Cancel Mineru FE + Load Null Fuse ?
    ---
    versions: ["1.0.0"]
    obsolete: false
    ---

    1. Find a large weapon cairn, with 3 ghosts atop it. These are large enough for Mineru to spawn atop them.
    2. Zuggle any shield
    3. [Mineru FE](mineru-fuse-entanglement.md) another shield
    4. Highlight the target weapon with Fuse
    5. Make Mineru cull, and perform "Animated" [Mineru Cold Fuse](mineru-fuse-entanglement.md) on the target weapon (the frame which causes the visual and sound effects to play)
    6. On the frame you press ZL, **pause** the game. This can be done by opening a menu, or by performing this method on an unobtained weapon (??? prompt)
    7. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
    8. Highlight the target weapon with Fuse again
    9. Press ZL and +/- on the same frame, then load a save. The target should be where it was, but uninteractible
    10. Move away from the target weapon and use a Rocket Shield to detangle it from the zuggled shield
    11. The target weapon should regain interaction and remain floating

    #### Method 3: Pause-Cancel Overload FE + Warp Fuse ?

    1. Zuggle any non-DI shield
    2. [Overload Drop](zuggle-overload.md) another shield and fuse it to a weapon
    3. Highlight the target weapon with Fuse
    4. Press ZL and **pause** the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
    5. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
    6. Highlight the target weapon with Fuse again
    7. Press ZL and +/- on the same frame, then warp to your destination without unpausing
    8. Use Octo Detanglement on the _equipped_ shield. This will detangle from the _zuggled_ parent shield without having to time the cancel
    9. The target weapon should regain interaction and remain floating

    #### Pause-Cancel??? !

    Instead of pausing during the FE, any method requiring Pause-Cancel can alternatively be performed with Overload Pickup:

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move out of the ghost's update range, but stay within its spawn range
    3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
    4. **Fail-drop** the target, then **drop** it once it returns to Link
    5. Proceed with a given Pause-Cancel method; The ghost will not despawn even without performing Pause-Cancel

=== "Overload Pickup Methods"
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: true
    ---

    These Methods use Overload Pickup to move the target to a distance where the ghost can't detect it being tampered with.

    #### Method 4: Basic Loadless ?

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move out of the ghost's update range, but stay within its spawn range
    3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
    4. **Fail-drop** the target, then **drop** it once it returns to Link. It should remain floating and interactible
    5. Overload Pickup the target again and fuse it to a shield
    6. Move out of the spawn range of the ghost
    7. **Fail-drop** the target, then **drop** it once it moves from the shield to Link's back
    8. Move out of update range of the target and use Octo Detanglement on the parent shield
    9. The target weapon should regain interaction and remain floating

    This method relies on the ability to detach a fully-fused and ghosted weapon from its parent via Overload Pickup, allowing Octo Detanglement to be done out of update range.

    #### Method 5: Minimalist Loadless ?

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move to the edge of the ghost's spawn range. Face away from the ghost to prevent it from updating
    3. Fail-drop the target, then drop it once it returns. It should remain floating and interactible
    4. [Overload Drop](zuggle-overload.md) a shield and fuse it to a weapon
    5. Overload Cold Fuse the target to the shield on the frame Link exits the ghost's spawn range
    6. The target weapon should remain floating and interactible

    This method relies on the fact that an Overload Cold Fuse causes the target to be considered "Fused" for a single frame.

    #### Method 6: Temporary Ghosting ?

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move out of the ghost's update range, but stay within its spawn range
    3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
    4. Fail-drop the target, then drop it once it returns. It should remain floating and interactible
    5. [Overload Drop](zuggle-overload.md) a shield (A) and fuse it to a weapon
    6. Overload Cold Fuse a shield (B) to A
    7. **Fail-drop** A, then and *drop* it once it returns to Link
    8. Overload Pickup B, then move it out of Link's update range (max Ultrahand distance is far enough)
    9. Highlight the target weapon with Fuse
    10. Press ZL and **pause** the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
    11. When the game unpauses, the target weapon should warp to B and become uninteractible, without appearing fused in the inventory
    12. Exit the ghost's spawn range, then return to the target weapon; it should regain interaction and remain floating

### Deeper Instructions

All methods require a weapon currently held by a Depths Ghost, which will be referred to as the "target weapon" or "target".

=== "Pause-Cancel FE Methods"

    These Methods pause the game while performing FE on the target, preventing the ghost from detecting it being tampered with.

    #### Method 1: Pause-Cancel Overload FE + Load Null Fuse ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: true
    ---

    1. Zuggle any shield
    2. Overload Drop another shield and fuse it to a weapon
    3. Highlight the target weapon with Fuse
    4. Press ZL and **pause** the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
    5. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
    6. Highlight the target weapon with Fuse again
    7. Press ZL and +/- on the same frame, then load a save. The target should be where it was, but uninteractible
    8. Move away from the target weapon and use a Rocket Shield to detangle it from the zuggled shield
    9. The target weapon should regain interaction and remain floating

    #### Method 2: Pause-Cancel Mineru FE + Load Null Fuse ?
    ---
    versions: ["1.0.0"]
    obsolete: false
    ---

    1. Find a large weapon cairn, with 3 ghosts atop it. These are large enough for Mineru to spawn atop them.
    2. Zuggle any shield
    3. [Mineru FE](mineru-fuse-entanglement.md) another shield
    4. Highlight the target weapon with Fuse
    5. Make Mineru cull, and perform "Animated" [Mineru Cold Fuse](mineru-fuse-entanglement.md) on the target weapon (the frame which causes the visual and sound effects to play)
    6. On the frame you press ZL, **pause** the game. This can be done by opening a menu, or by performing this method on an unobtained weapon (??? prompt)
    7. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
    8. Highlight the target weapon with Fuse again
    9. Press ZL and +/- on the same frame, then load a save. The target should be where it was, but uninteractible
    10. Move away from the target weapon and use a Rocket Shield to detangle it from the zuggled shield
    11. The target weapon should regain interaction and remain floating

    #### Method 3: Pause-Cancel Overload FE + Warp Fuse ?

    1. Zuggle any non-DI shield
    2. [Overload Drop](zuggle-overload.md) another shield and fuse it to a weapon
    3. Highlight the target weapon with Fuse
    4. Press ZL and **pause** the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
    5. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
    6. Highlight the target weapon with Fuse again
    7. Press ZL and +/- on the same frame, then warp to your destination without unpausing
    8. Use Octo Detanglement on the _equipped_ shield. This will detangle from the _zuggled_ parent shield without having to time the cancel
    9. The target weapon should regain interaction and remain floating

    #### Pause-Cancel??? !

    Instead of pausing during the FE, any method requiring Pause-Cancel can alternatively be performed with Overload Pickup:

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move out of the ghost's update range, but stay within its spawn range
    3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
    4. **Fail-drop** the target, then **drop** it once it returns to Link
    5. Proceed with a given Pause-Cancel method; The ghost will not despawn even without performing Pause-Cancel

=== "Overload Pickup Methods"
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: true
    ---

    These Methods use Overload Pickup to move the target to a distance where the ghost can't detect it being tampered with.

    #### Method 4: Basic Loadless ?

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move out of the ghost's update range, but stay within its spawn range
    3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
    4. **Fail-drop** the target, then **drop** it once it returns to Link. It should remain floating and interactible
    5. Overload Pickup the target again and fuse it to a shield
    6. Move out of the spawn range of the ghost
    7. **Fail-drop** the target, then **drop** it once it moves from the shield to Link's back
    8. Move out of update range of the target and use Octo Detanglement on the parent shield
    9. The target weapon should regain interaction and remain floating

    This method relies on the ability to detach a fully-fused and ghosted weapon from its parent via Overload Pickup, allowing Octo Detanglement to be done out of update range.

    #### Method 5: Minimalist Loadless ?

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move to the edge of the ghost's spawn range. Face away from the ghost to prevent it from updating
    3. Fail-drop the target, then drop it once it returns. It should remain floating and interactible
    4. [Overload Drop](zuggle-overload.md) a shield and fuse it to a weapon
    5. Overload Cold Fuse the target to the shield on the frame Link exits the ghost's spawn range
    6. The target weapon should remain floating and interactible

    This method relies on the fact that an Overload Cold Fuse causes the target to be considered "Fused" for a single frame.

    #### Method 6: Temporary Ghosting ?

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move out of the ghost's update range, but stay within its spawn range
    3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
    4. Fail-drop the target, then drop it once it returns. It should remain floating and interactible
    5. [Overload Drop](zuggle-overload.md) a shield (A) and fuse it to a weapon
    6. Overload Cold Fuse a shield (B) to A
    7. **Fail-drop** A, then and *drop* it once it returns to Link
    8. Overload Pickup B, then move it out of Link's update range (max Ultrahand distance is far enough)
    9. Highlight the target weapon with Fuse
    10. Press ZL and **pause** the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
    11. When the game unpauses, the target weapon should warp to B and become uninteractible, without appearing fused in the inventory
    12. Exit the ghost's spawn range, then return to the target weapon; it should regain interaction and remain floating

#### Even Deeper Instructions

All methods require a weapon currently held by a Depths Ghost, which will be referred to as the "target weapon" or "target".

=== "Pause-Cancel FE Methods"

    These Methods pause the game while performing FE on the target, preventing the ghost from detecting it being tampered with.

    #### Method 1: Pause-Cancel Overload FE + Load Null Fuse ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: true
    ---

    1. Zuggle any shield
    2. Overload Drop another shield and fuse it to a weapon
    3. Highlight the target weapon with Fuse
    4. Press ZL and **pause** the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
    5. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
    6. Highlight the target weapon with Fuse again
    7. Press ZL and +/- on the same frame, then load a save. The target should be where it was, but uninteractible
    8. Move away from the target weapon and use a Rocket Shield to detangle it from the zuggled shield
    9. The target weapon should regain interaction and remain floating

    #### Method 2: Pause-Cancel Mineru FE + Load Null Fuse ?
    ---
    versions: ["1.0.0"]
    obsolete: false
    ---

    1. Find a large weapon cairn, with 3 ghosts atop it. These are large enough for Mineru to spawn atop them.
    2. Zuggle any shield
    3. [Mineru FE](mineru-fuse-entanglement.md) another shield
    4. Highlight the target weapon with Fuse
    5. Make Mineru cull, and perform "Animated" [Mineru Cold Fuse](mineru-fuse-entanglement.md) on the target weapon (the frame which causes the visual and sound effects to play)
    6. On the frame you press ZL, **pause** the game. This can be done by opening a menu, or by performing this method on an unobtained weapon (??? prompt)
    7. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
    8. Highlight the target weapon with Fuse again
    9. Press ZL and +/- on the same frame, then load a save. The target should be where it was, but uninteractible
    10. Move away from the target weapon and use a Rocket Shield to detangle it from the zuggled shield
    11. The target weapon should regain interaction and remain floating

    #### Method 3: Pause-Cancel Overload FE + Warp Fuse ?

    1. Zuggle any non-DI shield
    2. [Overload Drop](zuggle-overload.md) another shield and fuse it to a weapon
    3. Highlight the target weapon with Fuse
    4. Press ZL and **pause** the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
    5. When the game unpauses, the target should FE to the zuggled shield, but remain floating and interactible
    6. Highlight the target weapon with Fuse again
    7. Press ZL and +/- on the same frame, then warp to your destination without unpausing
    8. Use Octo Detanglement on the _equipped_ shield. This will detangle from the _zuggled_ parent shield without having to time the cancel
    9. The target weapon should regain interaction and remain floating

    #### Pause-Cancel??? !

    Instead of pausing during the FE, any method requiring Pause-Cancel can alternatively be performed with Overload Pickup:

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move out of the ghost's update range, but stay within its spawn range
    3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
    4. **Fail-drop** the target, then **drop** it once it returns to Link
    5. Proceed with a given Pause-Cancel method; The ghost will not despawn even without performing Pause-Cancel

=== "Overload Pickup Methods"
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: true
    ---

    These Methods use Overload Pickup to move the target to a distance where the ghost can't detect it being tampered with.

    #### Method 4: Basic Loadless ?

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move out of the ghost's update range, but stay within its spawn range
    3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
    4. **Fail-drop** the target, then **drop** it once it returns to Link. It should remain floating and interactible
    5. Overload Pickup the target again and fuse it to a shield
    6. Move out of the spawn range of the ghost
    7. **Fail-drop** the target, then **drop** it once it moves from the shield to Link's back
    8. Move out of update range of the target and use Octo Detanglement on the parent shield
    9. The target weapon should regain interaction and remain floating

    This method relies on the ability to detach a fully-fused and ghosted weapon from its parent via Overload Pickup, allowing Octo Detanglement to be done out of update range.

    #### Method 5: Minimalist Loadless ?

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move to the edge of the ghost's spawn range. Face away from the ghost to prevent it from updating
    3. Fail-drop the target, then drop it once it returns. It should remain floating and interactible
    4. [Overload Drop](zuggle-overload.md) a shield and fuse it to a weapon
    5. Overload Cold Fuse the target to the shield on the frame Link exits the ghost's spawn range
    6. The target weapon should remain floating and interactible

    This method relies on the fact that an Overload Cold Fuse causes the target to be considered "Fused" for a single frame.

    #### Method 6: Temporary Ghosting ?

    1. [Overload Pickup](zuggle-overload.md) the target weapon
    2. Move out of the ghost's update range, but stay within its spawn range
    3. This distance varies between ghosts, but can be made more lenient by facing the camera away from it
    4. Fail-drop the target, then drop it once it returns. It should remain floating and interactible
    5. [Overload Drop](zuggle-overload.md) a shield (A) and fuse it to a weapon
    6. Overload Cold Fuse a shield (B) to A
    7. **Fail-drop** A, then and *drop* it once it returns to Link
    8. Overload Pickup B, then move it out of Link's update range (max Ultrahand distance is far enough)
    9. Highlight the target weapon with Fuse
    10. Press ZL and **pause** the game on the same frame. This can be done by buffering the ability wheel, or by opening a menu
    11. When the game unpauses, the target weapon should warp to B and become uninteractible, without appearing fused in the inventory
    12. Exit the ghost's spawn range, then return to the target weapon; it should regain interaction and remain floating

## Properties
---

- Cannot be glued "from" (holding it/something attached to it), only "to" (holding something unattached to it)
- Uses an effective mass of 1,000,000 for certain purposes, such as calculating glue strength
- Does not collide with anything, though regular ("Dynamic") objects _will still collide with it_
- As it does not collide, external forces do not affect it, thus only a select few actions can change its velocity

### Known Ways to Move Kinematic Weapons ?

#### Pickup-related Actions

- Carrying it around; Drop Smuggle-like states retain collision and are notably more forceful than normal
- Dropping it while moving, which directly adds Link's velocity
- Throwing it, which directly adds throw velocity; Boomerangs will follow a return arc

#### Recall-related Actions

Kinematic Weapons obey the "position lock" and "velocity reset" of recall, so the following will work to **move**, then **stop** it:

- Recalling an attached object; May break the glue sometimes
- Recalling the Kinematic Weapon along a return path
- Recall-locking it and dropping it somewhere else

#### Other Actions

- Attaching an upside-down wing; Seems to directly add velocity to build instead of applying a force
- The "gravitational" force of attaching with Ultrahand can affect the velocity

!!! warning "Take care!"

    Warping causes a "sleep" on equipped items, which will undo this state! You can zuggle it to take it with you safely.

### Test section
---
versions: ["1.1.0", "1.1.1", "1.1.2"]
obsolete: true
---

Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn.

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
