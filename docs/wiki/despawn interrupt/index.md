---
title: "Despawn Interrupt Overview"
---

# Despawn Interrupt Overview
_Basic stub_

## Introduction
---
Despawn Interrupt refers to interrupting the despawning of an actor. When a piece of equipment despawns, the game sets its state as "dead". By interrupting the process, we get to keep the usable weapon in this "dead" state, which is what is known as a DI'd piece of equipment. This state is really powerful, as it makes the equipment not be affected by D-Pad Lock, as well as giving it infinite durability. On top of that, DI can be propagated to other equipment anywhere easily.

## Quick Navigation
---
- **[Despawn Interrupt Query](search:Despawn Interrupt)** - The main DI glitch with multiple setups
- **[Fuse Entanglement Query](search:Fuse Entanglement)** - Often combined with DI for duplication
- **[Detanglement Query](search:Detanglement)** - Remove items from DI parent bases
- **[Culling Overview](../culling/)** - Game culling mechanics that enable DI

## Despawn reasons
---
When a piece of equipment dies, the game provides a reason for the despawning, so that it knows how to handle the despawn (e.g. a fade out for void, a simple actor deletion).
For example, death reasons include:

- `FallIntoAbyss` for voiding out.
- `Eaten` for getting eaten by a frox or a molduga.
- `PickedUp` for picking up an item when something else is equipped.
Each reason corresponds to a number in an internal enumeration.

The two kinds of despawn we are able to interrupt are `FallIntoAbyss` and `Eaten`.
This splits DI into two sub-glitches: `FallIntoAbyss` DI, aka Void Dipping, and `Eaten` DI.
The behavioural changes stem from the way the game handles killing an already dead actor: the death will only go through if the newer death reason number is smaller than the older death reason number.
For example, `PickedUp` has a reason number of 7.
`FallIntoAbyss`'s number is 13, so picking up a void dipped item will properly delete it (7 < 13, death goes through). However, `Eaten`'s reason number is 6, and 6 < 7, so picking up a eaten DI'd piece of equipment will not delete it, putting a copy in the inventory but staying alive.
This is just an example, other differences emerge depending on which despawn reason was interrupted.

Note that to make writing setups quicker, FallIntoAbyss DI will be referred to as Void Dipping (VD) and Eaten DI simply as DI.

## What to expect in each writeup
---
- **Trigger:** how to reproduce (inputs, positions, equipment)
- **Requirements:** game version, objects, NPCs, devices
- **Behavior:** observable effects and common outcomes
- **Risks & Warnings:** save/desync risks and suggested safety steps
- **Notes** variations, related techniques, and links to follow-ups