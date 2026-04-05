---
title: "Equip Positions"
uid: "S8I"
aliases: ["equip position"]
---

# Equip Positions

Link can have equipment attached to him in one of a number of configurations:

## **Static**

A static equip position is properly connected to Link's back, or to his hand, but remains where it is until fully dropped. This is the most common position for zuggles and smuggles, so it gets to be the implicit default. Any zuggle or smuggle method that doesn't explicitly mention one of the other positions will be referring to this one.

Static equips, although not very useful, are possible with any of these methods:
- Warp with a strong [drop equip](uid:HY9)
- Pick up a [fail drop zuggle](uid:PM4)


## **Dynamic**

A dynamic equip position is properly connected to Link's back, or to his hand, and properly switches between them depending on his animation state. All normal equipment is attached in this position (it's technically a dynamic equip). It is possible to get dynamic smuggles and zuggles, but is usually more difficult than static or drop position.

## **Drop**

A drop equip position follows Link's general position, but doesn't attach to him in any precise way, sticking out from between his feet. It's sort of the equipment equivalent of T-posing. Equipment in the drop equip position can be picked up without needing to disconnect it from Link first.

It also (in the vast majority of cases) retains its collision, so picking up other items on the floor will be difficult with one of these attached to Link, as it'll often knock them away from you before you can get close enough for the correct pickup prompt to show up. Anything at chest height will get pickup prompt priority, so keeping something at that height (resting it on higher terrain, gluing it to a tall object, recalling it, etc) is a useful technique for overcoming this problem.

Equips, smuggles and zuggles can all be in the drop position.

## **Ground**

This term is sometimes used for overload dropped equipment, as it has no connection to Link, but does to the inventory.

If you drop a ground equip:
- It converts into a ground smuggle. As is the case with smuggles, this risks an opening for D-Pad Lock. Performing [zuggle dropping](search:Zuggle Drop) inputs will skip the ground smuggle state, although the equipment won't actually be a zuggle drop. Instead, it _almost_ becomes just a normal warm drop.
	- On version 1.1.1 and earlier, you can just warm drop into the ground smuggle state, then equip and warm drop something else of that type to unsmuggle it.
- If you pick up a ground smuggle, it becomes an equipped [drop smuggle](uid:089). Warping with this equipped will delete the item from the overworld, allowing for [unload WST](search:Unload Weapon State Transfer).
- If you pick a former ground smuggle, it becomes a strong [drop equip](uid:HY9). Warping with this equipped will turn it into a static equip.
