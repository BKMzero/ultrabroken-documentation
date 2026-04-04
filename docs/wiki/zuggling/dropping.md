---
title: "Dropping"
uid: "NYI"
draft: true
---

# Overview

The mechanics of how Tears of the Kingdom handles equipment dropping are surprisingly complex, and edge cases in these engine mechanics are what make smuggling and zuggling possible.

TODO: drop queue (general equipment, incl. cold drops), Link's is-dropping slots

## Dropping equipped items

When you drop something Link has equipped, the game broadcasts a 'start dropping' message to all equipment of that type. Similarly, Link puts a reference to the item he had equipped into his own 'is dropping' slot (he has three of these, one for each equippable type), and the game starts processing all queued drops. When the item in the 'is dropping' slot is free to drop fully, Link removes that reference. If anything in the drop queue fail drops, all items in the 'is dropping' slots are forcibly re-equipped onto Link.

If a second item of the same type is supposed to go into that slot, Link overwrites the old reference with a new one. The former smuggle then does one of two things:

- If it still responds to the original 'start dropping' message, it drops as normal. But because it's not the current smuggle anymore, Link fails to detach it from himself. This turns it into a [Zuggle Drop](zuggle-drop/).
- If it doesn't respond to the original 'start dropping' message, it stays attached to Link and becomes a zuggle. This usually happens with:
  - Invismuggles. As culled smuggles, they don't change their own state, but Link no longer considering them an active smuggle means they get promoted to invizuggles.
  - Dynamic smuggles. They don't consider themselves to be dropping, so they ignore the 'start dropping' message. They just get passively promoted to dynamic zuggles.
