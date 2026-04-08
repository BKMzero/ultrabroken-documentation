---
title: "Purgatory"
uid: "TAO"
label: "PURG"
tags: ["purgatory", "culling"]
aliases: ["Culled Purgatory", "Cull purg", "dpurg"]
---

# Purgatory

Is it equipped or not? Depends who you ask.

!!! danger "Warning"
    While purgatory is a useful equipment state to exploit, many ways to delete unculled purgatory equipment will **crash** the game.

## Overview

Normally, when you have something equipped, Link's actor and the equipment actor agree on what's going on:

- Link has the equipment connected to him (as [a dependency](uid:NYI), among other ways);
- The equipment considers Link to be its user.

With purgatory equipment, only the latter is true. It considers itself to be equipped on Link, but Link disagrees.

Purgatory equipment acts like it's properly equipped in some regards:

- You can't select it with Ultrahand, Fuse or Recall.
- It's always visible during Ascend animations.
- If Link catches fire (or starts glowing red as a fire warning), so will all wooden purgatory equipment.<!-- TODO: is the same true when Link freezes? -->
    - It won't have any visible fire effects, but will still burn up after 60 seconds (5 for shields) — this will **crash** the game if you don't extinguish the fire first!

But it has the following differences:

- It can't be picked up. If you try to pick it up with nothing of that kind equipped, nothing happens. If you try to pick it up when it would go straight into the inventory, the game will **crash**.
- You can't fuse it to Mineru. If you try, the existing fuse on that attachment point is deleted and nothing else happens.
- It ignores cull instructions from culling areas.

## Fuse Entanglement

Purgatory weapons and shields have some additional features when on one side of a fuse entanglement:

### As the FE parent

- Ultrahanding the FE child will temporarily reconnect the purgatory equipment to Link, and keep it at the same position it was at when first sent to purgatory. It re-releases when you let go of Ultrahand.<!-- I have a clip of doing this with a drop-purg shield and steering stick FE; should add it here. PF-->
- Ultrahanding the FE child while loading a different file will [UltraSLOT](search:UltraSLOT) the equipment.

### As the FE child

- Having the FE parent equipped will keep the purgatory child equipped or positioned on Link as it was when it first entered purgatory. If you drop the parent, the child will drop from Link.
    - This doesn't happen if the FE child was purgatorified due to physically culling Link.
- Warping with the FE parent equipped will undo the purgatory status of the FE child, which will drop at Link's last position before the warp.

## Creating purgatory equipment

To send equipment to pugatory (to 'purgatorify' it), you have several options:

- Drop equip a piece of equipment, then drop it.
    - Be ready for it to fly away from Link with great speed when you drop it!
- Smuggle a weapon or shield, then equip and shock-drop another. (If you smuggled a weapon, you can also throw the second instead.) The smuggle will lose collision and be purgatorified.
    - The second piece of equipment will be moved to the drop equip position, and thus also easy to purgatorify. It's a [weak drop equip](uid:HY9) though, and will move back if you change Link's animation state enough.
- Drop some equipment while it's culled, and you have a zuggle of the same equipment kind. The dropped equipment will be sent to culled purgatory.
    - This equipment will lose collision, even if you use an FE parent to uncull it later.
    - Equipment in culled purgatory isn't directly deleted on reload. If the equipment has an FE child that you then uncull with some other method, that item will persist across reloads as a [PSLOT](search:PSLOT).

## Culled purgatory

If equipment is in purgatory and culled, it will not be deleted on reload. If you fuse entangle something to that equipment, with some other way to uncull the object afterwards, that object will also persist as a [PSLOT](label:PSLOT).

## Crash risks

The following ways of deleting purgatory equipment will **crash** the game:

- Picking it up and sending it straight to the inventory.
- Burning it.
<!--TODO: there's more for sure -->

But the following are always safe to do:

- Reloading/warping, and letting purgatory equipment be deleted in the loading screen.
- Pausing and unequipping its FE parent.
- Any normally crash-prone method while the equipment's FE/CF child has a proper two-way connection to Link. This can include ultrahanding it, or having it equipped. (Zuggling it won't work here.)
