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

_Discovered by mulberry; Optimizations by Aergyl, Jordan, MandelbrotChaylay, mulberry, Squidwest_

Page Todos:

- Find better minigames to recommend
- Re-recheck duplication method(s)
- Actually obtain Zelda's Torch at some point to provide better directions and warn of the pitfalls
- Get some illustrative images, screenshots, and videos going
- Run the pre-`1.2.0` aerophasing setup by someone who actually plays an old patch
- Update/Publish the permalinked pages to include missing modern methods & tech
- Additionally, update the permalinked pages to include DI tech wherever needed/practical

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

There are three main use cases for SFO: obtaining Mineru's Arm, obtaining Zelda's Torch, and duplicating any material or zonai device. For the sake of providing clear instructions, a variant of each method is given for each valid use case.

=== "Method 1: Attached Purgatory + Overload Batch DI" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    #### Basic info ?
    ---
    notoc: true
    ---

    - This is a **Persistent** method that makes use of DI equipment to maximize adjustability, ease of use, and framerate. 
    - It can be used for anything, but is best-suited for Mineru's Arm and Zelda's Torch.
    - While it is technically possible on `1.1.2` and earlier, the absence of "Drop-Swap Culling" makes it significantly more difficult.
    - Methods 3 and 4 will be faster and easier on those versions (for local and persistent needs, respectively).

    _Method developed by MandelbrotChaylay, Squidwest; Optimized by MandelbrotChaylay, mulberry, Squidwest_

    #### For Mineru's Arm (Persistent SFO variant) ?

    ##### Prepare:
    ---
    notoc: true
    ---

    - 13 Zuggle Overload (9 on `1.0.0`)
    - If on `1.1.2` or earlier, Intangible Aerophasing
    - A bow to manage overload with
    - A DI Ghost Weapon `A1`
    - A DI Ghost Shield `B1`
    - Ideally, a second of each to simplify duplication
    - Optionally, a fused equipment item

    ##### Part 1: Creating the base setup
    ---
    notoc: true
    ---
    
    1. Ensure Mineru is summoned. This will save some headache later
    2. Enter Rasitakiwak Shrine, defeat all the constructs, and dispose of their weapons (for example by leaving/reentering)
    3. (Many other shrines may be used; Rasitakiwak is simply one valid option)
    4. B1 [Overload FE](uid:0XV#method-3-vddi-smugglezuggle) weapon `B2`
    5. [Recall Lock](uid:EY8) B2
    6. A1 and normal weapon `A2` [Ghost DI](uid:BEW#method-1-fuse-drop-swap-120) shield `A3`
    7. A1 **Overload FE** normal Shield `A4`
    8. Equip A2, [Smuggle](uid:TGY) A3, and [Overload Pickup](uid:8QH) A4
    9. A2-A4 [Overload Batch DI](uid:PG3#method-1-overload-pf-drop-swap-culling-120) 19 weapons `C1-C19`
    10. **Fail-Drop** A4
    11. A3 & A4 **Ghost DI** weapon `C20`
    12. **Drop** A4
    13. Re-smuggle A3, equip a random shield, and **Fuse** something disposable to it. This will leave A4 as the sole FE parent of C20
    14. Throw purgatory all C: Smuggle any _one_ C[n], equip and throw any random weapon, and unequip that weapon, then repeat
    15. **Recall Lock** A4, discarding A2 and A3 through the save load

    ##### Part 2: Performing and undoing SFO
    ---
    notoc: true
    ---

    1. [Zuggle Drop](uid:L84) B1, equip A4, and **Overload Pickup** B2
    2. B1, B2, & A4 **Overload Batch DI** 30 shields `D1-D30`
    3. There will be a substantial lag on the second fuse of each shield after D1, so using the D-pad to **drop-swap** is advised
    4. _Super Fuse Overload_ should occur on the 30th shield. If confirmation is needed, **drop** the fused equipment item. If the fuse is deleted, SFO is active
    5. To undo SFO: **pick up** each D[n], **unequip** it, and **drop** it. Each deleted shield will remove 20 dependencies from the global limit

    ##### Part 3: Obtaining Mineru's Arm
    ---
    notoc: true
    ---

    1. Equip a weapon and ensure there is space in your weapon pouch
    2. Warp to Mogisari Shrine at the Lomei Sky Labyrinth. Other low gravity zones may work, but are untested for stability during SFO
    3. As soon as you gain control, walk in a small clockwise circle while spamming A (see video below (uh, when I add it))
    4. Execution permitting, you will pick up a new 2-handed weapon, dealing 38 damage, which has no icon, description, model, or collision, and is called MsgNotFound
    5. If unsuccessful, stand nearish to the shrine entrance and spam A between Panic Blood Moons (see other video I also haven't added)
    6. If Mineru was not summoned, simply summon her after the warp (and optionally warp again to get a go at the primary strat)
    6. About 3 seconds after control is gained, a panic blood moon will occur, which will _usually_ give an autosave
    7. Either return to Rasitakiwak Shrine to clear SFO, or simply close the game after receiving the above autosave

    ##### Resources ?
    ---
    notoc: true
    ---

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

    #### For Zelda's Torch ?
    
    ##### Prepare:
    ---
    notoc: true
    ---

    - 13 Zuggle Overload (9 on `1.0.0`)
    - If on `1.1.2` or earlier, Intangible Aerophasing
    - A bow to manage overload with
    - A DI Ghost Weapon, `A1`
    - A DI Ghost Shield, `B1`
    - Ideally, a second of each to simplify duplication
    - Optionally, a fused equipment item
    - The _second_ prologue autosave (the torch falls OOB on the first autosave)

    ##### Part 1: Creating the base setup
    ---
    notoc: true
    ---

    1. Enter Rasitakiwak Shrine, defeat all the constructs, and dispose of their weapons (for example by leaving/reentering)
    2. (In this case, Rasitakiwak is ideal, as it contains both an overlapping area with the prologue, and multiple steering sticks to create a Portacull with)
    3. B1 [Overload FE](uid:0XV#method-3-vddi-smugglezuggle) weapon `B2`
    4. [Recall Lock](uid:EY8) B2
    5. A1 and normal weapon `A2` [Ghost DI](uid:BEW#method-1-fuse-drop-swap-120) shield `A3`
    6. A1 **Overload FE** normal shield `A4`
    7. Equip A2, [Smuggle](uid:TGY) A3, and [Overload Pickup](uid:8QH) A4
    8. A2-A4 [Overload Batch DI](uid:PG3#method-1-overload-pf-drop-swap-culling-120) 19 weapons `C1-C19`
    9. **Fail-Drop** A4
    10. A3 & A4 **Ghost DI** weapon `C20`
    11. **Drop** A4
    12. Re-smuggle A3, equip a random shield, and **Fuse** something disposable to it. This will leave A4 as the sole FE parent of C20
    13. Throw purgatory all C: smuggle any one_ C[n], equip and throw any random weapon, and unequip that weapon, then repeat
    14. **Recall Lock** A4, discarding A2 and A3 through the load

    ##### Part 2: Performing and undoing SFO
    ---
    notoc: true
    ---

    1. [Zuggle Drop](uid:L84) B1, equip A4, and **Overload Pickup** B2
    2. B1, B2, & A4 **Overload Batch DI** 30 shields `D1-D30`
    3. There will be a substantial lag on the second fuse of each shield after D1, so using the D-pad to **drop-swap** is advised
    4. _Super Fuse Overload_ should occur on the 30th shield. If confirmation is needed, **drop** the fused equipment item. If the fuse is deleted, SFO is active
    5. **Fail-drop** B2, then **drop** it after it returns
    6. To undo SFO: **pick up** each D[n], **unequip** it, and **drop** it. Each deleted shield will remove 20 dependencies from the global limit

    ##### Part 3: Obtaining Zelda's Torch
    ---
    notoc: true
    ---

    1. Load the prologue autosave. Zelda will drop her torch, so pick it up
    2. If she does not, try loading to Rasitakiwak and back; It may take a few tries for her torch to be one of the dependencies that fails
    3. Get another prologue autosave with the torch in the inventory, then either load back to Rasitakiwak to clear SFO, or simply close the game
    4. Follow your preferred method to obtain MNF, but zuggle/SLD Zelda's Torch back to your progressed save instead
    5. Save the game or get an autosave

    ##### Resources ?
    ---
    notoc: true
    ---

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

    #### For duplication ?

    ##### Prepare:
    ---
    notoc: true
    ---

    - 13 Zuggle Overload (9 on `1.0.0`)
    - If on `1.1.2` or earlier, Intangible Aerophasing
    - A bow to manage overload with
    - A DI Ghost Weapon, dubbed "A1"
    - A DI Ghost Shield, dubbed "B1"
    - Ideally, a second of each to simplify duplication
    - Optionally, a fused equipment item
    - 1 or more of the duplication target

    ##### Part 1: Creating the base setup
    ---
    notoc: true
    ---
    
    1. Enter a minigame with no timer, such as House Building or the Desert Race's prep phase. If only materials (and not Zonai Devices) are to be duped, a shrine will also work
    2. (You don't have to actually enter the minigame until part 2)
    3. B1 [Overload FE](uid:0XV#method-3-vddi-smugglezuggle) weapon `B2`
    4. [Recall Lock](uid:EY8) B2
    5. A1 and normal weapon `A2` [Ghost DI](uid:BEW#method-1-fuse-drop-swap-120) shield `A3`
    6. A1 **Overload FE** normal shield `A4`
    7. Equip A2, [Smuggle](uid:TGY) A3, and [Overload Pickup](uid:8QH) A4
    8. A2-A4 [Overload Batch DI](uid:PG3#method-1-overload-pf-drop-swap-culling-120) 19 weapons `C1-C19`
    9. **Fail-Drop** A4
    10. A3 & A4 **Ghost DI** weapon `C20`
    11. **Drop** A4
    12. Re-smuggle A3, equip a random shield, and **Fuse** something disposable to it. This will leave A4 as the sole FE parent of C20
    13. Throw purgatory all C: smuggle any one_ C[n], equip and throw any random weapon, and unequip that weapon, then repeat
    14. **Recall Lock** A4, discarding A2 and A3 through the load

    ##### Part 2: Performing and undoing SFO
    ---
    notoc: true
    ---

    1. [Zuggle Drop](uid:L84) B1, equip A4, and **Overload Pickup** B2
    2. B1, B2, & A4 **Overload Batch DI** 30 Shields `D1-D30`
    3. There will be a substantial lag on the second fuse of each shield after D1, so using the D-pad to **drop-swap** is advised
    4. _Super Fuse Overload_ should occur on the 30th shield. If confirmation is needed, **drop** the fused equipment item. If the fuse is deleted, SFO is active
    5. To undo SFO: **pick up** each D[n], **unequip** it, and **drop** it. Each deleted shield will remove 20 dependencies from the global limit

    ##### Part 3: Duplicating with SFO
    ---
    notoc: true
    ---

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

    - Throw hold is slower but does devices
    - SFO BID is faster but doesn't
    - Speed seems slightly different than normal BID but I'm not sure which way
    - Both dupes found by mulberry

    ##### Resources ?
    ---
    notoc: true
    ---

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

=== "Method 2: Attached Purgatory + DI" ###
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    #### Basic info ?
    ---
    notoc: true
    ---

    - This is a **Local** method that makes use of a specially-prepared equipment item to maximize portability and in-the-moment speed.
    - It is ideal for duplication, and can be used for Mineru's Arm by an older route, but cannot be used for Zelda's Torch (...yet).
    - While it is technically possible on `1.1.2` and earlier, the absence of "Drop-Swap Culling" makes it significantly more difficult.
    - Methods 3 and 4 will be faster and easier on those versions (for local and persistent needs, respectively).

    _Method developed by mulberry_

    #### The equipment ?

    - In summary, make a DI Ghost shield with 30-32 DI Ghost weapons Cold Fused to it, then purgatorize all the weapons so that they can all be "equipped" at once by zuggle dropping the shield.
    - This needn't be done using the given steps. However, they are optimized for speed and practicality.

    ##### Prepare:
    ---
    notoc: true
    ---

    - 13 Zuggle Overload
    - A DI Ghost Shield `A` and normal shield `B`
    - A Torch
    - A Flame Emitter

    ##### Steps
    ---
    notoc: true
    ---

    1. Follow [this Batch DI method](uid:PG3#method-2-overload-pf-torch-culling-all-versions) to create a DI Ghost shield `C` with 30 DI Ghost weapon children (`F1` through `F30`)
    2. Swap shields to delete CF parent `D` (it is not desired), then drop the equipped shield to drop C
    3. Distance despawn B, then [Smuggle](uid:TGY) A and use a rocket shield. This will remove C's two parent dependencies, making room for 2 more children
    4. C and random shield [Ghost DI](uid:BEW#method-1-fuse-drop-swap-120) weapon `F31`
    5. Distance despawn random shield
    6. Repeat steps 4 and 5 to create F32
    7. Smuggle any _one_ F[n], then **pick up** another and **throw** it.
    8. Swing weapon or ready weapon throw to return the thrown weapon to Link's hand
    9. Repeat steps 7 and 8 for _all_ F[n], using any normal weapon for the final throw (it can be unequipped afterwards)
    10. The final result should be DI Ghost shield `C` with 32 attached purgatory DI Ghost weapon children (`F1` through `F32`)

    #### For Duplication ?

    ##### Prepare:
    ---
    notoc: true
    ---

    - The special equipment
    - A DI Weapon to dupe with (optional, you _are_ expected to have overload at this point and that dupes just fine)
    - Up to 21 materials

    ##### Part 1: Setting up and destroying SFO
    ---
    notoc: true
    ---

    1. Enter a minigame with no timer, such as House Building or the Desert Race's prep phase. If only materials (and not Zonai Devices) are to be duped, a shrine will also work
    2. Zuggle Drop C to attach the 32 weapons to Link
    3. Dupe a weapon `G1` and equip it
    4. G1 [Ghost DI](uid:BEW) material/equipment `H1`. **Do not detangle or delete G1.**
    5. **Repeat** until attempting to fuse H[n] to G[n] fails (18-21 repetitions are expected depending on environment); Menu Link should be overloaded at this point
    6. To destroy SFO, simply inventory pickup each G[n], or exit shrine if in one. Distance despawn _will not fully work_ due to the properties of DI
    7. If safety is preferred, use equipment for all H[n] instead of materials. This way, if G[n] is destroyed by drop limit/distance, H[n] can still be manually destroyed to clear the dependencies.

    ##### Part 2: Duplicating with SFO
    ---
    notoc: true
    ---

    ??? abstract "Throw Hold Duplication (devices or materials)"

        1. Ready a **throw** of the duplication target. It should fall to the ground
        2. **Collect** it
        3. Press **cancel** (B/X). This will "put away" the target Link "still had held", returning it to the pouch
        4. Ready **throw** again. Each cycle will increase the quantity of the target by 1
        5. **Inventory pickup** all G[n] to end SFO before ending the minigame (shrine exit will end SFO automatically)
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
        10. **Inventory pickup** all G[n] to end SFO before ending the minigame (shrine exit will end SFO automatically)
        11. Save the game/get an autosave

    - Throw hold is slower but does devices
    - SFO BID is faster but doesn't
    - Speed seems slightly different than normal BID but I'm not sure which way
    - Both dupes found by mulberry

    ##### Resources ?
    ---
    notoc: true
    ---

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            C["DI Ghost Shield<br/>(C)"]
            F["32 Purgatory Weapons<br/>(F1-F32)"]
            PARENTS["Normal Parents<br/>(G1-G21)"]
            CHILDREN["DI Children<br/>(H1-H21)"]

            C -->|CF| F
            F -->|"Fuse<br/>(becomes CF)"| CHILDREN
            PARENTS -->|"Fuse<br/>(stays attached)"| CHILDREN
        ```
        
    #### For Mineru's Arm (Local SFO variant) ?

    ##### Prepare:
    ---
    notoc: true
    ---

    - The special equipment
    - A DI Weapon to dupe with (optional, you _are_ expected to have overload at this point and that dupes just fine)
    - Up to 21 materials
    - A Portacull Shield or the means to make one portably

    ##### Part 1: Setting up SFO
    ---
    notoc: true
    ---

    1. Defeat Army and enter the tunnel before Ganondorf
    2. Zuggle C to attach the 32 weapons to Link
    3. Dupe a weapon `G1` and equip it
    4. G1 [Ghost DI](uid:BEW) DI material/equipment `H1`; **Do not detangle or delete G1.**
    5. **Repeat** until attempting to fuse H[n] to G[n] fails (18-21 repetitions are expected); Menu Link should be overloaded at this point
    6. Glue all G[n] together and Ultrahand them into Ganon's Room, holding them far aside to keep them out of the way

    ##### Part 2: Obtaining Mineru's Arm
    ---
    notoc: true
    ---

    1. Progress the fight to Phase 2 (2nd form), and **drop** a fused equipment. The fuse should delete. If not, **drop** more one at a time until it does
    2. Progress to Phase 3 (sages blown away), and find Mineru
    3. **Pick up** her arm, which is invisible, collisionless, and repeatedly drops from either visible arm. It cannot be collected with an empty hand when undiscovered. Take several to be safe
    4. **Inventory pickup** all G[n] to undo SFO and UNDOCK THE CONSOLE
    5. **Fuse** something to Mineru's Arm. _If the console is docked, this will crash the game._
    6. Use the portacull to SRZ Mineru's Arm (it will naturally fail-drop, so a wall is not needed)
    7. Load a save. If you undid SFO, there will be no crash risk
    8. Go somewhere you can see a long way down and prepare Recall (atop a Hover Stone raised with a Rocket is excellent)
    9. **Drop** an equipped weapon and immediately **Recall** the item fused to Mineru's Arm (which still has no collision)
    10. **Equip** a weapon and **pick up** Mineru's Arm (if undiscovered on this save, it still cannot be collected with an empty hand)
    11. If planning to use Mineru's arm as a fail-drop wall, **destroy** the fuse (If the console is docked, dropping a fused Mineru's Arm will _crash the game_)
    12. Save the game/Get an autosave

    ##### Resources ?
    ---
    notoc: true
    ---

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            C["DI Ghost Shield<br/>(C)"]
            F["32 Purgatory Weapons<br/>(F1-F32)"]
            PARENTS["Normal Parents<br/>(G1-G21)"]
            CHILDREN["DI Children<br/>(H1-H21)"]

            C -->|CF| F
            F -->|"Fuse<br/>(becomes CF)"| CHILDREN
            PARENTS -->|"Fuse<br/>(stays attached)"| CHILDREN
        ```

    #### Persistent Variant (but not yet) ?
    ---
    notoc: true
    ---

    - It is possible to exploit the mechanics of DI to make SFO persistent.
    - This will be provided as a seperate method at a later date (The minimum form and what it's good for need to be determined first).
    - If a persistent method is desired, Methods 1 or 4 will almost certainly be easier (for `1.2.0+` and `1.0.0-1.1.2` respectively).

=== "Method 3: Overload Cold Fuse" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    #### Basic info ?
    ---
    notoc: true
    ---

    - This is a **Local** method with minimal additional glitches required. 
    - It is perfectly acceptable for duplicating throwables and holdables on all versions, and can obtain Mineru's Arm by an older route.
    - It can also be made permanent via permacull; This is provided as Method 4 for clarity.
    
    _Method by mulberry(?); Optimized by Aergyl, mulberry(?)_

    #### For Duplication ?

    ##### Prepare:
    ---
    notoc: true
    ---

    - 13 zuggle overload (9 on `1.0.0`)
    - A bow
    - A weapon
    - 2+ unfused shields
    - A handful of fused equipment items
    - 31+ materials
    - 1+ of the duplication target

    ##### Part 1: Performing SFO
    ---
    notoc: true
    ---

    1. Enter a minigame with no timer, such as House Building or the Desert Race's prep phase. If only materials (and not Zonai Devices) are to be duped, a shrine will also work
    2. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
    3. **Overload Drop** a weapon `A` and **Fuse** it to a shield `B`
    4. [Overload Cold Fuse](uid:O64) 21 shields `C1-C21` to A (the 19 dropped & 2 from inventory)
    5. **Fail-drop** A and **drop** B
    6. [Overload Pickup](uid:8QH) C1 and **Overload Cold Fuse** 30 materials `D1-D30` to it
    7. **Fail-drop** C1 and **drop** it aside
    8. Repeat 7 for C2-C19 with the **same** D1-D30
    9. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, _proceed to step 11_
    10. **Overload Cold Fuse** an unrelated material to C[n]. If it works, **collect it** and **Overload Cold Fuse** the next D[n], then repeat. If it fails, _proceed to step 12_
    11. **Fail-drop** C(n) and **drop** it. You may have to **unequip your bow** for it to return. _Be sure it returns before dropping it._

    ##### Part 2: Duplicating with SFO
    ---
    notoc: true
    ---

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

    - Throw hold is slower but does devices
    - SFO BID is faster but doesn't
    - Speed seems slightly different than normal BID but I'm not sure which way
    - Both dupes found by mulberry

    ##### Resources ?
    ---
    notoc: true
    ---

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            A{"Enter Minigame/Shrine"} -->|Equip| B[Shield B]
            A -->|Overload Drop| C[Weapon A]
            B -->|Fuse| C
            C -->|cf| D[Shields C1-C21]
            D -->|cf| E[Materials D1-D30]
        ```

    #### For mineru's Arm (Local SFO variant) ?

    ##### Prepare:
    ---
    notoc: true
    ---

    - 13 zuggle overload (9 on `1.0.0`)
    - A bow
    - A weapon
    - 2+ unfused shields
    - Several fused equipment items
    - 31+ materials
    - If on 1.2.0+, a Portacull Shield (or the materials to make one via Overload Cold Fuse)
    - A bucket-shaped autobuild with enough Hover Stones to float (and optionally 1-2 Big Batteries)

    ##### Part 1: Performing SFO
    ---
    notoc: true
    ---

    1. Defeat Army and enter the tunnel before Ganondorf
    2. Drop the portacull aside. Be sure not to go too far from any of the working objects (about halfway down the tunnel is safe)
    3. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
    4. **Overload Drop** a weapon `A` and **Fuse** it to a shield `B`
    5. [Overload Cold Fuse](uid:O64) 21 shields `C1-C21` to A (the 19 dropped & 2 from inventory)
    6. **Fail-drop** A and **drop** B
    7. [Overload Pickup](uid:8QH) C1 and **Overload Cold Fuse** 30 materials `D1-D30` to it
    8. **Fail-drop** C1 and **drop** it aside
    9. Repeat 7 for C2-C19 with the **same** D1-D30
    10. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, _proceed to step 11_
    11. **Overload Cold Fuse** an unrelated material to C[n]. If it works, **collect it** and **Overload Cold Fuse** the next D[n], then repeat. If it fails, _proceed to step 12_
    12. **Fail-drop** C(n) and **drop** it. You may have to **unequip your bow** for it to return. **Be sure it returns before dropping it.**
    13. **Drop** A, not too close to where the barrier will spawn (it cannot be moved after dropping it!)
    14. Move B, all of C, and all of D into the bucket build using Ultrahand
    15. Carry the bucket into Ganondorf's room, holding it high and far aside to keep it out of the way of the fight

    ##### Part 2: Obtaining Mineru's Arm
    ---
    notoc: true
    ---

    1. Progress the fight to Phase 2 (2nd form), and **drop** a fused equipment. The fuse should delete. If not, **drop** more one at a time until it does
    2. Progress to Phase 3 (sages blown away), and find Mineru
    3. **Pick up** her arm, which is invisible, collisionless, and repeatedly drops from either visible arm. It cannot be collected with an empty hand when undiscovered. Take several to be safe
    4. **Collect** the materials in the bucket to undo SFO and UNDOCK THE CONSOLE
    5. **Fuse** something to Mineru's Arm. _If the console is docked, this will crash the game._
    6. Zuggle Mineru's Arm. It will always fail-drop while on the ground, so either version can be done without a wall
    7. If on `1.1.2` or earlier, Map Zuggle Mineru's Arm
    8. If on `1.2.0` or later, use the portacull to SRZ Mineru's Arm
    9. Load a save. If you undid SFO, there will be no crash risk
    10. Go somewhere you can see a long way down and prepare Recall (atop a Hover Stone raised with a Rocket is excellent)
    11. **Drop** an equipped weapon and immediately **Recall** the item fused to Mineru's Arm (which still has no collision)
    12. **Equip** a weapon and **pick up** Mineru's Arm (if undiscovered on this save, it still cannot be collected with an empty hand)
    13. If planning to use Mineru's arm as a fail-drop wall, **destroy** the fuse (If the console is docked, dropping a fused Mineru's Arm will _crash the game_)
    14. Save the game/Get an autosave

    ##### Resources ?
    ---
    notoc: true
    ---

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

=== "Method 4: Overload Cold Fuse + Permacull" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    #### Basic info ?
    ---
    notoc: true
    ---

    - This is a **Permacull** method with minimal additional glitches required. It is acceptable for Zelda's Torch and Mineru's Arm.
    - It _can_ be used for duplication, but is needlessly complex and hazardous for this usage; Use Method 3 instead.
    - The steps given are specialized for `1.1.2` and below. They will work on `1.2.0+`, but are inefficient.

    #### For Zelda's Torch ?

    ##### Prepare:
    ---
    notoc: true
    ---

    - 13 Zuggle overload (9 on `1.0.0`)
    - Intangible Aerophasing (guide assumes this is set up at Akkala Citadel Ruins)
    - A bow
    - 2+ unfused weapons
    - 2+ unfused shields
    - Several fused equipment items
    - A material
    - A DI Ghost Shield `E`
    - The _second_ prologue autosave

    ##### Part 1: Performing SFO
    ---
    notoc: true
    ---

    1. Use the Aerophasing setup to ensure it has a cull stored; this will allow the culling area to remain loaded through a banc change
    2. Walk up to the nearby shrine ("Domizuin") and enter it. **Do not warp there.**
    3. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
    4. **Overload Drop** a weapon `A` and fuse it to a shield `B`
    5. [Overload Cold Fuse](uid:O64) 21 shields `C1-C21` to A (the 19 dropped & 2 from inventory)
    6. **Fail-drop** A and **drop** B
    7. [Overload Pickup](uid:8QH) C1
    8. Duplicate 30 shields `D1-D30` off E, dropping each on the ground and **Overload Cold Fusing** them to C1 as you go
    9. **Fail-drop** C1 and **drop** it aside
    10. Repeat 7-9 for C2-C19 with the **same** D1-D30
    11. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, _proceed to step 11_
    12. **Overload Cold Fuse** an unrelated material to C[n]. If it works, **Collect it** and **Overload Cold Fuse** the next D[n], then repeat. If it fails, _proceed to step 12_
    13. **Fail-drop** C(n) and **drop** it. You may have to **unequip your bow** for it to return. **Be sure it returns before dropping it.**
    14. **Drop** A

    ##### Part 2: Permaculling the shields
    ---
    notoc: true
    ---

    1. [Smuggle](uid:TGY) E. If E was not prepared, Zuggle any other unrelated shield by your preferred method
    2. Equip one of B, C, or D and step onto the phasing platform
    3. **Pause** the game while Link is **culled**. This will cause Link to consistently be **unculled** when the game is unpaused
    4. **Unpause** the game and immediately **open** the Shield Quick Menu (D-pad Left). If Link is **unculled** behind the menu, **drop** the equipped shield. If not, repeat step 3.
    5. Repeat steps 1-4 for _all_ B, C, and D, ultimately resulting in the entire setup being permaculled

    ##### Part 3: Obtaining Zelda's Torch
    ---
    notoc: true
    ---

    1. Load your prologue save. Zelda will drop her torch, so pick it up
    2. If she does not, try loading to Domizuin and back; It may take a few tries for her torch to be one of the dependencies that fails
    3. Get another autosave and close the game to clear SFO
    4. Follow your preferred method to obtain MNF, but zuggle/SLD Zelda's Torch back to your progressed save instead
    5. Save the game or get an autosave

    ##### Resources ?
    ---
    notoc: true
    ---

    ??? example "Method Structure Diagram"

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

    #### For Mineru's Arm (persistent SFO variant) ?

    ##### Prepare:
    ---
    notoc: true
    ---

    - 13 Zuggle overload (9 on `1.0.0`)
    - Intangible Aerophasing (guide assumes this is set up at Akkala Citadel Ruins)
    - A bow
    - 2+ unfused weapons
    - 2+ unfused shields
    - Several fused equipment items
    - A material
    - A DI Ghost shield `E`

    ##### Part 1: Performing SFO
    ---
    notoc: true
    ---

    1. Ensure Mineru is summoned. This will save some headache later
    2. Use the Aerophasing setup to ensure it has a cull stored; this will allow the culling area to remain loaded through _a_ banc change
    3. Walk up to the nearby shrine ("Domizuin") and enter it. **Do not warp there.**
    4. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
    5. **Overload Drop** a weapon `A` and fuse it to a shield `B`
    6. [Overload Cold Fuse](uid:O64) 21 shields `C1-C21` to A (the 19 dropped & 2 from inventory)
    7. **Fail-drop** A and **drop** B
    8. [Overload Pickup](uid:8QH) C1
    9. Duplicate 30 shields `D1-D30` off the DI shield, dropping each on the ground and **Overload Cold Fusing** them to C1 as you go
    10. **Fail-drop** C1 and **drop** it aside
    11. Repeat 8-10 for C2-C19 with the same D1-D30
    12. For C20 and C21, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, proceed to step 12
    13. **Overload Cold Fuse** an unrelated material to C[n]. If it works, pick it back up and **Overload Cold Fuse** the next D[n], then repeat. If it fails, proceed to step 13
    14. **Fail-drop** C(n) and **drop** it. You may have to unequip your bow for it to return. **Be sure it returns before dropping it.**
    15. **Drop** A

    ##### Part 2: Permaculling the shields
    ---
    notoc: true
    ---

    1. [Smuggle](uid:TGY) E. If E was not prepared, Zuggle any other unrelated shield by your preferred method
    2. Equip one of B, C, or D and step onto the phasing platform
    3. **Pause** the game while Link is **culled**. This will cause Link to consistently be **unculled** when the game is unpaused
    4. **Unpause** the game and immediately **open** the Shield Quick Menu (D-pad Left). If Link is **unculled** behind the menu, **drop** the equipped shield. If not, repeat step 3.
    5. Repeat steps 1-4 for _all_ B, C, and D, ultimately resulting in the entire setup being permaculled

    ##### Part 3: Obtaining Mineru's Arm
    ---
    notoc: true
    ---

    1. Equip a weapon and ensure there is space in your weapon pouch
    2. Warp to Mogisari Shrine at the Lomei Sky Labyrinth. Other low gravity zones may work, but are untested for stability during SFO
    3. As soon as you gain control, walk in a small clockwise circle while spamming A (see video below (uh, when I add it))
    4. Execution permitting, you will pick up a new 2-handed weapon, dealing 38 damage, which has no icon, description, model, or collision, and is called MsgNotFound
    5. If unsuccessful, stand nearish to the shrine entrance and spam A between Panic Blood Moons (see other video I also haven't added)
    6. If Mineru was not summoned, simply summon her after the warp (and optionally warp again to get a go at the primary strat)
    6. About 3 seconds after control is gained, a panic blood moon will occur, which will _usually_ give an autosave
    7. Hard save the game if desired, then close it to clear SFO

    ##### Resources ?
    ---
    notoc: true
    ---

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

## Notes

### General SFO properties

- The global dependency heap is full, so no new dependencies can be registered.
- Every newly-loaded NPC and enemy will overload drop everything they're carrying.
- Many such overload drops will crash the game (presumably due to missing code for interacting with the world as a dropped item?).
- Every newly-loaded fused equipment item will lose its fuse in-world (not in the inventory). It will detangle for one frame and then be deleted.

### Tips and Additional Uses

- Link's equipment can be used for fine-grained control over the final few dependency slots. With a bow, fused shield, fused weapon (and its sheath), and fully synced armor, up to 9 dependencies are fully controllable.
- SFO bypasses the "Overload SDC protection" present on `1.2.0` and up, allowing any mountable actor to be SDC'd simply by mounting.
- Depths Ghosts will despawn without having ever taken ownership of their weapons, allowing for Kinematic Weapons to be obtained without fusing them.
- Every attempt at fusing something will cause Fuse Overload Fuse Storage, allowing for [Fuse Overload Fuse Entanglement](uid:G8Q) without performing actual Fuse Overload.

### Credits

I might end up distributing this into the right places but idk. Maybe both, for maximum referencing speed?

- SFO discovered by ??? (I guess I need another round of asking about the origin)
- SFO first performed on vanilla by Aergyl, mulberry - Dec 05th, 2025
- Mineru's Arm ganon route found by mulberry - Dec 07th, 2025
- Zelda's Torch obtained by mulberry - Dec 07th, 2025
- SFO Throw Duplication found by mulberry - Dec 06th, 2025
- SFO BID found by mulberry - Mar 27th, 2026
- Mineru's Arm mainfield route found by Squidwest - Mar 18th, 2026
- SFOFE by mulberry(?) - Feb 24th, 2026(?)
- SFO KW found by Squidwest - Apr 24th, 2026

- DI SFO by MandelbrotChaylay - Feb 01st, 2026
- Rediscovered and optimized by Squidwest - Feb 24th, 2026
- Hand Purg + non-batch DI SFO by mulberry - Feb 24th, 2026
- Overload Cold Fuse SFO by Aergyl, mulberry - Dec 05th, 2026
- (Method 4 is really only an extension of Method 3, so I don't think it even _has_ seperate credits? I ought to try this "reading" thing sometime idk)

### Resources

??? quote "Discord Resources"

    - [Original Discovery](https://discord.com/channels/1086729144307564648/1110956205624532993/1446913364268683395)
    - [Original Zelda's Torch Get](https://discord.com/channels/1086729144307564648/1110956205624532993/1447220634987003984)
    - [Original Mineru's Arm Get](https://discord.com/channels/1086729144307564648/1110956205624532993/1447304812197838930)
    - [SFO Throw Duplication](https://discord.com/channels/1086729144307564648/1110956205624532993/1446921416875446423)
    - [Original DI Method](https://discord.com/channels/1086729144307564648/1109838351596527726/1467646671142916238)
    - [Optimized Hand Purg + BDI Method](https://discord.com/channels/1111875355758837830/1128775917376897145/1475776267910516747) (not the first nor the best to use purg, but the one I have a source for 👍)
    - [Hand Purg + DI Method](https://discord.com/channels/1111875355758837830/1128775917376897145/1475872486359830538)
    - [SFOFE](https://discord.com/channels/1111875355758837830/1128775917376897145/1475878511720923380)
    - [Easier Mineru's Arm Route](https://discord.com/channels/1086729144307564648/1113557914444111873/1484238374909902868)
    - [SFO BID](https://discord.com/channels/1086729144307564648/1113557914444111873/1487214470131486862)
    - [SFO KW](https://discord.com/channels/1086729144307564648/1105598687167664239/1497841862579327147)

### Related
- [Zuggle Overload](search:Zuggle Overload)
- [Despawn Interrupt](search:Despawn Interrupt)
- [Fuse Entanglement](search:Fuse Entanglement)
