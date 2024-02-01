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
    "dead Creature (p49)",  # TODO: generate dead creatures with simple algorithm
    "bones/remains",
    "book/scroll/map",
    "broken door/wall",
    "breeze/wind/smell",
    "lichen/moss/fungus",
    #"Oddity (p50)"  # Removed
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
    # "connection to another dungeon"  # Not for MVP
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
    "roll twice"
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
    "roll twice"
)
DANGERS_CREATURE = (
    "waiting in ambush",
    "fighting/squabbling",  # TODO: make depended on number appearing
    "prowling/on patrol",
    "looking for food",
    "eating/resting",
    "guarding",  # TODO: make depended on findings
    "on the move",
    "searching/scavenging",
    "returning to den",
    "making plans",  # TODO: make depended on intelligence
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
    "Monster lord",  # TODO: monster lord
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
HUMANOID_COMMON = (  # Chances changed
    "halfling",
    "dwarf",
    "elf",
    "half-elf",
    "goblin"
    "goblin",
    "hobgoblin",
    "kobold",
    "dwarf",
    "orc",
    "orc",
    "half-orc",
)
HUMANOID_UNCOMMON = (  # Chances changed
    "fey (tiny)",
    "catfolk",
    "dogfolk",
    "lizardfolk",
    "birdfolk",
    "ogre",
    "troll",
    "ogre",
    "troll",
    "cyclopes",
    "giant"
)
HUMANOID_HYBRID = (  # Content changed
    "centaur",
    "centaur",
    "centaur",
    "werewolf",
    "werewolf",
    "werewolf",
    "werebear",
    "weresnake",
    "wereboar",
    "werecat",
    "weredeer",
    "wereraven",
    "human-shark hybrid"
)
MONSTER_UNUSUAL = (  # Content changed
    "plant (human size)",
    "plant (human size)",
    "fungus (human size)",
    "undead human",
    "undead human",
    "undead human",
    "undead elf",
    "undead dwarf",
    "undead halfling",
    "undead orc",
    "undead goblin",
    "wolf with huge strength and wierd color",
    "big rat with huge strength and wierd color",
    "giant bug",
    "lizard with fire breath",
    "lizard with frosty breath",
    "small dragon turtle",
)
MONSTER_RARE = (  # Content changed
    "slime/ooze (amorphous)",
    "slime/ooze (amorphous)",
    "slime/ooze (amorphous)",
    "creation (construct)",
    "creation (construct)",
    "creation (construct)",
    "griffin",
    "chimera (lion, goat and snake hybrid)",
    "manticore (lion body, scorpion tale)",
    "hippogriff",
    "minotaur",
    "small dragon",
    "unnatural entity",
    "unnatural entity",
    "big dragon turtle",
    "huge insect",
)
MONSTER_LEGENDARY = (  # Content changed
    "fire dragon",
    "fire dragon",
    "fire dragon",
    "frost dragon",
    "acid dragon",
    "magic dragon"  # TODO: magic type
    "colossus"
    "huge plant",
    "undead giant",
    "undead dragon",
    "huge wolf/bear/boar",
    "huge raven",
    "huge snake",
    "huge creation (construct)"
    "huge unnatural entity",
    "huge unnatural entity",
    "divine spirit of nature (one element)",
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

