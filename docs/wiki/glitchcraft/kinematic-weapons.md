---
title: "Kinematic Weapons"
uid: "OO2"
label: "KW"
versions: ["1.1.0", "1.1.1", "1.1.2", "1.2.0", "1.2.1", "1.3.0/1.4.0", "1.4.1", "1.4.2", "1.4.3", "Switch 2"]
credits: ["mulberry", "dt13269", "Squidwest"]
date: "2026-02-25"
description: "Makes weapons immovable, except by picking up and dropping them."
aliases: ["kinematic equipment","unmovable equipment"]
tags: ["equipment"]
---

# Kinematic Weapons `KW`
`1.1.0` `1.1.1` `1.1.2` `1.2.0` `1.2.1` `1.3.0/1.4.0` `1.4.1` `1.4.2` `1.4.3` `Switch 2`

## Summary
---
Makes weapons immovable, except by picking up and dropping them.

_mulberry, dt13269; Optimizations by mulberry, Squidwest - 25 February 2026_

## Instructions
---

=== "Basic Setup"

    1. Overload pickup weapon held by depths ghost
    2. Go out of range - this varies between ghosts
    3. While looking away from the ghost fail drop weapon
    4. Wait until Link holds it
    5. Drop it - it should be stuck in mid-air
    6. Keep looking away and resync zuggle a shield unless you already have one zuggled
    7. Overload CF the weapon twice to a random shield to PF it
    8. Load a save
    9. Either detangle out of weapon range or drop the zuggle and octo detangle it

=== "DI PSLOT Kinematic Weapon Setup"

    1. Zuggle a DI ghost shield
    2. Overload pick up a kinematic weapon held by ghost
    3. Fail drop and drop the kinematic weapon out of range
    4. Overload FE the weapon (using the shield zuggle) and load null fuse it (= overload cold fuse to your shield + pause on the FE frame -> load)
    5. Detangle out of range
    6. Overload FE the kinematic weapon and unzuggle parent

=== "Basic Loadless Setup"

    1. Overload pick up a kinematic weapon held by ghost
    2. Fail-drop and drop the weapon out of update range
    3. Overload pickup the weapon again and fuse it to a shield
    4. Unload the ghost by distance
    5. Fail-drop and drop the weapon again
    6. Use Octo Detanglement out of update range of the weapon
    7. Pick up the weapon

    Due to the lack of a save load, the ghost will not automatically regain its weapon in this setup.

## Notes
---

!!! warning "Take care!"
    Warping causes a "sleep" on equipped items, which will undo this state! You can zuggle it to take it with you safely.

## Resources
---
- [Original discovery](https://discordapp.com/channels/1086729144307564648/1110956205624532993/1476367185642520639)
- [DI PSLOT Kinematic Weapon](https://discord.com/channels/1086729144307564648/1110956205624532993/1476693921533923390)

## Related
---
- [Zuggle Overload](search:Zuggle Overload)
