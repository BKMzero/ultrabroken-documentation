---
title: "Mineru's Arm"
uid: "J7X"
draft: true
label: "MinArm"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["mulberry", "Squidwest"]
date: "2025-12-07"
description: "Using Super Fuse Overload, the unique equipment used to control Mineru's 'arm' attachement point can be obtained."
aliases: []
tags: ["Equipment", "Zuggle", "Mineru", "Crash"]
---

# Mineru's Arm

## Summary

By completely filling the game's global dependency array, Sages and Sage Avatars can be forced to Overload Drop their equipment. Uniquely of all such equipment, Mineru's "arm" equipment can be picked up and retained.

_Discovered by mulberry; Mainfield route theorized by mulberry, found by Squidwest_

## Instructions

- There are two known routes to obtain Mineru's Arm: the "Ganon" route, which uses the version of Mineru in the Ganondorf battle, and the "Mainfield" route, which uses Mineru's sage avatar.
- The former is best performed with a "Local" SFO method, while the latter only works with a "Persistent" or "Permanent" SFO method.

=== "Ganon Route" ###

    #### Requirements
    ---
    notoc: true
    ---

    - Mineru
    - All the requirements for [Method 2](https://nan-gogh.github.io/ultrabroken-documentation/wiki/BW8/?sfo-nesting-test#method-2-localpurgatory-di) or [Method 3](https://nan-gogh.github.io/ultrabroken-documentation/wiki/BW8/?sfo-nesting-test#method-3-localoverload-cold-fuse) of Super Fuse Overload
    - A few fused equipment items
    - A bucket-shaped Autobuild schematic, ideally with a Hover Stone and one or more Big Batteries (useful for Method 2 and mandatory for Method 3)
    - If on `1.2.0+`, a Portacull Shield or the resources to make one portably via Zuggle Overload
    - If on `1.1.2`, an SDC shield with, some special setup idk. Just update to current, doofus. Learn to live again. It's better than everything except 1.0.0, what are you waiting for.

    #### Collecting Mineru's Arm
    ---
    notoc: true
    ---

    === "Via SFO Method 2" #####

        1. Defeat Ganondorf's Army (and any dungeon bosses not already defeated; best not to take any chances)
        2. Enter the tunnel before Ganondorf's Room
        3. Perform Method 2 of Super Fuse Overload, but Zuggle `C` instead of Zuggle Dropping it (or else it will unhelpfully remain in the tunnel)
        4. Glue together all `G[n]` (or put them in the bucket if available) and Ultrahand it into Ganondorf's Room
        5. Ganondorf should Overload Drop his Gloom Sword in the cutscene, though not seeing this isn't _always_ a failure
        6. Without getting too far from any `G[n]` (they can still distance despawn and must not), Progress the fight to Phase 2 (2nd Form)
        7. One by one, drop fused equipment items until the fuse is deleted from one (this step isn't strictly necessary, but is good insurance)
        8. Once confident that SFO is _fully_ active, proceed to phase 3 (sages blown away) and find Mineru
        9. Dropping from near each of her arms, there should be an undiscovered item. It cannot be collected without a weapon equipped.
        10. Upon collection, a "MsgNotFound" weapon with no icon and 38 damage should be collected. It will respawn immediately, so feel free to take several to be safe
        11. **Inventory pickup** at least several `G[n]` (ideally all of them) to correctly end SFO
        12. _Undock the console._ Fusing to Mineru's Arm while docked crashes the game, which assuredly you do not want
        13. Fuse something to Mineru's Arm; this will give it a model to target with Recall later
        14. Leave the fused Mineru's Arm equipped; this is necessary to Zuggle it

    === "Via SFO Method 3" #####

        1. Defeat Ganondorf's Army (any any dungeon bosses not already defeated; best not to take any chances)
        2. Enter the tunnel before Ganondorf's Room
        3. Perform Method 3 of Super Fuse Overload
        4. After Step 12 of Method 3, drop `A` just after the ledge before Ganondorf's Room (not too close to the doorway), and **equip** the Portacull if already made
        5. Collect all of `B`, `C[n]`, and `D[n]` into the bucket and Ultrahand it into Ganondorf's Room
        6. Ganondorf should Overload Drop his Gloom Sword in the cutscene, though not seeing this isn't always a failure
        7. Without getting too far from the entrance or the bucket (All the parts can still distance despawn and must not), Progress the fight to Phase 2 (2nd Form)
        8. One by one, drop fused equipment items until the fuse is deleted from one (this step isn't strictly necessary, but is good insurance)
        9. Once confident that SFO is _fully_ active, proceed to phase 3 (sages blown away) and find Mineru
        10. Dropping from near each of her arms, there should be an undiscovered item. It cannot be collected without a weapon equipped.
        11. Upon collection, a "MsgNotFound" 2-handed weapon with no icon and 38 damage should be added to the inventory. It will respawn immediately, so feel free to take several to be safe
        12. **Collect** at least several `D[n]` (ideally all of them) to end SFO
        13. _Undock the console._ Fusing to Mineru's Arm while docked crashes the game, which assuredly you do not want
        14. Fuse something to Mineru's Arm; this will give it a model to target with Recall later
        15. Leave the fused Mineru's Arm equipped; this is necessary to Zuggle it

    #### Zuggling Mineru's Arm
    ---
    notoc: true
    ---

    === "Map Zuggle" #####
        ---
        versions: ["1.0.0", "1.1.0", "1.1.1"]
        ---

        Preferred Zuggle method for all working patches.

        1. Hold L to open the ability wheel and select the Map rune
        2. As soon as the wheel closes, use D-Pad Right to open the Weapon Quick Menu (spamming usually works)
        3. Drop Mineru's Arm and reopen the Weapon QM immediately, then equip a droppable weapon (ie not the Master Sword)
        4. Let the Map open, and press + to enter the inventory
        5. Drop the swapped-to weapon and unpause
        6. Mineru's Arm will cause both itself and the swapped-to weapon to fail-drop, so a wall is not needed to Zuggle it

    === "Cull Storage Zuggle" #####
        ---
        versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
        ---

        Though possible on all versions, this Zuggle method is only preferred on `1.1.2`, the awkward middle child that has no other options.

        1. I do not know how to set up cull storage within the bounds of the Ganon Room.
        2. I think Aeroculling works but I don't remember how or if what I got was actually cull storage

        But the gist:

        1. **Pause**
        2. Drop a buffer drop, then an SDC shield with a cull stored
        3. Hold `L`, then **unpause**, so that the ability wheel opens as soon as possible
        4. Select the Map Rune
        5. As soon as the wheel closes, use D-Pad Right to open the Weapon Quick Menu (spamming usually works)
        6. Drop Mineru's Arm and reopen the Weapon QM immediately, then equip a droppable weapon (ie not the Master Sword)
        7. Let the Map open, and press + to enter the inventory
        8. Drop the swapped-to weapon and unpause
        9. Mineru's Arm will cause both itself and the swapped-to weapon to fail-drop, so a wall is not needed to Zuggle it

    === "Swap Resync Zuggle" #####
        ---
        versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
        ---

        Preferred Zuggle Method for all working patches. Steps given include additional buffer drops to widen the timing window.

        1. If a Portacull Shield is not already prepared, create one
        2. **Pause** the game
        3. **Drop** a buffer equipment item
        4. **Drop** the Portacull Shield and **swap** to another shield
        5. **Drop** 2 more buffer items (not the swapped-to shield)
        6. **Drop** Mineru's Arm and **swap** to another droppable weapon (ie not the master Sword)
        7. **Pause Buffer** (unpause and pause again 3 frames later; any faster will eat the input)
        8. **Swap**, **equip**, or **unequip** any armor or bow
        9. **Drop** the swapped-to weapon and **unpause**
        10. Mineru's Arm will cause both itself and the swapped-to weapon to fail-drop, so a wall is not needed to Zuggle it

    #### Retrieving Mineru's Arm
    ---
    notoc: true
    ---

    1. After successfully zuggling Mineru's Arm, load a save. If SFO was fully undone, this will not carry any risk of crashing
    2. Go somewhere you can see a long way down (atop a Hover Stone raised by a Rocket is excellent), and prepare Recall as the active rune
    3. **Drop** an equipped weapon to drop the zuggled Mineru's Arm and _immediately_ open Recall
    4. **Recall** the material fused to Mineru's Arm
    5. **Equip** any weapon and **collect** Mineru's Arm (it was reverted to being undiscovered)
    6. If intending to use Mineru's Arm as a fail-drop wall, destroy the fuse (fail-dropping a fused Mineru's Arm while docked crashes the game)
    7. Save the game or get an autosave to lock in your prize

    #### Video Resources
    ---
    notoc: true
    ---

    ??? tip "Retrieving Fused+Zuggled Mineru's Arm"

        placeholder

=== "Mainfield Route" ###

    #### Requirements
    ---
    notoc: true
    ---

    - Mineru
    - All the requirements for [Method 1](uid:BW8#method-1-persistentpurgatory-overload-batch-di) or [Method 4](uid:BW8#method-4-permanentoverload-cold-fuse-permacull) of Super Fuse Overload
    - The warp-point for Mogisari Shrine at the Lomei Sky Labyrinth. Other low-gravity zones may work, but are untested for stability during SFO.

    #### Preparing SFO
    ---
    notoc: true
    ---

    === "Via SFO Method 1" #####

        1. Ensure Mineru is summoned; this will save some headache later
        2. Enter Rasitakiwak Shrine and dispose of _all_ the constructs and their weapons
        3. (most shrines work, so long as there are no enemies and enough room to work)
        4. Perform Method 1 of Super Fuse Overload
        5. Equip extra equipment via the D-Pad menus (with fuses on weapon and/or shield if needed) until SFO is _fully_ active
        6. This can be proven by attempting to nock an arrow; it should appear but remain where the quiver was when ZR was pressed. If it attaches correctly or doesn't appear at all, SFO is not reached.

    === "Via SFO Method 4" #####

        1. Ensure Mineru is summoned; this will save some headache later
        2. Perform Method 4 of Super Fuse Overload within the selected shrine
        3. After completing SFO, re-equip the Aerophasing parent equipment to prevent its fuses from unloading
        4. Equip extra equipment via the D-Pad menus, with a fuse on the non-aerophasing base type if needed, until SFO is _fully_ active
        5. This can be proven by attempting to nock an arrow; it should appear but remain where the quiver was when ZR was pressed. If it attaches to the bow or doesn't appear at all, SFO is not reached.

    #### Collecting Mineru's Arm
    ---
    notoc: true
    ---

    1. Equip a weapon and ensure there is space in your weapon pouch
    2. Warp to Mogisari Shrine
    3. As soon as you gain control, walk in a small clockwise circle while spamming A (see "Mainfield Mineru's Arm Route" resource below)
    4. Execution permitting, you will pick up a new 2-handed weapon, dealing 38 damage (as listed in the menu), which has no icon, description, model, or collision, and is called MsgNotFound
    5. If unsuccessful, stand about halfway between the shrine's warp point and its left/east "Dragon pillar", and spam A between Panic Blood Moons (see "Mainfield Route Backup Strat" resource below)
    6. If Mineru was not summoned in advance, simply summon her after the warp (and optionally warp again to get a go at the primary strat)
    7. About 3 seconds after control is gained, a panic blood moon will occur, which will _usually_ give an autosave. Further PBMs will occur much sooner than the first, and are unlikely to provide an autosave
    8. Make a hard save if desired, then close the game to clear SFO if desired

    #### Video Resources
    ---
    notoc: true
    ---

    ??? tip "Mainfield Route Primary Strat"

        placeholder


    ??? tip "Mainfield Route Backup Strat"

        placeholder

## Notes

### Properties

#### As a weapon:
---
notoc: true
---

- Mineru's Arm is a 40 damage, 40 durability 2-handed weapon with no model, collision, name, or description.
- It can be guarded with, even if it does not have a shield fused to it.
- It can be fused to, but doing so can crash the game (see below).
- Though there is a seperate Left and Right arm, picking up either adds the Left arm to the pouch.

#### Crashing:
---
notoc: true
---

- If the game attempts to generate an icon for a fused Mineru's Arm while running in Docked Mode, the game will crash.
- This happens both on the initial fuse, and when picking up or fail-dropping a fused arm.
- By having another fused item generate an icon just before Mineru's Arm does, it will inherit a corrupted version of the first item's icon. This prevents the game crash above.

#### As a tool:
---
notoc: true
---

- While standing on the ground, or in certain (very limited) airborne circumstances, Mineru's Arm will always fail-drop.
- This also causes anything later than it in the drop queue to fail-drop as well.
- Thus, Mineru's Arm can be used as a portable wall whenever _nearly any_ glitch requires a fail-drop to occur at some moment.

### Credits

- Mineru's Arm ganon route found by mulberry - Dec 07th, 2025
- Mineru's Arm mainfield route found by Squidwest - Mar 18th, 2026

### Resources

??? quote "Discord Resources"

    - [Original Mineru's Arm Get](https://discord.com/channels/1086729144307564648/1110956205624532993/1447304812197838930)
    - [Mainfield Mineru's Arm Route](https://discord.com/channels/1086729144307564648/1113557914444111873/1484238374909902868)
    - [Mainfield Route Backup Method](https://discord.com/channels/1086729144307564648/1110956205624532993/1510038404178383040)

### Related
- [Zuggle Overload](search:Zuggle Overload)
- [Despawn Interrupt](search:Despawn Interrupt)
- [Fuse Entanglement](search:Fuse Entanglement)

### page todos ?
---
notoc: true
---

- embed important clips instead of just linking to them
- do CSZ to figure out how best to do it in ganons loser cave
- format mainfield route section better, it's messy
