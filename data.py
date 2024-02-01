# Dungeon meta

SIZES = ("small", "medium", "large", "huge")

FOUNDATION_BUILDERS = (
    "aliens/precursors",
    "demigod/demon",
    "natural (caves, etc.)",
    "natural (caves, etc.)",
    "religious order/cult",
    "some humanoid race (p. 49)",  # TODO: add humanoid random choice
    "some humanoid race (p. 49)",
    "dwarves/gnomes",
    "dwarves/gnomes",
    "elves",
    "wizard/madman",
    "monarch/warlord"
)
FOUNDATION_FUNCTIONS = (
    "source/portal",
    "mine",
    "tomb/crypt",
    "tomb/crypt",
    "prison",
    "lair/den/hideout",
    "lair/den/hideout",
    "stronghold/sanctuary",
    "stronghold/sanctuary",
    "shrine/temple/oracle",
    "archive/library",
    "unknown/mystery"
)
RUINATIONS = (
    "arcane disaster",
    "damnation/curse",
    "earthquake/fire/flood",
    "earthquake/fire/flood",
    "plague/famine/drought",
    "plague/famine/drought",
    "overrun by monsters",
    "overrun by monsters",
    "war/invasion",
    "war/invasion",
    "depleted resources",
    "better prospects elsewhere"
)
THEMES_MUNDANE = (
    "rot/decay",
    "torture/agony",
    "madness",
    "all is lost",
    "noble sacrifice",
    "savage fury",
    "survival",
    "criminal activity",
    "secrets/treachery",
    "tricks and traps",
    "invasion/infestasion",
    "factions at war"
)
THEMES_UNUSUAL = (
    "creation/invention",
    "Element (p. 50)",  # TODO: make generation of elements
    "knowledge/learning",
    "growth/expansion",
    "deepening mystery",
    "transformation/change",
    "chaos and destruction",
    "shadowy forces",
    "forbidden knowledge",
    "poison/disease",
    "corruption/blight",
    "impending disaster",
)
THEMES_EXTRAORDINARY = (
    "scheming evil",
    "divination/scrying",
    "blasphemy",
    "arcane research",
    "occult forces",
    "an ancient curse",
    "mutation",
    "the unquiet dead",
    "bottomless hunger",
    "incredible power",
    "unspeakable horrors",
    "holy war",
)

# Area content, discoveries and dangers

# Content in tuples:
# themed/unthemed, common/unique, # of discoveries, # of dangers
AREA_CONTENT = (
    ("unthemed", "common", False, False),
    ("unthemed", "common", False, True),
    ("unthemed", "common", True, True),
    ("unthemed", "common", True, True),
    ("unthemed", "common", True, False),
    ("unthemed", "common", True, False),
    ("themed", "common", False, True),  # TODO: choose theme randomly with countdowns
    ("themed", "common", True, True),
    ("themed", "common", True, False),
    ("themed", "unique", False, True),
    ("themed", "unique", True, True),
    ("themed", "unique", True, False),
)
DISCOVERIES_DRESSING = (
    "junk/debris",
    "tracks/marks",
    "signs of battle",
    "writing/carving",
    "warning",
    "dead Creature (p49)",  # TODO: generate creatures
    "bones/remains",
    "book/scroll/map",
    "broken door/wall",
    "breeze/wind/smell",
    "lichen/moss/fungus",
    "Oddity (p50)"  # TODO: generate oddities
)
DISCOVERIES_FEATURE = (
    "cave-in/collapse",
    "pit/shaft/chasm",
    "pillars/columns",
    "locked door/gate",
    "alcoves/niches",
    "bridge/stairs/ramp",
    "fountain/well/pool",
    "puzzle",
    "altar/dais/platform",
    "statue/idol",
    "magic pool/statue/idol",
    "connection to another dungeon"
)
DISCOVERIES_FIND = (
    "trinkets",
    "tools",
    "weapons/armor",
    "supplies/trade goods",
    "coins/gems/jewelry",
    "poisons/potions",
    "adventurer/captive",
    "magic item",
    "scroll/book",
    "magic weapon/armor",
    "artifact",
    "roll twice"  # TODO: roll twice except this result and combine answers
)
DANGERS_TRAP = (
    "alarm",
    "ensnaring/paralyzing",
    "pit",
    "crushing",
    "piercing/puncturing",
    "chopping/slashing",
    "confusing (maze, etc.)",
    "gas (poison, etc.)",
    "Element (p50)"  # TODO: roll for element
    "ambush",
    "magical",
    "roll twice"  # TODO: roll twice except this result
)
DANGERS_CREATURE = (  # TODO: roll for all params of creature
    "waiting in ambush",
    "fighting/squabbling",
    "prowling/on patrol",
    "looking for food",
    "eating/resting",
    "guarding",
    "on the move",
    "searching/scavenging",
    "returning to den",
    "making plans",
    "sleeping",
    "dying"
)
DANGERS_ENTITY = (
    "alien interloper",
    "vermin lord",
    "criminal mastermind",
    "warlord",
    "high priest",
    "oracle",
    "wizard/witch/alchemist",
    "Monster lord (p49)",  # TODO: monster lord
    "evil spirit/ghost",
    "undead lord (lich, etc.)",
    "demon",
    "dark god"
)

