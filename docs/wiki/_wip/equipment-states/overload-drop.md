---
title: "Overload Drop"
uid: "2U2"
aliases: ["Overload Equip", "Overload Pickup"]
---

# Overload Drop

When Link is supposed to have some new equipment attached to him, but he is [overloaded](search:Zuggle Overload), newly spawned actors for equipment don't form any connection to Link's actor model. They still connect to the game's inventory system properly.

## Terminology

The 'drop' in 'overload drop' does _not_ refer to the usual act of dropping equipment, or the drop equip position. It instead refers to the fact that the equipment spawns at about the height of Link's feet, but as it fails to connect to Link, it drops to the ground (or often _through_ the ground).

The term 'overload pickup' (sometimes 'overload equip') refers to the exact same equipment state, but is usually used when the equipment already exists in the world, and is picked up while Link is overloaded.

## Undoing

If Link is no longer overloaded, fail dropping an overload equip will reattach it properly. Doing this to an overload equip that was fused to another item makes it an [equipped ghost](uid:30A).

## Reloading

When you reload straight into a different file, while you have enough zuggles to be close to the overload threshold, Link's new equipment can often overload drop. This happens because the game tries to add the new equipment from the loading file to Link before deleting the old equipment from the file you were just playing. To fix this, you can unequip and re-equip, or fail drop the current equipment.

If this happens to parts of Link's body, it's because the armor-dependent actors failed to connect properly. Changing which armor you have equipped in that slot will fix this.

## Effects

Equipping items while Link is overloaded opens up the possibility of fuse glitches (Fuse Entanglement, Cold Fuse, Pseudo Fuse) without needing to hit any timing windows (beyond those needed for zuggling).
