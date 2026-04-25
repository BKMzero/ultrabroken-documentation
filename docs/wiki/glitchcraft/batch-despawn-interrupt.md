---
title: "Batch Despawn Interrupt"
uid: "PG3"
draft: true
label: "BDI"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["Aergyl", "mulberry", "Squidwest"]
date: "2026-01-17"
description: "A collection of methods to produce large numbers of DI Ghosts quickly."
aliases: ["Batch DI", "Batch-DI"]
tags: ["despawn-interrupt", "culling"]
---

# Batch Despawn Interrupt

## Summary
Some of the properties of DI Ghosts (typically equipment, sometimes otherwise) are best exploited with large numbers of them. This page provides various convenient ways to produce large numbers of them.

_Credits - See individual methods_

## Instructions

Methods are partitioned based on their resulting structure.

=== "Overload methods" ###

    - These methods use Overload Pseudo Fuse to DI targets without ever creating normal parents, removing the need to despawn them between targets.
    - They are ideal for creating very large quantities of DI Ghosts, and are sometimes useful for the resulting structure (a DI parent and a normal parent, each sharing many cold-fused DI children).

    #### Method 1: <br/>Overload PF + Drop-Swap Culling ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This is the most basic overload method, requiring only the absolute minimum prerequisites.
    - As such, it can be done nearly anywhere at nearly any time.

    Prepare:

    - 13 Zuggle Overload
    - A DI Shield `A`, ideally a [DI Ghost](uid:BEW) (all types can be mirrored)

    Creating the setup:

    1. [Smuggle](uid:TGY) A and equip Normal Shield `B`
    2. **Fuse** Weapon `C` to B and **pause** a few frames after (for instance, by buffering the ability wheel at the same time as pressing Fuse, then selecting Map)
    3. **Drop** B, **swap** to another shield, and **unequip** that shield, then **Unpause**
    4. _Smuggle_ A again
    5. [Overload drop](uid:8QH) a shield and **Fuse** it to a weapon
    6. **Fuse** Weapon `D` to said shield, FEing it to A
    7. **Swap** shield, then **drop** it to leave A [Zuggle Dropped](uid:L84)
    8. **Unequip** weapon
    10. _Smuggle_ C, pick up B, and [Overload Pickup](uid:8QH) D
    11. Glue C to something to elevate it and ensure it cannot accidentally be targeted by Fuse
    12. Optionally, position a wall behind Link's back which can force B to **fail-drop**

    Creating DI Ghosts:

    1. **Fuse** target to D ([overload FE](uid:0XV) to C)
    2. **Fuse** target to D again. As it already has an FE parent (C), this time it will Pseudo-fuse to D and begin fading away
    3. **Pause** the game before the target fully fades out (buffering wheel and selecting Map will work here too)
    4. **Drop** B, **equip** another shield, and **unequip** it. This will cull B, and thus C, and thus the target, DI-ing it
    5. If you fail-dropped B, proceed with the next target. If not, pick it up before proceeding
    6. To continue beyond 30 successful uses, first **destroy** and **remake** C and D

    !!! danger "Fuse-Over(load)"

        Detangling a DI Ghost from its parent by "fuse-over" leaves a Cold Fuse connection behind, and detaching a DI Ghost from its PF parent does the same. Due to this, C and D will each gain one _peristent_ dependency for each DI Ghost produced. After 30 uses, C and D will reach Fuse Overload. If a 31st use is attempted, you will create a "Reference FE" connection, which will **crash the game** if you drop either!

    !!! danger "Self-Fusing"

        When an overload-pickup (here, C) has a connection back to Link (here, via A), it is possible to target it to be fused to itself. Under most circumstances, this will immediately **crash the game** if attempted.

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD

            A[DI Shield A]
            B[Normal Shield B]
            C[DI Weapon C]
            D[Normal Weapon D]
            TARGET[Target]

            B -->|DI| C
            A -->|DI| C
            A -->|FE| D
            C -->|FE| TARGET
            D -->|CF| TARGET
        ```

    _Method developed by mulberry - Jan 17, 2026_

    #### Method 2: <br/>Overload PF + Torch Culling ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method builds on Method 1 with a new culling method, increasing the speed and reducing the setup time and complexity.
    - However, it can only be performed at a culling area.

    Prepare:

    - 13 Zuggle Overload
    - A DI Weapon or Shield `A`
    - A torch
    - A flame emitter

    Creating the setup:

    1. A and normal item `B` [Ghost DI](uid:BEW) Shield `C`, keep normal parent
    2. [Smuggle](uid:TGY) C
    3. [Cold Drop](uid:C6H) the torch and place it next to a wall in a culling area
    4. Point the Flame Emitter at the head of the Torch from point-blank, ensuring the fire strikes a solid surface as close to the torch-head as possible.
    5. Glue B to the Torch and **activate** the Flame Emitter.
    6. To cull C, use the ability wheel to select and open Recall, causing a 2-frame pause. The torch should begin culling after cancelling recall
    7. [Overload Drop](uid:8QH) a shield `D` and **Fuse** it to a weapon `E`

    Creating DI Ghosts:

    1. **Fuse** the target to D ([Overload FE](uid:0XV) to C)
    2. Use the ability wheel to open recall, then use it to open fuse and _immediately_ fuse the target to D again
    3. As long as fuse is pressed more than 2 frames before the torch fully culls, the cull _will_ occur within the target's DI window
    4. To continue beyond 30 successful uses, first **destroy** and **remake** C and D

    !!! danger "Fuse-Over(load)"

        Detangling a DI Ghost from its parent by "fuse-over" leaves a Cold Fuse connection behind, and detaching a DI Ghost from its PF parent does the same. Due to this, C and D will each gain one _peristent_ dependency for each DI Ghost produced. After 30 uses, C and D will reach Fuse Overload. If a 31st use is attempted, you will create a "Reference FE" connection, which will **crash the game** if you drop either!

    !!! danger "Self-Fusing"

        When an overload-pickup (here, D) has a connection back to Link (here, via E), it is possible to target it to be fused to itself. Under most circumstances, this will immediately **crash the game** if attempted.

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD

            LINK[Link]
            TORCH[Torch]
            FLAME[Flame Emitter]
            A["DI Ghost (A)"]
            B["Normal Item (B)"]
            C["DI Ghost Shield (C)"]
            D["Normal Shield (D)"]
            E["Normal Weapon (E)"]
            F[Target]

            B -->|DI| C
            A -->|DI| C
            FLAME -->|"Point at"| TORCH
            B -->|Glue| TORCH
            LINK -->|Smuggle| C
            LINK -->|Equip| E
            LINK -->|"Overload<br/>Drop"| D
            E -->|Fuse| D
            C -->|FE| F
            D -->|CF| F
        ```

    _Method developed by mulberry - Feb 18, 2026_

    #### Method 3: <br/>Overload PF + Mineru Limbo ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses Mineru as a culling source, placing her in Limbo to maximize control over her culling.
    - It is the fastest overload method, but can only be done when & where Mineru's Sage Avatar can be summoned and put into Limbo.

    Prepare:

    - 13 Zuggle Overload
    - A DI Weapon `A` (all types can be inverted)
    - Mineru
    - A normal shield `B`
    - A Stake (or other setup to place Mineru into limbo)

    Creating the setup:

    1. Mineru FE B
    2. [Smuggle](uid:TGY) A, equip B, and target Shield `C` with Fuse
    3. Induce Mineru to **cull** and fuse C to B shortly before B culls; this will DI C
    4. Place B aside and _smuggle_ C
    5. [Overload Drop](uid:8QH) Shield `D` and fuse to Weapon `E`

    Creating DI Ghosts:
    
    1. Stand on a stake at the right height so that Mineru goes into "Limbo" when you cull her (Mineru invisible, but B and C unculled)
    2. **Fuse** target to D ([Overload FE](uid:0XV) to C)
    3. **Fuse** target to D again, and jump immediately after so that Mineru culls (and culls the target by extension)
    4. To continue beyond 30 successful uses, first **destroy** and **remake** C and D (start from setup step 2)

    !!! danger "Fuse-Over(load)"

        Detangling a DI Ghost from its parent by "fuse-over" leaves a Cold Fuse connection behind, and detaching a DI Ghost from its PF parent does the same. Due to this, C and D will each gain one _peristent_ dependency for each DI Ghost produced. After 30 uses, C and D will reach Fuse Overload. If a 31st use is attempted, you will create a "Reference FE" connection, which will **crash the game** if you drop either!

    !!! danger "Self-Fusing"

        When an overload-pickup (here, D) has a connection back to Link (here, E), it is possible to target it to be fused to itself. Under most circumstances, this will immediately **crash the game** if attempted.

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            MINERU[Mineru]
            A[DI Weapon A]
            B[Normal Weapon B]
            C[DI Shield C]
            D[Normal Shield D]
            E[Normal Weapon E]
            TARGET[Target]

            MINERU -->|FE| B
            A -->|DI| C
            B -->|DI| C
            E -->|Fuse| D
            C -->|FE| TARGET
            D -->|CF| TARGET
        ```

    _Method developed by mulberry - Mar 06, 2026_ 

    #### Method 4: <br/>Overload PF + Aerophasing ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - Method 4 uses Aerophasing as a culling source, allowing for a use-anywhere method on all patches.
    - However: It's not very good
    - (I should figure out the ghosted torch culling method and add it instead, huh...)
    - (Ugh I could recommend it for sfo too)

    Prepare:

    - 13 Zuggle Overload
    - A DI Shield `A`, ideally a DI Ghost (all types can be mirrored)
    - Intangible Aerophasing

    Creating the setup:

    1. [Smuggle](uid:TGY) A and equip Normal Shield `B`, then stand on the phasing platform
    2. Optionally, **Pause** the game while Link is culled. This causes him to always be unculled right after unpausing, making fuse timing easier throughout the method
    2. Just after Link unculls, **fuse** a weapon `C` to B; Link will cull soon enough to Ghost DI C
    3. Drop B and leave it aside, but **pick up** and re-**smuggle** A
    4. [Overload FE](uid:0XV) weapon `D` to A
    5. Swap shield, then drop it to leave A [Zuggle Dropped](uid:L84)
    6. **Smuggle** C, **equip** B, and [Overload Pickup](uid:8QH) D
    7. **Glue** D to something to elevate it and ensure it cannot accidentally be targeted by Fuse. Face the blade _away_ from the other object to keep fuse targets from colliding with it.

    Creating DI Ghosts

    1. Stand on the phasing platform
    2. Just after Link unculls, **fuse** target to D (overload fe)
    3. Just after Link unculls, **fuse** target to D again. As it already has an FE parent (C), this time it will Pseudo-Fuse to D and begin fading away
    4. Link will cull soon enough after to automatically DI the target (by culling B, which culls C)
    5. Repeat from step 2 with the next target. The previous targets can stay attached to D without issue 
    5. To continue beyond 30 successful uses, first **destroy** and **remake** C and D

    !!! danger "Fuse-Over(load)"

        Detangling a DI Ghost from its parent by "fuse-over" leaves a Cold Fuse connection behind, and detaching a DI Ghost from its PF parent does the same. Due to this, C and D will each gain one _peristent_ dependency for each DI Ghost produced. After 30 uses, C and D will reach Fuse Overload. If a 31st use is attempted, you will create a "Reference FE" connection, which will **crash the game** if you drop either!

    !!! danger "Self-Fusing"

        When an overload-pickup (here, C) has a connection back to Link (here, via A), it is possible to target it to be fused to itself. Under most circumstances, this will immediately **crash the game** if attempted.

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD

            A[DI Shield A]
            B[Normal Shield B]
            C[DI Weapon C]
            D[Normal Weapon D]
            TARGET[Target]

            B -->|DI| C
            A -->|DI| C
            A -->|FE| D
            C -->|FE| TARGET
            D -->|CF| TARGET
        ```

    _"Method" developed by Squidwest - no date or reference because it's not good enough lol_

