---
title: "Cold/Warm Drop"
uid: "A1A"
---

# Cold/Warm Drop

## Description

When Link drops an object from his inventory, whether it's an item or a piece of equipment, it can either be a cold drop or a warm drop.
A previously equipped piece of equipment will be warm when dropped, and any other object (items and equipment from the inventory) will be cold when dropped.

### Differences in behaviour

There are a couple differences in behaviour:

- Warm drops always cull a frame quicker than cold drops.
- When attempting to fuse a warm drop to a construct/Mineru, if the game is paused on a specific frame, the pause menu pauses the equipment one frame earlier than the newly created fuse actor. The exact inner workings haven't been figured out.

This second effect allows for Mineru/Construct FE simply by pausing on such a frame. Because of the one frame difference in pausing, when the fuse actor expects the equipment to have acknowledged the fuse, it hasn't because it already got paused, effectively causing fuse entanglement. See the Effects section for more detail.

When hovering over a warm drop with Ultrahand, Recall or Fuse, opening a menu (inventory, D-Pad, L Wheel, etc...) will interrupt the connection with Link for a frame (equipment will turn orange for UH, the visible bond will disappear for Fuse, etc...).

### Changing equipment drop temperature

=== "Cold to Warm" ####

- Pick up the equipment with nothing in that slot equipped.
- Drop, throw, or shock-drop the equipment to make it a warm drop.

=== "Warm to Cold" ####

- Convince an enemy to pick up the warm-dropped equipment.
    - If the enemy is near other equipment, you may need to destroy, steal, or otherwise move that equipment to make them pick up your warm drop instead.
- Kill or disarm the enemy to make them drop the equipment, which is now a cold drop.

### Effects

Drop temperature affects a few glitches:
- FSFE requires no memories for warm drops, because of the equipment culling a frame earlier.
- On version 1.0, everything culls another frame quicker. As such, by putting a warm drop in a culling area in the typical fuse storage setup, simply opening the menu will give enough time for the warm drop to cull (because of the aforementioned one frame disconnection). This means that 1.0 can fuse store simply by opening a menu, closing it and then timing a ZL/Y press. ([example](https://discord.com/channels/1086729144307564648/1110956205624532993/1325234295165685813))
- As mentioned prior, it is possible to perform Mineru Fuse Entanglement and Construct Fuse Entanglement on warm drops really easily, simply by pausing 3 frames after beginning the fuse for Mineru, and whenever the equipment glows green on the ground for a construct.

---


