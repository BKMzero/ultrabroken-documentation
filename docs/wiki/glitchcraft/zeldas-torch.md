---
title: "Zelda's Torch"
uid: "TW8"
draft: true
label: "ZTorch"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["mulberry, Aergyl, Jordan, MandelbrotChaylay, Squidwest"]
date: "2025-12-06"
description: "Using Super Fuse Overload, the unique torch Zelda carries in the prologue can be obtained."
aliases: [""]
tags: ["Equipment", "Zelda"]
---

# Zelda's Torch

## Summary

By completely filling the game's global dependency array with persistent dependencies, Prologue Zelda can be forced to Overload Drop her torch, which has unique properties. Once obtained in the prologue, it can be transferred to a progressed file in the same way as the Prologue Master Sword.

I'm sorry if you see this page like this. It's in a transitional state. Originally I wanted it to be like the Mineru's Arm page: a series of modular steps that are easy to mix and match to suit your particular tastes and needs. But Zelda's Torch is just a different beast. It needs special attention to autosave management, a half-dozen save loads, and is complex enough that adding a Mineru's Arm get into the middle is basically free.

So I'm converting the drafted modular format to a trio of specific guides, and I'm not done. Partly it's because 1.1.2 is a beast of beasts that I don't even know anything about to boot, but also I have a lot of location research to do (I want to find the absolute best prologue-overlapping shrines for each version, absolutely maximizing ease of item placement and transfer).

But like, there's a reason I haven't published the page. How did you get here?

_First obtained by mulberry - Dec 07th, 2025_

## Instructions

- This page will offer three guides, each tailored for a specific version range.
- There are other combinations of SFO Methods and transfer methods that will work on each version, but something had to go to make this page readable and I chose variations.
- The provided combinations are the most efficient on the listed version ranges.

