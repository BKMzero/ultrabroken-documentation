---
title: "Despawn Interrupt"
uid: "IF1"
---

# Despawn Interrupt

Culling and unculling a piece of equipment marked with a 'death' reason before it's fully despawned from the world allows for a powerful set of new equipment states. See the [section on Despawn Interrupt](uid:JEV) for more.

## Effects summary

DI equipment:

- remains smuggled when fail dropped.
- doesn't apply D-Pad Lock when smuggled. This makes it very easy to zuggle. 
- can't be accidentally deleted by picking it up while having something else of that type equipped.
- cannot be ultrahanded, fused, or recalled.

For Ghost DI equipment, the following is also true:

- It automatically SLOTs, without needing any other kind of persistent parent.
- It has no physics of its own, so doesn't need recall locking to not fall out of the world.
