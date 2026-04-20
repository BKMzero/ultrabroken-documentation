---
title: "Despawn Interrupt"
uid: "MG1"
label: "DI"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["mulberry", "Squidwest"]
date: "2026-01-16"
description: "A similar glitch to void dipping that has additional properties and is done with a molduga or frox."
aliases: ["despawn-interrupt", "eaten di", "frox dipping", "frox dip", "duga dipping", "duga dip"]
tags: ["item", "zuggling", "fuse", "despawn"]
---

# Despawn Interrupt

## Summary
A similar glitch to void dipping that has additional properties and is done with a molduga or frox.

_Discovered by mulberry; optimizations by Aergyl, Kleric, mulberry, Squidwest - 16 January 2026_

## Instructions

The general form of every method is as follows:

- Allow a Frox or Molduga to eat the target (almost always equipment)
- After the target begins to fade from existence, but before it fully despawns, cull it
- Usually, some final step is required to obtain a normally-equipped and independent DI item

Due to their differing attack patterns, the detailed instructions below will be partitioned by their choice of monster. Furthermore, due to the massive number of workable methods, only 4 of the most practical will be provided for each monster.

=== "Frox Methods" ###

    - Froxen are more abundant across Hyrule, but it can be harder to time DI with their attacks.

    #### Method 1: Overload + Portacull Mitosis ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses a Portacull to both cull the target and to safely swap off it without destroying it.
    - The steps given use the Frox's overhead attack for convenience, but it will work with any attack that has it open its mouth.

    Prepare:

    - Enough Zuggle Overload to Overload Drop the target
    - The target
    - A portacull of the opposite type of the target
    - A Frox

    Steps:

    1. Fall towards the Frox from above, and paraglide at the right height so that it opens its mouth but does not leap.
    2. Overload Drop the target so that it will fall in the Frox's mouth.
    3. As soon as the target visibly begins to despawn (which will happen at a consistent distance away from the Frox's mouth), pause the game.
    4. Drop the Portacull, swap to another item of that type, and swap to another item of the target's type.
    5. Unpause the game. If desired, the portacull can be saved by immediately entering bullet time, unequipping what was swapped to, and picking the portacull up.
    6. Assuming the timing window was hit correctly, the target will be DI'd and left on the ground somewhere nearish to the Frox. An ordinary duplicate of the target will also be left in the inventory due to the mitosis.
    7. Due to the darkness of the depths, it can be very beneficial to fuse something luminous to the target first. The fused item won't always survive the DI process, but when it does it makes tracking the target down much easier.

    #### Method 2: Overload + Portacull + Overload Drop Zuggle ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method is a variant of Method 1, Drop Zuggling the target to allow it to be used for the production of DI Ghosts more quickly.
    - Once the target is Drop Zuggled, it can only be removed by destruction.
    - The steps given use the Frox's overhead attack for convenience, but it will work with any attack that has it open its mouth.
    
    Prepare:

    - Enough Zuggle Overload to Overload Drop the target
    - The target (A)
    - A portacull of the opposite type of the target
    - A Frox

    Steps:

    1. Fall towards the Frox from above, and paraglide at the right height so that it opens its mouth but does not leap.
    2. Overload Drop A so that it will fall in the Frox's mouth.
    3. As soon as A visibly begins to despawn, **pause** the game. The fadeout is too short to pause on reaction, but it can be caught with pause buffering, and always happens at the same distance from the Frox's mouth.
    4. Drop the Portacull, swap to another item of that type.
    5. Unpause the game. If desired, the portacull can be saved by immediately entering bullet time, unequipping what was swapped to, and picking the portacull up.
    6. Assuming the timing window was hit correctly, A will be DI'd and left on the ground somewhere nearish to the Frox, while still being equipped.
    7. **Pause** the game, then **drop** A, **swap** to another of that type, and **unequip it**.
    8. **Unpause** the game and **Pick up** A. It will be drop equipped.
    9. **Pause** the game and swap to another of A's type, then unpause the game. It will now be drop smuggled, and can be used to create DI Ghosts as-is.
    10. If desired, A can be taken through warps and loads by fail-dropping an equipped item of A's type, converting the drop smuggle into a drop zuggle.

    #### Method 3: FE ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method gives the target an FE parent shield and uses "Drop-Swap Culling" to cull the parent and thus the target.
    - Alternately, a weapon can be used as the FE parent. However, detangling the target from it will not be possible, so it will not be especially portable.
    - The steps given use the Frox's overhead attack for convenience, but it will work with any attack that has it open its mouth.

    Prepare:

    - A shield
    - The target (A)
    - A Frox

    Steps:

    1. FE A to a shield (B). Equip both A and B (if A is a shield, it can be carried to the frox with Ultrahand or a vehicle).
    2. Fall towards the frox from above, and paraglide at the right height so that it opens its mouth but does not leap.
    3. Drop A so that it will fall in the Frox's mouth.
    4. As soon as A visibly begins to despawn, **pause** the game. The fadeout is too short to pause on reaction, but it can be caught with pause buffering, and always happens at the same distance from the Frox's mouth.
    4. Drop B, swap to another shield, and unequip that shield.
    5. Unpause the game and immediately enter bullet time. Use the bow aim to turn around and **pick up** B to prevent the Frox from eating it and destroying A.
    6. Assuming the timing window was hit correctly, A will be DI'd and left on the ground somewhere nearish to the Frox.
    7. Find and pick up A, or else carry it away with Ultrahand if it is a shield.
    8. If desired, use Octo Detanglement to detangle A from B, allowing it to be taken elsewhere.

    #### Method 4: Mineru Limbo ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses Mineru FE to make the target cull with Mineru, then uses Mineru Limbo to allow her to be rapidly culled and unculled, essentially guaranteeing the timing window will be hit.
    - It's reasonably consistent, but becomes nearly certain when used with a Molduga (see Method 5).

    Prepare:

    - The target (A)
    - Mineru
    - A Frox
    - Like a stake and/or some other crap I don't know how to limbo mineru consistently

    Steps:

    1. Mineru FE A and pick it up.
    2. Go a little ways outside the Frox's range, so that it only does its' suction attack
    3. Create the aforementioned build involving a stake to place Mineru into "Limbo" (A unculled, but Mineru invisible).
    4. Drop the target so that the Frox eats it, and jump repeatedly to cull A over and over.
    5. If done correctly, A will survive being eaten and can be collected at will
    6. If desired, detangle A from Mineru by fusing something else to that slot.

=== "Molduga Methods" ###

    - Moldugae are found on the surface of Gerudo Desert only, but their lunge attack is highly predictable and easy to time around.
    - Sometimes known as Duga Dipping.

    #### Method 5: Mineru Limbo ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses Mineru FE to cause the target to cull when Mineru does, then uses Mineru Limbo to cause her to cull the instant the molduga lunges, causing a nearly-guaranteed DI.
    - Usually the most consistent DI method of all.
    - Up to 3 targets can be DI'd at once with this method.
    - After DI, the target retains an FE connection to Mineru, allowing her to be used as the culling source for Ghost DI (most useful on `1.1.2` and below).

    Prepare:

    - Mineru
    - The target
    - A steering stick, ideally several in case of mishap
    - A tall wall (such as those around Siwakama Shrine), or two springs to create a wall
    - A Molduga

    Steps:

    1. Mineru FE the target (almost always a weapon or shield) and pick it up.
    2. Place the steering stick close to a wall near a Molduga.
    3. To create a wall portably. perform a neutral jump on level ground, **pause** at the peak, and deploy 2 springs and a steering stick in that order. The springs will spawn stacked, with the stick at their right.
    4. Mount and dismount the steering stick. 
    5. If the target appears on Link's back, but Mineru does not appear, she is in Limbo; Proceed to Step 6. If not, repeat step 4.
    6. Drop the target.
    7. Allow the Molduga to perform its lunge attack, eating Link, the steering stick, and the target all in one.
    8. Check if the target was DI'd. Due to the whims of the Sage of Spirit, the target will very occasionally be unchanged or completely destroyed. If needed, try again from step 2 or 1 respectively.
    9. Before dismissing Mineru, detangle the target from her by fusing something else to the same part.

    #### Method 6: FE ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method gives the target an FE parent shield and uses "Drop-Swap Culling" to cull the parent and thus the target.
    - Alternately, a weapon can be used as the FE parent. However, detangling the target from it will not be possible, so it will not be especially portable.

    Prepare:

    - A shield
    - The target
    - A Molduga

    Steps:

    1. FE the target to a shield.
    2. Stand somewhere the Molduga cannot hear Link, and drop the target onto the sand so that the Molduga notices it.
    3. Shortly after its detection symbol becomes a yellow !, it will lunge and eat the target. Use pause buffering to pause any time between frame 2 and frame 7 (inclusive) of this lunge.
    4. If, behind the pause menu, the Molduga is just starting to emerge from the sand, the timing is likely correct.
    5. Drop the target's parent and swap to another of that type, then unpause.
    6. If the pause occured during the DI window, the target will still exist after the molduga has passed, and it will no longer be interactible with runes.
    7. If desired, use Octo Detanglement to detangle the target from the shield, allowing it to be taken elsewhere.

    #### Method 7: Turbo FE ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method builds on Method 5 by using Octo Detanglement concurrently with the drop-swap that causes DI, instantly creating a detangled DI item.

    Prepare:

    - A shield
    - A second shield with an Octo Balloon fused to it
    - The target
    - A Molduga

    Steps:

    1. FE the target to a shield and equip that shield.
    2. Stand somewhere the Molduga cannot hear Link, and Ultrahand the target onto the sand so that the Molduga notices it.
    3. Unsheathe the shield and guard with it.
    3. Shortly after its detection symbol becomes a yellow !, it will lunge and eat the target. Use pause buffering to pause any time between frame 2 and frame 7 (inclusive) of this lunge.
    4. If, behind the pause menu, the Molduga is just starting to emerge from the sand, the timing is likely correct.
    5. Drop the parent shield and swap to the Octo Balloon Shield, then unpause and press **Cancel** (B/X) very shortly after to cancel the Octo Balloon flight.
    6. If the pause occured during the DI window, the target will still exist after the molduga has passed, and it will no longer be interactible with runes.

    #### Method 8: Overload + Portacull Mitosis ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses a Portacull to both cull the target and to safely swap off it without destroying it.

    Prepare:

    - Enough Zuggle Overload to Overload Drop the target
    - The target (A)
    - A portacull of the opposite type of the target
    - A Molduga

    Steps:

    1. Overload Drop or Overload Pickup A.
    2. Stand somewhere the Molduga cannot hear Link, and Ultrahand A onto the sand so that the Molduga notices it.
    3. Shortly after its detection symbol becomes a yellow !, it will lunge and eat A. Use pause buffering to pause any time between frame 2 and frame 7 (inclusive) of this lunge.
    4. If, behind the pause menu, the Molduga is just starting to emerge from the sand, the timing is likely correct.
    5. Drop the Portacull and swap to another item of that type, then swap to another item of A's type.
    6. If the pause occured during the DI window, A will still exist after the Molduga has passed, and it will no longer be interactible with runes.

=== "Other Methods" ###

    These methods are typically not used, but are functional, and to be quite honest I'm tired and don't want to figure out whether they need to be removed, and I'll get at it tomorrow.

    Yeah they came with the page sorry. I'm working on it please be patient

    ### Method 1 (1.2+, setupless frox setup) ?
    
    1. Approach a frox and wait until it is about to do a swallow attack.
    This is done most easily if you have a travel medallion directly next to the frox
    2. Put your target item between you and the frox and target it with fuse
    3. Right before the frox swallows the target, fuse it to a piece of equipment, preferably a shield
    4. **Quickly pause the game**
    5. *Drop the equipment you fused to, equip another item of the same type, then unequip*
    6. **Unpause the game**
    7. Pick up the dropped equipment and run away from the frox
    8. If done correctly, the fused item will now be in a despawn interrupted state and ghosted
    9. If you wish, detangle the fused item from its base. 

    This is easiest if the item you fused to was a shield

    ### Method 2 (1.2+, easier molduga setup) ?
    
    1. FE your target to a shield
    2. Drop your item near a molduga so that the molduga notices it
    3. Right after the molduga begins to jump, drop the fuse entangled shield, equip another shield, and unequip it
    4. Pick it up and retrive the target
    5. If you wish, detangle it from the base shield

    ### Method 3 (1.0-1.1.2, older versions molduga setup) >
    
    1. FE your target to Mineru
    2. Place the target near a molduga so the molduga notices it
    3. Climb so that mineru culls right after the molduga jumps out of the sand
    4. Retrive you target and if you wish, detangle it from mineru

    ### Setup for DI ghosts
    DI can propagate to other pieces of equipment, by making a DI ghost. Here are methods to do so:

    #### Method 1 (1.2+)
    1. Smuggle the DI equipment (Drop it, equip another item of the same type, and then unequip that item)
    2. Equip an item of the same type
    3. Fuse the thing you want to put in the DI state to the thing you just equipped
    4. Quickly after fusing, a couple frames after the FE frame, drop the fuse base, equip another item of the same type, and unequip it
    5. If you wish to detangle from the normal parent, you may distance despawn it or use octo detanglement.
    The distance method should be done before detangling from the DI parent
    6. If you want to detantangle from the DI parent, you may simply smuggle it, equip an item of the same type, and then fuse to that item

    #### Method 2 (1.0-1.1.2)
    1. Smuggle the DI equipment using the same drop swap unequip method
    2. FE an item of the same type to mineru and pick it up
    3. Fuse the thing you want to DI right before mineru culls
    4. Drop the item that you fuse entangled to mineru
    5. Same rules for detanglement apply

## Notes
- Also known as "Eaten DI". Often referred to as "Frox Dipping" or as "Duga Dipping".
- ALthough void dipping is also technically a form of despawn interrupt, DI and despawn interrupt refers to the eaten variation by convention.

## Resources
- [Spreadsheet link](https://docs.google.com/spreadsheets/d/1xNB1gOLZRSF9yp1mHUsS9ymogRJa1Wz8rTliTXezeRM/edit?pli=1&hl=de&gid=0#gid=0&range=294:294)
- [Original discovery](https://discordapp.com/channels/1086729144307564648/1110956205624532993/1461889160062173416)
- [Molduga optimization](https://discordapp.com/channels/1111875355758837830/1128775917376897145/1466939998023450796)
- [Link's Luxury Loadout](https://www.youtube.com/watch?v=kQuj0LBQdrM)

## Related
- [Fuse Entanglement](search:Fuse Entanglement)
- [Detanglement](search:Detanglement)
