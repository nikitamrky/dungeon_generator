# Dungeon meta

SIZES = ("small", "large")

FOUNDATION_BUILDERS = (
    "древняя цивилизация",
    "природа",
    "религиозный орден или культ",
    "люди",
    "эльфы",
    "гномы",
    "темные эльфы",
    "орки или гоблиноиды",
    "могущественный волшебник",
    "демон, демиург или полубог"
)
FOUNDATION_FUNCTIONS = (
    {"description": "портал или источник силы",
     "builders": ("древняя цивилизация",
                  "люди",
                  "эльфы",
                  "гномы",
                  "темные эльфы",
                  "орки или гоблиноиды",)
     },
    {"description": "шахта",
     "builders": ("древняя цивилизация",
                  "религиозный орден или культ",
                  "эльфы",
                  "орки или гоблиноиды",
                  "темные эльфы",)
     },
    {"description": "гробница",
     "builders": ("древняя цивилизация",
                  "религиозный орден или культ",
                  "эльфы",
                  "гномы",
                  "темные эльфы",
                  "могущественный волшебник",)
     },
    {"description": "тюрьма",
     "builders": ("эльфы",
                  "гномы",
                  "темные эльфы",
                  "могущественный волшебник",
                  "демон, демиург или полубог",)
     },
    {"description": "логово/убежище",
     "builders": ("древняя цивилизация",
                  "природа",
                  "религиозный орден или культ",
                  "люди",
                  "эльфы",
                  "гномы",
                  "темные эльфы",
                  "орки или гоблиноиды",)
     },
    {"description": "крепость/форпост",
     "builders": ("древняя цивилизация",
                  "религиозный орден или культ",
                  "люди",
                  "эльфы",
                  "гномы",
                  "могущественный волшебник",
                  "демон, демиург или полубог")
     },
    {"description": "храм/сакральное место",
     "builders": ("древняя цивилизация",
                  "природа",
                  "религиозный орден или культ",
                  "люди",
                  "эльфы",
                  "гномы",
                  "темные эльфы",
                  "демон, демиург или полубог")
     },
    {"description": "библиотека/лаборатория",
     "builders": ("религиозный орден или культ",
                  "люди",
                  "эльфы",
                  "гномы",
                  "темные эльфы",
                  "могущественный волшебник",
                  "демон, демиург или полубог")
     },
    {"description": "производственный центр",
     "builders": ("люди",
                  "эльфы",
                  "гномы",
                  "темные эльфы",)
     },
    {"description": "неизвестно",
     "builders": ("древняя цивилизация",
                  "природа",
                  "религиозный орден или культ",
                  "люди",
                  "эльфы",
                  "гномы",
                  "темные эльфы",
                  "орки или гоблиноиды",
                  "могущественный волшебник",
                  "демон, демиург или полубог")
     },
)
RUINATIONS = (
    "загадочная катастрофа",
    "проклятие",
    "естественный катаклизм",
    "эпидемия",
    "нашествие монстров",
    "война, набеги или междоусобица",
    "потеря значения/истощение ресурсов/исход"
)
CURRENT_CONDITIONS = (
    {"description": "заселено монстрами",
     "ruinations": ("загадочная катастрофа",
                    "проклятие",
                    "естественный катаклизм",
                    "эпидемия",
                    "нашествие монстров",
                    "война, набеги или междоусобица",
                    "потеря значения/истощение ресурсов/исход",)
     },
    {"description": "оккупировано",
     "ruinations": ("естественный катаклизм",
                    "естественный катаклизм",
                    "нашествие монстров",
                    "война, набеги или междоусобица",)
     },
    {"description": "противостояние",
     "ruinations": ("загадочная катастрофа",
                    "нашествие монстров",
                    "война, набеги или междоусобица",)
     },
    {"description": "исследование",
     "ruinations": ("загадочная катастрофа",
                    "проклятие",
                    "естественный катаклизм",
                    "эпидемия",
                    "война, набеги или междоусобица",
                    "потеря значения/истощение ресурсов/исход",),
     }
)
DISPOSITIONS = (
    "агрессия",
    "опасения/недоверие",
    "любопытство",
    "надежда"
)
REWARDS = (
    "клад",
    "накопленные богатства",
    "могущественный артефакт",
    "магический дар"
)


# Area content, discoveries and dangers

