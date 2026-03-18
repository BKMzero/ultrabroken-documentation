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

By creating 600-700 Cold Fuse connections, the game will be overloaded and unable to form any new dependencies. This causes every actor to act Zuggle Overloaded, and every equipment to act Fuse Overloaded.

_Discovered by mulberry, Aergyl; Optimizations by Jordan, MandelbrotChaylay, mulberry, Squidwest_

Have decided on tabs with dropdowns, and with the common elements of each method duplicated into said dropdowns. Will consider alternatives

Todo:

- Find a good, stable minigame or two to recommend (minecart land pre-cart entry seems good, provisionally)
- Double check duplication order of operations and correct if needed
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

    (these shall be Mandelbrot's Method)
    (I actually think mine is the better persistent method, but it feels wrong to put mine first)

    ??? abstract "For Zelda's Torch"

        (Mandelbrot's Method with Zorch extension)

    ??? abstract "For duplication"

        (Mandelbrot's Method with duping extension)

    ??? abstract "For Mineru's Arm"

        (Mandelbrot's Method with MinArm extension)
        (assuming the adaptation I devised for my method is valid for his)

=== "Method 2"
    This is a persistent method for versions `1.2.0` and up that makes use of DI equipment to maximize adjustability, ease of use, and framerate. It can be used for anything, but is best-suited for Zelda's Torch and duplication.

    ??? "For Zelda's Torch"

        Prepare:
        
        - 13 Zuggle Overload
        - A bow to manage overload with
        - A DI Ghost Weapon, dubbed "A1"
        - A DI Ghost Shield, dubbed "B1"
        - Ideally, a second of each to simplify duplication
        - Optionally, a fused equipment item
        - The _second_ prologue autosave

        Part 1: Creating the base setup
        
        1. Enter Rasitakiwak Shrine, defeat all the constructs, and dispose of their weapons (for example by leaving/reentering)
        2. B1 [Overload FE] Weapon B2
        3. Recall-Lock B2
        4. A1 and normal weapon A2 [make] DI Shield A3
        5. A1 Overload FE normal Shield A4
        6. Equip A2, [DI Smuggle] A3, and [Overload Pickup] A4
        7. A2-A4 [Overload Batch DI] 19 Weapons C1-C19
        8. *Fail-Drop* A4
        9. A3 & A4 make DI Weapon C20
        10. Drop A4
        11. Re-smuggle A3, equip a random shield, and fuse something disposable to it. This will leave A4 as the sole FE parent of C20
        12. [Throw purgatory] all C
        13. Recall-Lock A4, discarding A2 and A3 through the load

        Part 2: Performing and undoing SFO
        
        1. [DI Zuggle Drop] B1, equip A4, and Overload Pickup B2
        2. B1, B2, & A4 [Overload Batch DI] 30 Shields D1-D30
        3. There will be a substantial lag on the second fuse of each shield after D1, so using the D-pad to drop-swap is advised
        4. Super Fuse Overload should occur on the 30th shield. If confirmation is needed, drop the fused equipment item. If the fuse is deleted, SFO is active
        5. To undo SFO pick up each D[n], unequip it, and drop it. Each removed shield will remove 20 dependencies from the global array

        Part 3: Obtaining Zelda's Torch

        1. Load your prologue save. Zelda will drop her torch, so pick it up
        2. Get another prologue autosave with the torch in your inventory, then either load back to Rasitakiwak to clear your SFO, or simply close the game
        3. Follow your preferred method to obtain MNF, but zuggle Zelda's Torch instead
        4. Save the game or get an autosave

        ??? example "Diagram"

            ```mermaid
            graph TD
                A[B1] -->|FE| B[B2]
                C[A1] -->|DI| D[A3]
                E[A2] -->|DI| D
                C --> |FE| F[A4]
                D --> |Batch DI| G["C1-20"]
                F --> |Batch DI| G
                G --> |Batch DI| H["D1-30"]
                B --> |Batch DI| H
            ```

    ??? abstract "For duplication"

        Prepare:
        - 13 Zuggle Overload
        - A bow to manage overload with
        - A DI Ghost Weapon, dubbed "A1"
        - A DI Ghost Shield, dubbed "B1"
        - Ideally, a second of each to simplify duplication
        - Optionally, a fused equipment item
        - 1 or more of the duplication target
        
        Part 1: Creating the base setup
        
        1. If duplicating Zonai Devices, enter a minigame with no timer. If duplicating other materials, enter a minigame or a shrine
        2. B1 [Overload FE] Weapon B2
        3. Recall-Lock B2
        4. A1 and normal weapon A2 [make] DI Shield A3
        5. A1 Overload FE normal Shield A4
        6. Equip A2, [DI Smuggle] A3, and [Overload Pickup] A4
        7. A2-A4 [Overload Batch DI] 19 Weapons C1-C19
        8. *Fail-Drop* A4
        9. A3 & A4 make DI Weapon C20
        10. Drop A4
        11. Re-smuggle A3, equip a random shield, and fuse something disposable to it. This will leave A4 as the sole FE parent of C20
        12. [Throw purgatory] all C
        13. Recall-Lock A4, discarding A2 and A3 through the load

        Part 2: Performing and undoing SFO
        
        1. [DI Zuggle Drop] B1, equip A4, and Overload Pickup B2
        2. B1, B2, & A4 [Overload Batch DI] 30 Shields D1-D30
        3. There will be a substantial lag on the second fuse of each shield after D1, so using the D-pad to drop-swap is advised
        4. Super Fuse Overload should occur on the 30th shield. If confirmation is needed, drop the fused equipment item. If the fuse is deleted, SFO is active
        5. To undo SFO pick up each D[n], unequip it, and drop it. Each removed shield will remove 20 dependencies from the global array

        Part 3: Duplicating with SFO
        
        12. Ready a throw of the duplication target. It should fall to the ground
        13. Collect it
        14. Ready throw again. This will "put away" the target you "still had held" and drop another to the ground
        15. Each cycle will increase the quantity of your target by 1, and putting away the final throw will also add 1
        16. Destroy all D[n] to end SFO before ending the minigame/exiting the shrine
        
        ??? example "Diagram"

           ```mermaid
            graph TD
                A[B1] -->|FE| B[B2]
                C[A1] -->|DI| D[A3]
                E[A2] -->|DI| D
                C --> |FE| F[A4]
                D --> |Batch DI| G["C1-20"]
                F --> |Batch DI| G
                G --> |Batch DI| H["D1-30"]
                B --> |Batch DI| H
            ```

    ??? abstract "For Mineru's Arm"

        Prepare:
        
        - 13 Zuggle Overload
        - 2 DI Ghost Weapons, one for duping, the other dubbed "C"
        - 3 DI Ghost Shields, one for duping, the other two dubbed "A" and "B"
        - Several fused equipment items
        - A portacull Shield (or the materials to make one with [Overload Cold Fuse]

        An (auto)save in Rasitakiwak Shrine is recommended, though other shrines (or none at all) will work if you know what you're doing.
        Due to requiring recall-locks

        Part 1: Performing SFO
        
        1. Clip into the tunnel before Ganondorf without defeating Army
        2. Sit at a campfire to get an autosave. This will be used to Recall-lock certain setup elements
        3. B1 [Overload FE] Weapon B2
        4. Recall-Lock B2
        5. A1 and normal weapon A2 [make] DI Shield A3
        6. A1 Overload FE normal Shield A4
        7. Equip A2, [DI Smuggle] A3, and [Overload Pickup] A4
        8. A2-A4 [Overload Batch DI] 19 Weapons C1-C19
        9. *Fail-Drop* A4
        10. A3 & A4 make DI Weapon C20
        11. Drop A4
        12. Re-smuggle A3, equip a random shield, and fuse something disposable to it. This will leave A4 as the sole FE parent of C20
        13. [Throw purgatory] all C
        14. Recall-Lock A4, discarding A2 and A3 through the load

        Part 2: Performing SFO

        1. Move to the very start of the tunnel to activate Army, and defeat it. This will activate Panic Blood Moon protection and allow the Ganondorf fight to begin
        2. Use [Overload Cold Fuse] to create a Portacull Shield and set it aside
        2. [DI Zuggle Drop] B1, equip A4, and Overload Pickup B2
        3. B1, B2, & A4 [Overload Batch DI] 30 Shields D1-D30
        4. There will be a substantial lag on the second fuse of each shield after D1, so using the D-pad to drop-swap is advised
        5. Super Fuse Overload should occur on the 30th shield. If confirmation is needed, drop the fused equipment item. If the fuse is deleted, SFO is active
        6. Zuggle at least one D, ideally multiple.
        7. Pick up the Portacull Shield and enter Ganon's Room.

        Part 3: Obtaining Mineru's Arm

        1. Progress the fight to Phase 2 (2nd form), and drop a fused equipment. The fuse should delete. If not, drop more one at a time until it does
        2. Progress to Phase 3 (sages blown away), and find Mineru
        3. Pick up her arm, which is invisible, collisionless, and repeatedly drops from either visible arm. It cannot be collected with an empty hand. Take several to be safe
        4. Drop your zuggled "D"s and destroy them to reduce SFO, then UNDOCK THE CONSOLE
        5. Fuse something to Mineru's Arm. _If the console is docked, this will crash the game!_
        6. Use the Portacull to Swap Resync Zuggle Mineru's Arm. It will always fail-drop while on the ground, so you don't need a wall or any specific equipment
        7. Load your save in Rasitakiwak
        8. Stand on the grated portion of the wing platform and prepare recall
        9. Drop an equipped weapon and immediately recall the item fused to Mineru's Arm (which still has no collision)
        10. Equip a weapon and pick up Mineru's Arm (it still cannot be collected with an empty hand)
        11. Destroy the fuse on Mineru's Arm, this will prevent it from crashing the game when used as a faildrop wall while docked
        12. Save the game/Get an autosave

        ??? example "Diagram"

           ```mermaid
            graph TD
                A[B1] -->|FE| B[B2]
                C[A1] -->|DI| D[A3]
                E[A2] -->|DI| D
                C --> |FE| F[A4]
                D --> |Batch DI| G["C1-20"]
                F --> |Batch DI| G
                G --> |Batch DI| H["D1-30"]
                B --> |Batch DI| H
                H -->|Take in 1+| I[Ganon's Room]
            ```

=== "Method 3"
    This is a local method that makes use of specially-prepared DI equipment to maximize portability and speed. It is ideal for Mineru's Arm and duplication, but cannot be used for Zelda's Torch.

    ??? abstract "For Mineru's Arm"

        (Mulberry's Method with MinArm extension)

    ??? abstract "For Duplication"

        (Mulberry's Method with duping extension)

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
        - Perform your setup in Rasitakiwak, ensuring the absolute maximum overload is reached
        
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
