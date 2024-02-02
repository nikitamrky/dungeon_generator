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
    ("unthemed", "common", False, True),  # Previously "False, False"
    ("unthemed", "common", False, True),
    ("unthemed", "common", True, True),
    ("unthemed", "common", True, True),
    ("unthemed", "common", True, False),
    ("unthemed", "common", True, False),
    ("themed", "common", False, True),
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
    "Element (p50)",  # TODO: roll for element
    "ambush",
    "magical",
    "roll twice",
    "roll twice"  # More traps!
)
# DANGERS_ENTITY = (  TODO later maybe as tags or attrs
#     "alien interloper",
#     "vermin lord",
#     "criminal mastermind",
#     "warlord",
#     "high priest",
#     "oracle",
#     "wizard/witch/alchemist",
#     "Monster lord",
#     "evil spirit/ghost",
#     "undead lord (lich, etc.)",
#     "demon",
#     "dark god"
# )

# Creatures

HUMAN = (
    ("human", ["group"]),
    ("human", ["horde"]),
)
BEAST_EARTHBOUND = (
    ("big spider", ["swarm"]),
    ("big worm", ["swarm"]),
    ("big ant/centipede/scorpion", ["swarm"]),
    ("big snake/lizard", ["horde"]),
    ("vole/rat/wease", ["swarm"]),
    ("boar", ["group"]),
    ("dog/fox/wolf", ["group"]),
    ("lion/panther", ["group"]),
    ("cat", ["solitary"]),
    ("deer/horse/camel", ["group"]),
    ("ox/rhino", ["group"]),
    ("bear", ["solitary"]),
    ("ape/gorilla", ["group"]),
)
BEAST_AIRBORNE = (
    ("mosquito/firefly", ["swarm"]),
    ("locust/dragonfly/moth", ["swarm"]),
    ("bee/wasp", ["swarm"]),
    ("chicken/duck/goose", ["group"]),
    ("songbird/parrot", ["horde"]),
    ("gull/waterbird", ["group"]),
    ("heron/crane/stork", ["group"]),
    ("crow/raven", ["horde"]),
    ("hawk/falcon", ["group"]),
    ("eagle/owl", ["group"]),
    ("condor", ["group"]),

)
# BEAST_WATERGOING = (  # TODO: add later
#     "insect",
#     "jelly/anemone",
#     "clam/oyster/snail",
#     "eel/snake",
#     "frog/toad",
#     "fish",
#     "crab/lobster",
#     "turtle",
#     "alligator/crocodile",
#     "dolphin/shark",
#     "squid/octopus",
#     "whale"
# )
HUMANOID_COMMON = (  # Chances changed
    ("halfling", ["group"]),
    ("dwarf", ["horde"]),
    ("elf", ["group"]),
    ("half-elf", ["group"]),
    ("dark elf", ["horde"]),
    ("goblin", ["swarm"]),
    ("goblin", ["horde"]),
    ("hobgoblin", ["group"]),
    ("kobold", ["horde"]),
    ("orc", ["horde"]),
    ("orc", ["horde"]),
    ("half-orc", ["solitary"]),
)
HUMANOID_UNCOMMON = (  # Chances changed
    ("fey (tiny)", ["horde"]),
    ("catfolk", ["horde"]),
    ("dogfolk", ["horde"]),
    ("lizardfolk", ["horde"]),
    ("birdfolk", ["horde"]),
    ("ogre", ["group"]),
    ("ogre", ["group"]),
    ("troll", ["group"]),
    ("troll", ["group"]),
    ("cyclopes", ["solitary"]),
    ("giant", ["solitary"]),
)
HUMANOID_HYBRID = (  # Content changed
    ("centaur", ["horde"]),
    ("centaur", ["horde"]),
    ("centaur", ["horde"]),
    ("werewolf", ["solitary"]),
    ("werewolf", ["solitary"]),
    ("werewolf", ["solitary"]),
    ("werebear", ["solitary"]),
    ("weresnake", ["solitary"]),
    ("wereboar", ["solitary"]),
    ("werecat", ["solitary"]),
    ("weredeer", ["solitary"]),
    ("wereraven", ["solitary"]),
    ("triton/merman", ["horde"]),
    ("human-shark hybrid", ["group"]),
)
MONSTER_UNUSUAL = (  # Content changed
    ("undead human", ["horde"]),
    ("undead human", ["horde"]),
    ("undead human", ["group"]),
    ("undead elf", ["group"]),
    ("undead dwarf", ["horde"]),
    ("undead halfling", ["group"]),
    ("undead orc", ["horde"]),
    ("undead goblin", ["horde"]),
    ("ghost", ["horde"]),
    ("wolf with huge strength and wierd color", ["group"]),
    ("big rat with huge strength and wierd color", ["horde"]),
    ("boar with huge strength and wierd color", ["group"]),
    ("huge vampire bat", ["horde"]),
    ("giant bug", ["horde"]),
    ("giant spider", ["horde"]),
)
MONSTER_RARE = (  # Content changed
    ("slime/ooze (amorphous)", ["group"]),
    ("plant (human size)", ["group"]),
    ("fungus (human size)", ["group"]),
    ("creation (construct)", ["group"]),
    ("evil spirit", ["solitary"]),
    ("demon", ["group"]),
    ("griffin", ["solitary"]),
    ("gargoyle", ["group"]),
    ("chimera (lion, goat and snake hybrid)", ["solitary"]),
    ("manticore (lion body, scorpion tale)", ["solitary"]),
    ("hippogriff", ["group"]),
    ("harpy", ["group"]),
    ("minotaur", ["solitary"]),
    ("dinosaur (T-Rex)", ["group"]),
    ("pteranodon", ["group"]),
    ("small dragon", ["solitary"]),
    ("big dragon turtle", ["solitary"]),
    ("huge insect", ["group"]),
    ("lizard with fire breath", ["group"]),
    ("lizard with frosty breath", ["group"]),
    ("dragon turtle", ["group"]),
    ("earth elemental", ["solitary"]),
    ("water elemental", ["solitary"]),
    ("fire elemental", ["solitary"]),
    ("thunder elemental", ["solitary"]),
)
MONSTER_LEGENDARY = (  # Content changed
    ("fire dragon", ["solitary"]),
    ("fire dragon", ["solitary"]),
    ("fire dragon", ["solitary"]),
    ("frost dragon", ["solitary"]),
    ("acid dragon", ["solitary"]),
    ("magic dragon",  ["solitary"]), # TODO: magic type
    ("colossus", ["solitary"]),
    ("lich", ["solitary"]),
    ("huge plant", ["solitary"]),
    ("ancient spider lord", ["solitary"]),
    ("undead giant", ["solitary"]),
    ("undead dragon", ["solitary"]),
    ("huge wolf/bear/boar", ["solitary"]),
    ("huge raven", ["solitary"]),
    ("huge snake", ["solitary"]),
    ("huge turtle", ["solitary"]),
    ("huge creation (construct)", ["solitary"]),
    ("demon lord", ["solitary"]),
    ("dark god", ["solitary"]),
    ("vermin/insect lord", ["solitary"]),
    ("divine spirit of nature (one element)", ["solitary"]),
)
ACTIVITY = (
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
