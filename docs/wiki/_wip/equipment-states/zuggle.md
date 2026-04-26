---
title: "Zuggle"
uid: "A1E"
---

# Zuggle

Zuggled equipment is equipment that was supposed to drop, but neither completed the dropping process, nor got re-equipped properly. Zuggled equipment persists across reloads, making it an extremely useful equipment state. See the [zuggle section](uid:ESW) for more.

Most zuggles are in the static [equip position](uid:S8I), as this is the easiest to execute, and very often good enough.

From the equipment's perspective, a zuggle is the same as a smuggle of the same equip position. The difference is that Link has forgotten he had this equipment as a smuggle.

## Effects

- Zuggled equipment is not deleted on reload, due to its unexpected connection to Link.
	- This doesn't override transitive actor dependencies. For example, if you zuggle an FE child, but do nothing to keep the FE parent loaded, the zuggle will still be deleted during the next loading screen.
- Zuggled weapons and shields also become fuse entangle parents of any new fusions made to equipment of these types. This is a way to have a fusion (or fuse entangle) have additional fuse entangle parents.
	- If an item is fuse entangled to one or more zuggles, and has no other fusion parents, that item is a ZLOT, allowing it to also persist across reloads, but with its typical physics retained.
	- This doesn't spread across equipment types. All fuse/FE parents with this method are either all weapons, or all shields.
	- This also happens with cold fuse, provided that the full fuse animation still plays.
	- None of this happens with [culled zuggles](uid:M0U).

	!!! danger Replacement actors
		Fusing or fuse entangling [replacement actor](uid:G46) items while you have active \[unculled\] zuggles will cause the game to **crash**.
- Link can only tolerate so many zuggles before zuggle overload happens. This state is very useful, if you want it, but is better obtained with [invizuggles](uid:M0U).

## Undoing

To undo a static zuggle, equip and warm drop some other equipment of the same type.

## See Also

- **[Dynamic Zuggle](uid:CNV)**
- **[Drop Zuggle](uid:0YL)**
- **[Invizuggle](uid:M0U)**
