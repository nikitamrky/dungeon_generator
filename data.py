# Dungeon meta

SIZES = ("small", "large")

FOUNDATION_BUILDERS = {
    "ru": (
        "древняя цивилизация",
        "природа",
        "религиозный орден или культ",
        "люди",
        "эльфы",
        "гномы",
        "темные эльфы",
        "орки или гоблиноиды",
        "могущественный волшебник",
        "демон, демиург или полубог",
    ),
    "eng": (
        "ancient civilization",
        "nature",
        "religious order or cult",
        "humans",
        "elves",
        "dwarves",
        "dark elves",
        "orcs or goblinoids",
        "powerful wizard",
        "daemon, demiurge, or demigod",
    )
}
FOUNDATION_FUNCTIONS = {
    # "портал или источник силы", "шахта", "гробница", "тюрьма",
    # "логово/убежище", "крепость/форпост", "храм/сакральное место",
    # "библиотека/лаборатория", "производственный центр", "неизвестно"
    "ru": (
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
    ),
    "eng": (
        {"description": "portal or source of power",
         "builders": ("ancient civilization",
                      "humans",
                      "elves",
                      "dwarves",
                      "dark elves",
                      "orcs or goblinoids",)
         },
        {"description": "mine",
         "builders": ("ancient civilization",
                      "religious order or cult",
                      "elves",
                      "orcs or goblinoids",
                      "dark elves",)
         },
        {"description": "tomb",
         "builders": ("ancient civilization",
                      "religious order or cult",
                      "elves",
                      "dwarves",
                      "dark elves",
                      "powerful wizard",)
         },
        {"description": "prison",
         "builders": ("elves",
                      "dwarves",
                      "dark elves",
                      "powerful wizard",
                      "demon, demiurge, or demigod",)
         },
        {"description": "lair/sanctuary",
         "builders": ("ancient civilization",
                      "nature",
                      "religious order or cult",
                      "humans",
                      "elves",
                      "dwarves",
                      "dark elves",
                      "orcs or goblinoids",)
         },
        {"description": "fortress/outpost",
         "builders": ("ancient civilization",
                      "religious order or cult",
                      "humans",
                      "elves",
                      "dwarves",
                      "powerful wizard",
                      "demon, demiurge, or demigod")
         },
        {"description": "temple/sacred place",
         "builders": ("ancient civilization",
                      "nature",
                      "religious order or cult",
                      "humans",
                      "elves",
                      "dwarves",
                      "dark elves",
                      "demon, demiurge, or demigod")
         },
        {"description": "library/laboratory",
         "builders": ("religious order or cult",
                      "humans",
                      "elves",
                      "dwarves",
                      "dark elves",
                      "powerful wizard",
                      "demon, demiurge, or demigod")
         },
        {"description": "production center",
         "builders": ("humans",
                      "elves",
                      "dwarves",
                      "dark elves",)
         },
        {"description": "unknown",
         "builders": ("ancient civilization",
                      "nature",
                      "religious order or cult",
                      "humans",
                      "elves",
                      "dwarves",
                      "dark elves",
                      "orcs or goblinoids",
                      "powerful wizard",
                      "demon, demiurge, or demigod")
         },
    ),
}
RUINATIONS = {
    "ru": (
        "загадочная катастрофа",
        "проклятие",
        "естественный катаклизм",
        "эпидемия",
        "нашествие монстров",
        "война, набеги или междоусобица",
        "потеря значения/истощение ресурсов/исход"
    ),
    "eng": (
        "mysterious catastrophe",
        "curse",
        "natural disaster",
        "epidemic",
        "monster invasion",
        "war, raids, or civil strife",
        "loss of significance/resource depletion/exodus"
    )
}
CURRENT_CONDITIONS = {
    "ru": (
        {"description": "заселено монстрами",
         "ruinations": (
             "загадочная катастрофа",
             "проклятие",
             "естественный катаклизм",
             "эпидемия",
             "нашествие монстров",
             "война, набеги или междоусобица",
             "потеря значения/истощение ресурсов/исход",
         )
         },
        {"description": "оккупировано",
         "ruinations": (
             "естественный катаклизм",
             "естественный катаклизм",
             "нашествие монстров",
             "война, набеги или междоусобица",
         )
         },
        {"description": "противостояние",
         "ruinations": (
             "загадочная катастрофа",
             "нашествие монстров",
             "война, набеги или междоусобица",
         )
         },
        {"description": "исследование",
         "ruinations": (
             "загадочная катастрофа",
             "проклятие",
             "естественный катаклизм",
             "эпидемия",
             "война, набеги или междоусобица",
             "потеря значения/истощение ресурсов/исход",
         )
         }
    ),
    "eng": (
        {"description": "inhabited by monsters",
         "ruinations": (
             "mysterious catastrophe",
             "curse",
             "natural disaster",
             "epidemic",
             "monster invasion",
             "war, raids, or civil strife",
             "loss of significance/resource depletion/exodus",
         )
         },
        {"description": "occupied",
         "ruinations": (
             "natural disaster",
             "natural disaster",
             "monster invasion",
             "war, raids, or civil strife",
         )
         },
        {"description": "confrontation",
         "ruinations": (
             "mysterious catastrophe",
             "monster invasion",
             "war, raids, or civil strife",
         )
         },
        {"description": "exploration",
         "ruinations": (
             "mysterious catastrophe",
             "curse",
             "natural disaster",
             "epidemic",
             "war, raids, or civil strife",
             "loss of significance/resource depletion/exodus",
         )
         }
    )
}
DISPOSITIONS = {
    # No use, just to have them listed
    "ru": (
        "агрессия",
        "опасения/недоверие",
        "любопытство",
        "надежда"
    ),
    "eng": (
        "aggression",
        "fear/distrust",
        "curiosity",
        "hope"
    )
}
REWARDS = {
    "ru": (
        {"description": "клад",
         "builders": (
             "древняя цивилизация",
             "люди",
             "эльфы",
             "гномы",
             "темные эльфы"
         ),
         "functions": (
             "шахта",
             "логово/убежище",
             "крепость/форпост",
             "производственный центр",
             "неизвестно"
         )
         },
        {"description": "накопленные богатства",
         "builders": (
             "древняя цивилизация",
             "религиозный орден или культ",
             "люди",
             "эльфы",
             "гномы",
             "темные эльфы",
             "орки или гоблиноиды",
             "могущественный волшебник",
             "демон, демиург или полубог"
         ),
         "functions": (
             "портал или источник силы",
             "гробница",
             "логово/убежище",
             "крепость/форпост",
             "храм/сакральное место",
             "библиотека/лаборатория",
             "неизвестно"
         )
         },
        {"description": "могущественный артефакт",
         "builders": (
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
         ),
         "functions": (
             "портал или источник силы",
             "шахта",
             "гробница",
             "тюрьма",
             "логово/убежище",
             "крепость/форпост",
             "библиотека/лаборатория",
             "производственный центр",
             "неизвестно"
         )
         },
        {"description": "магический дар",
         "builders": (
             "древняя цивилизация",
             "природа",
             "религиозный орден или культ",
             "эльфы",
             "гномы",
             "темные эльфы",
             "могущественный волшебник",
             "демон, демиург или полубог"
         ),
         "functions": (
             "портал или источник силы",
             "шахта",
             "гробница",
             "логово/убежище",
             "храм/сакральное место",
             "неизвестно"
         )
         },
        {"description": "древние знания",
         "builders": (
             "древняя цивилизация",
             "религиозный орден или культ",
             "эльфы",
             "гномы",
             "темные эльфы",
             "могущественный волшебник",
             "демон, демиург или полубог"
         ),
         "functions": (
             "портал или источник силы",
             "гробница",
             "крепость/форпост",
             "храм/сакральное место",
             "библиотека/лаборатория",
             "производственный центр",
             "неизвестно"
         )
         }
    ),
    "eng": (
        {"description": "treasure",
         "builders": (
             "ancient civilization",
             "humans",
             "elves",
             "dwarves",
             "dark elves"
         ),
         "functions": (
             "mine",
             "lair/sanctuary",
             "fortress/outpost",
             "production center",
             "unknown"
         )
         },
        {"description": "accumulated wealth",
         "builders": (
             "ancient civilization",
             "religious order or cult",
             "humans",
             "elves",
             "dwarves",
             "dark elves",
             "orcs or goblinoids",
             "powerful wizard",
             "demon, demiurge, or demigod"
         ),
         "functions": (
             "portal or source of power",
             "tomb",
             "lair/sanctuary",
             "fortress/outpost",
             "temple/sacred place",
             "library/laboratory",
             "unknown"
         )
         },
        {"description": "powerful artifact",
         "builders": (
             "ancient civilization",
             "nature",
             "religious order or cult",
             "humans",
             "elves",
             "dwarves",
             "dark elves",
             "orcs or goblinoids",
             "powerful wizard",
             "demon, demiurge, or demigod"
         ),
         "functions": (
             "portal or source of power",
             "mine",
             "tomb",
             "prison",
             "lair/sanctuary",
             "fortress/outpost",
             "library/laboratory",
             "production center",
             "unknown"
         )
         },
        {"description": "magical gift",
         "builders": (
             "ancient civilization",
             "nature",
             "religious order or cult",
             "elves",
             "dwarves",
             "dark elves",
             "powerful wizard",
             "demon, demiurge, or demigod"
         ),
         "functions": (
             "portal or source of power",
             "mine",
             "tomb",
             "lair/sanctuary",
             "temple/sacred place",
             "unknown"
         )
         },
        {"description": "ancient knowledge",
         "builders": (
             "ancient civilization",
             "religious order or cult",
             "elves",
             "dwarves",
             "dark elves",
             "powerful wizard",
             "demon, demiurge, or demigod"
         ),
         "functions": (
             "portal or source of power",
             "tomb",
             "fortress/outpost",
             "temple/sacred place",
             "library/laboratory",
             "production center",
             "unknown"
         )
         }
    )
}
DRESSINGS = (  # Пока не использую
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
OBJECTS = {
    # Функции: "портал или источник силы", "шахта", "гробница", "тюрьма",
    # "логово/убежище", "крепость/форпост", "храм/сакральное место", "библиотека/лаборатория",
    # "производственный центр", "неизвестно"
    "ru": (
        {"description": "частичный обвал",
         "functions": ("universal",
                       "шахта")
         },
        {"description": "яма/разлом/ров/канава/река",
         "functions": ("universal",
                       "шахта")
         },
        {"description": "большая люстра или множество лампад",
         "functions": ("universal",)
         },
        {"description": "помосты, верхний ярус/этаж",
         "functions": ("universal",)
         },
        {"description": "вертикальные объекты: колонны, опоры, сталакт(гм)иты",
         "functions": ("universal",
                       "шахта")
         },
        {"description": "подвал или нижний ярус",
         "functions": ("universal",)
         },
        {"description": "кухня/столовая",
         "functions": ("тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "производственный центр")},
        {"description": "спальни или личные покои",
         "functions": ("логово/убежище",
                       "крепость/форпост",
                       "неизвестно")},
        {"description": "продовольственные кладовые",
         "functions": ("шахта",
                       "тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "производственный центр",
                       "неизвестно")},
        {"description": "мистические врата (арка, разрыв в пространстве и т.п.)",
         "functions": ("портал или источник силы",
                       "храм/сакральное место",
                       "неизвестно")},
        {"description": "проводники/аккумуляторы магии (камни и т.п.)",
         "functions": ("портал или источник силы",
                       "храм/сакральное место",
                       "библиотека/лаборатория",
                       "неизвестно")},
        {"description": "место для ритуалов (алтарь, площадка и т.п.)",
         "functions": ("портал или источник силы",
                       "храм/сакральное место",
                       "неизвестно")},
        {"description": "столы/купальни для подготовки к ритуалам",
         "functions": ("храм/сакральное место",)
         },
        {"description": "объект поклонения или крупный священный символ",
         "functions": ("храм/сакральное место",)
         },
        {"description": "алтарь/часовня",
         "functions": ("логово/убежище",
                       "крепость/форпост",
                       "храм/сакральное место")},
        {"description": "статуя/монумент",
         "functions": ("гробница",
                       "крепость/форпост",
                       "неизвестно")},
        {"description": "промышленные склады",
         "functions": ("шахта",
                       "производственный центр")},
        {"description": "транспорт (телеги, вагонетки, канатная дорога)",
         "functions": ("шахта",
                       "производственный центр")},
        {"description": "стол(ы) для бумажной работы",
         "functions": ("шахта",
                       "производственный центр",
                       "библиотека/лаборатория")},
        {"description": "производство: верстаки, жернова, лебедки, печи и т.п.",
         "functions": ("производственный центр",)},
        {"description": "закрытый проход, предупреждающий знак или защитный символ",
         "functions": ("гробница",
                       "тюрьма")},
        {"description": "врата или решетка со сложным механизмом",
         "functions": ("гробница",
                       "тюрьма",
                       "логово/убежище",
                       "крепость/форпост")},
        {"description": "цепи, кандалы и/или ограждения",
         "functions": ("тюрьма",)},
        {"description": "замаскированное укрытие: люк, потайная дверь и т.п.",
         "functions": ("логово/убежище",
                       "неизвестно")},
        {"description": "оружейные стойки",
         "functions": ("крепость/форпост",)
         },
        {"description": "оборонительные конструкции",
         "functions": ("крепость/форпост",)
         },
        {"description": "кафедра/постамент/амвон",
         "functions": ("храм/сакральное место",
                       "библиотека/лаборатория")},
        {"description": "книжные шкафы и/или полки для ингредиентов",
         "functions": ("библиотека/лаборатория",)
         },
        {"description": "столы для чтения и/или опытов",
         "functions": ("библиотека/лаборатория",)
         },
    ),
    "eng": (
        {"description": "partial collapse",
         "functions": ("universal",
                       "mine")
         },
        {"description": "pit/crevice/ditch/trench/river",
         "functions": ("universal",
                       "mine")
         },
        {"description": "large chandelier or multiple lamps",
         "functions": ("universal",)
         },
        {"description": "platforms, upper tier/floor",
         "functions": ("universal",)
         },
        {"description": "vertical objects: columns, supports, stalactites/stalagmites",
         "functions": ("universal",
                       "mine")
         },
        {"description": "basement or lower tier",
         "functions": ("universal",)
         },
        {"description": "kitchen/dining hall",
         "functions": ("prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "production center")},
        {"description": "bedrooms or private quarters",
         "functions": ("lair/sanctuary",
                       "fortress/outpost",
                       "unknown")},
        {"description": "food storage",
         "functions": ("mine",
                       "prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "production center",
                       "unknown")},
        {"description": "mystical gates (arch, spatial rift, etc.)",
         "functions": ("portal or source of power",
                       "temple/sacred place",
                       "unknown")},
        {"description": "magic conduits/accumulators (stones, etc.)",
         "functions": ("portal or source of power",
                       "temple/sacred place",
                       "library/laboratory",
                       "unknown")},
        {"description": "ritual site (altar, platform, etc.)",
         "functions": ("portal or source of power",
                       "temple/sacred place",
                       "unknown")},
        {"description": "tables/baths for ritual preparation",
         "functions": ("temple/sacred place",)
         },
        {"description": "object of worship or large sacred symbol",
         "functions": ("temple/sacred place",)
         },
        {"description": "altar/chapel",
         "functions": ("lair/sanctuary",
                       "fortress/outpost",
                       "temple/sacred place")},
        {"description": "statue/monument",
         "functions": ("tomb",
                       "fortress/outpost",
                       "unknown")},
        {"description": "industrial warehouses",
         "functions": ("mine",
                       "production center")},
        {"description": "transport (carts, minecarts, cableway)",
         "functions": ("mine",
                       "production center")},
        {"description": "desk(s) for paperwork",
         "functions": ("mine",
                       "production center",
                       "library/laboratory")},
        {"description": "production: workbenches, millstones, winches, furnaces, etc.",
         "functions": ("production center",)},
        {"description": "blocked passage, warning sign, or protective symbol",
         "functions": ("tomb",
                       "prison")},
        {"description": "gate or grate with a complex mechanism",
         "functions": ("tomb",
                       "prison",
                       "lair/sanctuary",
                       "fortress/outpost")},
        {"description": "chains, shackles, and/or fences",
         "functions": ("prison",)},
        {"description": "hidden shelter: hatch, secret door, etc.",
         "functions": ("lair/sanctuary",
                       "unknown")},
        {"description": "weapon racks",
         "functions": ("fortress/outpost",)
         },
        {"description": "defensive structures",
         "functions": ("fortress/outpost",)
         },
        {"description": "podium/pedestal/pulpit",
         "functions": ("temple/sacred place",
                       "library/laboratory")},
        {"description": "bookshelves and/or ingredient shelves",
         "functions": ("library/laboratory",)
         },
        {"description": "tables for reading and/or experiments",
         "functions": ("library/laboratory",)
         },
    )
}

DISCOVERIES_FIND = {
    # TODO: связать с текущим состоянием?
    # "trinkets", "tools/gear", "weapon(s)", "armor", "cloth(es)", "supplies/trade goods",
    # "coins/gems/jewellery", "potions/poisons", "magic trinket/tool/jewellery",
    # "scroll/book/map", "magic weapon/armor", "key", "valuable/important item(s)"
    "ru": (
        {"description": "безделушки",
         "functions": ("логово/убежище",
                       "крепость/форпост",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",
                        "война, набеги или междоусобица",
                        "потеря значения/истощение ресурсов/исход"),
         "conditions": ("",)
         },
        {"description": "инструменты/снаряжение",
         "functions": ("шахта",
                       "тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров"),
         "conditions": ("",)
         },
        {"description": "оружие",
         "functions": ("тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",
                        "война, набеги или междоусобица",),
         "conditions": ("",)
         },
        {"description": "доспехи",
         "functions": ("тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",
                        "война, набеги или междоусобица",),
         "conditions": ("",)
         },
        {"description": "одежда",
         "functions": ("портал или источник силы",
                       "шахта",
                       "тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "храм/сакральное место",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",
                        "война, набеги или междоусобица",),
         "conditions": ("",)
         },
        {"description": "припасы/товары для торговли",
         "functions": ("шахта",
                       "логово/убежище",
                       "крепость/форпост",
                       "храм/сакральное место",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",),
         "conditions": ("",)
         },
        {"description": "монеты/драгоценности/украшения",
         "functions": ("гробница",
                       "логово/убежище",
                       "крепость/форпост",
                       "храм/сакральное место",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",),
         "conditions": ("",)
         },
        {"description": "зелья/яды",
         "functions": ("портал или источник силы",
                       "шахта",
                       "тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "храм/сакральное место",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",
                        "война, набеги или междоусобица",
                        "потеря значения/истощение ресурсов/исход"),
         "conditions": ("",)
         },
        {"description": "магические безделушки/инструменты/украшения",
         "functions": ("портал или источник силы",
                       "шахта",
                       "гробница",
                       "логово/убежище",
                       "крепость/форпост",
                       "храм/сакральное место",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",
                        "война, набеги или междоусобица",
                        "потеря значения/истощение ресурсов/исход"),
         "conditions": ("",)
         },
        {"description": "свиток/книга/карта",
         "functions": ("портал или источник силы",
                       "шахта",
                       "гробница",
                       "тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "храм/сакральное место",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",
                        "война, набеги или междоусобица"),
         "conditions": ("",)
         },
        {"description": "магическое оружие/доспехи",
         "functions": ("портал или источник силы",
                       "гробница",
                       "тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",),
         "conditions": ("",)
         },
        {"description": "ключ",
         "functions": ("портал или источник силы",
                       "шахта",
                       "гробница",
                       "тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "храм/сакральное место",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",
                        "война, набеги или междоусобица",
                        "потеря значения/истощение ресурсов/исход"),
         "conditions": ("",)
         },
        {"description": "ценный/важный предмет",
         "functions": ("портал или источник силы",
                       "шахта",
                       "гробница",
                       "тюрьма",
                       "логово/убежище",
                       "крепость/форпост",
                       "храм/сакральное место",
                       "библиотека/лаборатория",
                       "производственный центр",
                       "неизвестно",),
         "ruinations": ("загадочная катастрофа",
                        "проклятие",
                        "естественный катаклизм",
                        "эпидемия",
                        "нашествие монстров",
                        "война, набеги или междоусобица",
                        "потеря значения/истощение ресурсов/исход"),
         "conditions": ("",)
         },
    ),
    "eng": (
        {"description": "trinkets",
         "functions": ("lair/sanctuary",
                       "fortress/outpost",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",
                        "war, raids, or civil strife",
                        "loss of significance/resource depletion/exodus"),
         "conditions": ("",)
         },
        {"description": "tools/gear",
         "functions": ("mine",
                       "prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion"),
         "conditions": ("",)
         },
        {"description": "weapon(s)",
         "functions": ("prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",
                        "war, raids, or civil strife",),
         "conditions": ("",)
         },
        {"description": "armor",
         "functions": ("prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",
                        "war, raids, or civil strife",),
         "conditions": ("",)
         },
        {"description": "cloth(es)",
         "functions": ("portal or source of power",
                       "mine",
                       "prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "temple/sacred place",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",
                        "war, raids, or civil strife",),
         "conditions": ("",)
         },
        {"description": "supplies/trade goods",
         "functions": ("mine",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "temple/sacred place",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",),
         "conditions": ("",)
         },
        {"description": "coins/gems/jewellery",
         "functions": ("tomb",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "temple/sacred place",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",),
         "conditions": ("",)
         },
        {"description": "potions/poisons",
         "functions": ("portal or source of power",
                       "mine",
                       "prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "temple/sacred place",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",
                        "war, raids, or civil strife",
                        "loss of significance/resource depletion/exodus"),
         "conditions": ("",)
         },
        {"description": "magic trinket/tool/jewellery",
         "functions": ("portal or source of power",
                       "mine",
                       "tomb",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "temple/sacred place",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",
                        "war, raids, or civil strife",
                        "loss of significance/resource depletion/exodus"),
         "conditions": ("",)
         },
        {"description": "scroll/book/map",
         "functions": ("portal or source of power",
                       "mine",
                       "tomb",
                       "prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "temple/sacred place",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",
                        "war, raids, or civil strife"),
         "conditions": ("",)
         },
        {"description": "magic weapon/armor",
         "functions": ("portal or source of power",
                       "tomb",
                       "prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",),
         "conditions": ("",)
         },
        {"description": "key",
         "functions": ("portal or source of power",
                       "mine",
                       "tomb",
                       "prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "temple/sacred place",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",
                        "war, raids, or civil strife",
                        "loss of significance/resource depletion/exodus"),
         "conditions": ("",)
         },
        {"description": "valuable/important item(s)",
         "functions": ("portal or source of power",
                       "mine",
                       "tomb",
                       "prison",
                       "lair/sanctuary",
                       "fortress/outpost",
                       "temple/sacred place",
                       "library/laboratory",
                       "production center",
                       "unknown",),
         "ruinations": ("mysterious catastrophe",
                        "curse",
                        "natural disaster",
                        "epidemic",
                        "monster invasion",
                        "war, raids, or civil strife",
                        "loss of significance/resource depletion/exodus"),
         "conditions": ("",)
         },
    )
}
TRAPS = {
    "ru": (
        {"description": "сигнальная",
         "conditions": ("оккупировано",
                        "исследование",)
         },
        {"description": "обездвиживающая/парализующая",
         "conditions": ("оккупировано",
                        "противостояние",)
         },
        {"description": "яма",
         "conditions": ("оккупировано",
                        "противостояние",)
         },
        {"description": "раздавливающая",
         "conditions": ("оккупировано",)
         },
        {"description": "протыкающая",
         "conditions": ("оккупировано",
                        "противостояние",
                        "исследование",)
         },
        {"description": "рубящая/режущая",
         "conditions": ("оккупировано",
                        "противостояние",)
         },
        {"description": "блокирующая проход",
         "conditions": ("оккупировано",
                        "противостояние",)
         },
        {"description": "ядовитый газ",
         "conditions": ("оккупировано",
                        "противостояние",
                        "исследование",)
         },
        {"description": "магическая (урон)",
         "conditions": ("оккупировано",
                        "противостояние",
                        "исследование",)
         },
        {"description": "магическая (не наносит урон)",
         "conditions": ("оккупировано",)
         },
    ),
    "eng": (
        {"description": "alarm",
         "conditions": ("occupied",
                        "exploration",)
         },
        {"description": "immobilizing/paralyzing",
         "conditions": ("occupied",
                        "confrontation",)
         },
        {"description": "pit",
         "conditions": ("occupied",
                        "confrontation",)
         },
        {"description": "crushing",
         "conditions": ("occupied",)
         },
        {"description": "piercing",
         "conditions": ("occupied",
                        "confrontation",
                        "exploration",)
         },
        {"description": "slashing/cutting",
         "conditions": ("occupied",
                        "confrontation",)
         },
        {"description": "passage blocker",
         "conditions": ("occupied",
                        "confrontation",)
         },
        {"description": "poison gas",
         "conditions": ("occupied",
                        "confrontation",
                        "exploration",)
         },
        {"description": "magical (deals damage)",
         "conditions": ("occupied",
                        "confrontation",
                        "exploration",)
         },
        {"description": "magical (non-damaging)",
         "conditions": ("occupied",)
         },
    )
}
# Creatures you can find
HUMANOIDS = {
    "ru": (
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
         "disposition": ("агрессия",),
         "alignment": ("злое",)
         },
        {"kind": "огр", "prevalence": "uncommon", "sociality": "group",
         "civilized": False,
         "disposition": ("агрессия", "опасения/недоверие"),
         "alignment": ("нейтральное", "хаотичное", "злое")
         },
        {"kind": "ящеролюди", "prevalence": "uncommon", "sociality": "horde",
         "civilized": False,
         "disposition": ("агрессия", "опасения/недоверие"),
         "alignment": ("нейтральное", "хаотичное", "злое")
         },
    ),
    "eng": (
        {"kind": "human", "prevalence": "common", "sociality": "group",
         "civilized": True,
         "disposition": ("aggression", "fear/distrust", "curiosity", "hope"),
         "alignment": ("good", "lawful", "neutral", "chaotic", "evil")
         },
        {"kind": "elf", "prevalence": "uncommon", "sociality": "group",
         "civilized": True,
         "disposition": ("aggression", "fear/distrust", "curiosity", "hope"),
         "alignment": ("good", "lawful", "neutral", "chaotic", "evil")
         },
        {"kind": "halfling", "prevalence": "rare", "sociality": "group",
         "civilized": True,
         "disposition": ("aggression", "fear/distrust", "curiosity", "hope"),
         "alignment": ("good", "lawful", "neutral", "chaotic", "evil")
         },
        {"kind": "dwarf", "prevalence": "common", "sociality": "group",
         "civilized": True,
         "disposition": ("aggression", "fear/distrust", "curiosity", "hope"),
         "alignment": ("good", "lawful", "neutral", "chaotic", "evil")
         },
        {"kind": "dark elf", "prevalence": "rare", "sociality": "horde",
         "civilized": True,
         "disposition": ("aggression", "fear/distrust", "hope"),
         "alignment": ("good", "lawful", "neutral", "chaotic", "evil")
         },
        {"kind": "orc", "prevalence": "common", "sociality": "horde",
         "civilized": False,
         "disposition": ("aggression", "fear/distrust"),
         "alignment": ("neutral", "chaotic", "evil")
         },
        {"kind": "goblin", "prevalence": "common", "sociality": "horde",
         "civilized": False,
         "disposition": ("aggression", "fear/distrust"),
         "alignment": ("neutral", "chaotic", "evil")
         },
        {"kind": "frogfolk", "prevalence": "rare", "sociality": "horde",
         "civilized": False,
         "disposition": ("aggression", "fear/distrust"),
         "alignment": ("chaotic", "evil")
         },
        {"kind": "kobold", "prevalence": "uncommon", "sociality": "horde",
         "civilized": False,
         "disposition": ("aggression", "fear/distrust"),
         "alignment": ("neutral", "chaotic", "evil")
         },
        {"kind": "troll", "prevalence": "rare", "sociality": "group",
         "civilized": False,
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "ogre", "prevalence": "uncommon", "sociality": "group",
         "civilized": False,
         "disposition": ("aggression", "fear/distrust"),
         "alignment": ("neutral", "chaotic", "evil")
         },
        {"kind": "lizardfolk", "prevalence": "uncommon", "sociality": "horde",
         "civilized": False,
         "disposition": ("aggression", "fear/distrust"),
         "alignment": ("neutral", "chaotic", "evil")
         },
    )
}

BEASTS = {
    "ru": (
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
    ),
    "eng": (
        {"kind": "giant spider", "prevalence": "common", "sociality": "swarm",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "giant rat", "prevalence": "common", "sociality": "swarm",
         "disposition": ("aggression", "fear/distrust"),
         "alignment": ("neutral", "evil")
         },
        {"kind": "giant centipede/scorpion", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "giant snake/lizard", "prevalence": "uncommon", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "giant bear", "prevalence": "common", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "ape/australopithecus", "prevalence": "rare", "sociality": "group",
         "disposition": ("aggression", "fear/distrust", "curiosity"),
         "alignment": ("neutral", "evil")
         },
        {"kind": "giant mosquito/hornet", "prevalence": "rare", "sociality": "swarm",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "giant eagle/condor", "prevalence": "uncommon", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "vampire bat", "prevalence": "uncommon", "sociality": "horde",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
    )
}

HUMANOID_HYBRIDS = {
    "ru": (
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
    ),
    "eng": (
        {"kind": "centaur", "prevalence": "rare", "sociality": "horde",
         "disposition": ("aggression", "fear/distrust", "curiosity", "hope"),
         "alignment": ("good", "neutral", "chaotic", "evil")
         },
        {"kind": "werewolf", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "chaotic", "evil")
         },
        {"kind": "werebear", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "chaotic", "evil")
         },
        {"kind": "weresnake", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "chaotic", "evil")
         },
    )
}

MONSTERS = {
    "ru": (
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
    ),
    "eng": (
        {"kind": "skeleton", "prevalence": "uncommon", "sociality": "horde",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "black pudding", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression", "fear/distrust"),
         "alignment": ("chaotic", "evil")
         },
        {"kind": "zombie", "prevalence": "uncommon", "sociality": "horde",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "rope golem", "prevalence": "rare", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "ankheg", "prevalence": "rare", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "strangler", "prevalence": "uncommon", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "unusual wolf/dog (strength, appearance)", "prevalence": "rare", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "otyugh", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "giant vampire bat", "prevalence": "rare", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "giant beetle", "prevalence": "rare", "sociality": "swarm",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "giant carnivorous plant", "prevalence": "rare", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "mechanism", "prevalence": "legendary", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("neutral",)
         },
        {"kind": "ghost/undead/evil spirit", "prevalence": "uncommon", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "manticore", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "chimera (lion, goat, snake hybrid)", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "harpy", "prevalence": "rare", "sociality": "horde",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "minotaur", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "dragon turtle", "prevalence": "legendary", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "gargoyle", "prevalence": "legendary", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "wyvern", "prevalence": "rare", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("neutral", "evil")
         },
        {"kind": "imp", "prevalence": "rare", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "beholder", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "succubus", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "lesser vampire", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral", "chaotic", "evil")
         },
        {"kind": "stone golem", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral",)
         },
        {"kind": "cyclops", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("neutral",)
         },
    )
}

BOSSES = {
    "ru": (
        {"kind": "дракон", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("агрессия", "опасения/недоверие",),
         "alignment": ("злое",)
         },
        {"kind": "ледяной дракон", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("агрессия", "опасения/недоверие",),
         "alignment": ("злое",)
         },
        {"kind": "кислотный дракон", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("агрессия", "опасения/недоверие",),
         "alignment": ("злое",)
         },
        {"kind": "линдвурм", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("агрессия", "опасения/недоверие",),
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
         "disposition": ("агрессия", "любопытство",),
         "alignment": ("хаотичное", "злое")
         },
        {"kind": "гигантское насекомое", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("агрессия",),
         "alignment": ("злое", "любопытство",)
         },
        {"kind": "гигантский волк/медведь/пес", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("агрессия",),
         "alignment": ("злое",)
         },
        {"kind": "огромный конструкт/механизм", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("агрессия", "опасения/недоверие"),
         "alignment": ("нейтральное",)
         },
        {"kind": "огромная змея/ящерица", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("агрессия",),
         "alignment": ("злое",)
         },
        {"kind": "демон", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("агрессия", "любопытство",),
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
         "disposition": ("агрессия", "опасения/недоверие", "любопытство",),
         "alignment": ("злое",)
         }
    ),
    "eng": (
        {"kind": "dragon", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression", "fear/distrust",),
         "alignment": ("evil",)
         },
        {"kind": "ice dragon", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression", "fear/distrust",),
         "alignment": ("evil",)
         },
        {"kind": "acid dragon", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression", "fear/distrust",),
         "alignment": ("evil",)
         },
        {"kind": "lindworm", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression", "fear/distrust",),
         "alignment": ("evil",)
         },
        {"kind": "lich", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "witches/cult leaders", "prevalence": "rare", "sociality": "group",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "giant intelligent bird", "prevalence": "legendary", "sociality": "group",
         "disposition": ("aggression", "curiosity",),
         "alignment": ("chaotic", "evil")
         },
        {"kind": "giant insect", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("evil", "curiosity",)
         },
        {"kind": "giant wolf/bear/dog", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "huge construct/mechanism", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression", "fear/distrust"),
         "alignment": ("neutral",)
         },
        {"kind": "huge snake/lizard", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "demon", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression", "curiosity",),
         "alignment": ("evil",)
         },
        {"kind": "elemental", "prevalence": "legendary", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("chaotic", "evil")
         },
        {"kind": "warlock/necromancer", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression",),
         "alignment": ("evil",)
         },
        {"kind": "powerful humanoid (artifact/godly power)", "prevalence": "rare", "sociality": "solitary",
         "disposition": ("aggression", "fear/distrust", "curiosity",),
         "alignment": ("evil",)
         }
    )
}
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
