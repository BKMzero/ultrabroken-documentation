---
title: "Despawn Interrupt"
uid: "MG1"
label: "DI"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["Aergyl", "Jordan", "Kleric", "mulberry", "ofstrings2", "Squidwest", "suusi"]
date: "2024-06-16"
description: "A similar glitch to Void Dipping that has additional properties and is done with a Frox, Molduga, or Like Like."
aliases: ["despawn-interrupt", "eaten di", "frox dipping", "frox dip", "duga dipping", "duga dip"]
tags: ["item", "zuggling", "fuse", "despawn"]
---

# Despawn Interrupt

## Summary

A similar glitch to Void Dipping that has additional properties and is done with a Frox, Molduga, or Like Like.

### Explanation

When something is eaten by a Like Like (objects only), or a Frox/Molduga (objects or equipment), it is given the "Eaten" death reason, which promptly calls "RequestFadeOutDelete" as part of the death procedure.

If this fadeout is interrupted by culling the object (which pauses all active alpha fades), the death procedure is halted indefinitely, allowing the numerous properties of the Eaten state to be accessed.

_Like Like DI discovered by mulberry - June 16th, 2024_

_Frox DI discovered by mulberry - January 16th, 2026_

_Duga Dipping discovered by Squidwest - January 30th, 2026_

_Additional credits below each method_

## Instructions

The general form of every method is as follows:

- Allow a hungry monster to eat an eligible target
- After the target begins to fade from existence, but before it fully despawns, cull it
- If the target is equipment, some final step is usually required to obtain a normally-equipped and independent DI item

Due to their differing attack patterns, the detailed instructions below will be partitioned by their choice of monster. Furthermore, due to the large number of workable methods, only 4 of the most practical will be provided for each monster. The remainder are collected in the "Other Methods" tab.

