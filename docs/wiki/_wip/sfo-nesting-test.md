---
title: "Super Fuse Overload"
label: "SFO"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["mulberry, Aergyl, Jordan, MandelbrotChaylay, Squidwest"]
date: "2025-12-06"
description: "By creating 600-700 Cold Fuse connections, the game can be prevented from forming _any_ new dependencies. Mainly used to obtain Mineru's Arm and Zelda's Torch."
aliases: ["super-fuse-overload"]
tags: ["Equipment", "Fuse", "Overload", "Mineru"]
---

# Super Fuse Overload
`1.0.0` `1.1.0` `1.1.1` `1.1.2` `1.2.0` `1.2.1` `1.3.0/1.4.0` `1.4.1` `1.4.2` `1.4.3` `Switch 2`

## Summary
---

By creating 600-700 Cold Fuse connections, the game will be overloaded and unable to form any new dependencies. This causes every actor to be Zuggle Overloaded, and every equipment to be Fuse Overloaded.

_Discovered by mulberry, Aergyl; Optimizations by Jordan, MandelbrotChaylay, mulberry, Squidwest_

The nesting works in theory. A/B testing with other ideas to see what works best.
Method 1: provides the method in the main tab body and the use-cases in the subtabs
Method 2: duplicates the method into the subtabs to maximize instruction clarity
Method 3: like method 1 but uses dropdowns instead of subtabs
Method 4: like method 2 but with dropdowns

Todo:
- Find a good, stable minigame or two to recommend
- Double check duplication order of operations and correct if needed
- Decide on preferred method layout and redo rejected method layouts to match
- Do mulberry & Mandelbrot's methods to more accurately write them up
- Actually obtain Zelda's Torch at some point to provide better directions and warn of the pitfalls
- probably seek help on crediting and resources at some point
- Make graphs better and maybe get some illustrative images & screenshots going
- write everything after the methods :/

## Forewarnings and Tips
---

!!! danger "Panic!"
    While SFO is active, Panic Blood Moons will constantly occur if they are able (ie on the main map and not in a minigame or cutscene). Additionally, some dependencies will **crash the game** if they fail to form!

!!! info "Buckle up!"
    Due to the massive number of connections required, every method is relatively complex. Before you begin, be sure to read the steps carefully, and be sure you understand the glitches that go into your chosen method.

