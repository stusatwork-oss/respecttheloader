## 👾 Help Wanted: Game Devs for the Mall_OS / Loader Prototype

This repo isn't just a weird loader experiment – it's the spine of a small, tightly scoped immersive sim about a dying mall that's actively fighting for its own survival.

**High-concept:**
- A single contained mall environment.
- Simulated "zones" (food court, arcade, back rooms, maintenance corridors, basement Cray altar, etc.).
- Each zone has heat/entropy, failure states, and NPC behaviors tied to those systems.
- Player goals: keep the mall coherent long enough to uncover what it really is.

The Loader exists so the game world can be:
- **Data-driven** (zone configs, missions, NPC behaviors in files, not hard-coded).
- **Scriptable** (text/JSON/configs that designers can iterate on without rebuilding the game).
- **Weird but robust** (filesystem metaphors, logs-as-lore, "/lost+found" as an actual in-world concept).

### Looking for collaborators

Right now I'm especially interested in talking to:

- **Engine Programmers**
  - Unreal, Unity, Godot, or custom engine experience.
  - Comfortable with simulation loops, state machines, save/load, and zone-based systems.

- **Gameplay / Systems Programmers**
  - Experience designing small but deep systemic environments (heat/entropy, NPC schedules, triggers).
  - Enjoy taking a strange high-level concept and turning it into clean, testable code.

- **Technical / Narrative Designers**
  - People who like turning lore + spreadsheets into actual missions, zone states, and in-world events.
  - Comfortable working in markdown/JSON/configs, not just Google Docs.

### What exists already

- A growing lore + systems bible (zones, entropy loops, NPC factions).
- Early pipeline thinking for:
  - mission templates,
  - zone "health",
  - and how the Loader should coordinate everything.
- A clear goal: a **small, dense, replayable sandbox**, not a giant open world.

### What I'm looking for right now

- Sanity checks on engine choice and architecture.
- Advice on the cleanest way to structure:
  - zone state updates,
  - NPC logic,
  - and data-driven missions.
- People who might want to prototype a **tiny vertical slice**:
  - one mall wing,
  - one crisis (entropy/heat event),
  - one or two NPC loops,
  - one mission chain.

If you're a dev who reads this and thinks *"I know exactly how I'd wire that up"*, I want to talk to you.

**Reach out via:**
- GitHub Issues (tag: `dev-collab`)
- or open a Discussion titled **"Loader / Mall_OS Dev Chat"**

---

## Why This Pattern Matters for the Game

The "RespectTheLoader" pattern isn't just repo organization – it's a **design philosophy** that mirrors the game's themes:

### The Mall as a System
- Protected archives = stable zones
- /lab/ = corrupted/experimental spaces
- shareware.yml = the mall's self-awareness manifest
- The Loader = the mall's survival instinct

### The Filesystem as Fiction
```
/archive/
  ├── food_court_stable/        # A zone that "remembers" what it was
  ├── arcade_degraded/           # Entropy creeping in
  └── maintenance_corridor_01/   # Back rooms, service spaces

/lab/
  └── glitch_zones/              # Unstable reality, player risk/reward

/lost+found/                     # In-game explorable space
                                 # Deleted memories, corrupted data
                                 # The mall's unconscious
```

### Data-Driven Design
Everything in YAML/JSON so designers can:
- Tweak zone behaviors without recompiling
- Add new NPCs through config files
- Script events in human-readable formats
- Version control game balance

**The repo structure IS the game architecture.**

---

## The Vision: Immersive Sim Meets Filesystem Horror

**Influences:**
- **System Shock / Prey** - Environmental storytelling, emergent gameplay
- **Dwarf Fortress** - Deep simulation, failure is fun
- **Control** - Architecture as character, bureaucratic horror
- **The Stanley Parable** - Meta-narrative, systems commenting on themselves

**What Makes This Different:**
- The "mall" is self-aware through the filesystem
- Player actions = filesystem operations
- Saving the mall = maintaining system coherence
- The Loader = unreliable narrator / antagonist / ally?

---

## Current State: Prototype Stage

**What's Working:**
- ✅ Conceptual framework (lore, zones, systems)
- ✅ Repository pattern (this!)
- ✅ Data pipeline thinking
- ✅ Clear scope (small, dense, replayable)

**What's Needed:**
- 🔨 Engine selection and architecture
- 🔨 Vertical slice implementation
- 🔨 Systems programming (heat/entropy loops)
- 🔨 Technical design (missions, state machines)
- 🔨 Playtesting and iteration

**Honest Assessment:**
I've hit my skill ceiling. I can design systems and write lore, but I need:
- Engineers who can wire up simulation loops
- Programmers who enjoy data-driven architecture
- Designers who get "weird but systemic"
- People who see this pitch and think "hell yes"

---

## How to Get Involved

### 1. **Lurk & Learn**
- Read THE_BOOK_OF_STULATIONS.md (it's funnier than you expect)
- Browse the repo structure
- Check existing issues tagged `dev-collab`

### 2. **Ask Questions**
- Open a Discussion: "Loader / Mall_OS Dev Chat"
- Ask about engine choices, architecture, scope
- Challenge assumptions, suggest alternatives

### 3. **Prototype Something**
- Pick one small system (zone health, NPC loop, heat event)
- Build a tiny proof-of-concept
- Share it for feedback

### 4. **Join the Sacred Order**
If you contribute meaningfully:
- Git commit credits
- Your name in the CONTRIBUTORS.md
- A parable written about you in THE_BOOK_OF_STULATIONS
- Co-creator status if this thing becomes real

---

## FAQ

**Q: Is this a game or a joke?**
A: Yes. It started as "protect my builds with humor" and evolved into "what if the joke was the game?"

**Q: What's the timeline?**
A: No deadlines. This is a "let's see if we can make something weird and good" project.

**Q: What if I just want to help with one small thing?**
A: Perfect! Even "here's how I'd structure zone state updates" is valuable.

**Q: Do you have funding?**
A: No. This is a passion project. If it becomes real, we'll figure out fair compensation/revenue sharing.

**Q: Why should I help you instead of making my own game?**
A: You shouldn't! But if this concept resonates, maybe we can make something neither of us could alone.

**Q: Is the "basement Cray altar" real?**
A: Read the lore. Then yes.

---

## Skills I'm Looking For

In order of current need:

### 🔴 Critical
- **Systems Architecture** - How to cleanly structure zone updates, NPC logic, event triggers
- **Engine Selection** - Unity vs Godot vs custom? What fits this design?
- **Simulation Programming** - Heat/entropy loops, state machines, emergent behavior

### 🟡 Important
- **Technical Design** - Turning lore into implementable missions and mechanics
- **Save/Load Systems** - Robust persistence that matches the filesystem metaphor
- **Performance** - Keeping simulation running smoothly with many NPCs

### 🟢 Nice to Have
- **UI/UX** - Making filesystem navigation feel good in-game
- **Audio** - Ambient soundscapes for dying mall vibes
- **Writing** - More lore, NPC dialogue, environmental storytelling

---

## The Pitch, Distilled

> What if you made an immersive sim where the game world is a filesystem, the protagonist is a mall fighting entropy, and the save/load system is part of the fiction?

If that sentence made you go "oh that's sick", **please reach out**.

---

*Respect the Loader. The mall fights back. Let's build something weird together.*

**Status:** Actively seeking collaborators (2025-11-27)
