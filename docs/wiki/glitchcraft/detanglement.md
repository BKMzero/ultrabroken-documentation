---
title: "Detanglement"
uid: "GDL"
label: "DTG"
versions: ["1.0.0", "1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["Zas"]
date: "2023-09-09"
description: "Using a rocket shield disconnects fuse-entangled objects from their source equipment without destroying the object."
aliases: ["detangling"]
tags: ["launching", "equipment", "fuse", "shield"]
---

# Detanglement

## Summary
Using a rocket shield disconnects fuse-entangled objects from their source equipment without destroying the object.

_Zas - 9 September 2023_

## Instructions
1. Zuggle a shield that has something fuse entangled to it
2. Use a rocket shield

## Notes
- Fuse entangling / fusing a previously detangled object and dropping (or fail dropping) the new parent will usually delete the fused object. This happens because detangling sets a _deletion flag_ on the object.
    - To prevent this, detangle the object while standing far enough away from it (i.e. be out of its _activation range_. The distance required varies between objects, but 20 units is usually more than enough.
    - If playing on version `1.2.0` or higher, and not detangling from a Despawn Interrupted shield, Octo Detangling never sets the deletion flag due to the drop–swap cull.
    - Recall Locked objects have infinite activation range.
- Can be used to detangle wuggled equipment, turning it into a true zuggle.
- Objects fuse entangled to Mineru can be detangled by fusing another object over the same slot as the target object.

## Resources
- [Twitter](https://vxtwitter.com/zasbotw/status/1700578075816403202)
- [Discord](https://discord.com/channels/1086729144307564648/1105598687167664239/1150136975504982167)

## Related
- [Zuggling](search:Zuggling)
- [Octo Detanglement](search:Octo Detanglement)
- [Fuse Entanglement](search:Fuse Entanglement)
