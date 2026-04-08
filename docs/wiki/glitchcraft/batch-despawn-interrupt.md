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

    This is the most basic overload method, requiring only the absolute minimum prerequisites. As such, it can be done nearly anywhere at nearly any time.

    !!! success "Verified"

        Method 1 is tested and verified to be functional and optimal.

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
    6. After 30 successful uses, **destroy** C and D, then remake them to continue

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

            A -->|DI| C
            B -->|DI| C
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

    This method builds on Method 1 with a new culling method, increasing the speed and reducing the setup time and complexity. However, it can only be performed at a culling area.

    Prepare:

    - 13 Zuggle Overload
    - A DI Weapon or Shield (A)
    - A torch
    - A flame emitter

    Creating the setup:

    1. A and normal item B make DI Ghost Shield C, keep normal parent
    2. Smuggle C
    3. Cold Drop the torch and place it next to a wall in a culling area
    4. Point the Flame Emitter at the head of the Torch from point-blank, ensuring the fire strikes a solid surface as close to the torch-head as possible.
    5. Glue B to the Torch and activate the Flame Emitter.
    6. To cull C, use the ability wheel to select and open Recall, causing a 2-frame pause. The torch should begin culling after cancelling recall
    7. Overload Drop a shield (D) and fuse it to a weapon (E)

    Creating DI Ghosts:

    1. Fuse the target to the shield (Overload FE)
    2. Use the ability wheel to open recall, then use it to open fuse and press fuse immediately
    3. As long as fuse is pressed more than 2 frames before the torch fully culls, the cull will occur within the target's DI window
    4. After 30 successful uses, destroy C and D before continuing

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
            A[DI Ghost (A)]
            B[Normal Item (B)]
            C[DI Ghost Shield (C)]
            D[Normal Shield (D)]
            E[Normal Weapon (E)]
            F[Target]
            
            subgraph CULL [Culling Area]
            B <-->|Glue| TORCH
            end

            FLAME --> |Point at| TORCH
            A -->|DI| C
            B -->|DI| C

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

    This method uses Mineru as a culling source, placing her in limbo to maximize control over her culling. It is the fastest overload method, but can only be done when & where Mineru can be summoned.

    !!! warning "Construction Zone"

        Method 3 _should_ be fully functional, but is not yet tested for optimality and step correctness.

    Prepare:

    - 13 Zuggle Overload
    - A DI Weapon (A) (all types can be inverted)
    - Mineru
    - A normal weapon (B)
    - A Stake

    Creating the setup:

    1. Mineru FE B
    2. Smuggle A, equip B, and target shield C with Fuse
    3. Induce Mineru to cull and fuse shortly before B culls; this will DI C
    3. Smuggle C
    4. Overload drop Shield (D) and fuse to Weapon (E)

    Creating DI Ghosts:
    
    5. Stand on a stake at the right height so that Mineru goes into "Limbo" (invisible, but B and C are unculled)
    6. Fuse target twice and jump shortly after the second fuse so that Mineru culls (and culls the target by extension)
    7. After 30 uses, destroy C and D before continuing

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

    Method 4 uses Aerophasing as a culling source, allowing for a use-anywhere method on all patches. I've never tried it and it probably sucks to use. But maybe it's peam???

    !!! warning "Construction Zone"

        Method 4 is not yet tested for function and optimality. I promise I'll get to it.

    Prepare:

    - 13 Zuggle Overload
    - A DI Shield (A), ideally a DI Ghost (all types can be mirrored)
    - Intangible Aerophasing

    Creating the setup:

    1. Smuggle A and equip Normal Shield B, then stand on the phasing platform
    2. Just after Link unculls, fuse a weapon C to B; Link will cull and C will DI
    3. Drop B and leave it aside, but pick up and re-smuggle A
    4. Overload FE weapon D to A
    5. Swap shield, then drop it to leave A Zuggle Dropped
    6. Smuggle C, equip B, and Overload Pickup D
    7. Glue D to something to elevate it and ensure it cannot accidentally be targeted by Fuse

    Creating DI Ghosts

    1. Stand on the phasing platform
    2. Just after Link unculls, fuse target to D (overload fe)
    3. Just after Link unculls, fuse target to D again. As it already has an FE parent (C), this time it will Pseudo-fuse to D and begin fading away
    4. Link will cull soon enough after to automatically DI the target (by culling B, which culls C)
    5. After 30 successful uses, destroy C and D, then remake them to continue

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

            A -->|DI| C
            B -->|DI| C
            A -->|FE| D
            C -->|FE| TARGET
            D -->|CF| TARGET
        ```

    _Method "developed" by Squidwest - not yet performed, so undated_

=== "DI Chaining Methods" ###

    - These methods create a chain of DI ghosts, allowing the normal-parent despawning to be saved until the end of the process (as each target retains a DI parent as long as desired).
    - They are ideal for medium batches and minimalist replication, but can _only_ be used for weapons and shields.

    #### Method 5: <br/>Chaining + Drop-Swap Culling ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    Method 5 is the most basic chaining method, and the most minimal batch method in general. Unlike with overload methods, the remaining methods in this section are generally downgrades, only serving to make the method possible on `1.1.2` and earlier.

    !!! success "Verified"

        Method 5 is tested and verified to be functional and optimal.

    ??? abstract "Safe Variant"

        Prepare:

        A DI Ghost Weapon or Shield (A)

        Steps:

        1. Duplicate three normal copies of A by DI Duping (B, C, & D)
        2. Smuggle A and equip B, then drop C on the ground
        3. Start to fuse C to B, then pause the game a few frames later (For example, by buffering the ability wheel at the same time as pressing fuse, then selecting Map)
        4. Drop B and swap to D
        5. C will be attached to B on the ground. Dupe two replacement copies (E and F), then drop D
        6. Optionally, pick up and drop A to remove its overload
        7. Pick up C
        8. Repeat from step 2, with C as the new smuggle, E as the new normal parent, and D as the new target
        9. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance or chasm (which also performa a FarDelete)

    ??? abstract "Fast Variant"

        Prepare:

        A DI Ghost Weapon or Shield (A)

        Steps:

        1. Duplicate three normal copies of A by DI Duping (B, C, & D)
        2. Equip A and drop C on the ground
        3. Ready fuse targeting C and pause the game
        4. Drop A and swap to B
        5. Unpause and press fuse immediately
        6. Either [pause immediately after pressing fuse, then pause buffer] or [pause a few frames after pressing fuse]
        7. Drop B and swap to D
        8. Dupe 2 copies of C, then drop D and pick up C
        9. Repeat from step 3 with D as the next target
        10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance or chasm (which also performs a FarDelete)

    !!! danger "Long Chains"

        Extended dependency chains (FE and CF) can cause instability, such as freezing the game on some cutscenes and loads.
        
        If this method is performed with shields, simply zuggle a handful at once and use a rocket shield to fully detangle each zuggle, repeating for all of them.
        
        If weapons were used, zuggle every other in the chain (or less frequently if desired), use fuse-over detangle to leave only a cf remnant, then **destroy** the detangled weapons to break the chain apart. (a proper weapon detanglement is not viable for this use-case)

    ??? example "Diagram"

        ```mermaid
        graph TD
            A[DI Ancestor] -->|DI| B[DI Child]
            C[Normal Parent] -->|DI| B
            B -->|DI| D[DI Grandchild]
            E[Normal Parent] -->|DI| D
            D -->|DI| F[DI Descendant]
            G[Normal Parent] -->|DI| F
            F -->|...| H{Further Generations}
            I[Normal Parent] -->|...| H
        ```

    _Method developed by Squidwest(?) - Jan 23, 2026(?)_

    #### Method 6: <br/>Chaining + Torch Culling ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    !!! warning "Construction Zone"

        Method 6 is not yet tested for function and optimality.

    Prepare:

    - A DI Weapon or Shield (A) with a normal parent (B)
    - A torch
    - A culling area
    - A flame emitter

    Making the setup:

    1. Duplicate 3 normal copies of A, named B, C, and D
    2. Cold Drop the torch and place it next to a wall in a culling area
    3. Point the Flame Emitter at the head of the Torch from point-blank, ensuring the fire strikes a solid surface as close to the torch-head as possible.
    4. Glue B to the Torch and activate the Flame Emitter.
    5. To cull A, use the ability wheel to select and open Recall, causing a 2-frame pause. The torch should begin culling after cancelling recall

    Making DI Ghosts:

    1. Smuggle A, equip B, and drop C on the ground
    2. Hold L to open the ability wheel, select Recall, and release L
    3. With the Recall view open, Hold L to open the ability wheel, and select Fuse
    4. Release L and **Fuse** C to B shortly after fuse opens
    5. Drop B and swap to D
    6. C will be attached to B on the ground. Dupe two replacement copies (E and F), then drop D
    7. Optionally, pick up and drop A to remove its overload
    8. Pick up C
    9. Repeat from step 2, with C as the new smuggle, E as the new normal parent, and D as the new target
    10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance or chasm (which also performa a FarDelete)

    _method "developed" by Squidwest - not yet performed, so undated_

    #### Method 7: <br/>Chaining + Aerophasing ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    !!! warning "Construction Zone"

        Method 7 is not yet tested for function and optimality.

    ??? abstract "Safe Variant"

        Prepare:

        - A DI Ghost Weapon or Shield (A)
        - Intangible Aerophasing

        Steps:

        1. Duplicate three normal copies of A by DI Duping (B, C, & D)
        2. Smuggle A and equip B, then drop C on the ground
        3. Stand on the phasing platform
        4. Right after Link unculls, fuse C to B. C will become a DI Ghost
        5. Drop B and swap to D
        6. C will be attached to B on the ground. Dupe two replacement copies (E and F), then drop D
        7. Optionally, pick up and drop A to remove its overload
        8. Pick up C
        9. Repeat from step 2, with C as the new smuggle, E as the new normal parent, and D as the new target
        10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance or chasm (which also performs a FarDelete)

    ??? abstract "Fast Variant"

        Prepare:

        A DI Ghost Weapon or Shield (A)
        Intangible Aerophasing

        Steps:

        1. Duplicate three normal copies of A by DI Duping (B, C, & D)
        2. Equip A and drop C on the ground
        3. Stand on the phasing platform
        4. Ready fuse targeting C and pause the game
        5. Drop A and swap to B
        6. Unpause and press fuse immediately; C will become a DI Ghost
        7. Drop B and swap to D
        8. C will be attached to B on the ground. Dupe 2 copies of C, then drop D and pick up C
        9. Repeat from step 3 with D as the next target
        10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance or chasm (which also performs a FarDelete)

    ??? example "Diagram"

        ```mermaid
        graph TD
            A[DI Ancestor] -->|DI| B[DI Child]
            C[Normal Parent] -->|DI| B
            B -->|DI| D[DI Grandchild]
            E[Normal Parent] -->|DI| D
            D -->|DI| F[DI Descendant]
            G[Normal Parent] -->|DI| F
            F -->|...| H{Further Generations}
            I[Normal Parent] -->|...| H
        ```

    _Method "developed" by Squidwest - not yet performed, so undated_

    #### Method 8: <br/>Chaining + Mineru FE ?
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    !!! warning "Construction Zone"

        Method 8 is not yet tested for function and optimality.

    Prepare:

    - A DI Shield (A) (Method works the same with weapons)
    - A normal shield (B)
    - Mineru
    - A stake

    Steps:

    1. Mineru FE B
    2. Smuggle A and equip B
    3. Target shield C with Fuse
    4. Induce Mineru to cull, and fuse C to B shortly before B culls via her
    5. Drop B and swap to another shield (D)
    6. Dupe 2 new shields off C by trying to pick it up (be careful B is not targeted)
    7. Drop D, and optionally pick up and drop A to remove its dependency (which contributes to Zuggle Overload)
    8. Pick up and smuggle C and equip duped shield E
    9. Induce Mineru to cull, and fuse D to E shortly before C culls (via B, via her)
    10. Repeat steps 5-9 with repeated new shields
    11. Once process has been repeated to satisfaction, destroy all remaining normal parents in any order via distance or chasm

    !!! danger "Long Chains"

        Extended dependency chains (FE and CF) can cause instability, such as freezing the game on some cutscenes and loads.
        
        If this method is performed with shields, simply zuggle a handful at once and use a rocket shield to fully detangle each zuggle, repeating for all of them.
        
        If weapons were used, zuggle every other in the chain (or less frequently if desired), use fuse-over detangle to leave only a cf remnant, then **destroy** the detangled weapons to break the chain apart. (a proper weapon detanglement is not viable for this use-case)

    ??? example "Diagram"

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

    _Method "developed" by Squidwest - not yet developed, so undated_

=== "Turbo Cloning Methods" ###

    These methods use a purgatorized DI shield to repeatedly fuse, then Octo Detangle, each target in turn. It is optimal for batch production without Zuggle Overload, and ideal for both shield batches of any size, and for repeatedly creating small batches of any target type.

    #### Method 9: <br/>Turbo Cloning + Drop-Swap Culling ?
    ---
    versions: ["1.2.0","1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    !!! success "Verified"

        Method 9 is tested and verified to be functional and optimal.

    The method differs depending on the target, and so it 

    ??? abstract "For Shields"

        Prepare:

        - A DI Shield (A)

        Creating the setup:
    
        1. Dupe 3 copies of A
        2. A make DI ghost B, dispose of the normal parent
        3. A make DI Octo Balloon, use the normal parent to detangle it
        4. Smuggle B and equip another shield over it
        5. Get shocked with shield unsheathed; this will purgatorize B and cause it to only attach when it has a dependency chain back to Link via A

        Creating DI Ghost Shields:

        1. Zuggle Drop A to attach B
        2. Equip another shield and a random weapon, then unsheathe them
        3. Face A and pick up a dupe of it, then turn 90 degrees (to face the target, if it already exists)
        4. Drop a target shield on the ground (if it doesn't yet exist) and highlight it with fuse
        5. Start holding ZL and pause the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
        6. Drop the equipped shield and swap to the Octo Balloon shield
        7. Unpause the game and mash cancel (B/X)
        8. Execution permitting, the new DI Ghost Shield will be detangled from both parents and have its pickup prompt displaced, the former normal parent will be left on the ground, and another shield will be already equipped for use
        9. Repeat from Step 3 until satisfied
        10. Pick up and drop A to detach B

        Done correctly, each new target will drop on the opposite side of Link as the previous one, and none will block A from being duped from. The only necessary movement will be turning to face A to grab a dupe, then turning to face the target before fusing it.

        !!! tip "Mistake recovery"

            If the detanglement is failed, disregard the still-attached target. Recover by additionally duping a new target from one of the prior targets and dropping it.

            If the DI is failed, continue as though it succeeded.

        ??? example "Diagram"

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

    ??? abstract "For Other Equipment Types"

        Prepare:

        - A DI Shield (A)
        - At least one of the target type, or a DI Ghost of it

        Creating the setup:
    
        1. Dupe 3 copies of A
        2. A make DI ghost B, dispose of the normal parent
        3. A make DI Octo Balloon, use the normal parent to detangle it
        4. Smuggle B and equip another shield over it
        5. Get shocked with shield unsheathed; this will purgatorize B and cause it to only attach when it has a dependency chain back to Link via A

        Making DI Ghost Weapons/Bows:

        1. If a DI ghost of the target is already prepared, place it next to A
        2. Leave only one empty space in the Shield pouch and the target type's pouch
        3. Zuggle Drop A to attach B
        4. Equip another shield and a random weapon, then unsheathe them
        5. Face A and pick up a dupe of it (and the target, if possible)
        6. Drop the target (dupe) and turn 90 degrees, then highlight it with fuse
        7. Start holding ZL and pause the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
        8. Drop the equipped shield and swap to the Octo Balloon Shield
        9. Unpause the game and mash cancel (B/X)
        10. Execution permitting, the new DI Ghost equipment will be detangled from both parents and have its pickup prompt displaced. The spent Octo Balloon Shields will build up on one side of Link, leaving the duping and fusing targets easily accessible
        11. If a DI Ghost of the target was not yet prepared, there is now one to be used
        12. Repeat from step 5 until satisfied
        13. Pick up and drop A to detach B

        !!! tip "Mistake recovery"

            If the detanglement is failed, disregard the still-attached target and continue as normal. It can technically be detangled later, but the timing is stricter and it's slower than just running the process again.

            If the DI is failed, continue as though it succeeded.

        ??? example "Diagram"

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

    ??? abstract "For Non-Equipment"

        Prepare:

        - A DI Shield (A)
        - One of the target for _each_ DI Ghost to be made

        Creating the Setup:
    
        1. Dupe 3 copies of A
        2. A make DI ghost B, dispose of the normal parent
        3. A make DI Octo Balloon, use the normal parent to detangle it
        4. Smuggle B and equip another shield over it
        5. Get shocked with shield unsheathed; this will purgatorize B and cause it to only attach when it has a dependency chain back to Link via A

        Making DI Ghosts:

        1. Zuggle Drop A to attach B
        2. Equip another shield and a random weapon, then unsheathe them
        3. Face A and pick up a dupe of it, then turn 90 degrees
        4. Drop/Deploy a target material/device and highlight it with fuse
        5. Start holding ZL and pause the game a few frames later; one way to do this is to also start holding L at the same time, and select the Map Rune
        6. Drop the equipped shield and swap to the Octo Balloon Shield
        7. Unpause the game and mash cancel (B/X)
        8. Execution permitting, the new DI object will be detangled from both parents. The spent Octo Balloon Shields will build up on one side of Link, leaving A and the fuse targets easily accessible
        9. Repeat from Step 3 until satisfied
        10. Pick up and drop A to detach B

        DI Ghost objects cannot be interacted with, so this variant is perhaps of intellectual interest only.

        !!! tip "Mistake recovery"

            If the detanglement is failed, disregard the still-attached target.

            If the DI is failed, continue as though it succeeded.

        ??? example "Diagram"

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

    _Turbo Replication developed by Aergyl - Jan 31, 2026_
    
    _Batch methods developed by Squidwest - Mar 05, 2026_

## Notes

- Due to the difference in resulting structure, these methods are usually _not_ interchangeable when called for by another tutorial. They have been grouped by structure for this reason.

## References and Resources

??? quote "Discord References"

    - [Overload + DS Culling](https://discord.com/channels/1086729144307564648/1110956205624532993/1462096452540043304)
    - [Overload + Torch Culling](https://discord.com/channels/1086729144307564648/1110956205624532993/1473846010207015167)
    - [Overload + Limbo](https://discord.com/channels/1086729144307564648/1110956205624532993/1479539674912526587)
    - Overload + Aerophasing is my own dodgy and untested invention
    - [Chaining + DS Culling](https://discord.com/channels/1086729144307564648/1113557914444111873/1468025665763938420)
    - So is Chaining + Aerophasing
    - And Chaining + Mineru Culling
    - yes and chaining + torch culling. I will simply have to make posts to reference for these...
    - [Batch Turbo Cloning for shields](https://discord.com/channels/1086729144307564648/1110956205624532993/1479327965807644777)
    - [Batch Turbo Cloning for weapons/bows]()
    - [Batch Turbo Cloning for objects/materials()

!!! warning "Construction Zone"

    Missing references will be added after a referent is created. Thank you for your patience.

## Related
- [Despawn Interrupt](search:Despawn Interrupt)
