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
Some of the properties of [DI Ghosts](uid:BEW) (typically equipment, sometimes otherwise) are best exploited with large numbers of them. This page provides various convenient ways to produce large numbers of them.

_Credits - See individual methods_

## Instructions

- Due to the difference in resulting structure (ie the "map" of connections between parts), these methods are usually _not_ interchangeable when called for by another tutorial.
- Thus, the methods are partitioned by the structure they create, which happens to sensibly divide them by general process as well.

=== "Overload methods" ###

    #### Info ?

    - These methods use Overload Pseudo Fuse to DI targets without ever creating normal parents, removing the need to despawn them between targets.
    - They are ideal for creating very large quantities of DI Ghosts, and are sometimes useful for the resulting structure (a DI parent and a normal parent, each sharing many cold-fused DI children).

    !!! danger "Fuse-Over(load)"

        Detangling a DI Ghost from its parent by "fuse-over" leaves a Cold Fuse connection behind, and detaching a DI Ghost from its PF parent does the same. Due to this, `C` and `D` in each of these methods will each gain one _peristent_ dependency for each DI Ghost produced. After 30 uses, C and D will reach Fuse Overload. If a 31st use is attempted, you will create a "Reference FE" connection, which will **crash the game** if you drop either!

    !!! danger "Self-Fusing"

        When an overload-pickup (`D` in these methods) has a connection back to Link, it is possible to target it to be fused to itself. Under most circumstances, this will immediately **crash the game** if attempted.

    #### Method 1: <br/>Overload PF + Drop-Swap Culling ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    ##### Info
    ---
    notoc: true
    ---

    - This is the most basic overload method, requiring only the absolute minimum prerequisites.
    - As such, it can be done nearly anywhere at nearly any time.

    _Method developed by mulberry - Jan 17, 2026_

    ##### Requirements
    ---
    notoc: true
    ---

    - 13 Zuggle Overload
    - A DI shield `#!python A`, ideally a [DI Ghost](uid:BEW) (all types can be mirrored)

    ##### Creating the setup
    ---
    notoc: true
    ---

    1. [Smuggle](uid:TGY) `#!python A` and equip normal shield `#!python B`
    2. **Fuse** weapon `#!python C` to `#!python B` and **pause** a few frames after (for instance, by buffering the ability wheel at the same time as pressing Fuse, then selecting Map)
    3. **Drop** `#!python B`, **swap** to another shield, and **unequip** that shield, then **unpause**
    4. _Smuggle_ `#!python A` again
    5. [Overload drop](uid:8QH) a shield and **Fuse** it to a weapon
    6. **Fuse** weapon `#!python D` to said shield, FE-ing it to `#!python A`
    7. **Swap** shield, then [Warm Drop](uid:C6H) it to leave `#!python A` [Zuggle Dropped](uid:L84)
    8. **Unequip** weapon
    9. _Smuggle_ `#!python C`, pick up `#!python B`, and [Overload Pickup](uid:8QH) `#!python D`
    10. Glue `#!python D` to something to elevate it and ensure it cannot accidentally be targeted by Fuse. Face the blade _away_ from the other object to keep fuse targets from colliding with it
    11. Optionally, position a wall behind Link's back which can force `#!python B` to **fail-drop**

    ##### Creating DI Ghosts
    ---
    notoc: true
    ---

    1. **Fuse** target to `#!python D` ([Overload FE](uid:0XV) to `#!python C`)
    2. **Fuse** target to `#!python D` again. As it already has an FE parent (`#!python C`), this time it will Pseudo-Fuse to `#!python D` and begin fading away
    3. **Pause** the game before the target fully fades out (buffering wheel and selecting Map will work here too)
    4. **Drop** `#!python B`, **equip** another shield, and **unequip** it. This will cull `#!python B`, and thus `#!python C`, and thus the target, Ghost DI-ing it
    5. If you fail-dropped `#!python B`, proceed with the next target. If not, pick it up before proceeding
    6. To continue beyond 30 successful uses, first **destroy** and **remake** `#!python C` and `#!python D`

    ##### Resources ?
    ---
    notoc: true
    ---

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

    #### Method 2: <br/>Overload PF + Torch Culling ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    ##### Info
    ---
    notoc: true
    ---

    - This method builds on Method 1 with a new culling method, increasing the speed and reducing the setup time and complexity.
    - However, it can only be performed at a culling area.

    _Method developed by mulberry - Feb 18, 2026_

    ##### Requirements
    ---
    notoc: true
    ---

    - 13 Zuggle Overload
    - A DI weapon or shield `#!python A`
    - A torch
    - A flame emitter

    ##### Creating the setup
    ---
    notoc: true
    ---

    1. A and normal item `#!python B` [Ghost DI](uid:BEW) Shield `#!python C`, keep normal parent
    2. [Smuggle](uid:TGY) `C`
    3. [Cold Drop](uid:C6H) the torch and place it next to a wall in a culling area
    4. Point the Flame Emitter at the head of the torch from point-blank, ensuring the fire strikes a solid surface as close to the torch-head as possible.
    5. Glue `B` to the torch and **activate** the Flame Emitter.
    6. To cull `C`, use the ability wheel to select and open Recall, causing a 2-frame pause. The torch should begin culling after cancelling Recall
    7. [Overload Drop](uid:8QH) a shield `#!python D` and **Fuse** it to a weapon `#!python E`

    ##### Creating DI Ghosts
    ---
    notoc: true
    ---

    1. **Fuse** the target to `D` ([Overload FE](uid:0XV) to `C`)
    2. Use the ability wheel to open recall, then use it to open fuse and _immediately_ fuse the target to `D` again
    3. As long as fuse is pressed more than 2 frames before the torch fully culls, the cull _will_ occur within the target's Ghost DI timing window
    4. To continue beyond 30 successful uses, first **destroy** and **remake** `C` and `D`

    ##### Resources ?
    ---
    notoc: true
    ---

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

    #### Method 3: <br/>Overload PF + Mineru Limbo ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    ##### Info
    ---
    notoc: true
    ---

    - This method uses Mineru as a culling source, placing her in Limbo to maximize control over her culling.
    - It is the fastest overload method, but can only be done when & where Mineru's Sage Avatar can be summoned and put into Limbo.

    _Method developed by mulberry - Mar 06, 2026_ 

    ##### Requirements
    ---
    notoc: true
    ---

    - 13 Zuggle Overload
    - A DI weapon `A` (all types can be inverted)
    - Mineru
    - A normal shield `B`
    - A Stake (or other setup to place Mineru into limbo)

    ##### Creating the setup
    ---
    notoc: true
    ---

    1. Mineru FE `B`
    2. [Smuggle](uid:TGY) `A`, equip `B`, and target shield `C` with Fuse
    3. Induce Mineru to **cull** and fuse `C` to `B` shortly before `B` culls; this will DI `C`
    4. Place `B` aside and _smuggle_ `C`
    5. [Overload Drop](uid:8QH) shield `D` and fuse to weapon `E`

    ##### Creating DI Ghosts
    ---
    notoc: true
    ---

    1. Stand on a stake at the right height so that Mineru goes into "Limbo" when you cull her (Mineru invisible, but `B` and `C` unculled)
    2. **Fuse** target to `D` ([Overload FE](uid:0XV) to `C`)
    3. **Fuse** target to `D` again, and jump _immediately_ after so that Mineru culls (and culls the target by extension)
    4. To continue beyond 30 successful uses, first **destroy** and **remake** `C` and `D` (start from setup step 2)

    ##### Resources ?
    ---
    notoc: true
    ---

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

    #### Method 4: <br/>Overload PF + Aerophasing ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    ##### Info
    ---
    notoc: true
    ---

    - Method 4 uses Aerophasing as a culling source, allowing for a use-anywhere method on all patches.
    - Unlike Methods 2 and 3, this method is a strict downgrade from Method 1 on patches that can perform the latter.

    _Don't know who did this first but I doubt they want to be credited_

    ##### Requirements
    ---
    notoc: true
    ---

    - 13 Zuggle Overload
    - A DI shield `A`, ideally a DI Ghost (all types can be mirrored)
    - [Intangible Aerophasing](8QL)

    ##### Creating the setup
    ---
    notoc: true
    ---

    1. [Smuggle](uid:TGY) A and equip normal shield `B`, then stand on the phasing platform
    2. Optionally, **Pause** the game while Link is culled. This causes him to always be unculled right after unpausing, making fuse timing easier throughout the method
    3. Just after Link unculls, **Fuse** a weapon `C` to B; Link will cull soon enough to Ghost DI C
    4. Drop B and leave it aside, but **pick up** and _re-smuggle_ A
    5. [Overload Drop](uid:8QH) a shield and **Fuse** it to a weapon
    6. **Fuse** weapon `D` to said shield, FE-ing it to A
    7. **Swap** shield, then [Warm Drop](uid:C6H) it to leave A [Zuggle Dropped](uid:L84)
    8. **Unequip** weapon
    10. _Smuggle_ C, **equip** B, and [Overload Pickup](uid:8QH) D
    11. **Glue** D to something to elevate it and ensure it cannot accidentally be targeted by Fuse. Face the blade _away_ from the other object to keep fuse targets from colliding with it

    ##### Creating DI Ghosts
    ---
    notoc: true
    ---

    1. Stand on the phasing platform
    2. Just after Link unculls, **fuse** target to D ([Overload FE](uid:0XV) to C)
    3. Just after Link unculls, **fuse** target to D again. As it already has an FE parent (C), this time it will Pseudo-Fuse to D and begin fading away
    4. Link will cull soon enough after to automatically Ghost DI the target (by culling B, which culls C)
    5. Repeat from step 2 with the next target. The previous targets can stay attached to D without issue 
    5. To continue beyond 30 successful uses, first **destroy** and **remake** C and D

    ##### Resources ?
    ---
    notoc: true
    ---

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

