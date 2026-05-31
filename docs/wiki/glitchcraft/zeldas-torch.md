---
title: "Zelda's Torch"
uid: "TW8"
draft: true
label: "ZTorch"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["mulberry, Aergyl, Jordan, MandelbrotChaylay, Squidwest"]
date: "2025-12-06"
description: "Using Super Fuse Overload, the unique torch Zelda carries in the prologue can be obtained."
aliases: [""]
tags: ["Equipment", "Zelda"]
---

# Zelda's Torch

## Summary

By completely filling the game's global dependency array, Prologue Zelda can be forced to Overload Drop her torch, which has unique properties. Once obtained in the prologue, it can be transferred to a progressed file in the same way as the Prologue Master Sword.

I'm sorry if you see this page like this. It's difficult to figure out best formatting when I want to provide both _the most thorough and efficient possible instructions for each patch_, but also _the most complete set of possible variants for all patches_. But I'm not really sure the modular format is working. So I might just go all in on the former and let anyone who thinks they have a bright idea give it a go themselves.

_First obtained by mulberry - Dec 07th, 2025_

## Instructions

- This page will cover the steps needed to collect Zelda's Torch within the prologue. The steps to transfer it to a progressed file vary greatly depending on version, personal preferences, etc.
- In general, _any_ method that can transfer the Prologue Master Sword (aka "MNF"/"MSG") can be used to transfer Zelda's Torch instead.
- (But I probably will still add some select methods here eventually, especially with our mnf page as sparse as it is right now)
- Anyway, due to the requirement of loading a Prologue autosave, only a "Persistent" SFO method will work. There are two popular such methods, so two altered variants of those methods will be provided here.



### Prep Phase

### SFO Phase

### Collection Phase

### Transfer Phase


### Requirements

- The stuff

### Prep Phase

- Placing DI Ghosts at the correct spot to yoink them in the prologue later (1.1.2+ only)
- For 1.0.0-1.1.1, nothing else either
- For 1.1.2, creating persistent wind and platforms to CSZ/SLD with later (I better ask about that huh)
- For 1.2.0+, getting overload and additional DI Ghosts for any other needs

#### Variant 1 (you are gonna sld early patch style)

#### Variant 2 (you are gonna CSZ/SLD or whatever middle-child style)

#### Variant 3 (heavenly smokeshows who get to SRZ and BALL and BALL and BALL)

### Performing SFO TO THE LIMIT!

#### Via method 1 (DI purg + double BDI)

#### Via Method 4 (Overload Cold Fuse + Permacull)

### Collecting Zelda's Torch & Preparing the Prologue-side Transfer Setup

- For each method, does the necessary save loads and/or equipment swaps to maximally sync outside the prologue
- that makes zorch drop, and take it
- 1.1.2+ also collects all extra stuff from the DI ghosts here
- Finally, another autosave for all of them (even you 1.0)
- And double finally, a game close on 1.0.0-1.1.1, a return to (whatever shrine) for 1.2.0+, and I really don't know what the malcolm does
- like it has a bunch of shit to set up that I don't want to end-load, but it kinda _has_ to close the game bc it does permacull SFO and factually cannot work under those conditions
- (so I guess it closes the game and just has to set up all the platforms and shit without getting too many autosaves)
- OR, enlightened option: just do prologue escape and dispose of the old reality (you get mnf and mnf armor for free)

### Transferring Zelda's Torch

#### SLD (for 1.0.0-1.1.1)

- Literally just reopen the game and sld it to whatever overlapping shrine you feel like (Rasitakiwak seems pretty close to ideal tbh, with how MUCH overlap there is and no floor holes either)
- admit i am a little jealous

#### Cull Storage Zuggle (or SLD idk)

- 1.1.2 gets to... Use cull storage _and_ LSW somehow
- I am not even a little bit jealous
- But (unless someone has a better idea) I figure it'll just use intangible aerophasing...
- So like, make grandfathered SDC (shield->either->stick), put the (either) on the wind/cull platform and the stick on some other platform
- Use the phasing to store cull, then drop zuggle the AC base I guess? can you even keep a cull stored in such dire conditions?
- anyway then you somehow also LSW (is it possible to make the lsw base also a cull-stored sdc??? that would be baller for 1.1.2 standards)

#### Based Swap Resync Zuggle

- Goes to domizuin, makes a portacull (either), FEs a battery to a shield, and ODZs said shield
- Then does LSW Lock with the battery shield and uses it as a portacull to SRZ afterwards

