---
title: "Version Differences"
uid: "1IR"
label: "VER"
credits: ["Suishi", "Emiya"]
---

# Version Differences

Tears of the Kingdom has had several updates since its initial release, and these strongly affect using glitches in practice. Most glitches do exist in all versions, but not all game versions can use all setups. There are also some differences to note between the Switch 1 and Switch 2 editions of the game.

# Version History

This section lists all versions of the game, as well as some of the most important changes for glitchcraft purposes.

## 1.0

The earliest-released version of the game. For the general public, this is only available if you buy the Switch 1 edition on a game card (code `HAC-P-AXN7A`) and never install any updates. It is not possible to play this version on a Switch 2.

1.0 is by far the most broken version of the game, with a lot of glitches easily to perform before you've even left GSI. It's also the version with the fastest available speedrun times, especially in shorter categories. It does, however, come with some important differences unique to this version:

- Zuggle Overload is achieved in fewer zuggles (the canonical minimum is 9 instead of 13).<!-- TODO: verify this lower number --> Additionally, any use of Earthwake or Sidon's water bubble will permanently attach them to Link until you close the game.
- Hyrule Castle is full of culling areas that are all gone in every other version.
- Swap–drop (equipping something in the pause screen, then dropping that item before unpausing) works differently, as 1.0 will spawn an actor for that equipment without you needing to unpause first.
- Back-jumping off a wall allows Link to regain collision during mount lock.
- There are currently no known ways to obtain kinematic weapons.

## 1.1.0

This is the day one patch, which updates a lot of game fundamentals. Some glitches are patched, although the majority of them are still there, and work the same way.

Glitches removed in this version:

- Swap–drop tech
- Memory Interrupt (original portable setup)
- Zonai Storage
- Infinite Horse Stamina

These important glitches remain:

- L-Cancel Fuse Entanglement
- Map Zuggle
- Stick Desync Clip
- Food Ability Buff Storage (FABS)
- Midair Sort Duplication
- Autobuild Cancel
- Memory Interrupt (Koltin method)

## 1.1.1

This version fixes a softlock that can theoretically happen in the main GSI quest _The Closed Door_. There are no other differences, so we frequently consider these two versions the same.

## 1.1.2

This is the killjoy version that patches a whole raft of glitches. Some of the most important changes are:

- Introduces **d-pad lock**, making map zuggling and Drop SLD impossible. You can still use the ability wheel to bypass this for shields and bows, so [Drop Delay Zuggle](search:Drop Delay Zuggle) still works. Throw SLD and L-cancel Fuse Entanglement also still work.
	- Despawn Interrupted equipment is exempt from these restrictions.
- Midair Sort Duping, Autobuild Cancel, and FABS are all patched.

## 1.2.0

This version made a fundamental change to how equipment behaves mid-drop, setting the stage for [portable culling](search:Portable Culling), which will be a vital mechanic for glitchcraft in all future versions.

- L-Cancel Fuse Entanglement is patched.
- The ability wheel no longer bypasses d-pad lock, preventing Drop Delay Zuggling.
- Equipped smuggles now cull if something else if equipped, allowing for Portable Culling.
- Any warm-dropped equipment now forcibly unculls itself and its children.
- Notably, fail drops _don't_ do this, allowing for [Quick Smuggling](search:Quick Smuggling).

## 1.2.1

This was the last version released in 2023, and remained the latest version until the launch of the Switch 2.

- Quick Smuggling is patched (fail drops also force-uncull).

## 1.3.0

The first version released in over a year. This version is best known as what ships on a Switch 2 Edition game card, as well as what pre-release public demos of the Switch 2 Edition ran.

This is the minimum version you're allowed to run on a Switch 2 console. It's not known how this version differs from 1.2.1 on the Switch 1 edition.

- Game performance is improved, making lag-based glitches such as [Hydro Clipping](search:Hydro Clipping) harder to perform.

## 1.4.0

- Released alongside the Switch 2 public launch. No known differences from 1.3.0 on S2; on S1, game performance is improved, and lag-based glitches are much harder to perform.

## 1.4.1

- Patches a GSI softlock with one of the Steward Constructs that gives you the Battery. No other known differences from 1.4.0.

## 1.4.2

- Hacked autobuilds no longer work (any object in the blueprint that doesn't contain an Ultrahand attachment point is deleted).

## 1.4.3

- All glitches related to the 'Link QR' (an autobuild blueprint containing a _Player_ entity) are patched.

# Switch 2

The Switch 2 Edition of the game contains some notable differences for glitchcraft:

- The higher frame rate makes timing-based glitches and pause buffers much harder to execute.
- Mineru turns into an orb and culls faster, giving Mineru cull-based glitches a different timing overall.
- All glitches that persist through returning to the title screen also persist through switching between File 1 / File 2.

Aside from improved performance, very little changes when running the Switch 1 edition of the game on Switch 2 hardware.

## Temporary downgrade

If your copy of Tears of the Kingdom is a Switch 1 edition physical game card, and you bought the Switch 2 edition upgrade as a one-time purchase from the eShop, you can eject the virtual game card for the upgrade and temporarily revert to the Switch 1 edition. You'll be back at 30fps, with all of your File 1 progress preserved (File 2 is inaccessible, but will _not_ be deleted or corrupted in any way). You can then re-insert the virtual game card to return to the Switch 2 edition of the game, with your updated save data intact.
