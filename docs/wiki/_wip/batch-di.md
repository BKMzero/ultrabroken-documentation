---
title: "Batch DI"
draft: true
label: "BDI"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["Aergyl", "mulberry", "Squidwest"]
date: "2025-01-17"
description: "A collection of methods to produce large numbers of DI Ghost items quickly."
aliases: []
tags: ["despawn-interrupt", "culling"]
---

# Batch DI

## Summary
---
Some of the properties of DI Ghosts (typically equipment, sometimes otherwise) are best exploited with large numbers of them. This page provides various convenient ways to produce large numbers of them.

_Credits - See individual methods_

## Instructions
---

Due to the absence of "Drop-Swap Culling" on versions prior to `1.2.0`, all applicable methods will be given with both an all-versions variant and a variant specific to 1.2.0 and up.

=== "Method 1: Overload Batch DI"
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This method uses Overload Pseudo Fuse to DI targets without ever creating normal parents, removing the need to despawn them between targets. It is ideal for creating very large quantities of DI Ghosts.
    
    ??? abstract "`1.2.0+`"

        Prepare:

        13 Zuggle Overload
        Two DI ghost equipment items, A and B

        Creating the setup:

        1. Overload FE normal item (C) to A; must be opposite of B's type
        2. Leave A Zuggle Dropped after completing step 1
        3. B make DI ghost (D) of C's type; keep the normal parent (E)
        4. Smuggle D, equip E, and overload pickup C
        5. glue C to something to elevate it and ensure it cannot accidentally be targeted by Fuse
        6. Optionally, position a wall behind Link's back which can force E to fail-drop

        Creating DI Ghosts
    
        1. Fuse target to C (overload fe)
        2. Fuse target to C again. As it already has an FE parent (D), this time it will Pseudo-fuse to C and begin fading away
        3. Pause the game before the target fully fades out
        4. Drop E, swap to another of that type, and unequip it. This will cull E, and thus D, and thus the target, DIing it
        5. If you fail-dropped E, proceed with the next target. If not, you'll need to pick it up

    ??? abstract "`All Versions`"

        Prepare:

        13 Zuggle Overload
        Two DI ghost equipment items, A and B
        Intangible Aerophasing

        (the steps)

        Creating the setup:

        1. Overload FE normal item (C) to A; must be opposite of B's type
        2. Leave A Zuggle Dropped after completing step 1
        3. Smuggle B and equip normal item of B's type (E)
        4. Stand on the phasing platform
        5  Right after Link unculls, fuse an item (D) of C's type to E; it will DI
        6. Smuggle D, equip E, and overload pickup C
        7. glue C to something to elevate it and ensure it cannot accidentally be targeted by Fuse

        Creating DI Ghosts

        1. Stand on the phasing platform
        2. Just after Link unculls, fuse target to C (overload fe)
        3. Just after Link unculls, fuse target to C again. As it already has an FE parent (D), this time it will Pseudo-fuse to C and begin fading away
        4. Link will cull soon enough after to automatically DI the target (by culling E, which culls D)

    !!! danger "Fuse-Over(load)"

        Detangling a DI Ghost from its parent by "fuse-over" leaves a Cold Fuse connection behind, and detaching a DI Ghost from its PF parent does the same. Due to this, D and E will each gain one _peristent_ dependency for each DI Ghost produced. After 30 uses, D and E will reach Fuse Overload. If a 31st use is attempted, you will create a "Reference FE" connection, which will **crash the game** if you drop D!

    !!! danger "Self-Fusing"

        When an overload-pickup has a connection back to link, it is possible to target it to be fused to itself. Under most circumstances, this will immediately **crash the game** if attempted.

    ??? example "Diagram"

        ```mermaid
        graph TD
            A[A] -->|FE| B[C]
            C[B] -->|DI| D[D]
            E[E] -->|DI| D
            D -->|FE| F[Target]
            B -->|CF| F
        ```

    _Method developed by mulberry - Jan 17, 2026_

=== "Method 2: DI Chaining"
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This method creates a chain of DI ghosts, allowing the normal-parent despawning to be saved until the end of the process (as each target retains a DI parent as long as desired). It is ideal for medium batches and minimal replication, but can _only_ be used for weapons and shields.

    ??? abstract "`1.2.0+`"

        Prepare:

        A DI Ghost Weapon or Shield (A)

        ??? abstract "Safe Method"

            1. Duplicate three normal copies of A by DI Duping (B, C, & D)
            2. Smuggle A and equip B, then drop C on the ground
            3. Start to fuse C to B, then pause the game a few frames later (after it starts to fade, but before it fades fully)
            4. Drop B and swap to D
            5. C will be attached to B on the ground. Dupe two replacement copies (E and F), then drop D
            6. Optionally, pick up and drop A to remove its overload
            7. Pick up C
            8. Repeat from step 2, with C as the new smuggle, E as the new normal parent, and D as the new target
            9. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance or chasm (which also performa a FarDelete)

        ??? abstract "Fast Method"

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

    ??? abstract "`All Versions`"
    
        Prepare:

        A DI Ghost Weapon or Shield (A)
        Intangible Aerophasing

        ??? abstract "Safe Method"

            1. Duplicate three normal copies of A by DI Duping (B, C, & D)
            2. Smuggle A and equip B, then drop C on the ground
            3. Stand on the phasing platform
            4. Right after Link unculls, fuse C to B. C will become a DI Ghost
            5. Drop B and swap to D
            6. C will be attached to B on the ground. Dupe two replacement copies (E and F), then drop D
            7. Optionally, pick up and drop A to remove its overload
            8. Pick up C
            9. Repeat from step 2, with C as the new smuggle, E as the new normal parent, and D as the new target
            10. After the process has been repeated to satisfaction, despawn all the normal parents of the chain by distance or chasm (which also performa a FarDelete)

        ??? abstract "Fast Method"

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

    !!! danger "Long Chains"

        Extended dependency chains (FE and CF) can cause instability, such as freezing the game on some cutscenes and loads.
        
        If this method is performed with shields, simply zuggle a handful at once and use a rocket shield to fully detangle them all, repeating for all of them.
        
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

=== "Method 3: Purgatory + Turbo Replication"
    ---
    versions: ["1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    obsolete: false
    ---

    This method uses a purgatorized DI shield to repeatedly fuse, then Octo Detangle, each target in turn. It is ideal for shield batches of any size, but can be adapted for small-med batches of other targets without too much trouble.

    Prepare:

    A DI Shield (A)

    First, creating the base setup:
    
    1. Dupe 3 copies of A
    2. A make DI ghost B, dispose of the normal parent
    3. A make DI Octo Balloon, use the normal parent to detangle it
    4. Smuggle B and equip another shield over it
    5. Get shocked with shield unsheathed; this will purgatorize B and cause it to only attach when it has a dependency chain back to Link via A

    Then, production, seperated by target type:

    ??? abstract "For shields"

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

    ??? abstract "For other equipment"

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

    ??? abstract "For non-equipment"

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
---

- Due to the difference in resulting structure, these methods are usually _not_ interchangable

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