# Creatures (in addition to DANGERS_CREATURE)

BEAST_EARTHBOUND = (
    "termite/tick/louse",
    "snail/slug/worm",
    "ant/centipede/scorpion",
    "snake/lizard",
    "vole/rat/wease",
    "boar/pig",
    "dog/fox/wolf",
    "cat/lion/panther",
    "deer/horse/camel",
    "ox/rhino",
    "bear/ape/gorilla",
    "mammoth/dinosaur"
)
BEAST_AIRBORNE = (
    "mosquito/firefly",
    "locust/dragonfly/moth",
    "bee/wasp",
    "chicken/duck/goose",
    "songbird/parrot",
    "gull/waterbird",
    "heron/crane/stork",
    "crow/raven",
    "hawk/falcon",
    "eagle/owl",
    "condor",
    "pteranodon"
)
BEAST_WATERGOING = (
    "insect",
    "jelly/anemone",
    "clam/oyster/snail",
    "eel/snake",
    "frog/toad",
    "fish",
    "crab/lobster",
    "turtle",
    "alligator/crocodile",
    "dolphin/shark",
    "squid/octopus",
    "whale"
)
HUMANOID_COMMON = (
    "halfling",
    "halfling",
    "halfling",
    "goblin/kobold",
    "goblin/kobold",
    "dwarf/gnome",
    "dwarf/gnome",
    "orc/hobgoblin/gnoll",
    "orc/hobgoblin/gnoll",
    "half-elf/half-orc, etc.",
    "half-elf/half-orc, etc.",
    "elf"
)
HUMANOID_UNCOMMON = (
    "fey (tiny)",
    "catfolk/dogfolk",
    "catfolk/dogfolk",
    "lizardfolk/merfolk",
    "lizardfolk/merfolk",
    "lizardfolk/merfolk",
    "birdfolk",
    "ogre/troll",
    "ogre/troll",
    "ogre/troll",
    "cyclopes/giant",
    "cyclopes/giant"
)
HUMANOID_HYBRID = (
    "centaur",
    "centaur",
    "werewolf/werebear",
    "werewolf/werebear",
    "werewolf/werebear",
    "werecreature (human + beast)",  # TODO: make human + beast werecreature
    "human + beast",  # TODO: make human-beast hybrids
    "human + beast",
    "human + beast",
    "human + beast",
    "human + 2 beasts",
    "human + 2 beasts"
)
MONSTER_UNUSUAL = (
    "plant/fungus",
    "plant/fungus",
    "plant/fungus",
    "Undead Human",
    "Undead Human",
    "Undead Humanoid",  # TODO: random humanoid choice
    "beast + beast",  # TODO: beast + beast creature
    "beast + beast",
    "beast + ability",  # TODO: beast + ability
    "beast + ability",
    "beast + feature",  # TODO: beast + feature
    "beast + feature",
)
MONSTER_RARE = (
    "slime/ooze (Amorphous)",
    "slime/ooze (Amorphous)",
    "slime/ooze (Amorphous)",
    "creation (Construct)",
    "creation (Construct)",
    "creation (Construct)",
    "beast + oddity",  # TODO: beast + oddity
    "beast + oddity",
    "beast + oddity",
    "Unnatural Entity",
    "Unnatural Entity",
    "Unnatural Entity"
)
MONSTER_LEGENDARY = (
    "dragon/colossus (Huge)",
    "dragon/colossus (Huge)",
    "dragon/colossus (Huge)",
    "Unusual + Huge",  # TODO: unusual + huge
    "Unusual + Huge",
    "Unusual + Huge",
    "Rare + Huge",  # TODO: rare + huge
    "Rare + Huge",
    "Rare + Huge",
    "Beast + dragon",  # TODO: beast + dragon
    "Unusual + dragon",  # TODO: unusual + dragon
    "Rare + dragon"  # # TODO: rare + dragon
)
ACTIVITY = (
    "waiting in ambush",
    "fighting/squabbling",
    "prowling/on patrol",
    "looking for food",
    "eating/resting",
    "guarding",
    "on the move",
    "searching/scavenging",
    "returning to den",
    "making plans",
    "sleeping",
    "dying"
)
ALIGNMENT = (  # Changed chances
    "chaotic",
    "chaotic",
    "evil",
    "evil",
    "neutral",
    "neutral",
    "neutral",
    "good",
    "lawful"
)
DISPOSITION = (
    "attacking",
    "hostile/aggressive",
    "hostile/aggressive",
    "cautious/doubtful",
    "cautious/doubtful",
    "fearful/fleeing",
    "neutral",
    "neutral",
    "curious/hopeful",
    "friendly"
)