=== "SFO Method 4 + SLD" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1"]
    ---

    - These versions predate the addition of active smuggles causing "D-Pad Lock", so they can perform Save Load Dupe on Zelda's Torch without having to cull Link.
    - This in turn avoids invoking the "Callback", which requires Lift Storage Warp to overcome in all newer patches.
    - However, they also predate Drop-Swap Culling, so they are more or less required to use Method 4 of Super Fuse Overload, which is moderately more difficult than Method 1.
    
    #### Part 1: Prep
    ---
    notoc: true
    ---

    1. By whichever means desired, get the "canonical minimum" Zuggle Overload (9 on `1.0.0`, 13 on `1.1.0+`)
    2. Prepare a DI Ghost Shield (`E`). This is technically optional, but it saves time and complexity and the steps assume you have it. Get it.
    3. Create an Intangible Aerophasing setup at (location).
    4. You will also need several unfused weapons and shields, a bow, at least one arrow, and a material.
    
    #### Part 2: SFO and Torch Collection
    ---
    notoc: true
    ---
    
    ##### 2a: Performing SFO

    1. Use the Aerophasing setup to ensure it has a cull stored; this will allow the culling area to remain loaded through a banc change
    2. Travel to (shrine) and enter it. **Do not warp there.**
    3. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
    4. **Overload Drop** a weapon `A` and fuse it to a shield `B`
    5. [Overload Cold Fuse](uid:O64) 21 shields `C1-C21` to A (the 19 dropped & 2 from inventory)
    6. **Fail-drop** `A` and **drop** `B`
    7. [Overload Pickup](uid:8QH) `C1`
    8. Duplicate 30 shields `D1-D30` off `E`, dropping each on the ground and **Overload Cold Fusing** them to `C1` as you go
    9. **Fail-drop** `C1` and **drop** it aside
    10. Repeat 7-9 for `C2-C19` with the **same** `D1-D30`
    11. For `C20` and `C21`, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, _proceed to step 11_
    12. **Overload Cold Fuse** an unrelated material to `C[n]`. If it works, **Collect it** and **Overload Cold Fuse** the next `D[n]`, then repeat. If it fails, _proceed to step 12_
    13. **Fail-drop** `C[n]` and **drop** it. You may have to **unequip your bow** for it to return. **Be sure it returns before dropping it.**
    14. **Drop** `A`

    ##### 2b: Permaculling the shields

    1. [Drop Zuggle](uid:0YL) a shield. If `E` was prepared, it can be used.
    2. Equip one of `B`, `C[n]`, or `D[n]` and step onto the phasing platform
    3. **Pause** the game while Link is **culled**. This will cause Link to consistently be **unculled** when the game is unpaused
    4. **Unpause** the game and immediately **open** the Shield Quick Menu (D-pad Left). If Link is **unculled** behind the menu, **drop** the equipped shield. If not, repeat step 3.
    5. Repeat steps 2-4 for _all_ `B`, `C[n]`, and `D[n]`, ultimately resulting in the entire setup being permaculled

    ##### 2c: Collecting Zelda's Torch in the prologue

    1. Return to the title screen and begin a new file. This will only enter the prologue scenario and create occasional autosaves (up to 4), so don't fret about your progressed file.
    2. Progress to the _second_ autosave (give timing cue but it's just after the first dialogue cutscene thing), then return to (shrine name).
    3. Use the D-Pad to unequip all equipment, then resync Link's armor, and finally use the D-Pad to re-equip items until a nocked arrow fails to attach to the bow (and instead just floats there).
    4. Load the second prologue autosave. Zelda will drop her torch, so pick it up.
    5. If she does not, try loading back to (shrine) and repeating steps 3-4; It may take a few tries for her torch to be one of the dependencies that fails.
    6. Proceed until receiving the _third prologue autosave.
    7. **Close the game** to end SFO

    #### Part 3: Save Load Dupe
    ---
    notoc: true
    ---

    1. Load a progressed file, then warp to (shrine) and enter it to receive an autosave (protip, make this the same as the SFO shrine in the final setup so they can skip this)
    2. Load the _third_ prologue autosave and walk to (location)
    3. Equip Zelda's Torch and **unpause** to make sure Link has it equipped in-world
    4. **Pause** the game, **drop** Zelda's Torch, and **swap** to another weapon (likely, you only have the Prologue Master Sword)
    5. **Pause buffer** (unpause and pause again 3 frames later; any earlier will eat the input and any later is too late)
    6. **Drop** the swapped-to weapon and **load** the (shrine) autosave
    7. If SLD was performed correctly, Zelda's Torch should be at (spot) within the shrine
    8. Collect Zelda's Torch and save the game

    #### Part 4: Bonuses
    ---
    notoc: true
    ---

    - This is a lot of work for a torch, even if it's really cool. But if you're careful, you can also obtain Mineru's Arm and Prologue Master Sword during this setup, for very little extra work. Like shockingly little.

    ##### Adjustments for Mineru's Arm

    1. Before beginning Part 2a, summon Mineru's Sage Avatar.
    2. After completing Part 2b, before returning to the title screen, warp to Mogisari Shrine, at Lomei Sky Labyrinth in the northeastern sky.
    3. Follow [These steps](uid:J7X#collecting-minerus-arm_1) to collect Mineru's Arm.
    4. Warp back to (shrine) and get a new autosave inside it with Mineru's Arm collected.
    5. Proceed as normal from the start of Part 2c.

    ##### Adjustments for the Prologue Master Sword

    1. After Part 3, step 8 ("Collect Zelda's Torch and save the game"), reload the third prologue autosave
    2. Repeat the SLD, but start with the Prologue Master Sword equipped, SLDing it instead.
    3. Yeah this is basically a free addon for `1.0.0-1.1.1`.

=== "SFO Method 4 + LSW + CSZ" ###
    ---
    versions: ["1.1.2"]
    ---

    - `1.1.2` is in a particularly awkward position, postdating D-Pad Lock but predating Drop-Swap Culling.
    - Thus, it is required to cull Link to be able to transfer Zelda's Torch, but has no easy way to achieve this cull in the prologue.
    - It also cannot perform Save Load Dupe, because the LSW required to avoid the "Callback" prevents the SLD from transferring the torch to a controlled location.
    - Furthermore, it cannot perform Swap Resync Zuggle _or_ SFO Method 1.
    - Thus, it must first perform SFO Method 4, then use a combination of LSW Lock and Cull Storage Zuggle.
    - Unless ☝️ someone figures out how to do long cull storage consistently

    #### Part 1: Prep
    ---
    notoc: true
    ---

    1. By whichever means desired, get 13 Zuggle Overload.
    2. Prepare a DI Ghost Shield (`E`). This is technically optional, but it saves time and complexity and the steps assume you have it. Get it.
    3. Create an Intangible Aerophasing setup at (location).
    4. You will also need several unfused weapons and shields, a bow, at least one arrow, and a material.
    
    #### Part 2: SFO and Torch Collection
    ---
    notoc: true
    ---
    
    ##### 2a: Performing SFO

    1. Use the Aerophasing setup to ensure it has a cull stored; this will allow the culling area to remain loaded through a banc change
    2. Travel to (shrine) and enter it. **Do not warp there.**
    3. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
    4. **Overload Drop** a weapon `A` and fuse it to a shield `B`
    5. [Overload Cold Fuse](uid:O64) 21 shields `C1-C21` to A (the 19 dropped & 2 from inventory)
    6. **Fail-drop** `A` and **drop** `B`
    7. [Overload Pickup](uid:8QH) `C1`
    8. Duplicate 30 shields `D1-D30` off `E`, dropping each on the ground and **Overload Cold Fusing** them to `C1` as you go
    9. **Fail-drop** `C1` and **drop** it aside
    10. Repeat 7-9 for `C2-C19` with the **same** `D1-D30`
    11. For `C20` and `C21`, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, _proceed to step 11_
    12. **Overload Cold Fuse** an unrelated material to `C[n]`. If it works, **Collect it** and **Overload Cold Fuse** the next `D[n]`, then repeat. If it fails, _proceed to step 12_
    13. **Fail-drop** `C[n]` and **drop** it. You may have to **unequip your bow** for it to return. **Be sure it returns before dropping it.**
    14. **Drop** `A`

    ##### 2b: Permaculling the shields

    1. [Drop Zuggle](uid:0YL) a shield. If `E` was prepared, it can be used.
    2. Equip one of `B`, `C[n]`, or `D[n]` and step onto the phasing platform
    3. **Pause** the game while Link is **culled**. This will cause Link to consistently be **unculled** when the game is unpaused
    4. **Unpause** the game and immediately **open** the Shield Quick Menu (D-pad Left). If Link is **unculled** behind the menu, **drop** the equipped shield. If not, repeat step 3.
    5. Repeat steps 2-4 for _all_ `B`, `C[n]`, and `D[n]`, ultimately resulting in the entire setup being permaculled

    ##### 2c: Collecting Zelda's Torch in the prologue

    1. Return to the title screen and begin a new file. This will only enter the prologue scenario and create occasional autosaves (up to 4), so don't fret about your progressed file.
    2. Progress to the _second_ autosave (give timing cue but it's just after the first dialogue cutscene thing), then return to (shrine name).
    3. Use the D-Pad to unequip all equipment, then resync Link's armor, and finally use the D-Pad to re-equip items until a nocked arrow fails to attach to the bow (and instead just floats there).
    4. Load the second prologue autosave. Zelda will drop her torch, so pick it up.
    5. If she does not, try loading back to (shrine) and repeating steps 3-4; It may take a few tries for her torch to be one of the dependencies that fails.
    6. Proceed until receiving the _third prologue autosave.
    7. **Close the game** to end SFO

    #### Part 3: CSZ Prep and Performing LSW Lock
    ---
    notoc: true
    ---

    1. I do not know how to do this. I will be asking for help. thumbs up emoji
    2. But the idea of holding off on getting autosave 4 until autosave 3 is about to expire is sound I think

    #### Part 4: Cull Storage Zuggle

    1. Dunno how to do this either.
    2. Like I can read. I see the Cull Storage Zuggle page and I can read it. Could probably execute a CSZ in a controlled trial.
    3. But I don't know how to store a cull through a load. And I definitely don't know the *easiest* way to do it.
    4. Also Mandelbrot did an sld I'm pretty sure, so maybe 1.1.2 doesn't need to LSW at all? I didn't consider the physical cull possibility...
    5. If I figure out cull storage SLD well enough I guess it might be good for 1.2.0+ as well???

    #### Part 5: Bonuses
    ---
    notoc: true
    ---

    - This is a lot of work for a torch, even if it's really cool. But if you're careful, you can also obtain Mineru's Arm and the Prologue Master Sword during this setup, for much less total work than obtaining all three one-by-one.

    ##### Adjustments for Mineru's Arm

    1. Before beginning Part 2a, summon Mineru's Sage Avatar.
    2. After completing Part 2b, before returning to the title screen, warp to Mogisari Shrine, at Lomei Sky Labyrinth in the northeastern sky.
    3. Follow [These steps](uid:J7X#collecting-minerus-arm_1) to collect Mineru's Arm.
    4. Warp back to (shrine) and get a new autosave inside it with Mineru's Arm collected.
    5. Proceed as normal from the start of Part 2c.

    ##### Adjustments for the Prologue Master Sword

    - need to figure out if the CSZ is even reusable. If not it's fine, just need to do the setup twice. but that's not "very little extra work" anymore.

=== "SFO Method 1 + LSW Lock + SRZ" ###
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    ---

    - These versions postdate both D-Pad Lock and Drop-Swap Culling.
    - Thus, they must cull Link to be able to transfer Zelda's Torch, but have access to an easy way to do so.
    - They also must use LSW Lock to avoid the "Callback", and so cannot Save-Load Dupe, but have access to Swap Resync Zuggle instead.
    - Finally, they may make efficient use of SFO Method 1, making the act of collecting Zelda's Torch within the prologue easier than other versions.
    
    #### Part 1: Prep
    ---
    notoc: true
    ---

    1. By whichever means desired, prepare 13 Zuggle Overload (such that having all equipment equipped acts normal, but drawing bow causes swaps to overload drop).
    2. Prepare 7 "Gen 2" DI Ghosts: 5 shields, 2 weapons, and a bow, with none of them sharing any dependencies (direct or indirect).
    3. Zuggle 2 of the shields and the bow, then travel to Mayatat Shrine (_A Sliding Device_) at Kara Kara Bazaar.
    4. Drop said DI Ghosts at the location pictured below, being sure to undo the resulting Zuggle Drops. Here, they will be able to be collected within the prologue at a specific desired time.
    5. Leave the third DI Ghost Shield at Akkala Citadel Ruins (or another preferred culling area).
    6. Zuggle the remaining 2 shields and 2 weapons and travel to (shrine).

    ??? info "Where to drop the Ghosts"

        placeholder

    #### Part 2: SFO and Torch Collection
    ---
    notoc: true
    ---

    - Parts 2a and 2b here are lifted from Method 1 on the Super Fuse Overload page. The only difference here is that it is performed in a specific location.
    - One of the DI Ghost weapons is `A1`, and one of the DI Ghost shields is `B1`. The other two are only for duping and are unnamed.
    
    ##### 2a: Creating the base setup

    1. Enter (shrine), defeat any constructs present, and dispose of their weapons (for example by leaving/reentering)
    2. (Need a little more testing to decide best shrine)
    3. `B1` [Overload FE](uid:0XV#method-3-vddi-smugglezuggle) weapon `B2`
    4. [Recall Lock](uid:EY8) `B2`
    5. `A1` and normal weapon `A2` [Ghost DI](uid:BEW#method-1-fuse-drop-swap-120) shield `A3`
    6. `A1` **Overload FE** normal shield `A4`; Leave `A1` [Zuggle Dropped](uid:L84) 
    7. Equip `A2`, [Smuggle](uid:TGY) `A3`, and [Overload Pickup](uid:8QH) `A4`
    8. `A2-A4` [Overload Batch DI](uid:PG3#method-1-overload-pf-drop-swap-culling-120) 19 weapons `C1-C19`:
        1. Place Link's back to a wall so that `A2` can be fail-dropped
        2. Drop a weapon `C1` on the ground and **fuse** it to `A4`
        3. **Fuse** `C1` to `A4` again and **pause** a few frames later
        4. **Drop** `A2`, **swap** to another weapon, **unequip** that weapon, and finally **unpause**
        5. Repeat Steps 8b-8d 18 more times, creating 19 total weapons `C1-C19`
    9. Confirm `C1-C19` all exist, then **Fail-Drop** `A4` to move it to Link's hand
    10. `A3` & `A4` **Ghost DI** weapon `C20`
    11. **Drop** `A4`
    12. Re-smuggle `A3`, equip a random shield, and **Fuse** something disposable to it. This will leave `A4` as the sole FE parent of `C20`
    14. Smuggle any _one_ `C`, then **equip** another and **throw it**. Finally, unsheathe weapon to return the thrown one to Link's hand. The smuggled weapon is now in Purgatory
    15. Repeat step 11 to Purgatorize _all_ `C`, using a random weapon for the final throw (it can be unequipped after)
    16. **Recall Lock** `A4`, discarding `A2` and `A3` through the load

    ##### 2b: Performing SFO

    1. Zuggle Drop `B1`, equip `A4`, and **Overload Pickup** `B2`
    2. `C1-20`, `B2`, & `A4` **Overload Batch DI** 30 Shields `D1-D30`:
        1. _Do not_ place Link's back to a wall; it is likely you will badly mess up if you do.
        2. Drop a shield `D1` on the ground and **fuse** it to `B2`
        3. **Fuse** `D1` to `B2` again and **open** the Shield Quick Menu a few frames later
        4. Without letting the game unpause, **drop** `A4`, **swap** to another shield, and **unequip** that shield
        5. If `B2` is a Zonaite-series weapon, check if the blade is present; if not, this DI was successful.
        6. Repeat Steps 2b-2d 29 more times, creating 30 total shields `D1-D30`
        7. There will be a substantial lag on Step 2b for each shield after `D1`, hence the recommendation to use the D-Pad (and thus to not fail-drop).
        8. This lag makes it likely to pause _too early_, which can be detected by checking if the twice-fused `D[n]` is still "Fuse-Target Blue".
    4. _Super Fuse Overload_ should occur on the 30th shield. If confirmation is needed, pick `A4` back up, then attempt to nock an arrow. If it fails to attach to the bow, and hangs in midair, SFO is fully active
    5. Leaving `A4` dropped, **fail-drop** `B2` and **drop** it _after_ it returns to Link's hand. Finally, un-Zuggle Drop `B1`
    6. The entire setup will now persist, and SFO will be fully active as long as Link equips each type of equipment (with exactly _one_ being fused)

    ##### 2c: Collecting Zelda's Torch in the prologue

    1. Return to the title screen and begin a new file. This will only enter the prologue scenario and create occasional autosaves (up to 5), so don't fret about your progressed file.
    2. Progress to the _second_ autosave (give timing cue but it's just after the first dialogue cutscene thing), then return to (shrine name).
    3. Use the D-Pad to unequip all equipment, then resync Link's armor, and finally use the D-Pad to re-equip items until a nocked arrow fails to attach to the bow (and instead just floats there).
    4. Load the second prologue autosave. Zelda will drop her torch, so pick it up.
    5. If she does not, try loading back to (shrine) and repeating steps 3-4; It may take a few tries for her torch to be one of the dependencies that fails.
    6. After collecting the torch, use overload duping to obtain additional torches/swords for buffer drop purposes. Additionally, collect 3 shields and a bow from the pre-placed DI Ghosts.
    7. Proceed until receiving the _third_ prologue autosave (timing cue), then load the (shrine) autosave.
    8. One by one, **pick up** and **unequip** all `D[n]` to destroy them, deleting all the dependencies and ending SFO.

    #### Part 3: Performing Drop Zuggle and LSW Lock
    ---
    notoc: true
    ---

    1. Warp to Domizuin Shrine and go to the small culling area there; dispose of the Scary Grabber if needed
    2. Prepare two portaculls, at least one being a shield 
    3. [Overload FE](uid:0XV#method-3-vddi-smugglezuggle) a Battery or other liftable to the pre-placed DI Ghost (`E`)
    4. Unequip shield, leaving `E` smuggled/zuggled
    5. Overload pickup a portacull shield and drop it; `E` will drop and prevent D-Pad lock. Pick up and drop it to undo the resulting Zuggle Drop.
    6. Pick the portacull shield back up; it should "equip" to Link's feet.
    7. **Pause** the game, **drop** the portacull, and **swap** to another shield
    8. **Pause buffer**, **swap** any non-shield piece of equipment, and **drop** the portacull
    9. The portacull should become drop zuggled. If the pause buffer was too slow, however, it might become purgatorized. If so, ignore it, make another, and try again from step 4.
    10. Stand within the culling margin. Place the other portacull in the culling area, lift the child of E, and walk outside the margin. Link and the liftable should cull.
    11. Load the _third_ prologue autosave. Link should be deep within the gray void around the prologue, and a _single_ fadeout should occur shortly after loading.

    #### Part 4: Performing Swap Resync Zuggle
    ---
    notoc: true
    ---

    1. Link is not actually falling, due to the LSW Lock's anti-movement powers. There is no rush. Do not rush.
    2. Ensure a shield is not currently equipped, then **pick up** the Drop Zuggled Portacull.
    3. For overload-management reasons, **unequip** Link's bow if it is equipped.
    4. **Unequip** whichever weapon is currently equipped, then **equip** Zelda's Torch; this ensures it is not overload dropped
    5. **Pause** the game
    6. **Drop** a buffer equipment item
    7. **Drop** the Portacull Shield and **swap** to another shield
    8. **Drop** 2 more buffer items (NOT the swapped-to shield)
    9. **Drop** Zelda's Torch and **swap** to another weapon
    10. **Pause Buffer** (unpause and pause again 3-4 frames later; any faster will eat the input and any slower is... too slow)
    11. **Equip**, then **unequip** the bow to resync
    12. **Drop** the swapped-to weapon
    13. **Load** a progressed save. This interrupts the dropping process, removing the need for a wall to fail-drop with
    14. If the SRZ was successful, Zelda's Torch will be on Link's back in the progressed save. However, Link will still be under the effects of LSW Lock, and is likely high in the air.
    15. Get some ground beneath Link; the easiest way is to fire a Hover Stone straight down and land on it (...slowly).
    16. Prepare Recall, then **Drop** an equipped weapon and use Recall on Zelda's Torch to make it easy to catch.
    17. Grab it and save the game.
    18. Likely, returning to Domizuin to destroy the LSW base is more trouble than it's worth. A game close will get rid of it, if you're ready (see below).

    #### Part 5: Bonuses
    ---
    notoc: true
    ---

    - This is a lot of work for a torch, even if it's really cool. But if you're careful, you can also obtain Mineru's Arm and the Prologue Master Sword during this setup, for much less total work than obtaining all three one-by-one.

    ##### Adjustments for Mineru's Arm

    1. Before beginning Part 2a, summon Mineru's Sage Avatar.
    2. After completing Part 2b, before returning to the title screen, warp to Mogisari Shrine, at Lomei Sky Labyrinth in the northeastern sky.
    3. Follow [These steps](uid:J7X#collecting-minerus-arm_1) to collect Mineru's Arm.
    4. Warp back to (shrine) and get a new autosave inside it with Mineru's Arm collected.
    5. Proceed as normal from the start of Part 2c.

    ##### Adjustments for the Prologue Master Sword

    1. On Part 4, Step 12 ("**Drop** the swapped-to weapon"), additionally **drop** the swapped-to _shield_. This will return the portacull to the drop zuggle position, allowing it to be reused.
    2. Then, after finishing Part 4 (including saving the game), load _back_ to the prologue and perform SRZ again, but zuggle the Prologue Master Sword instead.
    3. Continue through the rest of Part 4 as before, collecting the Prologue Master Sword and saving the game.

## Notes

### Properties

#### As a weapon:
---
notoc: true
---

- Zelda's Torch is a peculiar 1-handed weapon which uses a blend of the properties of the Torch and the Traveler's Sword✨, along with some entirely unique properties.
- Like the Torch, it uses the Torch model and sounds, has 8 base durability, can be lit aflame at its tip, and will not burn out.
- Like the Traveler's Sword✨, it uses the Traveler's Sword Sheath, deals 7 damage, and is sharp without a fuse.
- Like other glitch weapons, it has no name or description, and usually displays "MsgNotFound" in those fields instead. However, it _does_ have a unique icon of a lit torch.
- It can be fused to, but _cannot_ be fused to other things.
- Uniquely to Zelda's Torch, it will automatically light if Cold Dropped (or Overload Dropped, or any other way of making the actor not equipped by Link when created).
- Furthermore, it uses a unique color for the light it emanates when lit, yellower than the standard lit torch.

#### As a building part:

- Dropped in the world, Zelda's Torch again uses a blend of properties.
- Like a Torch, it has 50 mass and is buoyant, flammable, and so on.
- Like a Traveler's Sword✨, it acts sharp and can cut when moved quickly enough.
- Though it sparks in the inventory during a storm, it does not actually attract electricity.
- Uniquely, when autobuilt, it will be _lit by default_. This is most clearly useful with Balloons, but do consider the auto-detonating bomb my friend

#### As a tool:

- Fused with a Pine Cone, it can be overload dropped to instantly boost any nearby fire, then unequipped to preserve the Pine Cone.
- Fused with an explosive, it can be overload dropped to almost instantly blow Link up. I don't... know why you would do this. But you can.
- You can overload or cold drop it with a bow unsheathed but not drawn and it'll light your arrow. Neat.
- Ought to play with it more and find fun tool uses...

### Credits ?

- Zelda's Torch obtained by mulberry - Dec 07th, 2025

### Resources

??? quote "Discord Resources"

    - [Original Zelda's Torch Get](https://discord.com/channels/1086729144307564648/1110956205624532993/1447220634987003984)

### Related
- [Zuggle Overload](search:Zuggle Overload)
- [Despawn Interrupt](search:Despawn Interrupt)
- [Fuse Entanglement](search:Fuse Entanglement)

### Page Todos: ?
---
notoc: true
---

- Find better shrines to use for each version (I want grounded overlap with somewhere _before_ the 4th autosave)
- Research physical cull storage sld and find out if it's better for 1.2.0+ than LSW+SRZ (I dunno that part was pretty easy)
