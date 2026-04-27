---
title: "Super Fuse Overload"
uid: "BW8"
label: "SFO"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["mulberry, Aergyl, Jordan, MandelbrotChaylay, Squidwest"]
date: "2025-12-06"
description: "By creating 600-700 Cold Fuse connections, the game can be prevented from forming any new dependencies. Mainly used to obtain Mineru's Arm and Zelda's Torch."
aliases: ["super-fuse-overload"]
tags: ["Equipment", "Fuse", "Overload", "Mineru"]
---

# Super Fuse Overload

## Summary

By creating 600-700 Cold Fuse connections, the game will be overloaded and unable to form any new dependencies. This causes every actor to act Zuggle Overloaded, and every equipment to act Fuse Overloaded.

_Discovered by Aergyl, mulberry; Optimizations by Jordan, MandelbrotChaylay, mulberry, Squidwest_

Page Todos:

- Find a good, stable minigame or two to recommend (minecart land pre-cart entry seems good, provisionally, but I'm worried about all the gorons in the area (which iirc will crash if they load during sfo))
- Re-recheck duplication method(s)
- Actually obtain Zelda's Torch at some point to provide better directions and warn of the pitfalls
- Seek help on crediting and resources at some point
- Get some illustrative images, screenshots, and videos going
- write everything else after the methods :/
- Run the pre-`1.2.0` aerophasing setup by someone who actually plays an old patch
- Update/Publish the permalinked pages to ensure nobody drop zuggles to do overload FE in 2026
- (Do we need to make a page for VD/DI state manipulation? Interacting with them in general is different enough that a wiki-user only familiar with standard equipment state manipulation will make a lot of things unnecessarily difficult...)
- I think updating each linked page to include best-practices for DI equipment (and/or entirely unique methods DI enables) is best...

## Forewarnings and Tips

!!! danger "Panic!"
    While SFO is active, Panic Blood Moons will constantly occur if they are able (ie on the main map and not in a minigame or cutscene). Additionally, some dependencies will **crash the game** if they fail to form!

!!! info "Buckle up!"
    Due to the massive number of connections required, every method is relatively complex. Before you begin, be sure to read the steps carefully, and be sure you understand the glitches that go into your chosen method.

!!! info "Method Types"
    There are three types of SFO method:

    - Local methods are usually simpler and easier, but cannot be used for some cases (eg Zelda's Torch) because they will be destroyed on warp (including Panic Blood Moons), load, or excessive distance.
    - Persistent methods are usually more complex, but can be used for all cases due to being protected from unintentional destruction (but still able to be destroyed on purpose).
    - Permacull methods are local methods with all the components permanently culled. This balances usefulness and simplicity, at the cost of needing to close the game to be undone.

## Instructions

There are three main use cases for SFO: obtaining Mineru's Arm, obtaining Zelda's Torch, and duplicating anything you can throw. For the sake of providing clear instructions, a variant of each method is given for each valid use case.

=== "Method 1: Attached Purgatory + Overload Batch DI" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This is a **Persistent** method that makes use of DI equipment to maximize adjustability, ease of use, and framerate. It can be used for anything, but is best-suited for Mineru's Arm and Zelda's Torch.
    - While it is technically possible on `1.1.2` and earlier, the absence of "Drop-Swap Culling" makes it significantly more difficult. Methods 3 and 4 will be faster and easier on those versions (for local and persistent needs, respectively).

    ??? abstract "For Mineru's Arm (Persistent SFO variant)"

        Prepare:
        
        - 13 Zuggle Overload (9 on `1.0.0`)
        - If on `1.1.2` or earlier, Intangible Aerophasing
        - A bow to manage overload with
        - A DI Ghost Weapon, dubbed "A1"
        - A DI Ghost Shield, dubbed "B1"
        - Ideally, a second of each to simplify duplication
        - Optionally, a fused equipment item

        Part 1: Creating the base setup
        
        1. Ensure Mineru is summoned. This will save some headache later
        2. Enter Rasitakiwak Shrine, defeat all the constructs, and dispose of their weapons (for example by leaving/reentering)
        3. B1 [Overload FE](uid:0XV) Weapon B2
        4. [Recall Lock](uid:EY8) B2
        5. A1 and normal weapon A2 [Clone](uid:BEW) DI Shield A3
        6. A1 **Overload FE** normal Shield A4
        7. Equip A2, [Smuggle](uid:TGY) A3, and [Overload Pickup](uid:8QH) A4
        8. A2-A4 [Overload Batch DI](uid:PG3) 19 Weapons C1-C19
        9. **Fail-Drop** A4
        10. A3 & A4 **Clone** DI Weapon C20
        11. **Drop** A4
        12. Re-smuggle A3, equip a random shield, and **Fuse** something disposable to it. This will leave A4 as the sole FE parent of C20
        13. Throw purgatory all C: smuggle any _one_ C[n], equip and throw any random weapon, and unequip that weapon, then repeat
        14. **Recall Lock** A4, discarding A2 and A3 through the load

        Part 2: Performing and undoing SFO
        
        1. [Zuggle Drop](uid:L84) B1, equip A4, and **Overload Pickup** B2
        2. B1, B2, & A4 **Overload Batch DI** 30 Shields D1-D30
        3. There will be a substantial lag on the second fuse of each shield after DI, so using the D-pad to **drop-swap** (if on `1.2.0+`) is advised
        4. _Super Fuse Overload_ should occur on the 30th shield. If confirmation is needed, **drop** the fused equipment item. If the fuse is deleted, SFO is active
        5. To undo SFO: **pick up** each D[n], **unequip** it, and **drop** it. Each removed shield will remove 20 dependencies from the global limit

        Part 3: Obtaining Mineru's Arm

        1. Equip a weapon and ensure there is space in your weapon pouch
        2. Warp to Mogisari Shrine at the Lomei Sky Labyrinth. Other low gravity zones may work, but are untested for stability during SFO
        3. As soon as you gain control, walk in a small clockwise circle while spamming A (see video below)
        4. Execution permitting, you will pick up a new 2-handed weapon, dealing 38 damage, which has no icon, description, model, or collision, and is called MsgNotFound
        5. If unsuccessful, warp to the shrine again to make another attempt. Otherwise, subsequent Panic Blood Moons will occur too frequently to reach the arm in time
        6. If Mineru was not summoned, simply summon her after the warp and treat it as a failed attempt
        6. About 3 seconds after control is gained, a panic blood moon will occur, which will give an autosave
        7. Either return to Rasitakiwak Shrine to clear SFO, or simply close the game after receiving the above autosave

        ??? example "Method Structure Diagram"

            ```mermaid
            graph TD

                B1[B1]
                B2[B2]
                A1[A1]
                A2[A2]
                A3[A3]
                A4[A4]
                PARENTS["Purgatory Parents<br/>(C1-C20)"]
                CHILDREN["DI Children<br/>(D1-D30)"]

                B1 -->|FE| B2
                A2 -->|DI| A3
                A1 -->|DI| A3
                A1 -->|FE| A4
                A3 -->|Batch DI| PARENTS
                A4 -->|Batch DI| PARENTS
                PARENTS -->|Batch DI| CHILDREN
                B2 -->|Batch DI| CHILDREN
            ```

    ??? abstract "For Zelda's Torch"

        Prepare:
        
        - 13 Zuggle Overload (9 on `1.0.0`)
        - If on `1.1.2` or earlier, Intangible Aerophasing
        - A bow to manage overload with
        - A DI Ghost Weapon, dubbed "A1"
        - A DI Ghost Shield, dubbed "B1"
        - Ideally, a second of each to simplify duplication
        - Optionally, a fused equipment item
        - The _second_ prologue autosave

        Part 1: Creating the base setup
        
        1. Enter Rasitakiwak Shrine, defeat all the constructs, and dispose of their weapons (for example by leaving/reentering)
        2. B1 [Overload FE](uid:0XV) Weapon B2
        3. [Recall Lock](uid:EY8) B2
        4. A1 and normal weapon A2 [Clone](uid:BEW) DI Shield A3
        5. A1 **Overload FE** normal Shield A4
        6. Equip A2, [Smuggle](uid:TGY) A3, and [Overload Pickup](uid:8QH) A4
        7. A2-A4 [Overload Batch DI](uid:PG3) 19 Weapons C1-C19
        8. **Fail-Drop** A4
        9. A3 & A4 **Clone** DI Weapon C20
        10. **Drop** A4
        11. Re-smuggle A3, equip a random shield, and **Fuse** something disposable to it. This will leave A4 as the sole FE parent of C20
        12. Throw purgatory all C: smuggle any one_ C[n], equip and throw any random weapon, and unequip that weapon, then repeat
        13. **Recall Lock** A4, discarding A2 and A3 through the load

        Part 2: Performing and undoing SFO
        
        1. [Zuggle Drop](uid:L84) B1, equip A4, and **Overload Pickup** B2
        2. B1, B2, & A4 **Overload Batch DI** 30 Shields D1-D30
        3. There will be a substantial lag on the second fuse of each shield after D1, so using the D-pad to **drop-swap** (if on `1.2.0+`) is advised
        4. _Super Fuse Overload_ should occur on the 30th shield. If confirmation is needed, **drop** the fused equipment item. If the fuse is deleted, SFO is active
        5. To undo SFO: **pick up** each D[n], **unequip** it, and **drop** it. Each removed shield will remove 20 dependencies from the global limit

        Part 3: Obtaining Zelda's Torch

        1. Load the prologue autosave. Zelda will drop her torch, so pick it up
        2. If she does not, try loading again; It may take a few tries for her torch to be one of the dependencies that fails
        3. Get another prologue autosave with the torch in the inventory, then either load back to Rasitakiwak to clear SFO, or simply close the game
        4. Follow your preferred method to obtain MNF, but zuggle/SLD Zelda's Torch instead
        5. Save the game or get an autosave

        ??? example "Method Structure Diagram"

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
        - 13 Zuggle Overload (9 on `1.0.0`)
        - If on `1.1.2` or earlier, Intangible Aerophasing
        - A bow to manage overload with
        - A DI Ghost Weapon, dubbed "A1"
        - A DI Ghost Shield, dubbed "B1"
        - Ideally, a second of each to simplify duplication
        - Optionally, a fused equipment item
        - 1 or more of the duplication target
        
        Part 1: Creating the base setup
        
        1. If duplicating Zonai Devices, enter a minigame with no timer, such as Bayge/Heehl's minigames at Mine-Cart Land. If duplicating other materials, enter a minigame _or_ a shrine
        2. B1 [Overload FE](uid:0XV) Weapon B2
        3. [Recall Lock](uid:EY8) B2
        4. A1 and normal weapon A2 [Clone](uid:BEW) DI Shield A3
        5. A1 **Overload FE** normal Shield A4
        6. Equip A2, [Smuggle](uid:TGY) A3, and [Overload Pickup](uid:8QH) A4
        7. A2-A4 [Overload Batch DI](uid:PG3) 19 Weapons C1-C19
        8. **Fail-Drop** A4
        9. A3 & A4 **Clone** DI Weapon C20
        10. **Drop** A4
        11. Re-smuggle A3, equip a random shield, and **Fuse** something disposable to it. This will leave A4 as the sole FE parent of C20
        12. Throw purgatory all C: smuggle any _one_ C, equip and throw any random weapon, and unequip that weapon, then repeat
        13. **Recall Lock** A4, discarding A2 and A3 through the load

        Part 2: Performing and undoing SFO
        
        1. [Zuggle Drop](uid:L84) B1, equip A4, and **Overload Pickup** B2
        2. B1, B2, & A4 **Overload Batch DI** 30 Shields D1-D30
        3. There will be a substantial lag on the second fuse of each shield after D1, so using the D-pad to **drop-swap** (if on `1.2.0+`) is advised
        4. _Super Fuse Overload_ should occur on the 30th shield. If confirmation is needed, **drop** the fused equipment item. If the fuse is deleted, SFO is active
        5. To undo SFO: **pick up** each D[n], **unequip** it, and **drop** it. Each removed shield will remove 20 dependencies from the global limit

        Part 3: Duplicating with SFO

        ??? abstract "Throw Hold Duplication (devices or materials)"

            1. Ready a **throw** of the duplication target. It should fall to the ground
            2. **Collect it** by stepping backwards and pressing A
            3. Press **cancel** (B/X). This will "put away" the target Link "still had held", returning it to the pouch
            4. Ready **throw** again. Each cycle will increase the quantity of the target by 1
            5. **Destroy** all D[n] to end SFO before ending the minigame/exiting the shrine
            6. Save the game/get an autosave

        ??? abstract "SFO BID (materials only)"

            1. **Pause**, hold 1 random material and **unpause**. It will fall from Link's cupped hands
            2. Press A to **drop** the material. Link will still do the dropping animation
            3. Hold 1 of the same material(?) and 4 of the duplication target. These will not appear in the world
            4. Ready throw with the same material(???). This will make the duplication targets appear on the ground as well
            5. Throw will need to stay readied from here out. It can be cancelled with B if necessary, so long as it is re-readied before continuing
            6. **Collect** the 5 materials on the ground
            7. **Pause**, un-hold the 4 duplication targets, and re-hold 4 duplication targets (they can be different)
            8. **Unpause** and **collect** the 4 materials on the ground
            9. Repeat steps 7 and 8 to satisfaction
            10. **Destroy** all D[n] to end SFO before ending the minigame/exiting the shrine

        ??? example "Method Structure Diagram"

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

    _SFO Method developed by MandelbrotChaylay and Squidwest_

=== "Method 2: Attached Purgatory + DI" ###
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This is a **Local** method that makes use of a specially-prepared equipment item to maximize portability and in-the-moment speed. It is ideal for duplication, and can be used for Mineru's Arm by an older route, but cannot be used for Zelda's Torch.
    - While it is technically possible on `1.1.2` and earlier, the absence of "Drop-Swap Culling" makes it significantly more difficult. Methods 3 and 4 will be faster and easier on those versions (for local and persistent needs, respectively).

    #### The equipment ?

    - In summary, make a DI Ghost shield with 30-32 DI Ghost weapons Cold Fused to it, then purgatorize all the weapons so that they can all be "equipped" at once by zuggle dropping the shield.
    - The steps given will use [this method](uid:BEW#method-2-overload-pf-torch-culling-all-versions) of Batch DI to create the first 30 weapons, which is usually plenty.
    - Afterwards, it will use [this method](uid:BEW#ghost-despawn-interrupt#method-1-fuse-drop-swap-120) of Ghost DI to create the final 2 weapons, which are helpful for reaching sfo but not mandatory.
    - Apparently by "will use" I don't mean "later in the page" I mean "when I write it"
    - Sorry about this one I mistook the basics of this method and had to completely rewrite it

    Prepare:

    - 13 Zuggle Overload (9 on 1.0.0)
    - A DI Shield `A`
    - A Torch
    - A Flame Emitter

    Steps:

    1. Follow the torch culling thing verbatim until 30 DI weapons have been created with `C` as DI Parent
    2. Safely delete both of C's parents
    3. Use C to make 2 more DI weapons and delete the normal parents
    4. Smuggle a DI weapon, then equip a random weapon and throw it, then unequip random
    5. Repeat for all weapons
    6. I think my head's not in this right now sorry
    7. I'll fix it and add a pre-1.2.0 method when my brain is workin right (and restore the all versions badge)

    #### For Duplication ?

    Prepare:

    - The special equipment
    - Up to 21 materials (optional)
    - A DI Weapon to dupe with (optional, you _are_ expected to have overload at this point and that dupes just fine)

    Part 1: Setting up and destroying SFO

    1. Enter a minigame with no timer. If only materials (and not Zonai Devices) are to be duped, a shrine will also work
    2. Zuggle Drop C to attach the 32 weapons to Link
    3. Dupe a weapon `A1` and equip it
    4. A1 [Ghost DI](uid:BEW) Material/equipment `B1`. **Do not detangle or delete A1.**
    5. **Repeat** until attempting to fuse B[n] to A[n] fails (18-21 repetitions are expected depending on environment); Menu Link should be overloaded at this point
    6. To destroy SFO, simply inventory pickup each A[n], or exit shrine if in one. Distance despawn _will not fully work_ due to the properties of DI
    7. If safety is preferred, use equipment for all B[n] instead of materials. This way, if A[n] is destroyed by drop limit/distance, B[n] can still be manually destroyed to clear the dependencies.

    Part 2: Duplicating with SFO

    ??? abstract "Throw Hold Duplication (devices or materials)"

        1. Ready a **throw** of the duplication target. It should fall to the ground
        2. **Collect** it
        3. Press **cancel** (B/X). This will "put away" the target Link "still had held", returning it to the pouch
        4. Ready **throw** again. Each cycle will increase the quantity of the target by 1
        5. **Inventory pickup** all A[n] to end SFO before ending the minigame (shrine exit will end SFO automatically)
        6. Save the game/get an autosave

    ??? abstract "SFO BID (materials only)"

        1. **Pause**, hold 1 random material and **unpause**. It will fall from Link's cupped hands
        2. Press A to drop the material. Link will still do the dropping animation
        3. Hold 1 of the same material(?) and 4 of the duplication target. These will not appear in the world
        4. Ready **throw** with the same material(???). This will make the duplication targets appear on the ground as well
        5. Throw will need to stay readied from here out. It can be cancelled with B if necessary, so long as it is re-readied before continuing
        6. **Collect** the 5 materials on the ground
        7. **Pause**, un-hold the 4 duplication targets, and re-hold 4 duplication targets (they can be different)
        8. **Unpause** and **collect** the 4 materials on the ground
        9. Repeat steps 7 and 8 to satisfaction
        10. **Inventory pickup** all A[n] to end SFO before ending the minigame (shrine exit will end SFO automatically)
        11. Save the game/get an autosave

    - Throw hold is slower but does devices
    - SFO BID is faster but doesn't
    - It's a little faster than normal BID iirc? I'll get back to you on that

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            SPECIAL["Special Equipment's 32<br/>Purgatory Weapons"]
            PARENTS["Normal Parents<br/>(A1-A21)"]
            CHILDREN["DI Children<br/>(B1-B21)"]

            SPECIAL -->|"Fuse<br/>(becomes CF)"| CHILDREN
            PARENTS -->|"Fuse<br/>(stays attached)"| CHILDREN
        ```

    #### For Mineru's Arm (Local SFO variant) ?

    Prepare:

    - The special equipment
    - Up to 21 materials
    - A DI Weapon to dupe with
    - A Portacull Shield or the means to make one portably

    Part 1: Setting up SFO

    1. Defeat Army and enter the tunnel before Ganondorf
    2. Zuggle C to attach the 32 weapons to Link
    3. Dupe a weapon `A1` and equip it
    4. A1 [Ghost DI](uid:BEW) DI Material or equipment `B1`; **Do not detangle or delete A1.**
    5. **Repeat** until attempting to fuse B[n] to A[n] fails (18-21 repetitions are expected); Menu Link should be overloaded at this point
    6. Glue all A[n] together and ultrahand them into Ganon's Room, holding them far aside to keep them out of the way

    Part 2: Obtaining Mineru's Arm

    1. Progress the fight to Phase 2 (2nd form), and **drop** a fused equipment. The fuse should delete. If not, **drop** more one at a time until it does
    2. Progress to Phase 3 (sages blown away), and find Mineru
    3. **Pick up** her arm, which is invisible, collisionless, and repeatedly drops from either visible arm. It cannot be collected with an empty hand when undiscovered. Take several to be safe
    4. **Inventory pickup** all A[n] to undo SFO and UNDOCK THE CONSOLE
    5. **Fuse** something to Mineru's Arm. _If the console is docked, this will crash the game_
    6. Zuggle Mineru's Arm. It will always fail-drop while on the ground, so either version can be done without a wall
    7. If on `1.1.2` or earlier, Map Zuggle Mineru's Arm
    8. If on `1.2.0` or later, use the portacull to SRZ Mineru's Arm
    9. Load a save. If you undid SFO, there will be no crash risk
    10. Go somewhere you can see a long way down and prepare recall (atop a Hover Stone raised with a Rocket is excellent)
    11. Drop an equipped weapon and immediately recall the item fused to Mineru's Arm (which still has no collision)
    12. Equip a weapon and pick up Mineru's Arm (it reverts to undiscovered, so it still cannot be collected with an empty hand)
    13. Destroy the fuse on Mineru's Arm, this will prevent it from crashing the game when used as a faildrop wall while docked
    14. Save the game/Get an autosave

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            SPECIAL["Special Equipment's 32<br/>Purgatory Weapons"]
            PARENTS["Normal Parents<br/>(A1-A21)"]
            CHILDREN["DI Children<br/>(B1-B21)"]

            SPECIAL -->|"Fuse<br/>(becomes CF)"| CHILDREN
            PARENTS -->|"Fuse<br/>(stays attached)"| CHILDREN
        ```

    #### Nope

    ??? failure "No, it really can't"
    
    - While it is technically possible to make the SFO permanent by permaculling all A[n], it completely nullifies the speed and portability of this method.
    - If a pcull-based permanent method is desired, Method 4 will almost unquestionably be easier, faster, and simpler.

    _SFO Method developed by mulberry_

=== "Method 3: Overload Cold Fuse" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This is a **Local** method with minimal additional glitches required. It is perfectly acceptable for duplicating throwables on all versions, and can obtain Mineru's Arm by an older route. It can also be made permanent via permacull; This is provided as Method 4 for clarity.

    ??? abstract "For Duplication"

        Prepare:
        
        - 13 zuggle overload (9 on `1.0.0`)
        - A bow
        - A weapon
        - 2+ unfused shields
        - A handful of fused equipment items
        - 31+ materials
        - 1+ of the duplication target

        Part 1: Performing SFO

        1. If duplicating Zonai Devices, enter a minigame with no timer. If duplicating materials, enter a minigame or a shrine
        2. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
        3. **Overload Drop** a weapon (A) and **Fuse** it to a shield (B)
        4. [Overload Cold Fuse](uid:O64) 21 shields (C1-C21) to A (the 19 dropped & 2 from inventory)
        5. **Fail-drop** A and **drop** B
        6. [Overload Pickup](uid:8QH) C1 and **Overload Cold Fuse** 30 materials (D1-D30) to it
        7. **Fail-drop** C1 and **drop** it aside
        8. Repeat 7 for C2-C19 with the **same** D1-D30
        9. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, _proceed to step 11_
        10. **Overload Cold Fuse** an unrelated material to C[n]. If it works, **collect it** and **Overload Cold Fuse** the next D[n], then repeat. If it fails, _proceed to step 12_
        11. **Fail-drop** C(n) and **drop** it. You may have to **unequip your bow** for it to return. **Be sure it does so before dropping it.**

        Part 2: Duplicating with SFO

        ??? abstract "Throw Hold Duplication (devices or materials)"
        
            1. Ready a **throw** of the duplication target. It should fall to the ground
            2. **Collect it** by stepping backwards and pressing A
            3. Press **cancel** (B/X). This will "put away" the target Link "still had held", returning it to the pouch
            4. Ready **throw** again. Each cycle will increase the quantity of the target by 1
            5. **Collect** the cold-fused materials to end SFO before ending the minigame/exiting the shrine
            6. Save the game/get an autosave

        ??? abstract "SFO BID (materials only)"

            1. **Pause**, hold 1 random material and **unpause**. It will fall from Link's cupped hands
            2. Press A to **drop** the material. Link will still do the dropping animation
            3. Hold 1 of the same material(?) and 4 of the duplication target. These will not appear in the world
            4. Ready throw with the same material(???). This will make the duplication targets appear on the ground as well
            5. Throw will need to stay readied from here out. It can be cancelled with B if necessary, so long as it is re-readied before continuing
            6. **Collect** the 5 materials on the ground
            7. **Pause**, un-hold the 4 duplication targets, and re-hold 4 duplication targets (they can be different)
            8. **Unpause** and **collect** the 4 materials on the ground
            9. Repeat steps 7 and 8 to satisfaction
            10. **Collect** the cold-fused materials to end SFO before ending the minigame/exiting the shrine
            11. Save the game/get an autosave

        ??? example "Method Structure Diagram"

            ```mermaid
            graph TD
                A{"Enter Minigame/Shrine"} -->|Equip| B[Shield B]
                A -->|Overload Drop| C[Weapon A]
                B -->|Fuse| C
                C -->|cf| D[Shields C1-C21]
                D -->|cf| E[Materials D1-D30]
            ```

    ??? abstract "For mineru's Arm (Local SFO variant)"

        Prepare:
        
        - 13 zuggle overload (9 on `1.0.0`)
        - A bow
        - A weapon
        - 2+ unfused shields
        - Several fused equipment items
        - 31+ materials
        - If on 1.2.0+, a Portacull Shield (or the materials to make one via Overload Cold Fuse)
        - A bucket-shaped autobuild with enough Hover Stones to float (and optionally 1-2 Big Batteries)

        Part 1: Performing SFO

        1. Defeat Army and enter the tunnel before Ganondorf
        2. Drop the portacull aside. Be sure not to go too far from any of the working objects (about halfway down the tunnel is fine)
        3. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
        4. **Overload Drop** a weapon (A) and **Fuse** it to a shield (B)
        5. [Overload Cold Fuse](uid:O64) 21 shields (C1-C21) to A (the 19 dropped & 2 from inventory)
        6. **Fail-drop** A and **drop** B
        7. [Overload Pickup](uid:8QH) C1 and **Overload Cold Fuse** 30 materials (D1-D30) to it
        8. **Fail-drop** C1 and **drop** it aside
        9. Repeat 7 for C2-C19 with the **same** D1-D30
        10. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, _proceed to step 11_
        11. **Overload Cold Fuse** an unrelated material to C[n]. If it works, **collect it** and **Overload Cold Fuse** the next D[n], then repeat. If it fails, _proceed to step 12_
        12. **Fail-drop** C(n) and **drop** it. You may have to **unequip your bow** for it to return. **Be sure it does so before dropping it.**
        13. **Drop** A, not too close to where the barrier will spawn (it cannot be moved after dropping it!)
        14. Move B, all of C, and all of D into the bucket build
        15. Carry the bucket into Ganondorf's room, holding it high and far aside to keep it out of the way of the fight

        Part 2: Obtaining Mineru's Arm

        16. Progress the fight to Phase 2 (2nd form), and **drop** a fused equipment. The fuse should delete. If not, **drop** more one at a time until it does
        17. Progress to Phase 3 (sages blown away), and find Mineru
        18. **Pick up** her arm, which is invisible, collisionless, and repeatedly drops from either visible arm. It cannot be collected with an empty hand. Take several to be safe
        19. **Collect** the materials in the bucket to undo SFO and UNDOCK THE CONSOLE
        20. **Fuse** something to Mineru's Arm. _If the console is docked, this will crash the game_
        21. Zuggle Mineru's Arm. It will always fail-drop while on the ground, so either version can be done without a wall
        22. If on `1.1.2` or earlier, Map Zuggle Mineru's Arm
        23. If on `1.2.0` or later, use the portacull to SRZ Mineru's Arm
        24. Load a save. If you undid SFO, there will be no crash risk
        25. Go somewhere you can see a long way down and prepare recall (atop a Hover Stone raised with a Rocket is excellent)
        26. **Drop** an equipped weapon and immediately **recall** the item fused to Mineru's Arm (which still has no collision)
        27. **Equip** a weapon and **pick up** Mineru's Arm (it still cannot be collected with an empty hand)
        28. **Destroy** the fuse on Mineru's Arm, this will prevent it from **crashing the game** when used as a faildrop wall while docked
        29. Save the game/Get an autosave

        ??? example "Method Structure Diagram"
        
            ```mermaid
            graph TD
                A[Shield B] -->|Fuse| B[Weapon A]
                B -->|cf| C[Shields C1-C21]
                C -->|cf| D[Materials D1-D30]
                A -->|Take in| E{Ganon Room}
                C -->|Take in| E
                D -->|Take in| E
            ```

    _Method by Aergyl and mulberry_ (needs double-checked; this was a little before my time)

=== "Method 4: Overload Cold Fuse + Permacull" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This is a **Permacull** method with minimal additional glitches required. It is acceptable for Zelda's Torch and Mineru's Arm.
    - It _can_ be used for duplication, but is needlessly complex and hazardous for this usage; Use Method 3 instead.
    - The steps given are specialized for `1.1.2` and below. They will work on `1.2.0+`, but are inefficient.

    ??? abstract "For Zelda's Torch"

        Prepare:

        - 13 Zuggle overload (9 on `1.0.0`)
        - Intangible Aerophasing (guide assumes this is set up at Akkala Citadel Ruins)
        - A bow
        - 2+ unfused weapons
        - 2+ unfused shields
        - Several fused equipment items
        - A material
        - A DI Shield (E)
        - The _second_ prologue autosave

        Part 1: Performing SFO

        1. Use the Aerophasing setup to ensure it has a cull stored; this will allow the culling area to remain loaded through a banc change
        2. Walk up to the nearby shrine ("Domizuin") and enter it. **Do not warp there.**
        3. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
        4. **Overload Drop** a weapon (A) and fuse it to a shield (B)
        5. [Overload Cold Fuse](uid:O64) 21 shields (C1-C21) to A (the 19 dropped & 2 from inventory)
        6. **Fail-drop** A and **drop** B
        7. [Overload Pickup](uid:8QH) C1
        8. Duplicate 30 shields (D1-D30) off the DI shield, dropping each on the ground and **Overload Cold Fusing** them to C1 as you go
        9. **Fail-drop** C1 and **drop** it aside
        10. Repeat 7-9 for C2-C19 with the **same** D1-D30
        11. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, _proceed to step 11_
        12. **Overload Cold Fuse** an unrelated material to C[n]. If it works, **Collect it** and **Overload Cold Fuse** the next D[n], then repeat. If it fails, _proceed to step 12_
        13. **Fail-drop** C(n) and **drop** it. You may have to **unequip your bow** for it to return. **Be sure it does so before dropping it.**
        14. **Drop** A

        Part 2: Permaculling the setup

        1. [Smuggle](uid:TGY) E. If E was not prepared, Zuggle any other unrelated shield by your preferred method
        2. Equip one of B, C, or D and step onto the phasing platform
        3. **Pause** the game while Link is **culled**. This will cause Link to consistently be **unculled** when the game is unpaused
        4. **Unpause** the game and immediately **open** the Shield Quick Menu (D-pad Left). If Link is **unculled** behind the menu, **drop** the equipped shield. If not, repeat step 3.
        5. Repeat steps 2-4 for _all_ B, C, and D, ultimately resulting in the entire setup being permaculled

        Part 3: Obtaining Zelda's Torch

        1. Load your prologue save. Zelda will drop her torch, so pick it up
        2. If she does not, try loading again; It may take a few tries for her torch to be one of the dependencies that fails
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
                B -->|Indirect Permacull| E
            ```
    
    ??? abstract "For Mineru's Arm (persistent SFO variant)"

        Prepare:

        - 13 Zuggle overload (9 on `1.0.0`)
        - Intangible Aerophasing (guide assumes this is set up at Akkala Citadel Ruins)
        - A bow
        - 2+ unfused weapons
        - 2+ unfused shields
        - Several fused equipment items
        - A material
        - A DI shield (E)

        Part 1: Performing SFO

        1. Ensure Mineru is summoned. This will save some headache later
        2. Use the Aerophasing setup to ensure it has a cull stored; this will allow the culling area to remain loaded through _a_ banc change
        3. Walk up to the nearby shrine ("Domizuin") and enter it. **Do not warp there.**
        4. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
        5. **Overload Drop** a weapon (A) and fuse it to a shield (B)
        6. [Overload Cold Fuse](uid:O64) 21 shields (C1-C21) to A (the 19 dropped & 2 from inventory)
        7. **Fail-drop** A and **drop** B
        8. [Overload Pickup](uid:8QH) C1
        9. Duplicate 30 shields (D1-D30) off the DI shield, dropping each on the ground and **Overload Cold Fusing** them to C1 as you go
        10. **Fail-drop** C1 and **drop** it aside
        11. Repeat 8-10 for C2-C19 with the same D1-D30
        12. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, proceed to step 12
        13. **Overload Cold Fuse** an unrelated material to C[n]. If it works, pick it back up and **Overload Cold Fuse** the next D[n], then repeat. If it fails, proceed to step 13
        14. **Fail-drop** C(n) and **drop** it. You may have to unequip your bow for it to return. **Be sure it does so before dropping it.**
        15. **Drop** A

        Part 2: Permaculling the setup

        1. [Smuggle](uid:TGY) E. If E was not prepared, Zuggle any other unrelated shield by your preferred method
        2. Equip one of B, C, or D and step onto the phasing platform
        3. **Pause** the game while Link is **culled**. This will cause Link to consistently be **unculled** when the game is unpaused
        4. **Unpause** the game and immediately **open** the Shield Quick Menu (D-pad Left). If Link is **unculled** behind the menu, **drop** the equipped shield. If not, repeat step 3.
        5. Repeat steps 2-4 for _all_ B, C, and D, ultimately resulting in the entire setup being permaculled

        Part 3: Obtaining Mineru's Arm

        1. Equip a weapon and ensure there is space in your weapon pouch
        2. Warp to Mogisari Shrine at the Lomei Sky Labyrinth. Other low-gravity zones may work, but are untested for stability under SFO
        3. As soon as you gain control, walk in a small clockwise circle while mashing A (see video below)
        4. Execution permitting, you will pick up a new 2-handed weapon, dealing 38 damage, which has no icon, description, model, or collision, and is called MsgNotFound
        5. If unsuccessful, warp to the shrine again to make another attempt. Otherwise, subsequent Panic Blood Moons will occur too frequently to reach the arm in time
        6. If Mineru was not summoned, simply do so after the first warp and treat it as a failed attempt
        7. About 3 seconds after control is gained, a panic blood moon will occur, which will give an autosave
        8. Hard save the game if desired, then close it to clear SFO

        ??? example "Method Structure Diagram"

            ```mermaid
            graph TD

                LINK[Link]
                AERO[Aerophasing]
                LOCATION[Shrine]
                A[Weapon A]
                B[Shield B]
                C["Shields<br/>C1-C21"]
                D["Shields<br/>D1-D30"]
                PERMACULL[Permacull]
                STATE[Permanent]

                LINK -->|Store cull| AERO
                LINK -->|"Enter without<br/>warping"| LOCATION
                AERO -->|"Still works<br/>inside"| LOCATION
                LINK -->|Equip| B
                LINK -->|Overload Drop| A
                B -->|Fuse| A
                A -->|CF| C
                C -->|CF| D
                AERO -->|Allows| PERMACULL
                B -->|Directly| PERMACULL
                C -->|Directly| PERMACULL
                D -->|Directly| PERMACULL
                A -->|Indirectly| PERMACULL
                PERMACULL -->|Makes| STATE
            ```

## Properties

- The global dependency heap is full, so no new dependencies can be registered
- Every newly-loaded NPC and enemy will overload drop everything they're carrying
- Many such overload drops will crash the game (presumably due to missing code for interacting with the world as a dropped item?)
- Every newly-loaded fused equipment item will lose its fuse (It will detangle for one frame and then be deleted)
- This does not de-fuse the item in the inventory

## Tips and Additional Uses

- Link's equipment can be used for fine-grained control over the final few dependency slots. With a bow, fused shield, fused weapon (and its sheath), and fully synced armor, up to 9 dependencies are fully controllable.
- SFO bypasses normal SDC protection on `1.2.0` and up, allowing any mountable object to be SDC'd simply by mounting
- Depths Ghosts will despawn without having ever taken ownership of their weapons, allowing for Kinematic Weapons to be obtained without fusing them
- Every attempt at fusing something will cause Fuse Overload Fuse Storage, allowing for [Fuse Overload Fuse Entanglement](uid:G8Q) without performing actual Fuse Overload

### Credits

I might end up distributing this into the right places but idk. Maybe both, for maximum referencing speed?

- SFO discovered by Aergyl, mulberry(?)
- Mineru's Arm (local route) found by (???)
- Zelda's Torch found by (???)
- SFO Throw Duplication found by (???)
- SFO BID found by mulberry
- Mineru's Arm (peristent route) found by Squidwest
- SFOFE by mulberry(?)
- SFO KW found by Squidwest

- Hand Purg + Batch DI SFO by MandelbrotChaylay, Squidwest
- Hand Purg + non-batch DI SFO by mulberry
- Overload Cold Fuse SFO by (probably also Aergyl and mulberry, this was the og method)
- (Method 4 is really only an extension of Method 3, so I don't think it even _has_ seperate credits?)

(it needs to be cleaned up and dated before anything else)

## Resources

Behold all my empty reference links (I don't want to do this right now but I do want to figure out what I even need to go track down)

- [Original Discovery]()
- [Original Mineru's Arm Get]()
- [Original Zelda's Torch Get]()
- [SFO Throw Duplication]()
- [Original Hand Purg + BDI Method]()
- [Optimized Hand Purg + BDI Method]()
- [Hand Purg + DI Method]()
- [SFOFE]()
- [Easier Mineru's Arm Route]()
- [SFO BID]()
- [SFO KW]()

## Related
- [Searchbar Query](search:Searchbar Query)
