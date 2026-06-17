---
title: "Smuggle"
uid: "TGY"
aliases: ["smuggling"]
---

# Smuggle

## Description

An equipment smuggle is the relation Link has to a piece of equipment when it is in the act of being dropped. Smuggles naturally get created for 4 frames when any equipment is dropped from Link's hand. During those frames, the piece of equipment is outside of Link's inventory but is still visibly dropping, ready for the game to handle the drop.
This state is supposed to be short-lived, but can be kept for longer than intended using several methods in all versions.

Smuggling is an equipment state, but more importantly, it's also an additional relation Link has to the equipment.

The main reason to obtain longer-lasting smuggles is to trivially upgrade them into [zuggles](uid:A1E), but they're also useful for fuse entanglement.

## Variants

Smuggles can come in different variants, depending on their [equip position](uid:S8I), and if they're culled or not:

<table>
    <tr>
        <th />
        <th>Static</th>
        <th>Dynamic</th>
        <th>Drop</th>
    </tr>
    <tr>
        <th>Name (when unculled)</th>
        <td>Smuggle (Static Smuggle, if clarifying is important)</td>
        <td>Dynamic Smuggle</td>
        <td>Drop Smuggle</td>
    </tr>
    <tr>
        <th>Name (when culled)</th>
        <td>Invismuggle</td>
        <td>Dynamic Invismuggle</td>
        <td>Drop Invismuggle</td>
    </tr>
    <tr>
    <tr>
        <th>Common abbreviation</th>
        <td />
        <td>dsmuggle</td>
        <td>ds</td>
    </tr>
    <tr>
        <th>Unsmuggling it</th>
        <td>Equip something else of that type, and warm drop it</td>
        <td>Equip something else of that type, and throw or shock drop it</td>
        <td>Equip the smuggle and fail drop it</td>
    </tr>
    <tr>
        <th>Upgrading it to a zuggle</th>
        <td>Equip something else of that type, and fail drop it</td>
        <td colspan="2">Equip something else of that type, and warm drop or fail drop it</td>
    </tr>
</table>

!!! warning
    The steps to unsmuggle a smuggle in the above table assume that the smuggle is unculled (fully visible on Link). If it's [culled](uid:445), you will either upgrade it into an invizuggle, or send it to [culled purgatory](uid:TAO).

The distinction between different equip positions is less important for culled smuggles and zuggles.

## Creating smuggles

!!! warning "D-Pad Lock"
    If playing on version 1.1.2 or higher, consider [Despawn Interrupting](search: Despawn Interrupt) the equipment first, to avoid problems with D-Pad Lock.

Although a smuggle is technically created whenever you [warm drop](uid:C6H) equipment, there are ways to create more persistent smuggles:

=== "Culling" ###
    Cull the equipment (without culling Link) and drop it. The easiest way to do this is to Fuse Entangle it to some other equipment, which you leave in a culling area, or by FE-ing the equipment [to Mineru](uid:IG2).

=== "Overload" ###
    Overload pickup the equipment, then drop it. This will be a Ground Drop Smuggle.

=== "Despawn Interrupt" ###
    DI equipment never unsmuggles itself when fail dropped, doesn't cull when replaced with another equip, and doesn't cause D-Pad Lock. Equip some DI equipment and drop–swap it against a wall. (The equip is due to the animation state desync mentioned below).

## Comparison to zuggles

Smuggles and zuggles are very similar in behaviour and nature. From the equipment's perspective, they are _exactly_ the same. The only difference is in how Link treats them; if Link considers the equipment to be what he is actively dropping, it's a smuggle. If not, it's a zuggle.

## Effects

- **Culling** on version `1.2.0` and up - On newer versions of the game, a smuggle is culled if something else of that type is equipped, and unculled when the smuggle fully drops. This is what makes portable culling work (and why it takes a drop–swap, not just a drop).
    - Fail drops didn't forcibly uncull until version `1.2.1`, so version `1.2.0` specifically can quick smuggle with no effort.
    - [Despawn Interrupted](uid:JEV) equipment is exempt from this.
- **D-Pad Lock** - An active smuggle causes the D-Pad to lock on version `1.1.2` and up, meaning that it is not possible to use the D-Pad or drop/swap/unequip equipment of the smuggle's type.
    - On version `1.1.2` specifically, you can bypass d-pad lock for shields and bows by opening the ability wheel, then going straight to the quick menu before the game unpauses.
    - Smuggling [espawn Interrupted equipment doesn't cause d-pad lock on any version.
    - D-Pad Lock doesn't happen while Link is culled.
- **Fuse Entanglement** - Anything fused, fuse entangled, or animated cold fused to intended equipment will also fuse entangle to any unculled smuggle.
- **Link equip state desync** - Most methods of smuggling equipment don't make Link realise he can directly equip new pickups. If you need to equip something after smuggling without it going straight into the inventory, you'll need to equip and unequip something else first.

## See also

- [Dropping mechanics](uid:NYI)

