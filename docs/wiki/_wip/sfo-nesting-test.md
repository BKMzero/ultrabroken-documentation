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

## Summary
---

By creating 600-700 Cold Fuse connections, the game will be overloaded and unable to form any new dependencies. This causes every actor to act Zuggle Overloaded, and every equipment to act Fuse Overloaded.

_Discovered by mulberry, Aergyl; Optimizations by Jordan, MandelbrotChaylay, mulberry, Squidwest_

Have decided on tabs with dropdowns, and with the common elements of each method duplicated into said dropdowns. Will still consider alternatives, especially for mulberry's method due to the intended portability and modularity setting it apart from the others

Todo:

- Find a good, stable minigame or two to recommend (minecart land pre-cart entry seems good, provisionally)
- Recheck duplication method(s)
- Do mulberry's method to more accurately write it up
- Actually obtain Zelda's Torch at some point to provide better directions and warn of the pitfalls
- probably seek help on crediting and resources at some point
- Get some illustrative images, screenshots, and videos going
- write everything after the methods :/
- Run the pre-`1.2.0` aerophasing setup by someone who actually plays an old patch (uh, after you write it)
- Make pages for Overload FE, Overload Batch DI, and just manipulating DI equipped states in general, to make all the steps you abbreviated as pretend page links actually viable

## Forewarnings and Tips
---

!!! danger "Panic!"
    While SFO is active, Panic Blood Moons will constantly occur if they are able (ie on the main map and not in a minigame or cutscene). Additionally, some dependencies will **crash the game** if they fail to form!

!!! info "Buckle up!"
    Due to the massive number of connections required, every method is relatively complex. Before you begin, be sure to read the steps carefully, and be sure you understand the glitches that go into your chosen method.