=== "DI Chaining Methods" ###

    #### Info ?

    - These methods create a chain of DI ghosts, allowing the normal-parent despawning to be saved until the end of the process (as each target retains a DI parent as long as desired).
    - They are ideal for medium batches and minimalist replication, but can _only_ be used for weapons and shields.
    - These methods are all written to use shields, but will work exactly the same if used with weapons (or even some mixtures of the two).
    - Unlike with overload methods, Methods 6-8 are _all_ strict downgrades from Method 5 on patches that can perform the latter.
    - Some methods can make use of a time-saving trick: drop-swapping each DI parent immediately before fusing allows the fuse to apply to it during that temporary smuggle just as if it was permanently smuggled.
    - On methods where this can be consistently performed, it is provided as a "Fast" variant after the normal "Safe" variant.

    !!! danger "Long Chains"

        - Extended dependency chains (FE and CF(?)) can cause instability, such as freezing the game on some cutscenes and loads. 
        - To avoid this risk, it is necessary to **detangle** the DI parents used in any of these methods.
        - Detanglement should not be performed until _after_ the normal parents have been destroyed.
        - For shields, simply zuggle a handful of DI parents at once and use a rocket shield to fully detangle each zuggle, repeating for all the DI parents.
        - For weapons, zuggle every second DI parent in the chain (or every third etc if desired), use fuse-over detangle to leave only a cf remnant, then **destroy** the detangled weapons to break the chain apart. (full weapon detanglement is not possible here)

    #### Method 5: <br/>Chaining + Drop-Swap Culling ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    ##### Info
    ---
    notoc: true
    ---

    - Method 5 is the most basic chaining method, and the most minimal batch method in general.

    _Method developed by Squidwest(?) - Jan 23, 2026(?)_

    ##### Requirements

    - A DI Ghost shield `A`

    ##### Safe Variant ?
    ---
    notoc: true
    ---

    1. Duplicate three normal copies of A by DI Duping (`B`, `C`, & `D`)
    2. [Smuggle](uid:TGY) A and **equip** B, then **drop** C on the ground
    3. Start to **fuse** C to B, then **pause** the game a few frames later (For example, by buffering the ability wheel at the same time as pressing fuse, then selecting Map)
    4. **Drop** B and **swap** to D
    5. C will be attached to B on the ground. Dupe two replacement copies (E and F), then **drop** D
    6. Optionally, **pick up** and **drop** A to remove its overload
    7. **Pick up** C
    8. **Repeat** from step 2, with C as the new smuggle, E as the new normal parent, and D as the new target
    9. After the process has been repeated to satisfaction, **despawn** all the normal parents of the chain by distance, drop limit, or chasm (which all perform a FarDelete)

    ##### Fast Variant ?
    ---
    notoc: true
    ---

    1. Duplicate three normal copies of A by DI Duping (`B`, `C`, & `D`)
    2. **Equip** A and **drop** C on the ground
    3. Highlight C with Fuse and **pause** the game
    4. **Drop** A and **swap** to B
    5. **Unpause** and **fuse** C to B immediately, then **pause** a few frames later (For example, by pausing on the **same** frame as fusing, then performing a **pause-buffer**)
    6. **Drop** B and **swap** to D
    7. Dupe 2 copies of C, then **drop** D and **pick up** C
    8. **Repeat** from step 3 with D as the next target
    9. After the process has been repeated to satisfaction, **despawn** all the normal parents of the chain by distance, drop limit, or chasm (which all perform a FarDelete)

    ##### Resources ?
    ---
    notoc: true
    ---

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

    #### Method 6: <br/>Chaining + Mineru FE ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    ##### Info
    ---
    notoc: true
    ---

    - This method uses Mineru FE to make the normal ancestor of the chain cull with her, allowing it to be used on any patch and anywhere Mineru's sage avatar can be summoned.
    - As many of the all-version Ghost DI methods end with a Mineru FE'd DI Ghost, steps 1-7 can be replaced with any such method (which may already be complete).
    - It does not feature Safe/Fast variants due to the difficulty of timing a drop-swap with Mineru's culling. However, it is technically possible.

    _Method developed by ??? - I don't know when it was done first_

    ##### Requirements
    ---
    notoc: true
    ---

    - A DI Ghost shield `A`
    - A normal shield `B`
    - Mineru

    ##### Steps
    ---
    notoc: true
    ---

    1. Mineru FE B
    2. [Smuggle](uid:TGY) A and equip B
    3. Target shield `C` with Fuse
    4. Induce Mineru to cull, and **fuse** C to B shortly before B culls via her
    5. **Drop** B and **swap** to another shield `D`
    6. Dupe 2 new shields off C by trying to pick it up (be careful B is not picked up)
    7. **Drop** D, and optionally **pick up** and **drop** A to remove its dependency (which contributes to Zuggle Overload)
    8. **Pick up** and _smuggle_ C, then **equip** duped shield E
    9. Induce Mineru to cull, and **fuse** D to E shortly before C culls (via B, via her)
    10. **Repeat** steps 5-9 with repeated new shields
    11. Once process has been repeated to satisfaction, **destroy** all remaining normal parents in any order via distance, drop limit, or chasm (which all perform a FarDelete)
    12. Finally, **detangle** B from Mineru before warping or dismissing her, to prevent her from destroying all your hard work

    ##### Resources ?
    ---
    notoc: true
    ---

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

    #### Method 7: <br/>Chaining + Aerophasing ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    ##### Info
    ---
    notoc: true
    ---

    - This method uses Intangible Aerophasing to cull Link, and thus the intended normal parent of each DI item in the chain, allowing for a portable chaining method on all versions.
    - Astonishingly, it's actually decent, at least in that it's consistent enough to permit a fast variant.

    !!! success "Decent"

        Method 7 is decent.

    _Method developed by ??? - I don't know who did it first or when so I'm not prepared to claim authorship_

    ##### Requirements

    - A DI Ghost shield `A`
    - Intangible Aerophasing

    ##### Safe Variant ?
    ---
    notoc: true
    ---

    1. Duplicate three normal copies of A by DI Duping (`B`, `C`, & `D`)
    2. [Smuggle](uid:TGY) A and **equip** B, then **drop** C on the ground
    3. Stand on the phasing platform
    4. Highlight C with Fuse, then **pause** the game while Link is **culled**
    4. **Unpause** and immediately fuse C to B; C will become a DI Ghost
    5. **Drop** B and **swap** to D
    6. C will be attached to B on the ground. **Dupe** two replacement copies (`E` and `F`), then **drop** D
    7. Optionally, **pick up** and **drop** A to remove its overload
    8. **Pick up** C
    9. **Repeat** from step 2, with C as the new smuggle, E as the new normal parent, and D as the new target
    10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance, drop limit, or chasm (which all perform a FarDelete)

    ##### Fast Variant ?
    ---
    notoc: true
    ---

    1. Duplicate three normal copies of A by DI Duping (`B`, `C`, & `D`)
    2. **Equip** A and **drop** C on the ground
    3. Stand on the phasing platform
    4. Highlight C with Fuse, then **pause** the game while Link is **culled**
    5. **Drop** A and **swap** to B
    6. Unpause and immediately fuse C to B; C will become a DI Ghost
    7. **Drop** B and **swap** to D
    8. C will be attached to B on the ground. **Dupe** 2 copies of C, then **drop** D and **pick up** C
    9. **Repeat** from step 3, replacing A, B, and C with the next equivalents in the chain
    10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance, drop limit, or chasm (which all perform a FarDelete)

    ##### Resources ?
    ---
    notoc: true
    ---

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

    #### Method 8: <br/>Chaining + Manual Culling ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: true
    ---

    ##### Info
    ---
    notoc: true
    ---

    - This method uses manual movement in and out of a culling margin to cull the normal ancestor of the chain, thus culling all the DI Ghosts in the chain.
    - It is the most minimal chaining method that works on all versions, but is much slower than Methods 5-7.
    - It does not feature a fast variant due to timing strictness, but it is likely possible to perform, maybe even consistently.

    _Method possibly developed by Squidwest - But idk_

    ##### Requirements
    ---
    notoc: true
    ---

    - A DI Ghost shield `A`

    ##### Steps
    ---
    notoc: true
    ---

    1. Duplicate five normal copies of A by DI Duping (`B`, `C`, `D`, `E`, and `F`)
    2. Optionally, Cold Fuse B to protect it from the drop limit. This will streamline the process when used with very long chains (>10 shields long)
    3. Use A and B to [Ghost DI](uid:BEW#full-fuse-methods) shield `C`, keep B
    4. Place B inside a culling area so that C can be culled by walking back and forth over the culling margin
    5. [Smuggle](uid:TGY) C and **equip** normal shield `D`
    6. Drop target shield `E` on the ground on the outside of the culling margin and highlight it with Fuse
    7. Walk over the margin and **Fuse** E to D at the same time, erring on the side of crossing the margin first
    8. As long as B began culling 0-2 frames after Fuse was pressed, E will successfully Ghost DI
    9. Re-enter the culling margin, then **Drop** D and swap to F
    10. E will be attached to D on the ground. Dupe two copies of E (`G` and `H`) to replace the shields spent, then **drop** F
    11. Optionally, **pick up** and **drop** C to remove its overload
    12. **Pick up** E
    13. Repeat from step 5, with E as the new smuggle, G as the new normal parent, and F as the new target
    14. After 10 or so uses, if step 2 was skipped, B will despawn due to the drop limit. Replace it in the culling area with the _newest_ normal parent in the chain before continuing
    15. After the process has been repeated to satisfaction, **despawn** all the remaining normal parents by distance, chasm, or drop limit (which all perform a FarDelete)

    ##### Resources ?
    ---
    notoc: true
    ---

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
            AREA[Culling Area]

            A -->|DI| C
            B -->|DI| C
            B -->|Place in| AREA
            C -->|DI| E
            D -->|DI| E
            E -->|DI| G
            F -->|DI| G
            G -->|DI| I
            H -->|DI| I
        ```

    #### Method 9: <br/>Chaining + Torch Culling ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: true
    ---

    ##### Info
    ---
    notoc: true
    ---

    - This method uses Pyroculling to cull the normal ancestor of the chain on command, thus culling the entire chain and allowing the DI chaining to continue. Chain.
    - I don't like it very much and I invented it. It's complicated and slow, the timing is tight, and it's prone to self-destruction.
    - I'm only including it because it _exists_, but maybe someone will see it and make it good...
    - It does not permit a Fast variant due to the strictness of the timing window. (though it is _probably_ possible?)

    _Method developed by Squidwest - And I am so sorry I did_

    ##### Requirements
    ---
    notoc: true
    ---

    - A DI shield `A`
    - A torch `B`
    - A culling area
    - A flame emitter

    ##### Making the setup
    ---
    notoc: true
    ---

    1. Duplicate 2 normal copies of A (`C` and `D`)
    2. [Cold Drop](uid:C6H) B and drop C
    3. Overload Cold Fuse B and C to protect them from the drop limit
    4. Use A and C to [Ghost DI](uid:BEW) D    
    5. Ultrahand B and place it next to a wall in a culling area
    6. Point the Flame Emitter at the head of B from point-blank, ensuring the fire strikes a solid surface as close to the torch-head as possible
    7. Glue C to B (also within the culling area) and activate the Flame Emitter
    9. To cull D, use the ability wheel to select and open Recall, causing a 2-frame pause. The torch should begin culling after cancelling Recall, allowing C to cull with it

    ##### Making DI Ghosts
    ---
    notoc: true
    ---

    1. [Smuggle](uid:TGY) D, **equip** Normal Shield `E`, and **drop** target Shield `F` on the ground
    2. Hold L to open the ability wheel, select Recall, and release L
    3. With the Recall view open, Hold L to open the ability wheel, and select Fuse
    4. Release L and **Fuse** F to E shortly after fuse opens
    5. **Drop** E and **swap** to Normal Shield `G`
    6. F will be attached to B on the ground. Dupe two replacement copies (`H` and `I`), then **drop** G
    7. Optionally, **pick up** and **drop** D to remove its overload
    8. **Pick up** F
    9. **Repeat** from step 2, with F as the new smuggle, G as the new target, and H as the new normal parent
    10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance, drop limit (except C), or chasm (which all perform a FarDelete)

    ##### Resources ?
    ---
    notoc: true
    ---

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

=== "Turbo Cloning Methods" ###

    #### Info ?

    ##### General info
    ---
    notoc: true
    ---

    - These methods use a purgatorized DI shield to repeatedly [Turbo Clone](uid:BEW#method-2-turbo-replication-120) each target in turn, without inadvertently dropping the DI shield.
    - The setup will persist in place indefinitely until the game is closed.
    - They are optimal for batch production without Zuggle Overload.
    - They are also ideal for both shield batches of any size, and for repeatedly creating small batches of any target type.
    - When performing them on terrain that isn't _perfectly_ flat, it is advised to stand atop a fully-driven **Stake** to minimize the chance of accidentally fail-dropping a fused shield.

    ##### Page-specific info
    ---
    notoc: true
    ---
    
    - The steps differ slightly depending on target type, so what is really one method is divided into 3 for clarity reasons.
    - Each method has a "steady" variant and a "fast" variant, which aim to maximize ease/speed respectively.
    - The Steady variant clones each Octo-Balloon Shield just before use, which inadvertently locks out Fuse targeting for about a second, but simplifies the steps.
    - The Fast variant clones an inventory-full of Octo-Balloon Shields at a time, which minimizes targeting lockout, but complicates the steps.

    _Turbo Replication discovered by Aergyl - Jan 31, 2026_

    _Batch methods developed by Squidwest - Mar 05, 2026_

    #### The Setup ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This is the base part of the setup, which only needs to be created once, and can be used for all the below methods.
    - Thus, the below methods will assume this portion was already performed, and will use the established names for the components.

    ##### Requirements
    ---
    notoc: true
    ---

    - A DI Shield `A`
    - An Octo Balloon
    - A Shock Fruit (or other shock source)

    ##### Steps:
    ---
    notoc: true
    ---

    1. **Dupe** 3 copies of A
    2. Use A to [Ghost DI](uid:BEW#method-1-fuse-drop-swap-120) DI shield `B`, then dispose of the normal parent
    3. Use A and normal parent `C` to Ghost DI an Octo Balloon
    4. [Smuggle](uid:TGY) B and **equip** C
    5. Get shocked with shield unsheathed; this will purgatorize B and cause it to only attach when it has a dependency chain back to Link via A
    6. Use C so that the Octo Ballon detangles from it; C can then be disposed of or reused in the DI process

    #### Method 10: <br/>For Shields ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - This method is the simplest and fastest of the Turbo Cloning methods, making it ideal for quickly producing DI Ghosts to, for example, PSLOT objects.
    - Nothing extra is required besides the base setup.

    ##### Shields - Steady Variant ?
    ---
    notoc: true
    ---

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

    ###### Resources ?

    !!! tip "Mistake recovery"

        - If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable). A new target will need to be duped from one of the prior targets.
        - If a DI is failed, continue as though it was never attempted.

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            A["DI Ghost (A)"]
            B["Purgatorized<br/>DI Ghost (B)"]
            OCTO["DI Ghost<br/> Octo Balloon"]
            C[Target 1]
            D[Normal Parent 1]
            E[Dupe of A]
            F[Target 2]
            G[Normal Parent 2]

            A -->|DI| B
            A -->|DI| OCTO
            B -->|DI| C
            D -->|DI| C
            E -->|Detangles| D
            D -->|Becomes| F
            E -->|Becomes| G
        ```

    ##### Shields - Fast Variant ?
    ---
    notoc: true
    ---

    1. [Zuggle Drop](uid:L84) A to attach B.
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

    ###### Resources ?

    !!! tip "Mistake recovery"

        - If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable). The large pool of potential targets generally prevents this from affecting the process.
        - If a DI is failed, continue as though it was never attempted.

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            A["DI Ghost (A)"]
            B["Purgatorized<br/>DI Ghost (B)"]
            OCTO["DI Ghost<br/> Octo Balloon"]
            C[Target From Pool 1]
            D[Normal Parent 1]
            E[Dupe of A]
            F[Target Pool 2]
            G[Normal Parent 2]

            A -->|DI| B
            A -->|DI| OCTO
            B -->|DI| C
            D -->|DI| C
            E -->|Detangles| D
            D -->|Enters| F
            E -->|Becomes| G
        ```

    #### Method 11: <br/>For Weapons/Bows ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - Due to the fact that the parents are still shields, this method produces a (fuseless) duplicate of A as a byproduct each time it is used.
    - Careful movement and a flat space (and perhaps a Stake to stand on) will prevent this from becoming a problem.
    - Besides the base setup, at least one of the target will be needed. A DI Ghost of it is preferred, but will be created if not yet prepared.

    ##### Weapons/Bows - Steady Variant ?
    ---
    notoc: true
    ---

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

    ###### Resources ?

    !!! tip "Mistake recovery"

        If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable).

        If a DI is failed, continue as though it was never attempted.

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            A["DI Ghost (A)"]
            B["Purgatorized<br/>DI Ghost (B)"]
            OCTO["DI Ghost<br/> Octo Balloon"]
            C[Target 1]
            D[Normal Parent 1]
            E[Dupe of A]
            F[Discarded]
            G[Normal Parent 2]

            A -->|DI| B
            A -->|DI| OCTO
            B -->|DI| C
            D -->|DI| C
            E -->|Detangles| D
            D -->|Becomes| F
            E -->|Becomes| G
        ```

    ##### Weapons/Bows - Fast Variant ?
    ---
    notoc: true
    ---

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

    ###### Resources ?

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
            D[Normal Parent 1]
            E[Dupe of A]
            F[Discarded]
            G[Normal Parent 2]

            A -->|DI| B
            A -->|DI| OCTO
            B -->|DI| C
            D -->|DI| C
            E -->|Detangles| D
            D -->|Becomes| F
            E -->|Becomes| G
        ```

    #### Method 12: <br/>For Non-equipment ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    - Unlike equipment, DI Ghost objects (even materials from the pouch) cannot be used as a cloning source, or interacted with in general, so they are typically less useful to DI.
    - This method is provided mostly for posterity, but there are occasional uses for DI Ghost objects, so who knows what may come.
    - Besides the base setup, one of the target object will be required for _each_ DI Ghost to be made.

    ##### Objects - Steady Variant ?
    ---
    notoc: true
    ---

    1. [Zuggle Drop](uid:L84) `A` to attach `B`
    2. **Equip** another shield and a random weapon, then **unsheathe** them
    3. Face A and **pick up** a dupe of it
    4. **Drop/Deploy** a target material/device and highlight it with Fuse
    5. Start holding ZL and **pause** the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
    6. **Drop** the equipped shield and **swap** to the dupe of A
    7. **Unpause** the game and mash **Cancel** (`B/X`) to Octo Detangle the target from both parents (if successful, it will be floating in the air, not attached to the normal parent)
    8. **Repeat** from Step 3 until satisfied
    9. **Pick up** and drop A to detach B

    ###### Resources ?

    !!! tip "Mistake recovery"

        If a detanglement is failed, disregard the still-attached target and continue as normal. Don't detangle it later, as it will remain persistently Cold Fused to A (which can eventually make it unusable).

        If a DI is failed, continue as though it was never attempted.

    ??? example "Method Structure Diagram"

        ```mermaid
        graph TD
            A["DI Ghost (A)"]
            B["Purgatorized<br/>DI Ghost (B)"]
            OCTO["DI Ghost<br/> Octo Balloon"]
            C[Target 1]
            D[Normal Parent 1]
            E[Dupe of A]
            F[Discarded]
            G[Normal Parent 2]

            A -->|DI| B
            A -->|DI| OCTO
            B -->|DI| C
            D -->|DI| C
            E -->|Detangles| D
            D -->|Becomes| F
            E -->|Becomes| G
        ```

    ##### Objects - Fast Variant ?
    ---
    notoc: true
    ---

    1. [Zuggle Drop](uid:L84) `A` to attach `B`
    2. **Equip** another shield and a random weapon, then **unsheathe** them
    3. Face A and **fill** the inventory with dupes of it
    4. **Drop/Deploy** many target materials/devices and highlight one with Fuse
    5. Start holding ZL and **pause** the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
    6. **Drop** the equipped shield and **swap** to a dupe of A
    7. **Unpause** the game and mash **Cancel** (`B/X`) to Octo Detangle the target from both parents (if successful, it will be floating in the air, not attached to the normal parent)
    8. **Repeat** from Step 3 until satisfied
    9. **Pick up** and **drop** A to detach B

    ###### Resources ?

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
            D[Normal Parent 1]
            E[Dupe of A]
            F[Discarded]
            G[Normal Parent 2]

            A -->|DI| B
            A -->|DI| OCTO
            B -->|DI| C
            D -->|DI| C
            E -->|Detangles| D
            D -->|Becomes| F
            E -->|Becomes| G
        ```

