---
title: "Smuggle"
---

# Smuggle

## Description

An equipment smuggle is the state an equipment is put in when it is currently in the action of dropping, i.e. when it is in the drop queue. Smuggles naturally get created for 4 frames when any equipment is dropped from Link's hand. During those frames, the piece of equipment is outside of Link's inventory but is still visibly dropping, as the game is handling the drop.
This state can be abused and kept for as long as desired using several methods in all versions.

The main reason to obtain longer-lasting smuggles is to trivially upgrade them to zuggles.

## Variants

Smuggles can come in different variants, depending on their equip position, and if they're culled or not:

<table>
	<tr>
		<th />
		<th colspan="3">Position</th>
	</tr>
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
		<td colspan="2" />
		<td colspan="2"><small>This distinction is less important for culled smuggles and zuggles.</small></td>
	</tr>
	<tr>
		<th>Unsmuggling it</th>
		<td>Equip something else of that type, and warm drop it</td>
		<td>Equip something else of that type, and throw or shock drop it</td>
		<td>Equip the smuggle, fail drop it, then use any drop method</td>
	</tr>
	<tr>
		<th>Upgrading it to a zuggle</th>
		<td>Equip something else of that type, and fail drop it</td>
		<td>Equip something else of that type, and warm drop or fail drop it</td>
		<td>Equip it, and <a href="zuggle-drop/">zuggle drop</a> it</td>
	</tr>
</table>

## Creating smuggles

!!! warning "D-Pad Lock"
	If playing on version 1.1.2 or higher, consider [Despawn Interrupting](search: Despawn Interrupt) the equipment first, to avoid problems with D-Pad Lock.

Although a smuggle is technically created whenever you [warm drop](cold-warm-drop/) equipment, there are ways to create more persistent smuggles:

### Culling ===

Cull the equipment (without culling Link) and drop it. The easiest way to do this is to Fuse Entangle it to some other equipment, which you leave in a culling area.

### Overload ===

Overload pickup the equipment, then drop it.

## Comparison to zuggles

Smuggles and zuggles are very similar in behaviour and nature. From the equipment's perspective, they are _exactly_ the same. The only difference is in how Link treats them; if Link considers the equipment to be what he is actively dropping, it's a smuggle. If not, it's a zuggle.

## Effects

- **D-Pad Lock** - An active smuggle causes the D-Pad to lock on 1.1.2+, meaning that it is not possible to use the D-Pad or drop/swap/unequip equipment of the smuggle's type.
	- On version 1.1.2 specifically, you can bypass d-pad lock by opening the ability wheel, then going straight to the quick menu before the game unpauses.
	- Smuggling Despawn Interrupted equipment doesn't cause d-pad lock on any version.
- **Fuse Entanglement** - Anything fused, fuse entangled, or animated cold fused to intended equipment will also fuse entangle to any unculled smuggle.