=== "Via SFO Method 1" ###
    ---
    versions: ["1.2.0" "1.2.1", "1.3.0;/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]

    - Ideal for versions `1.2.0` and up. I know the step list is longer but trust me twin
    - Possible on `1.1.2` and below, but suboptimal.
    - The steps given make no consideration for the latter version range, in order to be made optimal for the former.

    #### Requirements
    ---
    notoc: true
    ---
    
    - 13 Zuggle Overload
    - A bow to manage overload with
    - A DI Ghost weapon `A1`
    - A DI Ghost shield `B1`
    - Ideally, a second DI Ghost of each type to simplify duplication

    #### Part 1: Creating the base setup
    ---
    notoc: true
    ---

    1. Enter Rasitakiwak Shrine, defeat all the constructs, and dispose of their weapons (for example by leaving/reentering)
    2. (In this case, Rasitakiwak is ideal, as it contains both an overlapping area with the prologue, and multiple steering sticks to create a Portacull with)
    3. `B1` [Overload FE](uid:0XV#method-3-vddi-smugglezuggle) weapon `B2`
    4. [Recall Lock](uid:EY8) `B2`
    5. `A1` and normal weapon `A2` [Ghost DI](uid:BEW#method-1-fuse-drop-swap-120) shield `A3`
    6. `A1` **Overload FE** normal shield `A4`; Leave `A1` [Zuggle Dropped](uid:L84) 
    7. Equip `A2`, [Smuggle](uid:TGY) `A3`, and [Overload Pickup](uid:8QH) `A4`
    8. `A2-A4` [Overload Batch DI](uid:PG3#method-1-overload-pf-drop-swap-culling-120) 19 weapons `C1-C19`
    9. Confirm `C1-C19` all exist, then **Fail-Drop** `A4` to move it to Link's hand
    10. `A3` & `A4` **Ghost DI** weapon `C20`
    11. **Drop** `A4`
    12. Re-smuggle `A3`, equip a random shield, and **Fuse** something disposable to it. This will leave `A4` as the sole FE parent of `C20`
    14. Smuggle any _one_ `C`, then **equip** another and **throw it**. Finally, unsheathe weapon to return the thrown one to Link's hand. The smuggled weapon is now in Purgatory
    15. Repeat step 11 to Purgatorize _all_ `C`, using a random weapon for the final throw (it can be unequipped after)
    16. **Recall Lock** `A4`, discarding `A2` and `A3` through the load

    ##### Part 2: Performing and undoing SFO
    ---
    notoc: true
    ---

    1. Zuggle Drop `B1`, equip `A4`, and **Overload Pickup** `B2`
    2. `C1-20`, `B2`, & `A4` **Overload Batch DI** 30 Shields `D1-D30`
    3. There will be a substantial lag on the second fuse of each shield after `D1`, so using the D-pad to **drop-swap** is advised. To prevent mishaps with this, _do not_ fail-drop `A4`.
    4. _Super Fuse Overload_ should occur on the 30th shield. If confirmation is needed, **drop** the fused equipment item. If the fuse is deleted, SFO is fully active
    5. Leaving `A4` dropped, **fail-drop** `B2` and **drop** it _after_ it returns to Link's hand. Finally, un-Zuggle Drop `B1`
    6. The entire setup will now persist, and SFO will be fully active as long as Link equips each type of equipment (with exactly _one_ being fused)
    7. To undo SFO: **pick up** each `D`, **unequip** it, and **drop** it. Each deleted shield will remove 20 dependencies from the global limit

    ##### Part 3: Obtaining Zelda's Torch
    ---
    notoc: true
    ---

    1. Return to the title screen and begin a new file. This will only enter the prologue scenario and create occasional autosaves, so don't worry.
    2. Progress to the _second_ autosave (give timing cue but it's just after the first dialogue cutscene thing), then return to (shrine name).
    3. Use the D-Pad to unequip all equipment, then resync Link's armor, and finally use the D-Pad to re-equip items until a nocked arrow fails to attach to the bow (and instead just floats there).
    4. Load the second prologue autosave. Zelda will drop her torch, so pick it up
    5. If she does not, try loading to Rasitakiwak and back; It may take a few tries for her torch to be one of the dependencies that fails
    6. Get another prologue autosave with the torch in the inventory, then either load back to Rasitakiwak to clear SFO, or simply close the game
    7. Follow your preferred method to obtain MNF, but zuggle/SLD Zelda's Torch back to your progressed save instead
    8. Save the game or get an autosave

=== "Via SFO Method 4" ###
    ---
    versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
    ---

    - Ideal for versions `1.1.2` and below. I mean, unless it's not, but I really think so.
    - Possible on all versions, but suboptimal on `1.2.0` and up. No uncertainty about that.
    - The steps given make no consideration for the latter version range, in order to be made optimal for the former.

    #### Requirements
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
    - A DI Ghost Shield `E` (technically optional, but you definitely want it)
    - The _second_ prologue autosave

    ##### Part 1: Performing SFO
    ---
    notoc: true
    ---

    1. Use the Aerophasing setup to ensure it has a cull stored; this will allow the culling area to remain loaded through a banc change
    2. Travel to a nearby shrine ("Mayachideg" is best for a Citadel setup) and enter it. **Do not warp there.**
    3. [Overload Drop](uid:8QH) a shield and pick it up to duplicate shields until there are 19 dropped and 3+ spare in the inventory
    4. **Overload Drop** a weapon `A` and fuse it to a shield `B`
    5. [Overload Cold Fuse](uid:O64) 21 shields `C1-C21` to A (the 19 dropped & 2 from inventory)
    6. **Fail-drop** `A` and **drop** `B`
    7. [Overload Pickup](uid:8QH) `C1`
    8. Duplicate 30 shields `D1-D30` off `E`, dropping each on the ground and **Overload Cold Fusing** them to `C1` as you go
    9. **Fail-drop** `C1` and **drop** it aside
    10. Repeat 7-9 for `C2-C19` with the **same** `D1-D30`
    11. For `C20` and `C21`, check periodically in the menu to see if Menu Link starts overload dropping things. Once he does, _proceed to step 11_
    12. **Overload Cold Fuse** an unrelated material to `C[n]`. If it works, **Collect it** and **Overload Cold Fuse** the next `D[n]`, then repeat. If it fails, _proceed to step 12_
    13. **Fail-drop** `C[n]` and **drop** it. You may have to **unequip your bow** for it to return. **Be sure it returns before dropping it.**
    14. **Drop** `A`

    ##### Part 2: Permaculling the shields
    ---
    notoc: true
    ---

    1. [Smuggle](uid:TGY) `E`. If `E` was not prepared, Zuggle any other unrelated shield by your preferred method
    2. Equip one of `B`, `C[n]`, or `D[n]` and step onto the phasing platform
    3. **Pause** the game while Link is **culled**. This will cause Link to consistently be **unculled** when the game is unpaused
    4. **Unpause** the game and immediately **open** the Shield Quick Menu (D-pad Left). If Link is **unculled** behind the menu, **drop** the equipped shield. If not, repeat step 3.
    5. Repeat steps 1-4 for _all_ `B`, `C[n]`, and `D[n]`, ultimately resulting in the entire setup being permaculled

    ##### Part 3: Obtaining Zelda's Torch
    ---
    notoc: true
    ---

    1. Load your prologue save. Zelda will drop her torch, so pick it up
    2. If she does not, try loading to Mayachideg and back; It may take a few tries for her torch to be one of the dependencies that fails
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

## Notes

### Properties

#### As a weapon:
---
notoc: true
---

- Zelda's Torch is a peculiar 1-handed weapon which uses a blend of the properties of the Torch and the Traveler's Sword✨, along with some entirely unique properties.
- Like the Torch, it uses the Torch model and sounds, has 8 base durability, can be lit aflame at its tip, and will not burn out.
- Like the Traveler's Sword✨, it uses the Traveler's Sword Sheath, deals 7 damage, and is sharp without a fuse.
- Like other glitch weapons, it has no name or description, and usually displays "MsgNotFound" in those fields instead. However, it _does_ have a unique icon of a lit torch.
- It can be fused to, but _cannot_ be fused to other things.
- Uniquely to Zelda's Torch, it will automatically light if Cold Dropped (or Overload Dropped, or any other way of making the actor not equipped by Link when created).
- Furthermore, it uses a unique color for the light it emanates when lit, yellower than the standard lit torch.

#### As a building part:

- Dropped in the world, Zelda's Torch again uses a blend of properties.
- Like a Torch, it has 50 mass and is buoyant, flammable, and so on.
- Like a Traveler's Sword✨, it acts sharp and can cut when moved quickly enough.
- Though it sparks in the inventory during a storm, it does not actually attract electricity.
- Uniquely, when autobuilt, it will be _lit by default_.

#### As a tool:

- ...I haven't really played with it to see if it has tool uses besides being, uh, warm?
- Yeah. WIPs, amirite?
- You can overload or cold drop it with a bow unsheathed but not drawn and it'll light your arrow?

### Credits ?

- Zelda's Torch obtained by mulberry - Dec 07th, 2025

### Resources

??? quote "Discord Resources"

    - [Original Zelda's Torch Get](https://discord.com/channels/1086729144307564648/1110956205624532993/1447220634987003984)

### Related
- [Zuggle Overload](search:Zuggle Overload)
- [Despawn Interrupt](search:Despawn Interrupt)
- [Fuse Entanglement](search:Fuse Entanglement)

### Page Todos: ?
---
notoc: true
---

- Find a better shrine to use (I want grounded overlap with somewhere _before_ the 4th autosave)
- Find the best way to srz in prologue (It's probably _possible_ to DZ the lsw base instead of a portacull, but is it _easier_? (probably))
- Research MNF methods across history, particularly for CSZ which is... troublesome... to try and do in the prologue (but a DZ'd AC shield and RL'd platform is probably the way to go...?)