=== "Frox Methods" ###

    - Froxen are abundant across Hyrule's Depths, but it can be hard to time DI with their attacks.

    #### Method 1: Overload + Portacull Mitosis ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses a Portacull to both cull an equipment target and to safely swap off it without destroying it.
    - The steps given use the Frox's overhead attack for convenience, but it will work with any attack that has it open its mouth.

    Prepare:

    - Enough Zuggle Overload to [Overload Drop](uid:8QH) the target
    - A target weapon, shield, or bow
    - A portacull of a different type than the target's type
    - A Frox

    Steps:

    1. Fall towards the Frox from above, and paraglide at the right height so that it opens its mouth but does not leap.
    2. **Overload Drop** the target so that it will fall in the Frox's mouth.
    3. As soon as the target visibly begins to despawn, **pause** the game. The fadeout is too short to pause on reaction, but it can be caught with pause buffering, and always happens at the same distance from the Frox's mouth.
    4. **Drop** the Portacull, **swap** to another item of that type, and **swap** to another item of the target's type.
    5. **Unpause** the game. If desired, the portacull can be saved by immediately entering bullet time, **unequipping** what was swapped to, and **picking up** the portacull.
    6. Assuming the timing window was hit correctly, the target will be DI'd and left on the ground somewhere nearish to the Frox. An ordinary duplicate of the target will also be left in the inventory due to the mitosis.
    7. Due to the darkness of the depths, it can be very beneficial to **fuse** something luminous to the target first. The fused item won't always survive the DI process, but when it does it makes tracking the target down much easier.

    _Discovered by Jordan, mulberry - Jan 19th, 2026_

    #### Method 2: Overload + Portacull + Overload Drop Zuggle ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method is a variant of Method 1, [Drop Zuggling](uid:0YL) the target to allow it to be used for the production of [DI Ghosts](uid:BEW) more quickly.
    - Once the target is Drop Zuggled, it can only be removed by destruction.
    - The steps given use the Frox's overhead attack for convenience, but it will work with any attack that has it open its mouth.
    
    Prepare:

    - Enough Zuggle Overload to [Overload Drop](uid:8QH) the target
    - A target weapon, shield, or bow
    - A portacull of a different type than the target's type
    - A Frox

    Steps:

    1. Fall towards the Frox from above, and paraglide at the right height so that it opens its mouth but does not leap.
    2. **Overload Drop** the target so that it will fall in the Frox's mouth.
    3. As soon as the target visibly begins to despawn, **pause** the game. The fadeout is too short to pause on reaction, but it can be caught with pause buffering, and always happens at the same distance from the Frox's mouth.
    4. **Drop** the Portacull, then **swap** to another item of that type.
    5. **Unpause** the game. If desired, the portacull can be saved by immediately entering bullet time, **unequipping** what was swapped to, and **picking up** the portacull.
    6. Assuming the timing window was hit correctly, the target will be DI'd and left on the ground somewhere nearish to the Frox, while still being equipped.
    7. **Pause** the game, then **drop** the target, **swap** to another of that type, and **unequip it**.
    8. **Unpause** the game and **Pick up** the target. It will be drop equipped.
    9. **Pause** the game and swap to another of the target's type, then unpause the game. It will now be drop smuggled, and can be used to create **DI Ghosts** as-is.
    10. If desired, the target can be taken through warps and loads by dropping or fail-dropping a warm-equipped item of the target's type, converting the drop smuggle into a drop zuggle.

    _Discovered by mulberry, Suusi - Jan 19th, 2026_

    #### Method 3: Fuse Entanglement ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method gives the target an FE parent shield and uses "Drop-Swap Culling" to cull the parent and thus the target.
    - Alternately, a weapon can be used as the FE parent. However, detangling the target from it will not be possible, so it will not be especially portable.
    - The steps given use the Frox's vaccuum attack for timing convenience, but it will work with any attack that has it open its mouth.

    Prepare:

    - A shield
    - The target (A)
    - A Frox

    Steps:

    1. **FE** A to a shield (B). **Equip** both A and B (if A and B are the same type, A can be carried to the frox with Ultrahand or a vehicle).
    2. Approach a Frox and wait until it is about to do a vaccuum attack. This is nearly always the first attack it does, and is also the only attack it will do when Link is slightly outside its territory
    3. **Ultrahand** the target in front of the Frox's mouth, at a distance where it will cancel Ultrahand from the target's end before Link gets pulled in
    4. As soon as Ultrahand is cancelled by the target beginning to despawn, **pause** the game. The timing window can be caught with pause buffering if desired.
    5. **Drop** B, **swap** to another shield, and **unequip** that shield.
    6. **Unpause** the game and immediately **pick up** B before it gets eaten and destroys A with it
    7. Assuming the timing window was hit correctly, A will be DI'd and left on the ground somewhere nearish to the Frox.
    8. Find and **pick up** A. If neccessary, drop B and carry it away with Ultrahand.
    9. If desired, use Octo Detanglement to detangle A from B, allowing it to be properly zuggled and taken elsewhere.

    _Discovered by mulberry - Jan 16th, 2026_

    _Optimizations by mulberry, Squidwest - Jan 17th, 2026_

    #### Method 4: Mineru Limbo ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses Mineru FE to make the target cull with Mineru, then uses Mineru Limbo to allow her to be rapidly culled and unculled via jumping, causing the timing window to almost always be hit.
    - It's reasonably consistent, but becomes nearly certain when used with a Molduga (see Method 5).
    - Up to 3 targets can be DI'd at once with this method.
    - After DI, the target retains an FE connection to Mineru, allowing her to be used as the culling source for [Ghost DI](uid:BEW) (most useful on `1.1.2` and below, and for batch DI on all versions).

    Prepare:

    - The target
    - Mineru
    - A Frox
    - Either a stake and a spring, 3 stakes, or another build which can force Mineru into the Limbo state
    - The discord references below will be very helpful

    Steps:

    1. **Mineru FE** the target
    2. Go a little ways outside the Frox's range, so that it only does its' suction attack
    3. Create the aforementioned build involving a stake to place Mineru into "Limbo" (the target unculled, but Mineru invisible).
    4. **Drop** the target so that the Frox eats it, and **jump** repeatedly to cull the target over and over.
    5. If done correctly, the target will survive being eaten and can be collected at will
    6. If desired, detangle the target from Mineru by fusing something else to the target's slot.

    _Discovered by Kleric - Jan 17th, 2026_

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
    - After DI, the target retains an FE connection to Mineru, allowing her to be used as the culling source for [Ghost DI](uid:BEW) (most useful on `1.1.2` and below, and for Batch DI on all versions).

    Prepare:

    - Mineru
    - The target
    - A Steering Stick, ideally several in case of mishap
    - A tall wall (such as those around Siwakama Shrine), or two Springs to create a wall
    - A Molduga

    Steps:

    1. **Mineru FE** the target (almost always a weapon or shield) and pick it up.
    2. Place the Steering Stick close to a wall and somewhere a Molduga can attack.
    3. To create a Limbo wall portably: Perform a **neutral jump** on level ground, **pause** at the peak, and deploy 2 Springs and a Steering Stick in that order. The Springs will spawn stacked, with the Steering Stick to their right.
    4. **Mount** and **dismount** the Steering Stick. 
    5. If the target appears on Link's back, but Mineru does not appear, she is in Limbo; Proceed to Step 6. If not, repeat step 4.
    6. **Drop** the target and whistle the Molduga over if it hasn't already noticed Link.
    7. Allow the Molduga to perform its lunge attack, eating Link, the Steering Stick, the Springs (if present), and the target all in one.
    8. Check if the target was DI'd. Due to the whims of the Sage of Spirit, the target will rarely be unchanged or completely destroyed (usually the former). If needed, try again from step 2 or 1 respectively.
    9. If desired, detangle the target from Mineru by fusing something else to the target's slot.

    _Spring Stack Wall Method discovered by mulberry - Mar 13th, 2026_
    _Siwakama Wall Method discovered by Squidwest - Late Mar 2026_

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

    1. **FE** the target to a shield and equip that shield.
    2. Stand somewhere the Molduga cannot hear Link, and **drop** the target onto the sand so that the Molduga notices it.
    3. Shortly after its detection symbol becomes a yellow !, it will lunge and eat the target. Use pause buffering to **pause** any time between **frame 2** and **frame 7** (inclusive) of this lunge.
    4. If, behind the pause menu, the Molduga is just starting to emerge from the sand, the timing is likely correct.
    5. **Drop** the target's parent, **swap** to another of that type, and **unequip** what was swapped to.
    6. **Unpause**. If the pause occured during the DI window, the target will still exist after the molduga has passed, and it will no longer be interactible with runes.
    7. To allow the target to be safely zuggled and taken elsewhere, use Octo Detanglement to detangle the target from the parent shield.

    _Discovered by Squidwest - Jan 30th, 2026_

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

    1. **FE** the target to a shield and **equip** that shield.
    2. Stand somewhere the Molduga cannot hear Link, and **drop** the target onto the sand so that the Molduga notices it.
    3. **Unsheathe** the shield and **guard** with it.
    4. Shortly after its detection symbol becomes a yellow !, it will lunge and eat the target. Use pause buffering to **pause** any time between **frame 2** and **frame 7** (inclusive) of this lunge.
    5. If, behind the pause menu, the Molduga is just starting to emerge from the sand, the timing is likely correct.
    6. **Drop** the parent shield and **swap** to the Octo Balloon Shield, then **unpause** and press **Cancel** (B/X) very shortly after to cancel the Octo Balloon flight.
    7. If the pause occured during the DI window, the target will still exist after the molduga has passed, and it will no longer be interactible with runes.
    8. If the Octo Balloon flight was cancelled on the correct frame, the shield will no longer be a parent of the target.

    _Turbo detanglement discovered by Aergyl - Jan 31st, 2026_

    #### Method 8: Overload + Portacull Mitosis ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses a Portacull to both cull the target and to safely swap off it without destroying it.
    - Unlike Method 1, this version is a good option to DI an existing item (such as UB equipment), due to the ability to more or less choose when the Molduga attacks.

    Prepare:

    - Enough Zuggle Overload to [Overload Drop](uid:8QH) the target
    - A target weapon, shield, or bow
    - A portacull of a different type than the target's type
    - A Molduga

    Steps:

    1. **Overload Drop** or **Overload Pickup** the target.
    2. Stand somewhere the Molduga cannot hear Link, and **Ultrahand** the target onto the sand so that the Molduga notices it.
    3. Shortly after its detection symbol becomes a yellow !, it will lunge and eat the target. Use pause buffering to **pause** any time between **frame 2** and **frame 7** (inclusive) of this lunge.
    4. If, behind the pause menu, the Molduga is just starting to emerge from the sand, the timing is likely correct.
    5. Drop the Portacull and swap to another item of that type, then swap to another item of the target's type.
    6. If the pause occured during the DI window, the target will still exist after the Molduga has passed, and it will no longer be interactible with runes.

    _Discovered by Jordan - Feb 02nd, 2026_

