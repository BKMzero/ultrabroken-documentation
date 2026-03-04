---
title: "Void Dipping"
uid: "JDP"
label: "VD"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["Squidwest", "mulberry", "Aergyl"]
date: "2025-12-29"
description: "An extremely powerful equipment state caused by interrupting the fadeout of an equipment item that has been destroyed by the void, then retrieving it."
aliases: ["void-dipping"]
tags: ["item", "equipment", "ultrahand", "despawn"]
---

# Void Dipping `VD` `JDP`
`1.0.0` `1.1.0` `1.1.1` `1.1.2` `1.2.0` `1.2.1` `1.3.0/1.4.0` `1.4.1` `1.4.2` `1.4.3` `Switch 2`

## Summary
---
An extremely powerful equipment state caused by interrupting the fadeout of an equipment item that has been destroyed by the void, then retrieving it.

_Squidwest, mulberry, Aergyl - 29 December 2025_

## Methodology
---
All methods follow the same general pattern:

- Make a target equipment item enter a Voidout
- Cull the target after it starts fading, but before it fully disappears
- Retrieve the target (some methods do this before the cull)

### Locations
Most Voidouts are in big pits with little ability to get close. Three of the most popular exceptions (and how to retrieve from them) are given below:

#### Fire Temple
Warp there, turn around, and take the first right turn to find a lava river with a Hydrant making Lava Slabs. At the near-side downstream corner of the channel (not in the alcove), there is a Voidout under the lava. Retrieve targets by climbing down the corner wall, mounting Mineru to stand in the lava, or fishing it out with an object.

[Fire Temple VD location](x:1321.68, z:-2823.71, Depths, 9)

#### Lomei Ledge
East of Oshozan-u Shrine, on the way to the North Lomei Labyrinth, there's a ledge (height ~160) with a vertical Voidout wall starting at X=-1117. Retrieve targets by picking them up before they slide down the cliff.

#### Nachoyah Shrine (The Ability to Rewind)
In the alcove the rafts disappear into, there's a small Voidout at the back. Retrieve targets by swimming into the alcove and mashing A.

### Instructions
There are many viable methods. Three of the most popular are given in detail below, along with a summary of other more marginal methods.

=== "FE Method"
    _Discovered by Squidwest_

    Requires a way to cull Link (and thus the parent) on `1.1.2` or earlier, due to the absence of drop-swap culling.

    1. Use Fuse Entanglement to give the target an FE parent shield
    2. Equip the parent shield
    3. Ultrahand the target into the Voidout
    4. Switch directly to Recall without closing UH
    5. **Pause** the game and watch a memory
    6. Drop the parent, equip another shield, and unequip it
    7. **Unpause** and retrieve the target
    8. Use Octo Detanglement on the parent shield to remove the connection without destroying the target

=== "Overload Method"
    _Discovered by mulberry, Aergyl (?)_

    Specifc wall geometry, equipment collision, or a modified setup is required to fail-drop the target without fail-dropping the portacull, but skips the retrieval step. Requires a different culling method entirely on `1.1.2` or earlier (most feasibly aerophasing).

    1. Prepare a Portacull equipment of a different type than the target
    2. Overload Drop or Overload Pickup the target
    3. Ultrahand it into the Voidout
    4. Switch directly to Recall without closing UH
    5. **Pause** the game, fail-drop the target if possible, then watch a memory
    6. Activate the portacull
    7. If the target was not fail-dropped, swap to another equipment of that type
    8. **Unpause**
    9. If target was not fail-dropped, retrieve it

=== "Mineru FE Limbo Method"
    _Discovered by Kleric, Squidwest_

    Lomei Ledge version - requires significant modification in other locations, due to the delicate nature of Mineru Limbo and the lack of a vertical Voidout elsewhere.

    1. Fuse Entangle the target to Mineru
    2. Face west and inch backwards against the wall until you reach X=-1117. Dropping the target here will put it directly in the void
    3. Momentarily scope in on Mineru to put her in "Limbo": The target should appear on your back, while Mineru remains absent. If she reappears, scope in where she reappears until she stops (turning back around after if needed)
    4. Drop the target and activate Ultrahand immediately after to cull the target
    5. Cancel Ultrahand and pick up the target as soon as it unculls
    6. Fuse over the target on Mineru to detangle it

=== "Other Methods"

    - Mineru FE the target and have her orb return immediately after the target starts fading
    - Pickup the target as soon as it starts fading and immediately cull Link
    - Throw a boomerang into a large Voidout and cull it right after it enters, then simply catch it to retrieve

## Notes
---
### Void Dipped equipment properties
- Uninteractable by runes, including fusing directly to it
- Cannot lose durability, but can break if it is thrown at low durability and strikes terrain
- Some single-use fuses become infinite use (eg Ancient Blades)
- Cannot be directly culled from drop swap culling
- Can be easily smuggled via drop swap unequip or fail drop
- Does not induce smuggle locking (d-pad lock) when smuggled on `1.1.2+`
- Must be zuggled to keep its properties on warp

## Resources
---
- [Discord](https://discord.com/channels/1111875355758837830/1128775917376897145/1455340505096261796)
- [Discord](https://discord.com/channels/1086729144307564648/1113557914444111873/1456747616430850126)

## Related
---
- [Portable Culling](search:Portable Culling)
- [Fuse Entanglement](search:Fuse Entanglement)
- [Zuggle Overload](search:Zuggle Overload)
- [Aeroculling](search:Aeroculling)