AREA_CONTENT = (
    {"dressing": False, "enemies": True, "traps": False, "object": True, "discoveries": False},
    {"dressing": False, "enemies": True, "traps": False, "object": False, "discoveries": True},
    {"dressing": False, "enemies": True, "traps": False, "object": False, "discoveries": True},
    {"dressing": False, "enemies": True, "traps": True, "object": False, "discoveries": True},
    {"dressing": True, "enemies": False, "traps": True, "object": False, "discoveries": True},
    {"dressing": False, "enemies": False, "traps": True, "object": True, "discoveries": False},
    {"dressing": True, "enemies": False, "traps": True, "object": True, "discoveries": True},
    {"dressing": True, "enemies": True, "traps": False, "object": False, "discoveries": False},
)
DRESSINGS = (
    {"description": "следы монстров или их жизнедеятельности",
     "current_condition": "заселено монстрами"},
    {"description": "следы монстров или их жизнедеятельности",
     "current_condition": "заселено монстрами"},
    {"description": "признаки того, что привлекло монстров: остатки их еды, ценные вещи и т.п.",
     "current_condition": "заселено монстрами"},
    {"description": "остатки жертв: тело(а) или вещи",
     "current_condition": "заселено монстрами"},
    {"description": "хлам/мусор",
     "current_condition": "оккупировано"},
    {"description": "что-то осталось от прежней стоянки",
     "current_condition": "оккупировано"},
    {"description": "следы ремесленных работ",
     "current_condition": "оккупировано"},
    {"description": "выброшенная/оставшаяся еда",
     "current_condition": "оккупировано"},
    {"description": "устройства, конструкции или инструменты",
     "current_condition": "оккупировано"},
    {"description": "трупы",
     "current_condition": "противостояние"},
    {"description": "следы боя",
     "current_condition": "противостояние"},
    {"description": "устройства, конструкции или инструменты",
     "current_condition": "противостояние"},
    {"description": "оборонительные сооружения (баррикады или др.)",
     "current_condition": "противостояние"},
    {"description": "труп искателя приключений",
     "current_condition": "исследование"},
    {"description": "следы боя",
     "current_condition": "исследование"},
    {"description": "следы лагеря",
     "current_condition": "исследование"},
    {"description": "следы работ или исследований",
     "current_condition": "исследование"},
)
# DISCOVERIES_FEATURE = (  TODO: объекты, связать с функцией
#     "cave-in/collapse",
#     "pit/shaft/chasm",
#     "pillars/columns",
#     "locked door/gate",
#     "alcoves/niches",
#     "bridge/stairs/ramp",
#     "fountain/well/pool",
#     "puzzle",
#     "altar/dais/platform",
#     "statue/idol",
#     "magic pool/statue/idol",
#     # "connection to another dungeon"  # Not for MVP
# )
# DISCOVERIES_FIND = ( TODO: связать с функцией, причиной разрушения и текущим состоянием
#     "trinkets",
#     "tools",
#     "weapons/armor",
#     "supplies/trade goods",
#     "coins/gems/jewelry",
#     "poisons/potions",
#     "adventurer/captive",
#     "magic item",
#     "scroll/book",
#     "magic weapon/armor",
#     "artifact",
# )
# DANGERS_TRAP = (  TODO: связать с текущим состоянием
#     "alarm",
#     "ensnaring/paralyzing",
#     "pit",
#     "crushing",
#     "piercing/puncturing",
#     "chopping/slashing",
#     "confusing (maze, etc.)",
#     "gas (poison, etc.)",
#     "ambush",
#     "magical",
# )


