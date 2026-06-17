---
title: "Dropping"
uid: "NYI"
draft: true
---

# Overview

The mechanics of how Tears of the Kingdom handles equipment dropping are surprisingly complex, and edge cases in these engine mechanics are what make smuggling and zuggling possible.

## The Drop Queue

The global equipment drop queue is one of the two key pieces.

The pause screen inventory has the ability to drop multiple pieces of equipment while the game is paused. It inherits this from Breath of the Wild, but changes how the equipment actually drops:

- Equipment actors are only \[potentially\] spawned when you unpause, which is when the game starts processing the drop queue.
- Only one item is processed per frame, and nothing is processed on the first unpaused frame.
- The game attempts to drop multiple items in separate positions behind Link, instead of all in a vertical stack.
- The game scans for space behind Link to drop the item in question. If it finds enough space to drop the item, it spawns an actor for the item.
- If it _doesn't_ find space behind Link to drop the item, it **fail drops** it, displaying the message "You can't take that out here." in an on-screen banner. The game then abandons trying to drop anything else, flushing the drop queue out in its entirety by fail dropping all unconsidered items. Their inventory slots are re-created.
- A large enough height gap behind Link (e.g. off the edge of a wall) also triggers a fail drop. If you can't find an appropriate wall for getting a fail drop when you need one, a strong _absence_ of wall is just as good. The minimum height difference required for this is less than you might think.

That's how it works for items that are unequipped. Although dropping equipped items works broadly the same way from the drop queue's perspective, the actors (in-world 3D objects) for the equipment and for Link play a more active role.

!!! note "How equipped is 'equipped'?"
    If you equip something new in the pause screen, and then immediately drop it, are you dropping something equipped? Version `1.0` of the game says yes, which is why that version has some exclusive swap–drop tech in its setups. Every other version waits until the game unpauses before actually creating an equipment actor on Link, so swap–dropping on other versions works much more like a regular cold drop (plus unequip).

## Dropping equipped items

When you drop something Link has equipped, the game broadcasts a 'start dropping' message to all equipment of that type. Link changes his active equipment state to 'dropping', and puts a reference to the item he had equipped into his own 'is dropping' slot (he has three of these, one for each equippable type). The latter is what defines a smuggle, and the item is supposed to stay there until its turn comes in the drop queue. When the item referenced in the 'is dropping' slot is free to drop fully, the equipment drops, and Link removes that reference. If anything in the drop queue fail drops, all items in the 'is dropping' slots are forcibly re-equipped onto Link.

This all works fine, as long as Link never needs to replace one active smuggle with another. If a second item of the same type is supposed to go into that 'is dropping' slot, Link overwrites the old reference with a new one, forgetting the original smuggle entirely. The former smuggle then does one of three things:

- If it still responds to a 'start dropping' message, and succeeds in dropping, it drops and detaches from Link as normal. But because it's not the current smuggle anymore, Link fails to fully detach it from himself. If the item wasn't originally overload equipped, this also turns it into a [Zuggle Drop](uid:L84).
- If it still responds to a 'start dropping' message, but fail drops, it becomes a zuggle. The reason zuggle setups typically require a fail drop is because the second _Drop_ command from the inventory is broadcast to all equipment on Link, and the former first smuggle needs to stay put in order to actually become a zuggle.
- If it doesn't respond to a 'start dropping' message, it stays attached to Link and becomes a zuggle. This happens with:
    - Invismuggles. As culled smuggles, they don't change their own state, but Link no longer considering them an active smuggle means they get promoted to invizuggles.
    - Dynamic smuggles. They never considered themselves to be dropping in the first place, so they ignore the 'start dropping' message that makes the second smuggle. They just get passively promoted to dynamic zuggles.
    - Drop smuggles are promoted to zuggles in the same way for the same reason, despite having 'drop' in their name (in this case, 'drop' refers to the drop equip position, not the equipment dropping mechanic).

## Buffer drops

Some glitch setups (e.g. Swap Resync Zuggle, or setup adaptations for the Switch 2 Edition) make use of _buffer drops_; extra equipment inserted into the drop queue to delay further drops for a comparable number of frames. Whether these are expected to fully drop, or can fail drop, will vary depending on the setup.

## D-Pad Lock

Later versions of Tears of the Kingdom have extra protections designed to prevent zuggling and SLD:

- As of version `1.1.2`, if you have an active smuggle, equipment of that type is _D-Pad Locked_; you can't re-equip or drop equipment of that type at all, and the respective quick menu will not show up.
- As of version `1.2.0`, active smuggles are culled if you equip something else of that type, and uncull when dropped. They only uncull when fail dropped from version `1.2.1`, so a drop–swap–unequip–fail on version `1.2.0` gets you [quick smuggle](search:Quick Smuggle).

We can mostly work around these restrictions:

- On version `1.1.2` specifically, the D-Pad Lock restrictions for shields and bows can be bypassed by opening the ability wheel, then going straight to the requisite quick menu before the game unpauses.
- Portable Culling (`1.2.0+`) epxloits the game's 'cull active smuggles' behaviour and uses it to cull Link himself. D-Pad Lock is not active as long as Link remains culled, giving you a time window to do additional equipment changes.
    - New equips are not fully processed if Link is culled on the first unpaused frame, so your inventory can desync from Link's actor model. This does have its uses, as long as you're expecting it. We mostly work around this with Swap Resync.
- Despawn Interrupted equipment never applies D-Pad Lock, and never culls when smuggled.

