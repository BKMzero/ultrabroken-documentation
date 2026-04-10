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

- Only one item is processed per frame, and nothing is processed on the first unpaused frame.
- The game attempts to drop multiple items in separate positions behind Link, instead of all in a vertical stack.
- The game scans for space behind Link to drop the item in question. If it finds enough space to drop the item, it spawns an actor for the item.
- If it _doesn't_ find space behind Link to drop the item, it **fail drops** it, displaying the message "You can't take that out here." in an on-screen banner. The game then abandons trying to drop anything else, flushing the drop queue out in its entirety.
- A large enough height gap behind Link (e.g. off the edge of a wall) also triggers a fail drop. If you can't find an appropriate wall for manipulating this, a strong _absence_ of wall is just as good. The minimum height difference required for this is less than you might think.

That's how it works for items that are unequipped. Although dropping equipped items works broadly the same way from the drop queue's perspective, the actors for the equipment and for Link play a more active role.

!!! note How equipped is 'equipped'?
    If you equip something new in the pause screen, and then immediately drop it, are you dropping something equipped? Version 1.0 says yes, which is why that version has some exclusive swap–drop tech in its setups. Every other version waits until the game unpauses before actually creating an equipment actor on Link, so swap–dropping on other versions works much more like a regular cold drop. There are additional complications if Link is culled on the first unpaused frame.

## Dropping equipped items

When you drop something Link has equipped, the game broadcasts a 'start dropping' message to all equipment of that type. Link changes his active equipment state to 'dropping', and puts a reference to the item he had equipped into his own 'is dropping' slot (he has three of these, one for each equippable type). The latter is what defines a smuggle, and the item is supposed to stay there until its turn comes in the drop queue. When the item in the 'is dropping' slot is free to drop fully, the equipment drops, and Link removes that reference. If anything in the drop queue fail drops, all items in the 'is dropping' slots are forcibly re-equipped onto Link.

This all works fine, as long as Link never needs to replace one active smuggle with another. If a second item of the same type is supposed to go into that 'is dropping' slot, Link overwrites the old reference with a new one. The former smuggle then does one of three things:

- If it still responds to a 'start dropping' message, and succeeds in dropping, it drops and detaches from Link as normal. But because it's not the current smuggle anymore, Link fails to fully detach it from himself. If the item wasn't originally overload equipped, this also turns it into a [Zuggle Drop](uid:L84).
- If it still responds to a 'start dropping' message, but fail drops, it becomes a zuggle. The reason zuggle setups require a fail drop is because the second _Drop_ command from the inventory is broadcast to all equipment on Link, and the former first smuggle needs to stay put in order to actually become a zuggle.
- If it doesn't respond to a 'start dropping' message, it stays attached to Link and becomes a zuggle. This happens with:
    - Invismuggles. As culled smuggles, they don't change their own state, but Link no longer considering them an active smuggle means they get promoted to invizuggles.
    - Dynamic smuggles. They never considered themselves to be dropping in the first place, so they ignore the 'start dropping' message that makes the second smuggle. They just get passively promoted to dynamic zuggles.
    - Drop smuggles are promoted to zuggles in the same way for the same reason, despite having 'drop' in their name (in this case, 'drop' refers to the drop equip position, not the equipment dropping mechanic).

## Buffer drops

Some glitch setups (e.g. Swap Resync Zuggle, or setup adaptations for the Switch 2 Edition) make use of _buffer drops_; extra equipment inserted into the drop queue to delay further drops for a comparable number of frames. Whether these are expected to fully drop, or can fail drop, will vary depending on the setup.