!!! info "Local or persistent?"
    There are two main types of SFO method: Local methods, which _do not_ persist through warps and loads, and Persistent methods, which... _do_ persist through warps and loads.
    Local methods are usually faster and easier, but cannot be used for some cases (eg Zelda's Torch).
    Persistent methods can be used for all cases, but are usually more time consuming and complex, and their persistence can make them difficult to work with in some cases (eg Mineru's Arm).

## Instructions
---

!!! note "Choose your fighter!"
    There are three main use cases for SFO: Obtaining Mineru's Arm, obtaining Zelda's Torch, and duplicating anything you can throw. For the sake of providing clear instructions, a variant of each method is given for each valid use case.

=== "Method 1"
    This is a persistent method that makes use of DI equipment to maximize setup speed. It can be used for anything, but is best-suited for Zelda's Torch and duplication.

    (Main part of Mandelbrot's Method)

    === "For Zelda's Torch"
        To obtain Zelda's Torch, perform this setup in Rasitakiwak Shrine

        (extension that tells you how to get Zorch in an autosave, then links to the MNF page and tells you to zuggle it with your preferred MNF method)

    === "For duplication"
        To duplicate Zonai Devices, either A: perform this setup in a shrine, load a save at a minigame, and start it immediately, or B: perform this setup while already in a minigame. For other throwables, simply perform in a minigame.

    === "For Mineru's Arm"
        (I don't really know a stable way to get MinArm with this one. Ideally you don't have to go through army with SFO, since that's super unstable. But if you set up in the tunnel, you're gonna have a hell of a time reducing your overload enough to fuse to MinArm, and to zuggle it without overload dropping anything important.)

        (but presumably it's possible, say by: doing your initial overload with froxic ghosts in the tunnel, zuggling in your child shields, and destroying them after you have an appreciable number of Arms to attempt with?)

=== "Method 2"
    This is a persistent method for versions `1.2.0` and up that makes use of DI equipment to maximize adjustability, ease of use, and framerate. It can be used for anything, but is best-suited for Zelda's Torch and duplication.

    === "For Zelda's Torch"

        Prepare:
        - 13 Zuggle Overload
        - 2 DI Ghost Weapons, one for duping, the other dubbed "C"
        - 3 DI Ghost Shields, one for duping, the other two dubbed "A" and "B"
        - A fused equipment item
        - The _second_ prologue autosave
        - An autosave within a shrine (ideally Rasitakiwak)

        Part 1: Performing SFO
        1. Enter Rasitakiwak Shrine, defeat all the constructs, and dispose of their weapons (for example by leaving/reentering)
        2. A1 [Overload FE] Weapon D
        3. [Recall Lock] D
        4. B1 Overload FE Weapon E
        5. Recall Lock E
        6. Smuggle C and equip D
        8. C/D DI Shield F
        9. C Overload FE Shield G
        10. Recall lock G
        11. Smuggle F and equip D
        12. [Overload Pickup] G
        13. F/G [Overload Batch DI] 30 Weapons H1-H30
        14. Fail-drop G and leave it equipped
        15. [Throw Purgatory] all H
        16. [Zuggle Drop] C to "equip" all H
        17. Overload Pickup E
        18. Overload Batch DI **up to** 20 Shields (or Weapons/Bows) I1-I20. Starting with I17, check after each to see if Menu Link is overloaded. If so, proceed to step 19.
        19. Drop your fused item. If the fuse gets deleted, _you are done_. If it doesn't, pick it up and create exactly _one_ more "I", and then you will be done.

        Part 2: Obtaining Zelda's Torch

        20. Load your prologue save. Zelda will drop her torch, so pick it up
        21. Get another prologue autosave with the torch in your inventory, then either load back to Rasitakiwak to clear your SFO, or simply close the game
        22. Follow your preferred method to obtain MNF, but zuggle Zelda's Torch instead
        23. Save the game or get an autosave

        ??? example "Diagram"

            ```mermaid
            graph TD
                B[DI Shield] -->|FE| F[RL Weapon]
                E[DI Shield] -->|FE| G[RL Weapon]
                F -->|Fuse| H[DI Shield]
                C[DI Weapon] -->|FE| H
                C -->|FE| D[Normal Shield]
                H -->|FE| I["30 DI Weapons<br/>(purgatorized)"]
                D -->|CF| I
                I -->|FE| J["20 DI Shields<br/>(or weapons/bows)"]
                G -->|CF| J
            ```

    === "For duplication"

        Prepare:
        - 13 Zuggle Overload
        - 2 DI Ghost Weapons, one for duping, the other dubbed "C"
        - 3 DI Ghost Shields, one for duping, the other two dubbed "A" and "B"
        - A fused equipment item
        - 1 or more of the duplication target

        Part 1: Performing SFO
        1. If duplicating Zonai Devices, enter a minigame with no timer. If duplicating other materials, enter a minigame or a shrine
        2. A1 [Overload FE] Weapon D
        3. [Recall Lock] D
        4. B1 Overload FE Weapon E
        5. Recall Lock E
        6. Smuggle C and equip D
        8. C/D DI Shield F
        9. C Overload FE Shield G
        10. Recall lock G
        11. Smuggle F and equip D
        12. [Overload Pickup] G
        13. F/G [Overload Batch DI] 30 Weapons H1-H30
        14. Fail-drop G and leave it equipped
        15. [Throw Purgatory] all H
        16. [Zuggle Drop] C to "equip" all H
        17. Overload Pickup E
        18. Overload Batch DI **up to** 20 Shields (or Weapons/Bows) I1-I20. Starting with I17, check after each to see if Menu Link is overloaded. If so, proceed to step 19.
        19. Drop your fused item. If the fuse gets deleted, _you are done_. If it doesn't, pick it up and create exactly _one_ more "I", and then you will be done.

        Part 2: Duplicating with SFO
        
        12. Ready a throw of the duplication target. It should fall to the ground
        13. Collect it
        14. Ready throw again. This will "put away" the target you "still had held" and drop another to the ground
        15. Each cycle will increase the quantity of your target by 1, and putting away the final throw will also add 1
        16. Collect the cold-fused materials to end SFO before ending the minigame/exiting the shrine
        
        ??? example "Diagram"

            ```mermaid
            graph TD
                B[DI Shield] -->|FE| F[RL Weapon]
                E[DI Shield] -->|FE| G[RL Weapon]
                F -->|Fuse| H[DI Shield]
                C[DI Weapon] -->|FE| H
                C -->|FE| D[Normal Shield]
                H -->|FE| I["30 DI Weapons<br/>(purgatorized)"]
                D -->|CF| I
                I -->|FE| J["20 DI Shields<br/>(or weapons/bows)"]
                G -->|CF| J
            ```

    === "For Mineru's Arm"

        Prepare:
        - 13 Zuggle Overload
        - 2 DI Ghost Weapons, one for duping, the other dubbed "C"
        - 3 DI Ghost Shields, one for duping, the other two dubbed "A" and "B"
        - Several fused equipment items
        - A portacull Shield (or the materials to make one with [Overload Cold Fuse]

        An save in Rasitakiwak Shrine is recommended, though other shrines (or none at all) will work if you know what you're doing

        Part 1: Performing SFO
        1. Defeat Army and enter the tunnel before Ganondorf.
        2. A1 [Overload FE] Weapon D
        3. [Recall Lock] D
        4. B1 Overload FE Weapon E
        5. Recall Lock E
        6. Smuggle C and equip D
        8. C/D DI Shield F
        9. C Overload FE Shield G
        10. Recall lock G
        11. Smuggle F and equip D
        12. [Overload Pickup] G
        13. F/G [Overload Batch DI] 30 Weapons H1-H30
        14. Fail-drop G and leave it equipped
        15. [Throw Purgatory] all H
        16. [Zuggle Drop] C to "equip" all H
        17. Overload Pickup E
        18. Overload Batch DI **up to** 20 Shields (or Weapons/Bows) I1-I20. Starting with I17, check after each to see if Menu Link is overloaded. If so, proceed to step 19.
        19. Drop your fused item. If the fuse gets deleted, _you are done_. If it doesn't, pick it up and create exactly _one_ more "I", and then you will be done.
        20. Zuggle at least one "I", ideally as many as possible, and enter Ganon's Room.

        Part 2: Obtaining Mineru's Arm

        21. Progress the fight to Phase 2 (2nd form), and drop a fused equipment. The fuse should delete. If not, drop more one at a time until it does
        22. Progress to Phase 3 (sages blown away), and find Mineru
        23. Pick up her arm, which is invisible, collisionless, and repeatedly drops from either visible arm. It cannot be collected with an empty hand. Take several to be safe
        24. Drop your zuggled "I"s and destroy them to reduce SFO, then UNDOCK THE CONSOLE
        25. Fuse something to Mineru's Arm. _If the console is docked, this will crash the game!_
        26. Use the Portacull to Swap Resync Zuggle Mineru's Arm. It will always fail-drop while on the ground, so you don't need a wall or any specific equipment
        27. Load your save in Rasitakiwak
        28. Stand on the grated portion of the wing platform and prepare recall
        29. Drop an equipped weapon and immediately recall the item fused to Mineru's Arm (which still has no collision)
        30. Equip a weapon and pick up Mineru's Arm (it still cannot be collected with an empty hand)
        31. Destroy the fuse on Mineru's Arm, this will prevent it from crashing the game when used as a faildrop wall while docked
        32. Save the game/Get an autosave

        ??? example "Diagram"

            ```mermaid
            graph TD
                B[DI Shield] -->|FE| F[RL Weapon]
                E[DI Shield] -->|FE| G[RL Weapon]
                F -->|Fuse| H[DI Shield]
                C[DI Weapon] -->|FE| H
                C -->|FE| D[Normal Shield]
                H -->|FE| I["30 DI Weapons<br/>(purgatorized)"]
                D -->|CF| I
                I -->|FE| J["20 DI Shields<br/>(or weapons/bows)"]
                G -->|CF| J
                J -->|Take in 1+| K[Ganon's Room]
            ```

=== "Method 3"
    This is a local method that makes use of specially-prepared DI equipment to maximize portability and speed. It is ideal for Mineru's Arm and duplication, but cannot be used for Zelda's Torch.

    (main part of mulberry's method)

    ??? abstract "For Mineru's Arm"
        To obtain Mineru's Arm, perform this setup in the tunnel before Ganondorf

        (extension that tells you how to preserve SFO into the fight, obtain MinArm, and zuggle it out)

    ??? abstract "For Duplication"
        To duplicate Zonai Devices, perform this setup in the [find it] Minigame. For other throwables, simply perform in a shrine.

        (extension that tells you how to dupe with sfo)

=== "Method 4"
    This is a local method with minimal additional glitches required. It is perfectly acceptable for obtaining Mineru's Arm and duplicating throwables on all versions, but cannot be used to obtain Zelda's Torch.

    ??? abstract "For mineru's Arm"

        Prepare:
        - 13 zuggle overload
        - A bow
        - A weapon
        - 2+ unfused shields
        - Several fused equipment items
        - 31+ materials
        - If on 1.2.0+, a Portacull Shield (or the materials to make one via Overload Cold Fuse)
        - A bucket-shaped autobuild with enough Hover Stones to float (and optionally 1-2 Big Batteries)

        Part 1: Performing SFO

        1. Defeat Army and enter the tunnel before Ganondorf
        2. Drop the portacull aside. Be sure not to go too far from any of your working objects
        3. Overload Drop a shield and pick it up to duplicate shields until you have 19 dropped and 3+ spare
        4. Overload Drop a weapon (A) and fuse it to a shield (B)
        5. Overload Cold Fuse 21 shields (C1-C21) to A (the 19 dropped & 2 from inventory)
        6. Fail-drop A and drop B
        7. Overload pick up C1 and cf 30 materials (D1-D30) to it
        8. Fail-drop C1 and set it aside
        9. Repeat 7 for C2-C19 with the same D1-D30
        10. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, proceed to step 11
        11. cf an unrelated material to C(n). If it works, pick it back up and cf the next D, then repeat. If it fails, proceed to step 12
        12. Fail-drop C(n) and drop it. You may have to unequip your bow for it to return
        13. Drop A, not too close to where the barrier will spawn
        14. Collect B, all of C, and all of D into the bucket build
        15. Carry the bucket into Ganondorf's room, holding it high and far aside to keep it out of the way

        Part 2: Obtaining Mineru's Arm

        16. Progress the fight to Phase 2 (2nd form), and drop a fused equipment. The fuse should delete. If not, drop more one at a time until it does
        17. Progress to Phase 3 (sages blown away), and find Mineru
        18. Pick up her arm, which is invisible, collisionless, and repeatedly drops from either visible arm. It cannot be collected with an empty hand. Take several to be safe
        19. Collect the materials in the bucket to undo SFO and UNDOCK THE CONSOLE
        20. Fuse something to Mineru's Arm. _If the console is docked, this will crash the game_
        21. Zuggle Mineru's Arm. It will always fail-drop while on the ground, so either version can be done without a wall
        22. If on `1.1.2` or earlier, Map Zuggle Mineru's Arm
        23. If on `1.2.0` or later, use the portacull to SRZ Mineru's Arm
        24. Load a save. If you undid SFO, there will be no crash risk
        25. Go somewhere you can see a long way down and prepare recall
        26. Drop an equipped weapon and immediately recall the item fused to Mineru's Arm (which still has no collision)
        27. Equip a weapon and pick up Mineru's Arm (it still cannot be collected with an empty hand)
        28. Destroy the fuse on Mineru's Arm, this will prevent it from crashing the game when used as a faildrop wall while docked
        29. Save the game/Get an autosave

        ??? example "Diagram"
        
            ```mermaid
            graph TD
                A[Shield B] -->|Fuse| B[Weapon A]
                B -->|cf| C[Shields C1-C21]
                C -->|cf| D[Materials D1-D30]
                A -->|Take in| E{Ganon Room}
                C -->|Take in| E
                D -->|Take in| E
            ```
    
    ??? abstract "For Duplication"

        Prepare:
        - 13 zuggle overload
        - A bow
        - A weapon
        - 2+ unfused shields
        - A handful of fused equipment items
        - 31+ materials
        - 1+ of the duplication target

        Part 1: Performing SFO

        1. If duplicating Zonai Devices, enter a minigame with no timer. If duplicating materials, enter a minigame or a shrine
        2. Overload Drop a shield and pick it up to duplicate shields until you have 19 dropped and 3+ spare
        3. Overload Drop a weapon (A) and fuse it to a shield (B)
        4. Overload Cold Fuse 21 shields (C1-C21) to A (the 19 dropped & 2 from inventory)
        5. Fail-drop A and drop B
        6. Overload pick up C1 and cf 30 materials (D1-D30) to it
        7. Fail-drop C1 and set it aside
        8. Repeat 7 for C2-C19 with the same D1-D30
        9. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, proceed to step 11
        10. cf an unrelated material to C(n). If it works, pick it back up and cf the next D, then repeat. If it fails, proceed to step 12
        11. Fail-drop C(n) and drop it. You may have to unequip your bow for it to return

        Part 2: Duplicating with SFO

        12. Ready a throw of the duplication target. It should fall to the ground
        13. Collect it
        14. Ready throw again. This will "put away" the target you "still had held" and drop another to the ground
        15. Each cycle will increase the quantity of your target by 1, and putting away the final throw will also add 1
        16. Collect the cold-fused materials to end SFO before ending the minigame/exiting the shrine
        
        ??? example "Diagram"

            ```mermaid
            graph TD
                A{Enter Minigame} -->|Equip| B[Shield B]
                A -->|Overload Drop| C[Weapon A]
                B -->|Fuse| C
                C -->|cf| D[Shields C1-C21]
                D -->|cf| E[Materials D1-D30]
            ```

        (method, then explanation of how to dupe with SFO)

    ??? question "Or can it?"
    
        While it isn't ideal, and is far surpassed by Methods 1 and 2, this method _can_ be made persistent on `1.2.0` and up by permaculling the entire setup. The following adjustments will need to be made to obtain Zelda's Torch:

        - Instead of materials, make D1-D30 additional shields
        - Prepare a Portacull Weapon
        - Optionally, prepare a VD or DI shield (E) to save yourself about 51 SRZs
        - Prepare the _second_ autosave in the prologue, and an autosave in Rasitakiwak Shrine
        - Perform your setup in Rasitakiwak
        
        Then, after reaching SFO:

        1. Equip your portacull weapon
        2. Smuggle E and equip one of B, C, or D
        3. **Pause**
        4. Drop-swap the portacull, and drop your shield
        5. **Pause Buffer** (must be maximum speed)
        6. Equip and unequip any shield
        7. **Unpause**

        This will permacull the shield you dropped. Repeat for _all_ of B, C, and D, ultimately permaculling the entire setup.

        Finally, to obtain Zelda's Torch:

        8. Load your prologue save. Zelda will drop her torch, so pick it up
        9. Get another autosave and close the game to clear SFO
        10. Follow your preffered method to obtain MNF, but zuggle Zelda's Torch back to your progressed save instead
        11. Save the game or get an autosave

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