=== "DI Chaining Methods" ###

    - These methods create a chain of DI ghosts, allowing the normal-parent despawning to be saved until the end of the process (as each target retains a DI parent as long as desired).
    - They are ideal for medium batches and minimalist replication, but can _only_ be used for weapons and shields.

    #### Method 5: <br/>Chaining + Drop-Swap Culling ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - Method 5 is the most basic chaining method, and the most minimal batch method in general.
    - Unlike with overload methods, the remaining methods in this section are generally downgrades, only serving to make the method possible on `1.1.2` and earlier.

    ??? abstract "Safe Variant"

        Prepare:

        A DI Ghost Weapon or Shield `A`

        Steps:

        1. Duplicate three normal copies of A by DI Duping (`B`, `C`, & `D`)
        2. [Smuggle](uid:TGY) A and **equip** B, then **drop** C on the ground
        3. Start to **fuse** C to B, then pause the game a few frames later (For example, by buffering the ability wheel at the same time as pressing fuse, then selecting Map)
        4. **Drop** B and **swap** to D
        5. C will be attached to B on the ground. Dupe two replacement copies (E and F), then **drop** D
        6. Optionally, **pick up** and **drop** A to remove its overload
        7. **Pick up** C
        8. **Repeat** from step 2, with C as the new smuggle, E as the new normal parent, and D as the new target
        9. After the process has been repeated to satisfaction, **despawn** all the normal parents of the chain by distance or chasm (which also performa a FarDelete)

    ??? abstract "Fast Variant"

        Prepare:

        A DI Ghost Weapon or Shield (A)

        Steps:

        1. Duplicate three normal copies of A by DI Duping (`B`, `C`, & `D`)
        2. **Equip** A and **drop** C on the ground
        3. Highlight C with Fuse and **pause** the game
        4. **Drop** A and **swap** to B
        5. **Unpause** and **fuse** C to B immediately
        6. Either [pause immediately after pressing fuse, then pause buffer] or [pause a few frames after pressing fuse]
        7. **Drop** B and **swap** to D
        8. Dupe 2 copies of C, then **drop** D and **pick up** C
        9. **Repeat** from step 3 with D as the next target
        10. After the process has been repeated to satisfaction, **despawn** all the normal parents of the chain by distance, drop limit, or chasm (which all performs a FarDelete)

    !!! danger "Long Chains"

        Extended dependency chains (FE and CF) can cause instability, such as freezing the game on some cutscenes and loads.
        
        If this method is performed with shields, simply zuggle a handful at once and use a rocket shield to fully detangle each zuggle, repeating for all of them.
        
        If weapons were used, zuggle every other in the chain (or less frequently if desired), use fuse-over detangle to leave only a cf remnant, then **destroy** the detangled weapons to break the chain apart. (a proper weapon detanglement is not viable for this use-case)

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            A[DI Ancestor]
            B[Normal Ancestor]
            C[DI Parent]
            D[Normal Parent]
            E[DI Child]
            F[Normal Parent]
            G[DI Grandchild]
            H[Normal Parent]
            I{Further Generations}

            A -->|DI| C
            B -->|DI| C
            C -->|DI| E
            D -->|DI| E
            E -->|DI| G
            F -->|DI| G
            G -->|DI| I
            H -->|DI| I
        ```

    _Method developed by Squidwest(?) - Jan 23, 2026(?)_

    #### Method 6: <br/>Chaining + Mineru FE ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses Mineru FE to make the normal ancestor of the chain cull with her, allowing it to be used on any patch and anywhere Mineru's sage avatar can be summoned.

    Prepare:

    - A DI Shield `A` (Method works the same with weapons)
    - A normal shield `B`
    - Mineru
    - A stake

    Steps:

    1. Mineru FE B
    2. [Smuggle](uid:TGY) A and equip B
    3. Target shield `C` with Fuse
    4. Induce Mineru to cull, and **fuse** C to B shortly before B culls via her
    5. **Drop** B and **swap** to another shield `D`
    6. Dupe 2 new shields off C by trying to pick it up (be careful B is not picked up)
    7. **Drop** D, and optionally **pick up** and **drop** A to remove its dependency (which contributes to Zuggle Overload)
    8. **Pick up** and **smuggle** C, then **equip** duped shield E
    9. Induce Mineru to cull, and **fuse** D to E shortly before C culls (via B, via her)
    10. **Repeat** steps 5-9 with repeated new shields
    11. Once process has been repeated to satisfaction, **destroy** all remaining normal parents in any order via distance, drop limit, or chasm
    12. Finally, **detangle** B from Mineru before warping or dismissing her, to prevent her from destroying all your hard work

    !!! danger "Long Chains"

        Extended dependency chains (FE and CF) can cause instability, such as freezing the game on some cutscenes and loads.
        
        If this method is performed with shields, simply zuggle a handful at once and use a rocket shield to fully detangle each zuggle, repeating for all of them.
        
        If weapons were used, zuggle every other in the chain (or less frequently if desired), use fuse-over detangle to leave only a cf remnant, then **destroy** the detangled weapons to break the chain apart. (a proper weapon detanglement is not viable for this use-case)

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            MINERU[Mineru]
            A[DI Ancestor]
            B[Normal Ancestor]
            C[DI Parent]
            D[Normal Parent]
            E[DI Child]
            F[Normal Parent]
            G[DI Grandchild]
            H[Normal Parent]
            I{Further Generations}

            MINERU -->|FE| B
            A -->|DI| C
            B -->|DI| C
            C -->|DI| E
            D -->|DI| E
            E -->|DI| G
            F -->|DI| G
            G -->|DI| I
            H -->|DI| I
        ```

    _Method developed by ??? - I don't know when it was done first_

    #### Method 7: <br/>Chaining + Torch Culling ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses Pyroculling to cull the DI ancestor of the chain on command, thus culling the entire chain and allowing the DI chaining to continue. Chain.
    - I don't like it very much and I invented it. It's slow, inconsistent, and prone to self-destruction.
    - But if you're on an old patch for some poorly-thought out reason (or speedrunning, which might be the same thing?), I guess it's better than not having DI at all.
    - Just use the mineru one or one of the overload ones and leave the good methods to the people's patch.

    !!! warning "Mediocre"

        Method 7 is not especially great.

    Prepare:

    - A DI Weapon or Shield `A`
    - A torch `B`
    - A culling area
    - A flame emitter

    Making the setup:

    1. Duplicate 2 normal copies of A (`C` and `D`)
    2. Cold Drop B and drop C
    3. Overload Cold Fuse B and C to protect them from the drop limit
    4. Use A and C to [Ghost DI](uid:BEW) D    
    5. Ultrahand B and place it next to a wall in a culling area
    6. Point the Flame Emitter at the head of B from point-blank, ensuring the fire strikes a solid surface as close to the torch-head as possible
    7. Glue C to B (also within the culling area) and activate the Flame Emitter
    9. To cull D, use the ability wheel to select and open Recall, causing a 2-frame pause. The torch should begin culling after cancelling recall, allowing C to cull with it

    Making DI Ghosts:

    1. [Smuggle](uid:TGY) D, **equip** Normal Shield `E`, and **drop** target Shield `F` on the ground
    2. Hold L to open the ability wheel, select Recall, and release L
    3. With the Recall view open, Hold L to open the ability wheel, and select Fuse
    4. Release L and **Fuse** F to E shortly after fuse opens
    5. **Drop** E and **swap** to Normal Shield `G`
    6. F will be attached to B on the ground. Dupe two replacement copies (`H` and `I`, then **drop** G
    7. Optionally, **pick up** and **drop** D to remove its overload
    8. **Pick up** F
    9. **Repeat** from step 2, with F as the new smuggle, G as the new target, and H as the new normal parent
    10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance, drop limit (except C), or chasm (which all perform a FarDelete)

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
        
            FLAME["Flame Emitter"]
            A["DI Ancestor (A)"]
            B["Torch (B)"]
            C["Normal Ancestor (C)"]
            D["DI Parent (D)"]
            E[Normal Parent]
            F[DI Child]
            G[Normal Parent]
            H[DI Grandchild]
            I[Normal Parent]
            J{Further Generations}

            C -->|DI| D
            A -->|DI| D
            FLAME -->|"Point at"| B
            C -->|Glue| B
            D -->|DI| F
            E -->|DI| F
            F -->|DI| H
            G -->|DI| H
            H -->|DI| J
            I -->|DI| J
        ```

    _method "developed" by Squidwest - not worth posting about, even with the drop limit protection_

    #### Method 8: <br/>Chaining + Aerophasing ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method uses Intangible Aerophasing to cull Link, and thus the intended normal parent of each DI item in the chain, allowing for a portable chaining method on all versions.
    - Astonishingly, it's actually decent.

    !!! success "Decent"

        Method 8 is decent.

    ??? abstract "Safe Variant"

        Prepare:

        - A DI Ghost Weapon or Shield `A`
        - Intangible Aerophasing

        Steps:

        1. Duplicate three normal copies of A by DI Duping (`B`, `C`, & `D`)
        2. **Smuggle** A and **equip** B, then **drop** C on the ground
        3. Stand on the phasing platform
        4. Highlight C with Fuse, then **pause** the game while Link is **culled**
        4. **Unpause** and immediately fuse C to B. C will become a DI Ghost
        5. **Drop** B and **swap** to D
        6. C will be attached to B on the ground. **Dupe** two replacement copies (`E` and `F`), then **drop** D
        7. Optionally, **pick up** and **drop** A to remove its overload
        8. **Pick up** C
        9. **Repeat** from step 2, with C as the new smuggle, E as the new normal parent, and D as the new target
        10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance, drop limit, or chasm (which all perform a FarDelete)

    ??? abstract "Fast Variant"

        Prepare:

        A DI Ghost Weapon or Shield (A)
        Intangible Aerophasing

        Steps:

        1. Duplicate three normal copies of A by DI Duping (`B`, `C`, & `D`)
        2. **Equip** A and **drop** C on the ground
        3. Stand on the phasing platform
        4. Highlight C with Fuse, then **pause** the game while Link is **culled**
        5. **Drop** A and **swap** to B
        6. Unpause and immediately fuse C to B; C will become a DI Ghost
        7. **Drop** B and **swap** to D
        8. C will be attached to B on the ground. **Dupe** 2 copies of C, then **drop** D and **pick up** C
        9. **Repeat** from step 3 with D as the next target
        10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance or chasm (which also performs a FarDelete)

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            A[DI Ancestor]
            B[Normal Ancestor]
            C[DI Parent]
            D[Normal Parent]
            E[DI Child]
            F[Normal Parent]
            G[DI Grandchild]
            H[Normal Parent]
            I{Further Generations}

            A -->|DI| C
            B -->|DI| C
            C -->|DI| E
            D -->|DI| E
            E -->|DI| G
            F -->|DI| G
            G -->|DI| I
            H -->|DI| I
        ```

    _Method developed by ??? - I don't know who did it first or when so I'm not prepared to claim authorship_

=== "Turbo Cloning Methods" ###

    - These methods use a purgatorized DI shield to repeatedly [Turbo Clone] each target in turn, without inadvertently dropping the DI shield.
    - The setup will persist in place indefinitely until the game is closed.
    - They are optimal for batch production without Zuggle Overload.
    - They are also ideal for both shield batches of any size, and for repeatedly creating small batches of any target type.
    - The only difference between the methods lies in the conisderations made for the target type.

    #### The Setup ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This is the base part of the setup, which only needs to be created once, and can be used for all the below methods.
    - Thus, the below methods will assume this portion was already performed, and will use the established names for the components.

    Prepare:

    - A DI Shield `A`
    - An Octo Balloon
    - A Shock Fruit (or other shock source)
    
    Steps:

    1. **Dupe** 3 copies of A
    2. Use A to [Ghost DI](uid:BEW#method-1-fuse-drop-swap-120) DI shield `B`, then dispose of the normal parent
    3. Use A and normal parent `C` to Ghost DI an Octo Balloon
    4. [Smuggle](uid:TGY) B and **equip** C
    5. Get shocked with shield unsheathed; this will purgatorize B and cause it to only attach when it has a dependency chain back to Link via A
    6. Use C so that the Octo Ballon detangles from it; C can then be disposed of or reused in the DI process

    #### Method 9: <br/>For Shields ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method is the simplest and fastest of the Turbo Cloning methods, making it ideal for quickly producing DI Ghosts to, for example, PSLOT objects.

    Prepare:
    
    - The base setup

    ??? abstract "Creating DI Ghost Shields (Steady Variant)"

        - This variant is slower, but follows a steady rhythm that makes it easier.
        - It is slower because duping A prevents Fuse from highlighting the current target for roughly a full second.

        Steps:

        1. [Zuggle Drop](uid:L84) `A` to attach `B`
        2. **Equip** another shield and a random 1-handed weapon, then **unsheathe** them
        3. Face A and **pick up** a dupe of it, then **drop** a target shield on the ground (if not already present) and turn to face the target
        4. Every other repetition, instead turn to the target **first**, _then_ dupe (as the target will be past A)
        5. Highlight the target with Fuse
        6. Start holding ZL and **pause** the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
        7. **Drop** the equipped shield and **swap** to the dupe of A
        8. **Unpause** the game and mash **Cancel** (`B/X`) to Octo Detangle the target from both parents (if successful, it will be stuck in midair with a displaced pickup prompt)
        9. **Repeat** from step 3/4, depending on cycle parity, until satisfied
        10. **Pick up** and **drop** A to detach B; the setup will remain ready until needed again

        Done correctly, each new target will drop on the opposite side of Link as the previous one, and none will block A from being duped from. The only necessary movement will be a single 180 degree turn per DI.

        !!! tip "Mistake recovery"

            - If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable). A new target will need to be duped from one of the prior targets.
            - If a DI is failed, continue as though it was never attempted.

        ??? example "Method Structure Diagram"

            ```mermaid
            graph TD
                A[A] -->|DI| B[B]
                A -->|DI| C[Octo Balloon]
                B -->|DI| D[Target 1]
                E[Normal Parent 1] -->|DI| D
                F[Dupe of A] -->|Detangles| D
                E -->|Becomes| G[Target 2]
                F -->|Becomes| H[Normal Parent 2]
            ```

    ??? abstract "Creating DI Ghost Shields (Fast Variant)"

        - This variant is faster, but doesn't follow a steady rhythm, and is liable to fail on anything but perfectly level ground.
        - This is because buildup of spent Octo Balloon shields can cause new parents to fail-drop instead of fully dropping, but only on an upslope

        Steps:

        1. [Zuggle Drop](uid:L84) A to attach B
        2. **Equip** another shield and a random 1-handed weapon, then **unsheathe** them
        3. **Drop** many targets (up to 21) in a pile on one side of A
        4. **Fill** the shield inventory with dupes of A
        5. Highlight _any_ target in the pile with Fuse
        6. Start holding ZL and **pause** the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
        7. **Drop** the equipped shield and **swap** to a dupe of A
        8. **Unpause** the game and mash **Cancel** (`B/X`) to Octo Detangle the target from both parents (if successful, it will be stuck in midair with a displaced pickup prompt)
        9. **Repeat** from step 5 until either the dupes of A run out, or the target pile runs out
        10. Either dupe more copies of A, or turn to face the pile of detangled parents, respectively
        11. Continue until satisfied
        12. **Pick up** and **drop** A to detach B; the setup will remain ready until needed again

        !!! tip "Mistake recovery"

            - If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable). The large pool of potential targets generally prevents this from affecting the process.
            - If a DI is failed, continue as though it was never attempted.

        ??? example "Method Structure Diagram"

            ```mermaid
            graph TD
                A[A] -->|DI| B[B]
                A -->|DI| C[Octo Balloon]
                B -->|DI| D[Target From Pool 1]
                E[Normal Parent 1] -->|DI| D
                F[Dupe of A] -->|Detangles| D
                E -->|Enters| G[Target Pool 2]
                F -->|Becomes| H[Normal Parent 2]
            ```

    #### Method 10: <br/>For Weapons/Bows ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - Due to the fact that the parents are still shields, this method produces a duplicate of A as a byproduct each time it is used.
    - Careful movement and a flat space will prevent this from becoming a problem.

    Prepare:

    - The base setup
    - At least one of the target type, ideally a DI Ghost

    ??? abstract "Creating DI Ghost Weapons/Bows (Steady Variant)"

        - This variant is slower, but follows a steady rhythm that makes it easier.
        - It is slower because duping A prevents Fuse from highlighting the current target for roughly a full second.

        Steps:

        1. If a DI ghost of the target is already prepared, place it next to `A`
        2. Leave only one empty space in the Shield pouch and the target type's pouch. This will allow both A and the target to be consistently duplicated (versus duping 2 of one and none of the other)
        3. [Zuggle Drop](uid:L84) A to attach `B`
        4. **Equip** another shield and a random weapon, then **unsheathe** them
        5. Face A and **pick up** a dupe of it (and the target, if possible)
        6. **Drop** the (dupe of the) target and turn around, then highlight it with Fuse
        7. Start holding ZL and **pause** the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
        8. **Drop** the equipped shield and **swap** to the Octo Balloon Shield
        9. **Unpause** the game and mash **Cancel** (`B/X`) to Octo Detangle the target from both parents (if successful, it will be stuck in midair with a displaced pickup prompt)
        11. If a DI Ghost of the target was not yet prepared, there is now one to be used for duping
        10. The DI'd targets will build up on the opposite side of Link as A, while the spent dupes of A will build up behind it, neither obstructing duplication
        12. **Repeat** from step 5 until satisfied
        13. **Pick up** and **drop** A to detach B

        !!! tip "Mistake recovery"

            If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable).
            
            If a DI is failed, continue as though it was never attempted.

        ??? example "Method Structure Diagram"
    
            ```mermaid
            graph TD
                A[A] -->|DI| B[B]
                A -->|DI| C[Octo Balloon]
                B -->|DI| D[Target 1]
                E[Normal Parent 1] -->|DI| D
                F[Dupe of A] -->|Detangles| D
                E -->|Becomes| G[Discarded]
                F -->|Becomes| H[Normal Parent 2]
            ```

    ??? abstract "Creating DI Ghost Weapons/Bows (Fast Variant)"

        - This variant is faster, but doesn't follow a steady rhythm, and is liable to fail on anything but perfectly level ground.
        - This is because buildup of spent Octo Balloon shields can cause new parents to fail-drop instead of fully dropping, but only on an upslope

        Steps:

        1. [Zuggle Drop](uid:L84) `A` to attach `B`
        2. **Equip** another shield and a random 1-handed weapon, then **unsheathe** them.
        3. **Drop** many targets (up to 21) in a pile on one side of A
        4. Stand on the other side of A and **fill** the shield inventory with dupes of A
        5. Highlight _any_ target in the pile with Fuse
        6. Start holding ZL and **pause** the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
        7. **Drop** the equipped shield and **swap** to a dupe of A
        8. **Unpause** the game and mash **Cancel** (`B/X`) to Octo Detangle the target from both parents (if successful, it will be stuck in midair with a displaced pickup prompt)
        9. **Repeat** from step 5 until either the dupes of A run out, or the target pile runs out
        10. **Dupe** more of whatever was depleted before continuing.
        11. Continue until satisfied
        12. **Pick up** and **drop** A to detach B; the setup will remain ready until needed again

        !!! tip "Mistake recovery"

            If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable).

            If a DI is failed, continue as though it was never attempted.
    
        ??? example "Method Structure Diagram"
    
            ```mermaid
            graph TD
                A[A] -->|DI| B[B]
                A -->|DI| C[Octo Balloon]
                B -->|DI| D[Target From Pool]
                E[Normal Parent 1] -->|DI| D
                F[Dupe of A] -->|Detangles| D
                E -->|Becomes| G[Discarded]
                F -->|Becomes| H[Normal Parent 2]
            ```

    #### Method 11: <br/>For Non-equipment ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - Unlike equipment, DI Ghost objects (even materials from the pouch) cannot be used as a cloning source, or interacted with in general, so they are typically less useful to DI.
    - This method is provided mostly for posterity, but there are occasional uses for DI Ghost objects, so who knows what may come.

    Prepare:

    - The base setup (with named components)
    - One of the target for _each_ DI Ghost to be made

    ??? abstract "Creating DI Objects (Steady Variant)"

        - This variant is slower, but follows a steady rhythm that makes it easier.
        - It is slower because duping A prevents Fuse from highlighting the current target for roughly a full second.

        Steps:

        1. [Zuggle Drop](uid:L84) `A` to attach `B`
        2. **Equip** another shield and a random weapon, then **unsheathe** them
        3. Face A and **pick up** a dupe of it
        4. **Drop/Deploy** a target material/device and highlight it with Fuse
        5. Start holding ZL and **pause** the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
        6. **Drop** the equipped shield and **swap** to the dupe of A
        7. **Unpause** the game and mash **Cancel** (`B/X`) to Octo Detangle the target from both parents (if successful, it will be floating in the air, not attached to the normal parent)
        8. **Repeat** from Step 3 until satisfied
        9. **Pick up** and drop A to detach B

        !!! tip "Mistake recovery"

            If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable).

            If a DI is failed, continue as though it was never attempted.

        ??? example "Method Structure Diagram"

            ```mermaid
            graph TD
                A[A] -->|DI| B[B]
                A -->|DI| C[Octo Balloon]
                B -->|DI| D[Target 1]
                E[Normal Parent 1] -->|DI| D
                F[Dupe of A] -->|Detangles| D
                E -->|Becomes| G[Discarded]
                F -->|Becomes| H[Normal Parent 2]
            ```
    ??? abstract "Creating DI Objects (Fast Variant)"

        1. [Zuggle Drop](uid:L84) `A` to attach `B`
        2. **Equip** another shield and a random weapon, then **unsheathe** them
        3. Face A and **fill** the inventory with dupes of it
        4. **Drop/Deploy** many target materials/devices and highlight one with Fuse
        5. Start holding ZL and **pause** the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
        6. **Drop** the equipped shield and **swap** to a dupe of A
        7. **Unpause** the game and mash **Cancel** (`B/X`) to Octo Detangle the target from both parents (if successful, it will be floating in the air, not attached to the normal parent)
        8. **Repeat** from Step 3 until satisfied
        9. **Pick up** and **drop** A to detach B

        !!! tip "Mistake recovery"

            If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable).

            If a DI is failed, continue as though it was never attempted.

        ??? example "Method Structure Diagram"

            ```mermaid
            graph TD
                A["DI Ghost (A)"]
                B["Purgatorized<br/>DI Ghost (B)"]
                OCTO["DI Ghost<br/> Octo Balloon"]
                C[Target From Pool]
                D[Normal Parent]
                E[Dupe of A]
                F[Discarded]

                A -->|DI| B
                A -->|DI| OCTO
                B -->|DI| C
                D -->|DI| D
                E -->|Detangles| D
                D -->|Becomes| F
                E -->|Becomes| D
            ```

        ??? example "Method Structure Diagram"

            ```mermaid
            graph TD
                A[A] -->|DI| B[B]
                A -->|DI| C[Octo Balloon]
                B -->|DI| D[Target From Pool]
                E[Normal Parent 1] -->|DI| D
                F[Dupe of A] -->|Detangles| D
                E -->|Becomes| G[Discarded]
                F -->|Becomes| H[Normal Parent 2]
            ```

    _Turbo Replication discovered by Aergyl - Jan 31, 2026_

    _Batch methods developed by Squidwest - Mar 05, 2026_

