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

# Glitch Name
`1.0.0` `1.1.0` `1.1.1` `1.1.2` `1.2.0` `1.2.1` `1.3.0/1.4.0` `1.4.1` `1.4.2` `1.4.3` `Switch 2`

## Summary
---

By creating 600-700 Cold Fuse connections, the game will be overloaded and unable to form any new dependencies. This causes every actor to be Zuggle Overloaded, and every equipment to be Fuse Overloaded.

_Discovered by mulberry, Aergyl; Optimizations by Jordan, MandelbrotChaylay, mulberry, Squidwest_

...just gonna run with the idea that these can nest and get to work. even if not, the work can be reused. Could probably use dropdowns instead if needed?

## Forewarnings
---

!!! info "Buckle up"
    Due to the massive number of connections required, every method is relatively complex. Be sure to read the steps carefully, and be sure you understand the glitches that go into your chosen method, **before** you begin!

!!! warning "Panic!"
    While SFO is active, Panic Blood Moons will constantly occur if they are able (ie on the main map and not in a minigame or cutscene). Additionally, some dependencies will **crash the game** if they fail to form!

## Instructions
---

!!! note "Useful?"
    There are three main use cases for SFO: Obtaining Mineru's Arm, obtaining Zelda's Torch, and duplicating anything you can throw. For the sake of providing clear instructions, each method below has its use cases *nested* in its tab.

=== "Method 1"
    This is a persistent method that makes use of DI equipment to maximize setup speed. It can be used for anything, but is best-suited for Zelda's Torch and duplication.

    (Mandelbrot's method)

    === "For Zelda's Torch"
        To obtain Zelda's Torch, perform this setup in Rasitakiwak Shrine

        (extension that tells you how to get Zorch in an autosave, then links to the MNF page and tells you to zuggle it with your preferred MNF method)

    === "For duplication"
        To duplicate Zonai Devices, either A: perform this setup in a shrine, load a save at a minigame, and start it immediately, or B: perform this setup while already in a minigame. For other throwables, simply perform in a minigame.

    === "For Mineru's Arm"
        (I don't really know a stable way to get MinArm with this one. Ideally you don't have to go through army with SFO, since that's super unstable. But if you set up in the tunnel, you're gonna have a hell of a time reducing your overload enough to fuse to MinArm, and to zuggle it without overload dropping anything important.)

        (but presumably it's possible, say by: doing your initial overload with froxic ghosts in the tunnel, zuggling in your child shields, and destroying them after you have an appreciable number of Arms to attempt with?)

    !!! info "Persistent?"
        This setup _does_ persist through warps and loads, allowing it in theory to be used for any use case. However, it is more difficult to undo than local methods, which can be inconvenient.

=== "Method 2"
    This is a persistent method that makes use of DI equipment to balance speed, simplicity, and ease of use. It can be used for anything, but is best-suited for Zelda's Torch and duplication.

    (Squidwest's method)

    ??? example "Diagram"

        ```mermaid
        graph TD
            A[DI Shield] -->|FE| B["Recall Locked<br/>Weapon"]
            C[DI Shield] -->|FE| D["Recall Locked<br/>Weapon"]
            B -->|Fuse| E[DI Shield]
            F[DI Weapon] -->|FE| E
            E -->|FE| G["30 DI Weapons<br/>(Purgatorized)"]
            H[Normal Shield] -->|CF| G
            G -->|FE| H [20 DI Shields]
            D -->|CF| H
            H --> I{620 total connections}
            H --> J[Take in 1+]
        ```
        
    === "For Zelda's Torch"
        To obtain Zelda's Torch, perform this setup in a shrine.

    === "For duplication"
        (this repeats what I give in Mandelbrot's method)

    === "For Mineru's Arm"
        To obtain Mineru's Arm, perform this setup in the tunnel before Ganondorf

        (extension that tells you to zuggle 1+ child shields into the fight for later destruction (to undo SFO enough to fuse/zuggle Arm)

    !!! info "Persistent?"
        This setup _does_ persist through warps and loads, allowing it in theory to be used for any use case. However, it is more difficult to undo than local methods, which can be inconvenient.

=== "Method 3"
    This is a local method that makes use of DI equipment to maximize portability and speed. It is ideal for Mineru's Arm and duplication, but cannot be used for Zelda's Torch.

    (mulberry's method)

    === "For Mineru's Arm"
        To obtain Mineru's Arm, perform this setup in the tunnel before Ganondorf

        (extension that tells you how to preserve SFO into the fight, obtain MinArm, and zuggle it out)

    === "For Duplication"
        To duplicate Zonai Devices, perform this setup in the [find it] Minigame. For other throwables, simply perform in a shrine.

    !!! info "Local?"
        This setup _does not_ persist through warps and loads, limiting its uses. However, this also makes it easy to _undo_, and therefore more convenient for some tasks.

=== "Method 4"
    This is a local method with minimal additional glitches required. As a local method, it cannot be used for Zelda's Torch.

    (method based on Tahata's guide, placed last due to being somewhat outmoded by DI methods, but included due to being simplistic)

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
        
    === "For Mineru's Arm"
        To obtain Mineru's Arm, perform this setup in the tunnel before Ganondorf

        (extension that tells you how to properly preserve sfo into the fight, obtain MinArm, and zuggle it out)

    === "For Duplication"
        To duplicate Zonai Devices, perform this setup in the [find a stable minigame] Minigame. For other throwables, simply perform in a shrine.

        (explanation of how to dupe with SFO)

    !!! info "Local?"
        This setup _does not_ persist through warps and loads, limiting its uses. However, this also makes it easy to _undo_, and therefore more convenient for some tasks.

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