# Creatures you can find
HUMANOIDS = (
    {"kind": "человек", "prevalence": "common", "sociality": "group",
     "civilized": True,
     "disposition": ("агрессия", "опасения/недоверие", "любопытство", "надежда"),
     "alignment": ("доброе", "законное", "нейтральное", "хаотичное", "злое")
     },
    {"kind": "эльф", "prevalence": "uncommon", "sociality": "group",
     "civilized": True,
     "disposition": ("агрессия", "опасения/недоверие", "любопытство", "надежда"),
     "alignment": ("доброе", "законное", "нейтральное", "хаотичное", "злое")
     },
    {"kind": "полурослик", "prevalence": "rare", "sociality": "group",
     "civilized": True,
     "disposition": ("агрессия", "опасения/недоверие", "любопытство", "надежда"),
     "alignment": ("доброе", "законное", "нейтральное", "хаотичное", "злое")
     },
    {"kind": "гном", "prevalence": "common", "sociality": "group",
     "civilized": True,
     "disposition": ("агрессия", "опасения/недоверие", "любопытство", "надежда"),
     "alignment": ("доброе", "законное", "нейтральное", "хаотичное", "злое")
     },
    {"kind": "темный эльф", "prevalence": "rare", "sociality": "horde",
     "civilized": True,
     "disposition": ("агрессия", "опасения/недоверие", "надежда"),
     "alignment": ("доброе", "законное", "нейтральное", "хаотичное", "злое")
     },
    {"kind": "орк", "prevalence": "common", "sociality": "horde",
     "civilized": False,
     "disposition": ("агрессия", "опасения/недоверие"),
     "alignment": ("нейтральное", "хаотичное", "злое")
     },
    {"kind": "гоблин", "prevalence": "common", "sociality": "horde",
     "civilized": False,
     "disposition": ("агрессия", "опасения/недоверие"),
     "alignment": ("нейтральное", "хаотичное", "злое")
     },
    {"kind": "жаболюд", "prevalence": "rare", "sociality": "horde",
     "civilized": False,
     "disposition": ("агрессия", "опасения/недоверие"),
     "alignment": ("хаотичное", "злое")
     },
    {"kind": "кобольд", "prevalence": "uncommon", "sociality": "horde",
     "civilized": False,
     "disposition": ("агрессия", "опасения/недоверие"),
     "alignment": ("нейтральное", "хаотичное", "злое")
     },
    {"kind": "тролль", "prevalence": "rare", "sociality": "group",
     "civilized": False,
     "disposition": ("агрессия", ),
     "alignment": ("злое", )
     },
    {"kind": "огр", "prevalence": "uncommon", "sociality": "group",
     "civilized": False,
     "disposition": ("агрессия", "опасения/недоверие"),
     "alignment": ("нейтральное", "хаотичное", "злое")
     },
    {"kind": "ящеролюди", "prevalence": "uncommon", "sociality": "group",
     "civilized": False,
     "disposition": ("агрессия", "опасения/недоверие"),
     "alignment": ("нейтральное", "хаотичное", "злое")
     },
)
BEASTS = (
    {"kind": "большой паук", "prevalence": "common", "sociality": "swarm",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "большая крыса", "prevalence": "common", "sociality": "swarm",
     "disposition": ("агрессия", "опасения/недоверие"),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "гигантская сороконожка/скорпион", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "гигантская змея/ящерица", "prevalence": "uncommon", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "гигантский медведь", "prevalence": "common", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "обезъяна/австралопитек", "prevalence": "rare", "sociality": "group",
     "disposition": ("агрессия", "опасения/недоверие", "любопытство"),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "гигантский москит/шершень", "prevalence": "rare", "sociality": "swarm",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "крупный орел/кондор", "prevalence": "uncommon", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "летучая мышь-вампир", "prevalence": "uncommon", "sociality": "horde",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
)
HUMANOID_HYBRIDS = (  # Content changed
    {"kind": "кентавр", "prevalence": "rare", "sociality": "horde",
     "disposition": ("агрессия", "опасения/недоверие", "любопытство", "надежда"),
     "alignment": ("доброе", "нейтральное", "хаотичное", "злое")
     },
    {"kind": "оборотень", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "хаотичное", "злое")
     },
    {"kind": "вермедведь", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "хаотичное", "злое")
     },
    {"kind": "верзмей", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "хаотичное", "злое")
     },
)
MONSTERS = (
    {"kind": "скелет", "prevalence": "uncommon", "sociality": "horde",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "черный пудинг", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия", "опасения/недоверие"),
     "alignment": ("хаотичное", "злое")
     },
    {"kind": "зомби", "prevalence": "uncommon", "sociality": "horde",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "веревочник", "prevalence": "rare", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "анхег", "prevalence": "rare", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "душитель", "prevalence": "uncommon", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "необычный волк/собака (сила, внешний вид)", "prevalence": "rare", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "отьюх", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "гигантская летучая мышь-вампир", "prevalence": "rare", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "гигантский жук", "prevalence": "rare", "sociality": "swarm",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "гигантское хищное растение", "prevalence": "rare", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "механизм", "prevalence": "legendary", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное",)
     },
    {"kind": "призрак/умертвие/злой дух", "prevalence": "uncommon", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "мантикора", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "химера (гибрид льва, козла и змеи)", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "гарпия", "prevalence": "rare", "sociality": "horde",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "минотавр", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "черепаха-дракон", "prevalence": "legendary", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "гаргулья", "prevalence": "legendary", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "виверна", "prevalence": "rare", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "злое")
     },
    {"kind": "бес", "prevalence": "rare", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "бехолдер", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "суккуб", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "низший вампир", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное", "хаотичное", "злое")
     },
    {"kind": "каменный голем", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное",)
     },
    {"kind": "циклоп", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное",)
     },
)

BOSSES = (  # Content changed
    {"kind": "дракон", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "ледяной дракон", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "кислотный дракон", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "линдвурм", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "лич", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "ведьмы/лидеры культа", "prevalence": "rare", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "гигантская разумная птица", "prevalence": "legendary", "sociality": "group",
     "disposition": ("агрессия",),
     "alignment": ("хаотичное", "злое")
     },
    {"kind": "гигантское насекомое", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "гигантское насекомое", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "гигантский волк/медведь/пес", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "огромный конструкт/механизм", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("нейтральное",)
     },
    {"kind": "огромная змея/ящерица", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "демон", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "элементаль", "prevalence": "legendary", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("хаотичное", "злое")
     },
    {"kind": "колдун/некромант", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     },
    {"kind": "могущественный гуманоид (артефакт/сила богов)", "prevalence": "rare", "sociality": "solitary",
     "disposition": ("агрессия",),
     "alignment": ("злое",)
     }
)
ACTIVITY = (  # TODO
    # "waiting in ambush",
    # "fighting/squabbling",
    # "prowling/on patrol",
    # "looking for food",
    # "eating/resting",
    # "guarding",
    # "on the move",
    # "searching/scavenging",
    # "returning to den",
    # "making plans",
    # "sleeping",
    # "dying"
)
