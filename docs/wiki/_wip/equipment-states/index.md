---
title: "Equipment states"
uid: "SKY"
---

# Equipment States

Equipment in Tears of the Kingdom can be in a _lot_ more states than was intended.

This section describes [Equip Positions](uid:S8I), the difference between [cold and warm drops](uid:C6H), and covers the following states:

- [Despawn Interrupt](uid:IF1)
- [Drop Equip](uid:HY9)
- [Drop Smuggle](uid:089)
- [Drop Zuggle](uid:0YL)
- [Dynamic Smuggle](uid:85I)
- [Dynamic Zuggle](uid:3KD)
- [Equipped Ghost](uid:30A)
- [Fail Drop Equip](uid:F4E)
- [Fail Drop Zuggle](uid:PM4)
- [Invismuggle](uid:445)
- [Invizuggle](uid:M0U)
- [Overload Drop](uid:2U2)
- [Purgatory](uid:TAO)
- [Sluggle](uid:M4H)
- [Smuggle](uid:TGY)
- [Throken](uid:58H)
- [Zuggle Drop](uid:L84)
- [Zuggle](uid:A1E)

## Transformation

There are many ways of transforming some equipment from one state to another, based on what you do when it's equipped, or with something else of the same type already equipped:

|Existing state|Action|New state|Notes|
|-|:-|-|:-|
|\[Static\] [Smuggle](uid:TGY) / [Zuggle](uid:A1E)|Warm drop another|Both equipment drop|All static Smuggles and Zuggles will fully drop, becoming [zuggle drops](uid:L84)|
|\[Static\] Smuggle|Fail drop another|Smuggle becomes a zuggle| |
|\[Static\] Zuggle|Fail drop another|No change| |
|Dynamic Smuggle|Warm drop / fail drop another|Item becomes a Dynamic Zuggle| |
|Dynamic Zuggle|Warm drop / fail drop another|No change| |
|Dynamic Smuggle/Zuggle|Throw / Shock drop another|All Dynamic Smuggles / Zuggles released| |
|Drop Equip / Equipped Drop Smuggle|Warm drop|Equipment is sent to purgatory| |
|Drop Equip / Equipped Drop Smuggle|Fail drop|Equipment is reverted to normal| |
|Drop Equip / Equipped Drop Smuggle|Zuggle|Equipment is Drop Zuggled|This doesn't require a fail drop, so Zuggle Drop inputs also work|
|Drop Smuggle|Warm drop / fail drop another|Smuggle becomes a Drop Zuggle||
|Strong Drop Equip|Warp|Equips [statically](uid:S8I) on Link's back||
|Static Smuggle / Drop Smuggle|Throw / Shock drop another|Smuggle is sent to purgatory, new equip is a weak Drop Equip|The purgatory equipment will have no collision and cannot be retrieved without an existing FE parent|
|Ground Drop Smuggle|Throw / Shock drop another|New equip is a weak Drop Equip|The Ground Drop Smuggle is _not_ sent to purgatory|
|Equipped Smuggle (any position)|Change equipment|No change|Smuggle is unequipped but otherwise preserved|
|Equipped Drop Smuggle|Warp|Equipment object is deleted|This is a roundabout way to perform [WST](search:Weapon State Transfer)|
|Overload Equip|Warm drop|Ground Drop Smuggle|Risk of D-Pad Lock without portacull or DI|
|Ground Drop Smuggle|Equip it|Equipped Drop Smuggle||
|Ground Drop Smuggle|Warm drop another|Ground Drop Equip||
|Ground Drop Equip|Equip it|Strong Drop Equip||
|Invismuggle|Warm drop / Fail drop another|Invizuggle||
