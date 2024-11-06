import data

import random


class Dungeon:

    def init(self, dungeon_data: dict):
        self.id = 1  # В будущем придумать, как назначать id
        self.content = self.set_areas(dungeon_data)

    def set_areas(self, dungeon_data: dict) -> list:
        combinanions = self.set_combinations(dungeon_data)
        # TODO
        for i in combinations:
            print(i)

    def set_combinations(self, dungeon_data: dict) -> list:
        combinations = []
        main_creatures_num = len(dungeon_data["creatures"]["main_creatures"])
        traps_num = len(dungeon_data["traps"])
        objects_num = len(dungeon_data["objects"])
        main_items_num = len(dungeon_data["main_items"])

        # TODO
        # Мне нужен генератор, который вернет комбинации типа
        # [{"creature": True, "trap": False, "object": True, "item": False},
        #   <...>,
        # ]
        # Чтобы в сумме:
        # creature = main_creatures_num + 1-2 в зависимости от размера подземелья
        # trap = traps_num + 1-2
        # object = objects_num
        # item = main_items_num + 1-3

        return combinations


def generate_areas(dungeon_data: tuple) -> list:
    new_dungeon = Dungeon(dungeon_data) # Объект надо куда-то сохранить
    return new_dungeon.content
