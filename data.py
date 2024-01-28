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

# Discoveries and dangers

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
    "termite/tick/louse"
)
BEAST_AIRBORNE = (
    "mosquito/firefly"
)
BEAST_WATERGOING = (
    "insect"
)