=== "Like Like Methods" ###

    - Like Likes are the most abundant hungry monster, and can even cull the target automatically, but are unable to DI equipment.
    - In turn, this entirely prevents access to portable DI, Gen 2 DI, and DI equipment by these methods.
    - Due to these limitations, Like Like DI has mostly been explored for the creation of an Infinite Pocket Rocket.

    #### Method 9: Parent Feeding ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    ---
    
    - This method feeds the FE parent of the target to the Like Like at the same time as the target itself, automatically culling it within the DI window.
    - Optionally, Fuse Storage may be performed simultaneously, allowing for a Fuse or Pseudo Fuse parent to be created at the same time as the DI is performed.

    Steps for DI:

    1. Fuse Entangle the target to a weapon or shield
    2. Glue the target and a bomb flower (or other explosive) to the parent, and place them near the edge of the Like Like's attack range (at this distance to ensure everything gets eaten at the same time)
    3. If performing Fuse Storage, shake the target free to allow it to be fused
    4. When the Like Like eats the trio of objects, DI will occur automatically, and the parent+target will be unculled when the Bomb Flower detonates

    Getting Fuse Storage & converting to PF:
    
    1. 1-2 frames before the Like Like eats the three objects, input a Fuse (ZL/Y) on the target
    2. Due to the target culling with its existing parent, Fuse will be stored
    3. To convert the stored fuse to PF, target any Replacement Actor (such as a Bomb Flower) with Fuse (do not actually initiate fusion)
    4. When the bomb detonates and unculls the target, either Fuse or Pseudo Fuse will be performed on the parent used to perform Fuse Storage

    #### Method 10: Drop-Swap Culling ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    ---

    - This method uses "Drop-Swap Culling" to cull the target.
    - Compared to Method 9, it requires manual timing, but is both faster and cheaper.
    - A fuse can still be stored, but getting both DI and Fuse/PF is frame-perfect.

    Steps for DI:

    1. Fuse Entangle the target to a weapon or shield
    2. Place the target near the edge of the Like Like's attack range
    3. 2-7 frames after the target is eaten and begins to despawn, **pause** the game
    4. **Drop** the parent and **swap** to another item of its type (you may **unequip** or **drop** the swapped-to item if desired)
    5. When the game is unpaused, the target will be DI'd

    Getting Fuse Storage & converting to PF:

    1. On the first frame after the target is eaten (the last frame before Fuse is disabled), input a Fuse (ZL/Y) on the target
    2. Due to the target beginning to fade out the next frame, fuse will be stored
    3. Before the target fully fades out, but after D-Pad Lock ends, **pause** the game
    4. For full fuse, simply **Drop-Swap** the existing parent as above, leaving the fuse-stored parent equipped
    5. For Pseudo Fuse, **Drop** the fuse-stored parent, _then_ **Drop-Swap** the existing parent