## Notes

- Like all glitches involving FE, special considerations are required to use these methods on [Replacement Actors](uid:G46). Without these considerations, the **game will crash** as soon as Fuse is pressed.

### References and Resources

??? quote "Discord References"

    - [Overload + DS Culling](https://discord.com/channels/1086729144307564648/1110956205624532993/1462096452540043304)
    - [Overload + Torch Culling](https://discord.com/channels/1086729144307564648/1110956205624532993/1473846010207015167)
    - [Overload + Limbo](https://discord.com/channels/1086729144307564648/1110956205624532993/1479539674912526587)
    - Overload + Aerophasing is barely worth citing
    - [Chaining + DS Culling](https://discord.com/channels/1086729144307564648/1113557914444111873/1468025665763938420)
    - Chaining + Mineru culling is pretty okay I might make a referent for it if one doesn't already exist
    - So is Chaining + Aerophasing
    - Chaining + Manual Culling is okay I guess?
    - Chaining + Torch Culling is bad and naughty and should be set adrift
    - [Batch Turbo Cloning for shields](https://discord.com/channels/1086729144307564648/1110956205624532993/1479327965807644777)
    - [Batch Turbo Cloning for weapons/bows]()
    - [Batch Turbo Cloning for objects/materials]()
    - [Fast Batch Turbo Cloning Methods](https://discord.com/channels/1086729144307564648/1113557914444111873/1498029239780511764)

## Related
- [Despawn Interrupt](search:Despawn Interrupt)
- [Zuggle Overload](search:Zuggle Overload)
- [Fuse Entanglement](search:Fuse Entanglement)