!!! info "Local or persistent?"
    There are two main types of SFO method: Local methods, which _do not_ persist through warps and loads (including Panic Blood Moons), and Persistent methods, which... _do_ persist through warps and loads.
    Local methods are usually faster and easier, but cannot be used for some cases (eg Zelda's Torch).
    Persistent methods can be used for all cases, but are usually more time consuming and complex.

## Instructions
---

There are three main use cases for SFO: obtaining Mineru's Arm, obtaining Zelda's Torch, and duplicating anything you can throw. For the sake of providing clear instructions, a variant of each method is given for each valid use case.

=== "Method 1: Hand Purgatory + Overload Batch DI"
    This is a persistent method that makes use of DI equipment to maximize adjustability, ease of use, and framerate. It can be used for anything, but is best-suited for Mineru's Arm and Zelda's Torch. As given, its steps are adjusted to work on versions `1.2.0` and up _only_. See below for the adjustments needed to perform it on `1.1.2` and below.

    ??? abstract "For Mineru's Arm (Persistent SFO variant)"

        Prepare:
        
        - 13 Zuggle Overload
        - A bow to manage overload with
        - A DI Ghost Weapon, dubbed "A1"
        - A DI Ghost Shield, dubbed "B1"
        - Ideally, a second of each to simplify duplication
        - Optionally, a fused equipment item

        Part 1: Creating the base setup
        
        1. Ensure Mineru is summoned. This will save some headache later
        2. Enter Rasitakiwak Shrine, defeat all the constructs, and dispose of their weapons (for example by leaving/reentering)
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

        Part 2: Performing and undoing SFO
        
        1. [DI Zuggle Drop] B1, equip A4, and Overload Pickup B2
        2. B1, B2, & A4 [Overload Batch DI] 30 Shields D1-D30
        3. There will be a substantial lag on the second fuse of each shield after D1, so using the D-pad to drop-swap is advised
        4. Super Fuse Overload should occur on the 30th shield. If confirmation is needed, drop the fused equipment item. If the fuse is deleted, SFO is active
        5. To undo SFO pick up each D[n], unequip it, and drop it. Each removed shield will remove 20 dependencies from the global limit

        Part 3: Obtaining Mineru's Arm

        1. Equip a weapon and ensure there is space in your weapon pouch
        2. Warp to Mogisari Shrine at the Lomei Sky Labyrinth. Other low-grav zones may work but are untested
        3. As soon as you gain control, walk in a small clockwise circle while spamming A (see video below)
        4. Execution permitting, you will pick up a new 2-handed weapon, dealing 38 damage, which has no icon, description, model, or collision, and is called MsgNotFound
        5. If you fail, warp to the shrine again to make another attempt. Otherwise, subsequent Panic Blood Moons will occur too frequently to reach the arm in time
        6. About 3 seconds after control is gained, a panic blood moon will occur, which will give an autosave
        7. Either return to Rasitakiwak Shrine to clear SFO, or simply close the game after receiving the above autosave

        ??? example "Diagram"

            ```mermaid
            graph TD
                A[B1] -->|FE| B[B2]
                C[A2] -->|DI| D[A3]
                E[A1] -->|DI| D
                E --> |FE| F[A4]
                D --> |Batch DI| G["C1-20"]
                F --> |Batch DI| G
                G --> |Batch DI| H["D1-30"]
                B --> |Batch DI| H
            ```

    ??? abstract "For Zelda's Torch"

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
        5. To undo SFO pick up each D[n], unequip it, and drop it. Each removed shield will remove 20 dependencies from the global limit

        Part 3: Obtaining Zelda's Torch

        1. Load your prologue save. Zelda will drop her torch, so pick it up
        2. If she does not, try loading again; It may take a few tries for her torch to be one of the connections that fails
        3. Get another prologue autosave with the torch in your inventory, then either load back to Rasitakiwak to clear your SFO, or simply close the game
        4. Follow your preferred method to obtain MNF, but zuggle Zelda's Torch instead
        5. Save the game or get an autosave

        ??? example "Diagram"

            ```mermaid
            graph TD
                A[B1] -->|FE| B[B2]
                C[A2] -->|DI| D[A3]
                E[A1] -->|DI| D
                E --> |FE| F[A4]
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
        
        1. If duplicating Zonai Devices, enter a minigame with no timer, such as Bayge/Heehl's minigames at Mine-Cart Land. If duplicating other materials, enter a minigame _or_ a shrine
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
        5. To undo SFO pick up each D[n], unequip it, and drop it. Each removed shield will remove 20 dependencies from the global limit

        Part 3: Duplicating with SFO
        
        1. Ready a throw of the duplication target. It should fall to the ground
        2. Collect it
        3. Press cancel (B/X). This will "put away" the target Link "still had held", returning it to the pouch
        4. Ready throw again. Each cycle will increase the quantity of your target by 1
        5. Destroy all D[n] to end SFO before ending the minigame/exiting the shrine
        6. Save the game/get an autosave
        
        ??? example "Diagram"

            ```mermaid
            graph TD
                A[B1] -->|FE| B[B2]
                C[A2] -->|DI| D[A3]
                E[A1] -->|DI| D
                E --> |FE| F[A4]
                D --> |Batch DI| G["C1-20"]
                F --> |Batch DI| G
                G --> |Batch DI| H["D1-30"]
                B --> |Batch DI| H
            ```

    ??? info "Adapting for older patches"

        In order to use this method on `1.1.2` and below, where "Drop-Swap Culling" does not exist, an alternate method of culling each DI child must be used. "Aerophasing" is recommended.

        (and, eventually, I'll actually write up how to do it with aerophasing, or at least make a page I can link to...)

    _Method by MandelbrotChaylay and Squidwest_

=== "Method 2: Hand Purgatory + DI"
    This is a local method that makes use of specially-prepared DI equipment to maximize portability and speed. It is ideal for duplication, and can be used for an older, more difficult Mineru's Arm route, but cannot be used for Zelda's Torch.

    (might, if the layout is better, provide the creation of the equipment first, and the extensions below)

    ??? abstract "For Duplication"

        (mulberry's Method with duping extension)

    ??? abstract "For Mineru's Arm (Local SFO variant)"

        (mulberry's Method with MinArm extension (Army Route))

    ??? failure "No, it really can't"
        This method relies on a specialized piece of equipment that takes time to create. While it is technically possible to make the SFO permanent by permaculling E1-E20, it completely nullifies the speed and portability of this method. If a pcull-based permanent method is desired, Method 3 will almost unquestionably be easier.

    _Method by mulberry_

=== "Method 3: Overload Cold Fuse"
    This is a local method with minimal additional glitches required. It is perfectly acceptable for duplicating throwables on all versions, and can obtain Mineru's Arm by an older route. It can also be made permanent, though it's subjectively worse than a proper persistent method.

    ??? abstract "For Duplication"

        Prepare:
        
        - 13 zuggle overload (or 10 on 1.0.0)
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

        1. Ready a throw of the duplication target. It should fall to the ground
        2. Collect it
        3. Press cancel (B/X). This will "put away" the target Link "still had held", returning it to the pouch
        4. Ready throw again. Each cycle will increase the quantity of your target by 1
        5. Collect the cold-fused materials to end SFO before ending the minigame/exiting the shrine
        
        ??? example "Diagram"

            ```mermaid
            graph TD
                A{Enter Minigame} -->|Equip| B[Shield B]
                A -->|Overload Drop| C[Weapon A]
                B -->|Fuse| C
                C -->|cf| D[Shields C1-C21]
                D -->|cf| E[Materials D1-D30]
            ```

    ??? abstract "For mineru's Arm (Local SFO variant)"

        Prepare:
        
        - 13 zuggle overload (or 10 on 1.0.0)
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
    
    ??? info "Making it permanent"
    
        This method can be made permanent by permaculling the entire setup. The method to do so varies depending on version. As the persistent method above is optimized for `1.2.0` and up, the following methods will be given with the necessary adjustments for `1.1.2` and below.

        ??? abstract "For Zelda's Torch"

            Prepare:

            - 13 Zuggle overload (or 10 on 1.0.0) (need to be taught how to perform overload on early patches, since afaik iz isn't an option, or at least not a good one)
            - A bow
            - 2+ unfused weapons
            - 2+ unfused shields
            - Several fused equipment items
            - A material
            - A steering stick
            - A sled or other large object
            - A DI Shield (E)
            - The _second_ prologue autosave
        
             Part 1: Setting up Aerophasing

            (goes over creating an Akkala-citadel-based Aerophasing setup with early-patch strats that can persist into Domizuin)

            Part 2: Performing SFO

            1. Walk up to the nearby shrine ('Domizuin') and enter it. **Do not warp there.**
            2. Overload Drop a shield and pick it up to duplicate shields until you have 19 dropped and 3+ spare
            3. Overload Drop a weapon (A) and fuse it to a shield (B)
            4. Overload Cold Fuse 21 shields (C1-C21) to A (the 19 dropped & 2 from inventory)
            5. Fail-drop A and drop B
            6. Overload pick up C1
            7. Duplicate 30 shields (D1-D30) off the DI shield, dropping each on the ground and CFing them to C1 as you go
            8. Fail-drop C1 and set it aside
            9. Repeat 6-8 for C2-C19 with the same D1-D30
            10. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, proceed to step 11
            11. cf an unrelated material to C(n). If it works, pick it back up and cf the next D, then repeat. If it fails, proceed to step 12
            12. Fail-drop C(n) and drop it. You may have to unequip your bow for it to return, but ensure it does so before you drop it
            13. Drop A

            Part 3: Permaculling the setup

            1. Smuggle E. If E was not prepared, Zuggle any other unrelated shield by your preferred method
            2. Equip one of A, C, or D and step onto the phasing platform. Link will begin **culling** and **unculling** repeatedly
            3. **Pause** the game while Link is **culled**. This will cause Link to consistently be **unculled** when the game is unpaused
            4. **Unpause** the game and immediately **open** the Shield Quick Menu (D-pad Left). If Link is **unculled** behind the menu, **drop** the equipped shield. If not, repeat step 3.
            5. Repeat steps 2-4 for _all_ A, C, and D, ultimately resulting in the entire setup being permaculled

            Part 4: Obtaining Zelda's Torch

            1. Load your prologue save. Zelda will drop her torch, so pick it up
            2. If she does not, try loading again; It may take a few tries for her torch to be one of the connections that fails
            3. Get another autosave and close the game to clear SFO
            4. Follow your preferred method to obtain MNF, but zuggle Zelda's Torch back to your progressed save instead
            5. Save the game or get an autosave

            ??? example "Diagram"
        
                ```mermaid
                graph TD
                    A[Shield B] -->|Fuse| B[Weapon A]
                    B -->|cf| C[Shields C1-C21]
                    C -->|cf| D[Shields D1-D30]
                    A -->|Permacull| E{Persists}
                    C -->|Permacull| E
                    D -->|Permacull| E
                ```
    
        ??? abstract "For Mineru's Arm (persistent SFO variant)"
    
            Prepare:

            - 13 Zuggle overload (or 10 on 1.0.0) (need to be taught how to perform overload on early patches, since afaik iz isn't an option, or at least not a good one)
            - A bow
            - 2+ unfused weapons
            - 2+ unfused shields
            - Several fused equipment items
            - A material
            - A steering stick
            - A sled or other large object
            - A DI shield (E)

            Part 1: Setting up Aerophasing

            (goes over creating an Akkala-citadel-based Aerophasing setup with early-patch strats that can persist into Domizuin)

            Part 2: Performing SFO

            1. Ensure Mineru is summoned. This will save some headache later
            2. Walk up to the nearby shrine ('Domizuin') and enter it. **Do not warp there.**
            3. Overload Drop a shield and pick it up to duplicate shields until you have 19 dropped and 3+ spare
            4. Overload Drop a weapon (A) and fuse it to a shield (B)
            5. Overload Cold Fuse 21 shields (C1-C21) to A (the 19 dropped & 2 from inventory)
            6. Fail-drop A and drop B
            7. Overload pick up C1
            8. Duplicate 30 shields (D1-D30) off the DI shield, dropping each on the ground and CFing them to C1 as you go
            9. Fail-drop C1 and set it aside
            10. Repeat 7-9 for C2-C19 with the same D1-D30
            11. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, proceed to step 12
            12. cf an unrelated material to C(n). If it works, pick it back up and cf the next D, then repeat. If it fails, proceed to step 13
            13. Fail-drop C(n) and drop it. You may have to unequip your bow for it to return, but ensure it does so before you drop it
            14. Drop A

            Part 3: Permaculling the setup

            1. Smuggle E. If E was not prepared, Zuggle any other unrelated shield by your preferred method
            2. Equip one of A, C, or D and step onto the phasing platform. Link will begin **culling** and **unculling** repeatedly
            3. **Pause** the game while Link is **culled**. This will cause Link to consistently be **unculled** when the game is unpaused
            4. **Unpause** the game and immediately **open** the Shield Quick Menu (D-pad Left). If Link is **unculled** behind the menu, **drop** the equipped shield. If not, repeat step 3.
            5. Repeat steps 2-4 for _all_ A, C, and D, ultimately resulting in the entire setup being permaculled

            Part 4: Obtaining Mineru's Arm

            1. Equip a weapon and ensure there is space in your weapon pouch
            2. Warp to Mogisari Shrine at the Lomei Sky Labyrinth. Other low-grav zones may work but are untested
            3. As soon as you gain control, walk in a small clockwise circle while spamming A (see video below)
            4. Execution permitting, you will pick up a new 2-handed weapon, dealing 38 damage, which has no icon, description, model, or collision, and is called MsgNotFound
            5. If you fail, warp to the shrine again to make another attempt. Otherwise, subsequent Panic Blood Moons will occur too frequently to reach the arm in time
            6. About 3 seconds after control is gained, a panic blood moon will occur, which will give an autosave
            7. Hard save the game if desired, then close it to clear SFO

            ??? example "Diagram"
        
                ```mermaid
                graph TD
                    A[Shield B] -->|Fuse| B[Weapon A]
                    B -->|cf| C[Shields C1-C21]
                    C -->|cf| D[Shields D1-D30]
                    A -->|Permacull| E{Persists}
                    C -->|Permacull| E
                    D -->|Permacull| E
                ```

## Notes
---

Have half a mind that these should go on two seperate dedicated pages...

    ??? note "On Mineru's Arm"

        (properties of MinArm to be advised of)

    ??? note "On Zelda's Torch"

        (properties of ZTorch to be advised of)

### Remarks

I'm not really of the mind that these "Notes" subheaders are very critical. I can populate them if needed, but they seem to be a relic of the spreadsheet moreso than something a page of mine would be incomplete without

### Additions
Additions

### Extensions

do suppose SFOFE could be provided here, along with other more niche techniques

## Resources
---

augh I have to add so many references augh augh augh

## Related
---
- [Searchbar Query](search:Searchbar Query)