=== "Other Methods" ###

    - These methods are fully functional, but usually seen as less practical due to tighter timing windows, lower consistency, or both.
    - Some of them offer unique benefits, such as extreme minimalism or speed, while others are included only for archival purposes.
    
    #### Method 11: Direct Fusion ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    notoc: true
    obsolete: false
    ---

    - This method fuses the target to a shield _after_ the despawn begins, and then uses Drop-Swap Culling to interrupt the despawn.
    - It thus requires no advance setup whatsoever. However, it is precise in positioning and requires a frame-perfect Fuse input.
    - The target will be created in the "Gen 1" [Ghost DI](uid:BEW) state (no collision or gravity, but does not auto-PSLOT like a "Gen 2" DI Ghost).

    Prepare:

    - A Shield (A weapon may be used but can't easily be detangled from)
    - The target
    - A Frox or Molduga

    === "Steps (Frox)" #####

        1. Approach a Frox and wait until it is about to do a vaccuum attack. This is nearly always the first attack it does, and is also the only attack it will do when Link is slightly outside its territory
        2. Put your target item between you and the Frox and **highlight** it with Fuse
        3. On the first frame of the target despawning due to being eaten, **fuse** it to the shield and **pause** the game _immediately_
        4. If the pause was especially fast, D-Pad Lock will be active. If it is, either perform a pause-buffer (must be nearly optimal), or watch memories until D-Pad Lock ends
        5. **Drop** the shield, **swap** to another shield, and **unequip** that shield
        6. **Unpause** the game and pick up the shield. If it was successfully DI'd, it will not be interactible with runes
        7. Leave the area to avoid further Frox attacks
        8. **Detangle** the target from its parent. This will both restore the pickup prompt and prevent the parent shield from reparing/destroying the target

    === "Steps (Molduga)" #####

        1. Gently place the target upon the sand, as far from Link as possible while still being in Fuse range
        2. Cause a noise on the opposite side of the target from Link, as far as possible while still leaving the target in the zone-to-be-attacked
        3. These steps serve to allow the target to be eaten at the very edge of the Molduga's bite, keeping Link out of the line of fire (you will not be able to cull the target if you are hit)
        4. On the first frame after the target is eaten (the last frame before Fuse is disabled), Fuse the target to the shield
        5. 1-6 frames after fusing, **pause** the game
        6. **Drop** the shield, **swap** to another shield, and **unequip** that shield
        7. **Unpause** the game and pick up the shield. If it was successfully DI'd, it will not be interactible with runes
        8. Leave the area or find high ground to avoid further Molduga attacks
        9. **Detangle** the target from its parent. This will both restore the pickup prompt and prevent the parent shield from reparing/destroying the target

    _Discovered by mulberry - Jan 17th, 2026_

    #### Method 12: Pickup + Portacull ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    notoc: true
    obsolete: false
    ---

    - This method has Link pick up the target _after_ the despawn begins, allowing it to cull with him via a Portacull.
    - It does not require any other setup besides the Portacull. However, it is precise in positioning and requires a frame-perfect pickup input.
    - Unlike Method 11, the target will be created in the ordinary DI state, retaining its gravity and collision.

    Prepare:

    - A portacull of the opposite type as the target
    - The target
    - A Frox or Molduga

    === "Steps (Frox)" #####

        1. Approach a Frox and wait until it is about to do a vaccuum attack. This is nearly always the first attack it does, and is also the only attack it will do when Link is slightly outside its territory
        2. Put your target item between you and the Frox and have its pickup prompt ready
        3. On the first frame of the target despawning due to being eaten, **pick up** the target and **pause** the game _immediately_
        4. If the pause was on the same frame as the pickup or the frame after, it will be too soon to DI. Either perform a pause-buffer (must be nearly optimal), or watch 2 memories to advance to the correct timing
        5. **Drop** the portacull and **swap** to another of its type, then **unpause** the game
        6. Go away from the Frox so that it stops attacking, and test for DI. If the target was successfully DI'd, it will no longer be interactible with runes

    === "Steps (Molduga)" #####

        1. Gently place the target upon the sand, as far from Link as possible while still being in pickup range
        2. Cause a noise on the opposite side of the target from Link, as far as possible while still leaving the target in the zone-to-be-attacked
        3. These steps serve to allow the target to be eaten at the very edge of the Molduga's bite, keeping Link out of the line of fire (you will not be able to cull the target if you are hit)
        4. On the first frame after the target is eaten (the last frame before pickup is disabled), **pick up** the target
        5. 1-6 frames after pickup, **pause** the game
        6. **Drop** the portacull and **swap** to another of its type, then **unpause** the game
        7. Any time after Link unculls, **unequip** the portacull's type so that it may be taken with
        8. Leave the area or find high ground to avoid further Molduga attacks
        9. Test for DI: if the target was successfully DI'd, it will no longer be interactible with runes

    _Discovered by mulberry - Jan 18th, 2026_

    #### Method 13: Stake Culling ?
    ---
    versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    notoc: true
    obsolete: false
    ---

    - This method uses culling area phase culling to rapidly and automatically cull and uncull the target, ensuring it will always successfully DI.
    - Unlike most other DI methods, this one requires very specific circumstances (A culling area close to a Frox or Molduga).
    - My sincere apologies for allowing such unprofessional placeholder steps to actually be published... they simply slipped through the cracks.
    - This section will, however, remain placeholder'd for the time being while I track down the steps and give it a try.
    
    Prepare:

    - The target
    - A shield
    - A dragon part
    - A stake
    - A Frox or Molduga within 500m of a culling area

    Steps:

    1. FE the target to the shield
    2. **Glue** the stake, shield, and dragon part together in the culling area (possibly in some specific order)
    3. Take the target to the Frox or Molduga
    4. I don't remember how to make it phase :(
    5. Feed the target to the hungry monster while it is phasing
    6. Due to the constant culling and unculling, the target will basically always DI (excepting possibly on S2E?)
    7. To allow the target to be safely zuggled and taken elsewhere, use Octo Detanglement to detangle the target from the parent shield.

    _Discovered by mulberry - Jan 18th, 2026_

    #### Method 14: Mineru FE + Portacull ?
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    notoc: true
    obsolete: false
    ---

    - This method uses Mineru FE to cause the target to cull when Mineru does, then uses a Portacull to manually cull her as soon as the target begins despawning.
    - It is consistent up to the user's ability to time a pause within the 6-frame DI window.
    - After DI, the target retains an FE connection to Mineru, allowing her to be used as the culling source for [Ghost DI](uid:BEW) (most useful on `1.1.2` and below, and for Batch DI on all versions).

    Prepare:

    - Mineru
    - The target
    - A portacull of a type other than the target's
    - A Frox or Molduga
    - Optionally, a Homing Cart, if using a Molduga

    === "Steps (Frox)" #####

        1. Mineru FE the target
        2. Approach a Frox and wait until it is about to do a vaccuum attack. This is nearly always the first attack it does, and is also the only attack it will do when Link is slightly outside its territory
        3. **Drop** the target somewhere the Frox will suck it in, then **mount** Mineru and stand somewhere safe
        4. As soon as the target visibly begins to despawn, **pause** the game or **open** the D-Pad Menu. The fadeout is too short to pause on reaction, but it can be caught with pause/D-Pad buffering, and always happens at the same distance from the Frox's mouth.
        5. **Drop** the Portacull, then **swap** to another item of that type.
        6. **Unpause** the game. If desired, the portacull can usually be saved relatively easily.
        7. Assuming the timing window was hit correctly, the target will be DI'd and left on the ground somewhere nearish to the Frox.
        8. **Collect** the target and go away from the Frox so that it stops attacking.
        9. If desired, **detangle** the target from Mineru by **fusing** something else to the target's slot.

        _Discovered by mulberry - Jan 17th, 2026_

    === "Steps (Molduga)" #####

        1. Mineru FE the target
        2. Optionally, glue the target to a Homing Cart
        3. **Drop** the target somewhere the Molduga notices it (activating the cart if present)
        4. **Mount** Mineru somewhere safe, while remaining withing the Homing Cart's 50m activation radius (if applicable)
        5. Shortly after its detection symbol becomes a yellow !, the Molduga will lunge and eat the target. Use pause buffering or D-Pad buffering to **pause** 2-7 frames after the target is eaten
        6. If the Homing Cart was used, it offers additional timing cues: The Molduga will be damaged, and the glue between the target and the Homing Cart will break only when the timing window has actually begun.
        7. Once paused during this window, **drop** the portacull and **swap** to another item of that type
        8. **Unpause** the game. If successfully DI'd, the target will still exist after the Molduga has passed, and it will no longer be interactible with runes.
        9. **Collect** the target and return to safety
        10. If desired, **detangle** the target from Mineru by fusing something else to the target's slot

        _Homing Cart trick discovered by ofstrings2 - Jan 31st, 2026_

    #### Method 15: Alternate Mineru Limbo Methods (Molduga) ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    notoc: true
    obsolete: false
    ---

    - Unlike Method 5, these variants forego the use of either the wall or the steering stick, offering greater flexibility or reduced cost respectively.
    - After DI, the target retains an FE connection to Mineru, allowing her to be used as the culling source for [Ghost DI](uid:BEW) (most useful on `1.1.2` and below, and for Batch DI on all versions).


    === "Steering Stick Only" #####

        - Without the need of a wall, this variant can be performed anywhere in Molduga territory at a minimum cost.
        - However, the chain of states Mineru goes through notably reduces the consistency, particularly on Switch 1 Edition.
    
        Prepare:
    
        - Mineru
        - The target
        - A steering stick
        - A Molduga (a Frox's attacks are not readily compatible with this method)
    
        Steps:
    
        1. Mineru FE the target
        2. Enter a Molduga's territory and deploy a steering stick. Flatter terrain is usually more consistent.
        3. **Mount** the steering stick to center Link, then **dismount** and **drop** the target
        4. **Whistle** the Molduga over if it hasn't yet noticed Link, then **remount** the steering stick to cull Mineru
        5. If all goes well, when the Molduga eats Link, the target will be DI'd automatically over the next 2 steps:
        6. As soon as Link dismounts the steering stick, Mineru will enter Limbo and uncull the target.
        7. Then, as Link travels away from the ground, Mineru will exit Limbo into the culled state, culling the target during the DI window.
        8. The most likely failure state is for Mineru to not exit Limbo soon enough, causing the target to fully despawn and be destroyed.
    
        _Methods discovered by Kleric - Feb 4th, 2026_

    === "Wall Only" #####

        - Using only terrain to force Mineru into the Limbo state makes this method completely waste-free, while still being almost completely reliable.
        - However, the specific terrain required is both very rare, and can occasionally fail to induce Limbo. In the latter case, the attempt will need to be aborted (lest the target be destroyed).

        Prepare:
    
        - Mineru
        - The target
        - One of a few locations that can force Limbo within Molduga Territory
        - The Molduga that goes in said territory
    
        Steps:
    
        1. Mineru FE the target
        2. Stand at one of the known special locations within Molduga territory (pictures and map links provided below)
        3. **Climb** the wall or otherwise compel Mineru to cull
        4. Stop compelling Mineru to cull, allowing her to enter the Limbo state (the target should be unculled, but Mineru should not reappear from her orb)
        5. **Drop** the target and allow the Molduga to eat both Link and the target
        6. Check if the target was DI'd. Due to Mineru's catlike uncooperativity, the target will occasionally be unchanged or completely destroyed (usually the former). If needed, try again from step 2 or 1 respectively.
        9. If desired, **detangle** the target from Mineru by **fusing** something else to the target's slot.

        ??? example "Location 1: Toruma Dunes Ruins Rubble"

            - edited screenshot placeholder
            - object map embed placeholder

            - I don't think there's a Location 2 yet lemme cook sometime

        _Method and locations developed by Squidwest - Mar 13th, 2026_

    #### Method 16: Mineru FE Only (Either) ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    notoc: true
    obsolete: false
    ---

    - This method uses Mineru FE to cause the target to cull with Mineru, then uses the standard "orb return" culling method to cull her.
    - It is highly minimal and doesn't require any special location features, but is the most difficult to time.
    - After DI, the target retains an FE connection to Mineru, allowing her to be used as the culling source for [Ghost DI](uid:BEW) (most useful on `1.1.2` and below, and for Batch DI on all versions).

    Prepare:

    - Mineru
    - The target
    - A Frox or Molduga (the latter is likely easier)

    Steps:

    1. Mineru FE the target
    2. Place the target so that the Frox or Molduga will eat it
    3. Shortly before the monster's attack begins, start to **climb** a wall so that Mineru begins to cull
    4. If timed correctly, Mineru (and thus the target) will cull just after the target gets eaten
    5. **Collect** the target and, if desired, **detangle** it from Mineru by fusing something else to that slot

    _Don't know if this one has ever even been posted about lol_

## Properties

### All Objects

Shared with Void Dipping:

- Uninteractible by runes (including, for equipment, fusing directly to it)
- Durability/Duration calculations are skipped
- No longer react to the elements, nor break on physical impact (for those which retain collision when unfused)
- Some Zonai Devices become non-functional

Unique to DI:

- Protected against the "Deletion Flag" under most circumstances
- Protected against the "FarDelete" deletion type as long as it has a DI FE/Fuse parent

### Equipment

=== "(1.0.0-1.1.2)" ####
    ---
    notoc: true
    ---

    Shared with Void Dipping:

    - Some single-use fuses become infinite (eg Ancient Blades)
    - Faildrop and Faildrop-Swap cause unequipped smuggle
    - Drop-Swap-Unequip and Drop-Swap-Drop drop normally
    - Does not induce D-Pad Lock when smuggled on `1.1.2` (except if there is no dependency to Link)

    Unique to DI:

    - Due to the lower death reason number, it is immune to being destroyed by inventory pickup. Therefore, it can be used to duplicate that equipment en masse simply by picking it up with something else equipped
    - Propagates the Eaten death reason to anything fused to it (slightly conditional). This can in turn be interrupted to create a [DI Ghost](uid:BEW) (see linked page for details and methods)

=== "(1.2.0+)" ####
    ---
    notoc: true
    ---

    Shared with Void Dipping:

    - Some single-use fuses become infinite (eg Ancient Blades)
    - Does not directly cull from Drop-Swap Culling
    - Faildrop causes Equipped Smuggle
    - Faildrop-Swap, Drop-Swap-Unequip, and Drop-Swap-Drop cause unequipped smuggle
    - Does not induce D-Pad Lock when smuggled (except if there is no dependency to Link)

    Unique to DI:

    - Due to the lower death reason number, it is immune to being destroyed by inventory pickup. Therefore, it can be used to duplicate that equipment en masse simply by picking it up with something else equipped
    - Propagates the Eaten death reason to anything fused to it (slightly conditional). This can in turn be interrupted to create a [DI Ghost](uid:BEW) (see linked page for details and methods)

## Notes
- Sometimes known as "Eaten DI". "Frox Dipping" and "Frox Licking" are disused and discouraged monikers.
- Although void dipping is also technically a form of Despawn Interrupt, "DI" and "Despawn Interrupt" refer _only_ to the Eaten variation by convention.

## Resources
- [Spreadsheet link](https://docs.google.com/spreadsheets/d/1xNB1gOLZRSF9yp1mHUsS9ymogRJa1Wz8rTliTXezeRM/edit?pli=1&hl=de&gid=0#gid=0&range=294:294)
- [Link's Luxury Loadout](https://www.youtube.com/watch?v=kQuj0LBQdrM)

??? quote "Discord Resources"

    Like Like DI:

    - [Original Discovery](https://discord.com/channels/1086729144307564648/1105598687167664239/1251952401150377994)
    - [First Working DI IPR](https://discord.com/channels/1086729144307564648/1110956205624532993/1381773566529507459)
    - [DI IPR with Like Like Portacull FE](https://discord.com/channels/1086729144307564648/1113557914444111873/1406426209319125064)
    - [Minimalist DI IPR](https://discord.com/channels/1086729144307564648/1109838351596527726/1474924475098337320)
    - [Minimalist DI IPR Late-Fuse Recovery](https://discord.com/channels/1086729144307564648/1109838351596527726/1474961843263901797)

    Frox DI:

    - [Original Discovery](https://discord.com/channels/1086729144307564648/1110956205624532993/1461889160062173416)
    - [Portacull Mitosis Method Discovery](https://discord.com/channels/1086729144307564648/1113557914444111873/1462825674074095829)
    - [Original Overload Drop Zuggle Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1462832934179442861)
    - [Overhead Portacull Method with Overload Drop Zuggle and Cloning](https://discord.com/channels/1086729144307564648/1113557914444111873/1462832934179442861)
    - [Overload Drop Zuggle Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1468028451851337862)
    - [FE Method](https://discord.com/channels/1086729144307564648/1110956205624532993/1461982572509659211)
    - [Original Mineru Limbo Method](https://discord.com/channels/1111875355758837830/1128775917376897145/1462313834831151199)
    - [Mineru Limbo Method alternate build](https://discord.com/channels/1111875355758837830/1128775917376897145/1462613380597551366)
    - [Mineru Limbo Method Tutorial](https://discord.com/channels/1111875355758837830/1128775917376897145/1462399014078119987)
    - [Direct Fusion Discovery](https://discord.com/channels/1086729144307564648/1110956205624532993/1462193331361677362)
    - [Improved Direct Fusion Method](https://discord.com/channels/1086729144307564648/1110956205624532993/1462213495733883011)
    - [Pickup Method](https://discord.com/channels/1086729144307564648/1110956205624532993/1462447829304868945)
    - [Stake Culling Method](https://discord.com/channels/1111875355758837830/1128775917376897145/1462584623975633010)
    - [Mineru FE + Portacull Method](https://discord.com/channels/1086729144307564648/1110956205624532993/1462063753406320754)

    Duga DI:

    - [Original Discovery](https://discord.com/channels/1111875355758837830/1128775917376897145/1466939998023450796)
    - [Minimal Mineru Limbo Method](https://discord.com/channels/1086729144307564648/1105598687167664239/1482109073104306366)
    - [Spring Stack Wall Mineru Limbo Method](https://discord.com/channels/1086729144307564648/1105598687167664239/1482144535659155490)
    - [FE Method](https://discord.com/channels/1111875355758837830/1128775917376897145/1466965629616525312)
    - [Turbo FE Method](https://discord.com/channels/1111875355758837830/1128775917376897145/1467133823429906432)
    - [Portacull Mitosis Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1468008448451940605)
    - [Wall-less Mineru Limbo Method](https://discord.com/channels/1086729144307564648/1113557914444111873/1468543353040928971)
    - [Dog Duga Dip](https://discord.com/channels/1086729144307564648/1113557914444111873/1467059196003352587)
    - [Optimised Direct Fusion](https://discord.com/channels/1086729144307564648/1113557914444111873/1514300087210213418)
    - I don't have a ref for the wall-climb Mineru FE method the page came with

## Related
- [Fuse Entanglement](search:Fuse Entanglement)
- [Detanglement](search:Detanglement)
- [Despawn Interrupt](search:Despawn Interrupt)
