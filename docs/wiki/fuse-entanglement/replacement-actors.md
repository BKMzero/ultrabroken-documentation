---
title: "Replacement Actors"
uid: "G46"
draft: true
description: "Some fusible objects replace themselves with another object when fused, which can cause the game to crash if Fuse Entanglement is attempted."
aliases: ["Replacements"]
tags: ["entanglement", "crash"]
---

# Replacement Actors

## Summary

- Some fusible objects ("actors") replace themselves with another actor (sometimes of the same type) when fused. Without special considerations, attempting to Fuse Entangle these actors will _crash the game_.
- This page contains an easily-digestible table of such "Replacement Actors", with both the actor ID and a plain translation of which object this ID corresponds to, along with the equivalents for what the actor is replaced with.

## Table ?

| Row # | Base Actor ID | Base Actor Common Name | Additional Info || Replacement Actor ID | Replacement Actor Common Name | Additional Info |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AsbObj_Icicle_A_01 | Icicle | Normal Icicle | ➡️ | AsbObj_Icicle_A_01 | Icicle | Normal Icicle |
| 2 | AsbObj_Icicle_A_02 | Icicle | Large Icicle | ➡️ | AsbObj_Icicle_A_01 | Icicle | Normal Icicle |
| 3 | AsbObj_WoodSail_A_01 | Tattered Sail | Pivots | ➡️ | AsbObj_WoodSail_A_01_ForAttachment | Tattered Sail (Replacement) | Does not pivot |
| 4 | AsbObj_WoodSail_A_02 | Pristine Sail | Pivots | ➡️ | AsbObj_WoodSail_A_02_ForAttachment | Pristine Sail (Replacement) | Does not pivot |
| 5 | BombFruit | Bomb Flower | x | ➡️ | BombFruit | Bomb Flower | x |
| 6 | BrokenSnowBall | Snowball | Can Drop Items | ➡️ | BrokenSnowBallForAttachmentSmall | Snowball | Cannot Drop Items? |
| 7 | BrokenSnowBallForDrake | Gleeok Snowball | Cannot Drop Items? | ➡️ | BrokenSnowBallForAttachmentSmall | Snowball | Cannot Drop Items? |
| 8 | ConfusionFruit_Static | Muddle Bud (Static) | Doesn't Move | ➡️ | ConfusionFruit | Muddle Bud | Moves |
| 9 | DgnObj_BoardIron_E_Cart_02 | 8x4m Shrine Metal Plate | Only in Marakuguc - _Wheeled Wonders_ | ➡️ | DgnObj_BoardIron_E | 8x4m Shrine Metal Plate |  |
| 10 | DgnObj_FloatingWater_A_01 | Small Water Globule | Real | ➡️ | DgnObj_FloatingWater_A_01_ForAttachment | Small Water Globule (Replacement) | Water is fake |
| 11 | DgnObj_FloatingWater_A_02 | Large Water Globule | Real | ➡️ | DgnObj_FloatingWater_A_02_ForAttachment | Large Water Globule (Replacement) | Water is fake |
| 12 | DgnObj_IceBlock | Shrine Ice Block | x | ➡️ | DgnObj_IceBlock | Shrine Ice Block | x |
| 13 | DgnObj_Small_BoardStone_A_03 | 12x12m Shrine Stone Board | Only in Kimayat - _Proving Grounds: Smash_ | ➡️ | Dgn_Obj_BoardStone_A_04 | 8x8m Shrine Stone Board | x |
| 14 | DgnObj_Small_BoxIron_B_06 | 2x2x2m Shrine Iron Box (Heavy) | Only in Wao-os - _Lever Power_ | ➡️ | Obj_BoxIron_B_2x2x2_01 | 2x2x2m Shrine Iron Box (Normal) | x |
| 15 | DgnObj_Small_StonePole_A_02 | Stone Pole (?) | Only in Mayachin - _A Fixed Device_ | ➡️ | DgnObj_Small_StonePole_A_01 | Stone Pole (Normal) | x |
| 16 | DgnObj_Small_StonePole_A_03 | Stone Pole (Heavy) | Only in Riogok - _Force Transfer_ | ➡️ | DgnObj_Small_StonePole_A_01 | Stone Pole (Normal) | x |
| 17 | DgnObj_StoneBall_Fire | Flame Ball | Only In Lightning Temple | ➡️ | DgnObj_StoneBall_NoFire | Flame Ball (Extinguished) | x |
| 18 | DgnObj_WoodPole_A | Shrine Log | x | ➡️ | DgnObj_WoodPole_A_02 | Shrine Log (Replacement) | x |
| 19 | Drake_Icicle | Gleeok Icicle | ? | ➡️ | Drake_IcicleForAttachment | Gleeok Icicle (Replacement) | ? |
| 20 | DungeonBoss_Goron_Rock_Weapon | Small Gloom Rock | x | ➡️ | DungeonBoss_Goron_Rock_Weapon | Small Gloom Rock | x |
| 21 | DungeonBoss_Goron_Rock_Weapon_Large | Large Gloom Rock | x | ➡️ | DungeonBoss_Goron_Rock_Weapon_Large | Large Gloom Rock | x |
| 22 | ElectricalFruit | Shock Fruit | x | ➡️ | ElectricalFruit | Shock Fruit | x |
| 23 | FireFruit | Fire Fruit | x | ➡️ | FireFruit | Fire Fruit | x |
| 24 | FldObj_EnemyLookoutBanana_A_01_Trunk | Faron Enemy Lookout Tower Trunk | From Faron camps | ➡️ | Obj_EnemyLookoutBanana_A_01_ForAttachment | Faron Enemy Lookout Tower Trunk (Replacement) | x |
| 25 | FldObj_ScaffoldWood_A_03_Trunk | Enemy Lookout Tower Trunk | From most camps | ➡️ | Obj_ScaffoldWood_A_03_ForAttachment | Enemy Lookout Tower Trunk (Replacement) | x |
| 26 | IceFruit | Ice Fruit | x | ➡️ | IceFruit | Ice Fruit | x |
| 27 | IceWall_Piece | Ice Shard | From frozen water & ice chunks | ➡️ | IceWall_Piece | Ice Shard | x |
| 28 | IronBall_Light | Small Iron Ball (Light) | Only in Wao-os - _Lever Power_ | ➡️ | DgnObj_Small_IronBall_02 | Small Iron Ball (Normal) |  |
| 29 | Item_CatchInAir | Star Fragment (Falling) | Only for skydiving spawn | ➡️ | Item_Ore_J | Star Fragment | x |
| 30 | Item_Enemy_15 | Red Chuchu Jelly | x | ➡️ | Item_Enemy_15 | Red Chuchu Jelly | x |
| 31 | Item_Enemy_16 | Yellow Chuchu Jelly | x | ➡️ | Item_Enemy_16 | Yellow Chuchu Jelly | x |
| 32 | Item_Enemy_17 | White Chuchu Jelly | x | ➡️ | Item_Enemy_17 | White Chuchu Jelly | x |
| 33 | Item_Material_04 | Bird Egg | x | ➡️ | Item_Material_04 | Bird Egg | x |
| 34 | Item_Mushroom_D | Rushroom (Static) | Doesn't Move | ➡️ | Item_MushroomGet_D | Rushroom | Moves |
| 35 | Item_Mushroom_K | Brightcap (Static) | Doesn't Move | ➡️ | Item_MushroomGet_K | Brightcap | Moves |
| 36 | Item_Plant_A | Hyrule Herb (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Hyrule Herb | Moves |
| 37 | Item_Plant_B | Hearty Radish (Static) | Doesn't Move | ➡️ | Item_PlantGet_B | Hearty Radish | Moves |
| 38 | Item_Plant_B_TemporaryOwnedByNpc | Hearty Radish (Garden Tutorial)? | Doesn't Move | ➡️ | Item_PlantGet_A | Hearty Radish | Moves |
| 39 | Item_Plant_C | Big Hearty Radish (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Big Hearty Radish | Moves |
| 40 | Item_Plant_C_TemporaryOwnedByNpc | Big Heary Radish (Garden Tutorial)? | Doesn't Move | ➡️ | Item_PlantGet_A | Big Hearty Radish | Moves |
| 41 | Item_Plant_E | Cool Safflina (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Cool Safflina | Moves |
| 42 | Item_Plant_F | Warm Safflina (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Warm Safflina | Moves |
| 43 | Item_Plant_G | Mighty Thistle (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Mighty Thistle | Moves |
| 44 | Item_Plant_H | Armoranth (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Armoranth | Moves |
| 45 | Item_Plant_I | Blue Nightshade (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Blue Nightshade | Moves |
| 46 | Item_Plant_I_OwnedByNpc | Blue Nightshade (Oaki's) | Doesn't Move | ➡️ | Item_PlantGet_A | Blue Nightshade | Moves |
| 47 | Item_Plant_J | Silent Princess (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Silent Princess | Moves |
| 48 | Item_Plant_J_OwnedByNpc | Silent Princess (Oaki's) | Doesn't Move | ➡️ | Item_PlantGet_A | Silent Princess | Moves |
| 49 | Item_Plant_L | Electric Safflina (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Electric Safflina | Moves |
| 50 | Item_Plant_M | Swift Carrot (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Swift Carrot | Moves |
| 51 | Item_Plant_M_OwnedByNpc | Swift Carrot (Kakariko) | Doesn't Move | ➡️ | Item_PlantGet_A | Swift Carrot | Moves |
| 52 | Item_Plant_M_TemporaryOwnedByNpc | Swift Carrot (Garden Tutorial)? | Doesn't Move | ➡️ | Item_PlantGet_A | Swift Carrot | Moves |
| 53 | Item_Plant_O | Swift Violet (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Swift Violet | Moves |
| 54 | Item_Plant_Q | Endura Carrot (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Endura Carrot | Moves |
| 55 | Item_Plant_Q_TemporaryOwnedByNpc | Endura Carrot (Garden Tutorial)? | Doesn't Move | ➡️ | Item_PlantGet_A | Endura Carrot | Moves |
| 56 | Item_Plant_R | Sundelion (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Sundelion | Moves |
| 57 | Item_Plant_R_Kakariko_008 | Sundelion (Mellie's) | Doesn't Move | ➡️ | Item_PlantGet_A | Sundelion | Moves |
| 58 | Item_Plant_S | Stambulb (Static) | Doesn't Move | ➡️ | Item_PlantGet_A | Stambulb | Moves |
| 59 | Kibako_Contain_01_NoRespawn | Wooden Box (Gerudo Canyon Stable) | Doesn't Respawn | ➡️ | Kibako_Contain_01 | Wooden Box (ordinary) | x |
| 60 | LikeLikeRock | Rock Like Projectile | x | ➡️ | LikeLikeRock_ForAttachment | Rock Like Projectile (replacement) | x |
| 61 | MinusObj_TreeGeneralleaf_A_01_Trent_Trunk | Depths Evermean Log | _sic_ | ➡️ | MinusObj_TreeGeneralleaf_A_01_Treant_ForAttachment | Depths Evermean Log (Replacement) | x |
| 62 | MinusObj_TreeGeneralleaf_A_01_Trunk | Short Depths Log (From Tree) | x | ➡️ | Obj_TreeGeneralleaf_C_01_ForAttachment | Depths Log (Replacement) | x |
| 63 | MinusObj_TreeGeneralleaf_A_01_Trunk_Aligned | Short Depths Log | x | ➡️ | Obj_TreeGeneralleaf_C_01_ForAttachment | Depths Log (Replacement) | x |
| 64 | MinusObj_TreeGeneralleaf_B_01_Trunk | Medium Depths Log (From Tree) | x | ➡️ | Obj_TreeGeneralleaf_C_01_ForAttachment | Depths Log (Replacement) | x |
| 65 | MinusObj_TreeGeneralleaf_B_01_Trunk_Aligned | Medium Depths Log | x | ➡️ | Obj_TreeGeneralleaf_C_01_ForAttachment | Depths Log (Replacement) | x |
| 66 | MinusObj_TreeGeneralleaf_C_01_Trunk | Long Depths Log (From Tree) | x | ➡️ | Obj_TreeGeneralleaf_C_01_ForAttachment | Depths Log (Replacement) | x |
| 67 | MinusObj_TreeGeneralleaf_C_01_Trunk_Aligned | Long Depths Log | x | ➡️ | Obj_TreeGeneralleaf_C_01_ForAttachment | Depths Log (Replacement) | x |
| 68 | MinusObj_TreeGeneralleaf_D_01_Trunk | Long Blue Depths Log (From Tree) | x | ➡️ | Obj_TreeGeneralleaf_D_01_ForAttachment | Blue Depths Log (Replacement) | x |
| 69 | MinusObj_TreeGeneralleaf_D_01_Trunk_Aligned | Long Blue Depths Log | x | ➡️ | Obj_TreeGeneralleaf_D_01_ForAttachment | Blue Depths Log (Replacement) | x |
| 70 | Obj_FreezeBoard_A_01 | 4x4m? Ice Board | x | ➡️ | Obj_FreezeBoard_A_01 | 4x4m? Ice Board | x |
| 71 | Obj_FreezeBoard_A_02 | 4x8m? Ice Board | x | ➡️ | Obj_FreezeBoard_A_02 | 4x8m? Ice Board | x |
| 72 | Obj_TreeApple_A_L_01_Trunk | Apple Log (From Tree) | x | ➡️ | Obj_TreeApple_A_M_01_Trunk | Apple Log (Replacement) | x |
| 73 | Obj_TreeApple_A_L_01_Trunk_Aligned | Apple Log | x | ➡️ | Obj_TreeApple_A_M_01_Trunk | Apple Log (Replacement) | x |
| 74 | Obj_TreeBroadleafDead_B_L_01_Trunk | Oak Log Stump | x | ➡️ | Obj_TreeWood_A_01_ForAttachment | Oak Log (Replacement) | x |
| 75 | Obj_TreeBroadleaf_A_L_Treant_Trunk | Evermean Log | x | ➡️ | Obj_TreeWood_A_L_Treant_ForAttachment | Evermean Log (Replacement) | x |
| 76 | Obj_TreeBroadleaf_A_L_Trunk | Oak Log (From Tree) | x | ➡️ | Obj_TreeWood_A_01_ForAttachment | Oak Log (Replacement) | x |
| 77 | Obj_TreeBroadleaf_A_L_Trunk_Aligned | Oak Log | x | ➡️ | Obj_TreeWood_A_01_ForAttachment | Oak Log (Replacement) | x |
| 78 | Obj_TreeBurned_B_01_Trunk | Short Burned Log (From Tree) | x | ➡️ | Obj_TreeBurned_A_01_Trunk | Short Burned Log (Replacement) | x |
| 79 | Obj_TreeBurned_B_02_Trunk | Long Burned Log (From Tree) | x | ➡️ | Obj_TreeBurned_A_01_Trunk | Short Burned Log (Replacement) | x |
| 80 | Obj_TreeConiferousDead_A_01_Trunk | Long Dead Spruce Log (From Tree) | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 81 | Obj_TreeConiferousDead_A_01_Trunk_Aligned | Long Dead Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 82 | Obj_TreeConiferousDead_A_02_Trunk | Short Dead Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 83 | Obj_TreeConiferousDead_A_Snow_01_Trunk | Long Dead Snowy Spruce Log (From Tree) | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 84 | Obj_TreeConiferousDead_A_Snow_01_Trunk_Aligned | Long Dead Snowy Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 85 | Obj_TreeConiferous_A_01_Trunk | Short Spruce Log (From Tree) | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 86 | Obj_TreeConiferous_A_01_Trunk_Aligned | Short Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 87 | Obj_TreeConiferous_A_02_Trunk | Long Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 88 | Obj_TreeConiferous_A_03_Trunk | Large Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 89 | Obj_TreeConiferous_A_Snow_01_Trunk | Short Snowy Spruce Log (From Tree) | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 90 | Obj_TreeConiferous_A_Snow_01_Trunk_Aligned | Short Snowy Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 91 | Obj_TreeConiferous_A_Snow_02_Trunk | Long Snowy Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 92 | Obj_TreeConiferous_A_Snow_03_Trunk | Large Snowy Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 93 | Obj_TreeConiferous_C_01_Trunk | Short Pale Spruce Log (From Tree) | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 94 | Obj_TreeConiferous_C_01_Trunk_Aligned | Short Pale Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 95 | Obj_TreeConiferous_C_02_Trunk | Long Pale Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 96 | Obj_TreeConiferous_C_03_Trunk | Large Pale Spruce Log | x | ➡️ | Obj_TreeConiferous_A_01_ForAttachment | Spruce Log (Replacement) | x |
| 97 | Obj_TreeDeadLeaf_A_01_Trunk | Apple Log Stump | x | ➡️ | Obj_TreeDead_A_01_Trunk | Apple Log Stump (Replacement) | x |
| 98 | Obj_TreeDragonBlood_A_03_Trunk | Seres Scablands Tree Log | x | ➡️ | Obj_TreeWhiteBirch_ForAttachment | Birch Log (Replacement) | x |
| 99 | Obj_TreeGhost_A_03_Trunk | Lost Woods Tree Log | x | ➡️ | Obj_TreeWood_A_01_ForAttachment | Oak Log (Replacement) | x |
| 100 | Obj_TreeMaple_A_01_Trunk | Long Maple Log (From Tree) | x | ➡️ | Obj_TreeMaple_A_01_ForAttachment | Maple Log (Replacement) | x |
| 101 | Obj_TreeMaple_A_01_Trunk_Aligned | Long Maple Log | x | ➡️ | Obj_TreeMaple_A_01_ForAttachment | Maple Log (Replacement) | x |
| 102 | Obj_TreeMaple_A_02_Trunk | Short Maple Log | x | ➡️ | Obj_TreeMaple_A_01_ForAttachment | Maple Log (Replacement) | x |
| 103 | Obj_TreeMaple_B_01_Trunk | Long Maple Log 2? | x | ➡️ | Obj_TreeMaple_A_01_ForAttachment | Maple Log (Replacement) | x |
| 104 | Obj_TreeMaple_B_02_Trunk | Short Maple Log 2? | x | ➡️ | Obj_TreeMaple_A_01_ForAttachment | Maple Log (Replacement) | x |
| 105 | Obj_TreeMaple_C_01_Trunk | Long Maple Log 3? | x | ➡️ | Obj_TreeMaple_A_01_ForAttachment | Maple Log (Replacement) | x |
| 106 | Obj_TreeMaple_C_02_Trunk | Short Maple Log 3? | x | ➡️ | Obj_TreeMaple_A_01_ForAttachment | Maple Log (Replacement) | x |
| 107 | Obj_TreePalmBeach_A_01_Trunk | Straight Beach Palm Log (From Tree) | x | ➡️ | Obj_TreePalmBeach_A_01_ForAttachment | Straight Beach Palm Log (Replacement) | x |
| 108 | Obj_TreePalmBeach_A_01_Trunk_Aligned | Straight Beach Palm Log | x | ➡️ | Obj_TreePalmBeach_A_01_ForAttachment | Straight Beach Palm Log (Replacement) | x |
| 109 | Obj_TreePalmBeach_A_02_Trunk | Curved Beach Palm Log | x | ➡️ | Obj_TreePalmBeach_A_01_ForAttachment | Straight Beach Palm Log (Replacement) | x |
| 110 | Obj_TreePalm_A_01_Trunk | Long(?) Palm Log | x | ➡️ | Obj_TreePalmBeach_A_01_ForAttachment | Straight Beach Palm Log (Replacement) | x |
| 111 | Obj_TreePalm_A_02_Trunk | Short(?) Palm Log | x | ➡️ | Obj_TreePalmBeach_A_01_ForAttachment | Straight Beach Palm Log (Replacement) | x |
| 112 | Obj_TreeSkyApple_A_L_01_Trunk | Sky Apple Log (From Tree) | x | ➡️ | Obj_TreeSkyApple_A_M_01_Trunk | Sky Apple Log (Replacement) | x |
| 113 | Obj_TreeSkyApple_A_L_01_Trunk_Aligned | Sky Apple Log | x | ➡️ | Obj_TreeSkyApple_A_M_01_Trunk | Sky Apple Log (Replacement) | x |
| 114 | Obj_TreeSkyBroadleaf_A_L_Trunk | Sky Oak Log (From Tree) | x | ➡️ | Obj_TreeWhiteWood_A_01_ForAttachment | Sky Oak Log (Replacement) | x |
| 115 | Obj_TreeSkyBroadleaf_A_L_Trunk_Aligned | Sky Oak Log | x | ➡️ | Obj_TreeWhiteWood_A_01_ForAttachment | Sky Oak Log (Replacement) | x |
| 116 | Obj_TreeSkyBroadleaf_A_L_Trunk_NoDamage | Sky Oak Log (Raft Construct) | x | ➡️ | Obj_TreeWhiteWood_A_01_ForAttachment | Sky Oak Log (Replacement) | x |
| 117 | Obj_TreeSkyDead_A_Snow_01_Trunk | Dead Snowy Sky Oak Log | x | ➡️ | Obj_TreeWhiteWood_A_01_ForAttachment | Sky Oak Log (Replacement) | x |
| 118 | Obj_TreeWhiteBirch_A_01_Trunk | Birch Log 1? (From Tree) | x | ➡️ | Obj_TreeWhiteBirch_A_01_ForAttachment | Birch Log 1? (Replacement) | x |
| 119 | Obj_TreeWhiteBirch_A_01_Trunk_Aligned | Birch Log 1? | x | ➡️ | Obj_TreeWhiteBirch_A_01_ForAttachment | Birch Log 1? (Replacement) | x |
| 120 | Obj_TreeWhiteBirch_A_02_Trunk | Birch Log 2? | x | ➡️ | Obj_TreeWhiteBirch_A_01_ForAttachment | Birch Log 1? (Replacement) | x |
| 121 | Obj_TreeWhiteBirch_A_03_Trunk | Birch Log 3? | x | ➡️ | Obj_TreeWhiteBirch_A_01_ForAttachment | Birch Log 1? (Replacement) | x |
| 122 | Obj_TreeWhiteBirch_A_04_Trunk | Birch Log 4? | x | ➡️ | Obj_TreeWhiteBirch_A_01_ForAttachment | Birch Log 1? (Replacement) | x |
| 123 | Obj_TreeWillow_A_01_Trunk | Willow Log | x | ➡️ | Obj_TreeWillow_A_01_ForAttachment | Willow Log (Replacement) | x |
| 124 | SmokeFuit_Static | Puffshroom (Static) | _sic_ | ➡️ | SmokeFruit | Puffshroom | x |
| 125 | SpObj_BalloonEnvelope_Capsule_A_01 | Balloon (Capsule) | x | ➡️ | SpObj_BalloonEnvelope_A_01 | Balloon | x |
| 126 | SpObj_Beamos_Capsule_A_01 | Beam Emitter (Capsule) | x | ➡️ | SpObj_Beamos_A_01 | Beam Emitter | x |
| 127 | SpObj_Cannon_Capsule_A_01 | Cannon (Capsule) | x | ➡️ | SpObj_Cannon_A_01 | Cannon | x |
| 128 | SpObj_Cart_Capsule_A_01 | Cart (Capsule) | x | ➡️ | SpObj_Cart_A_01 | Cart | x |
| 129 | SpObj_Chaser_Capsule_A_01 | Homing Cart (Capsule) | x | ➡️ | SpObj_Chaser_A_01 | Homing Cart | x |
| 130 | SpObj_ControlStick_Capsule_A_01 | Steering Stick (Capsule) | x | ➡️ | SpObj_ControlStick_A_01 | Steering Stick | x |
| 131 | SpObj_CookSet_Capsule_A_01 | Portable Pot (Capsule) | x | ➡️ | SpObj_CookSet_A_01 | Portable Pot | x |
| 132 | SpObj_ElectricBoxGenerator_Capsule_A_01 | Shock Emitter (Capsule) | x | ➡️ | SpObj_ElectricBoxGenerator | Shock Emitter | x |
| 133 | SpObj_EnergyBank_Capsule_A_01 | Battery (Capsule) | x | ➡️ | SpObj_EnergyBank_A_01 | Battery | x |
| 134 | SpObj_EnergyBank_Capsule_A_02 | Big Battery (Capsule) | x | ➡️ | SpObj_EnergyBank_A_02 | Big Battery | x |
| 135 | SpObj_FastWheel_Capsule_A_01 | Small Wheel (Capsule) | x | ➡️ | SpObj_FastWheel_A_01 | Small Wheel | x |
| 136 | SpObj_FastWheel_Capsule_A_02 | Big Wheel (Capsule) | x | ➡️ | SpObj_SwitchWheel_A_01 | Big Wheel | x |
| 137 | SpObj_FlameThrower_Capsule_A_01 | Flame Emitter (Capsule) | x | ➡️ | SpObj_FlameThrower_A_01 | Flame Emitter | x |
| 138 | SpObj_FlashLight_Capsule_A_01 | Light (Capsule) | x | ➡️ | SpObj_FlashLight_A_01 | Light | x |
| 139 | SpObj_FloatingStone_Capsule_A_01 | Hover Stone (Capsule) | x | ➡️ | SpObj_FloatingStone_A_01 | Hover Stone | x |
| 140 | SpObj_GolemHead_Capsule_A_01 | Construct Head (Capsule) | x | ➡️ | SpObj_GolemHead_A_01 | Construct Head | x |
| 141 | SpObj_LiftableWaterPump_Capsule_A_01 | Hydrant (Capsule) | x | ➡️ | SpObj_WaterPump_A_01 | Hydrant | x |
| 142 | SpObj_LiftGeneratorWing_Capsule_A_01 | Wing (Capsule) | x | ➡️ | SpObj_LiftGeneratorWing_A_01 | Wing | x |
| 143 | SpObj_LightMirror_Capsule_A_01 | Mirror (Capsule) | x | ➡️ | SpObj_LightMirror_A_01 | Mirror | x |
| 144 | SpObj_Pile_Capsule_A_01 | Stake (Capsule) | x | ➡️ | SpObj_Pile_A_01 | Stake | x |
| 145 | SpObj_Rocket_Capsule_A_01 | Rocket (Capsule) | x | ➡️ | SpObj_Rocket_A_01 | Rocket | x |
| 146 | SpObj_SlipBoard_Capsule_A_01 | Sled (Capsule) | x | ➡️ | SpObj__A_01 | Sled | x |
| 147 | SpObj_SnowMachine_Capsule_A_01 | Frost Emitter (Capsule) | x | ➡️ | SpObj_SlipBoard_A_01 | Frost Emitter | x |
| 148 | SpObj_SpringPiston_Capsule_A_01 | Spring (Capsule) | x | ➡️ | SpObj_SnowMachine_A_01 | Spring | x |
| 149 | SpObj_TiltingDoll_Capsule_A_01 | Stabilizer (Capsule) | x | ➡️ | SpObj_TiltingDoll_A_01 | Stabilizer | x |
| 150 | SpObj_TimerBomb_Capsule_A_01 | Time Bomb (Capsule) | x | ➡️ | SpObj_TimerBomb_A_01 | Time Bomb | x |
| 151 | SpObj_WindGenerator_Capsule_A_01 | Fan (Capsule) | x | ➡️ | SpObj_WindGenerator_A_01 | Fan | x |
| 152 | TwnObj_Village_Fishing_Boat_A_02 | Tenoko Island Boat | x | ➡️ | TwnObj_Village_Fishing_Boat_A_02_ForAttachment | Tenoko Island Boat (Replacement) | x |
| 153 | Zonau_BlockMaster_Block | Flux Construct I Block | x | ➡️ | Zonau_BlockMaster_Block_ForAttachment | Flux Construct I Block (Replacement) | x |
| 154 | Zonau_BlockMaster_Block_Middle | Flux Construct II Block | x | ➡️ | Zonau_BlockMaster_Block_Middle_ForAttachment | Flux Construct II Block (Replacement) | x |
| 155 | Zonau_BlockMaster_Block_Senior | Flux Construct III Block | x | ➡️ | Zonau_BlockMaster_Block_Senior_ForAttachment | Flux Construct III Block (Replacement) | x |