## Notes

- Due to the difference in resulting structure, these methods are usually _not_ interchangeable when called for by another tutorial. They have been grouped by structure for this reason.

## References and Resources

??? quote "Discord References"

    - [Overload + DS Culling](https://discord.com/channels/1086729144307564648/1110956205624532993/1462096452540043304)
    - [Overload + Torch Culling](https://discord.com/channels/1086729144307564648/1110956205624532993/1473846010207015167)
    - [Overload + Limbo](https://discord.com/channels/1086729144307564648/1110956205624532993/1479539674912526587)
    - Overload + Aerophasing is barely worth citing
    - [Chaining + DS Culling](https://discord.com/channels/1086729144307564648/1113557914444111873/1468025665763938420)
    - Chaining + Mineru culling is pretty okay I might make a referent for it if one doesn't already exist
    - So is Chaining + Aerophasing
    - Chaining + Torch Culling is bad and naughty and should be set adrift
    - [Batch Turbo Cloning for shields](https://discord.com/channels/1086729144307564648/1110956205624532993/1479327965807644777)
    - [Batch Turbo Cloning for weapons/bows]()
    - [Batch Turbo Cloning for objects/materials]()
    - [Fast Batch Turbo Cloning Methods]()

## Related
- [Despawn Interrupt](search:Despawn Interrupt)
