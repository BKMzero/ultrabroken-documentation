---
title: "Despawn Interrupt Overview"
---

# Despawn Interrupt Overview
_Basic stub_

## Introduction
---
"Despawn Interrupt" refers to interrupting the despawning of an actor, however this event happens as a result of different game events, which are internally referred to as reasons. Eaten DI is associated with the "Eaten" reason, and encapsulates Frox Dipping, Duga Dipping and Like Like DI. Void Dipping is interrupting the "FallIntoAbyss" despawn, so it's sometimes referred to as FallIntoAbyss DI.
These two kinds of DI have differences, such as what happens upon being picked up. However, to simplify setups, FallIntoAbyss DI is referred to as VD, and Eaten DI simply as DI.

## Quick Navigation
---
- **[Despawn Interrupt Query](search:Despawn Interrupt)** - The main DI glitch with multiple setups
- **[Fuse Entanglement Query](search:Fuse Entanglement)** - Often combined with DI for duplication
- **[Detanglement Query](search:Detanglement)** - Remove items from DI parent bases
- **[Culling Overview](../culling/)** - Game culling mechanics that enable DI

## What to expect in each writeup
---
- **Trigger:** how to reproduce (inputs, positions, equipment)
- **Requirements:** game version, objects, NPCs, devices
- **Behavior:** observable effects and common outcomes
- **Risks & Warnings:** save/desync risks and suggested safety steps
- **Notes** variations, related techniques, and links to follow-ups