import data

import random


class Dungeon:

    def __init__(self, dungeon_data: dict):
        self.id = 1  # В будущем придумать, как назначать id
        self.content = self.set_areas(dungeon_data)

    def set_areas(self, dungeon_data: dict) -> list:

        #
        # traps_num = len(dungeon_data["traps"])
        # objects_num = len(dungeon_data["objects"])
        # main_items_num = len(dungeon_data["main_items"])

        # Создаем словарь областей, каждая из которых также является словарем;
        # количество областей на 1 меньше, поскольку область с боссом не участвует в распределении
        # и будет добавлена позднее
        Dungeon.areas = {i: dict() for i in range(1, dungeon_data["areas_num"])}

        # Случайно распределяем main creatures по областям без повторений, каких-то creatures должно быть мин. 2
        main_creatures_num = len(dungeon_data["creatures"]["main_creatures"]) + 1  # Заменить +1 на формулу
        target_areas = random.sample(range(1, len(Dungeon.areas) + 1), main_creatures_num)
        count = 0
        for i in target_areas:
            Dungeon.areas[i]["main_creature"] = dungeon_data["creatures"]["main_creatures"][count]
            # Когда main creatures заканчиваются - идем по списку сначала
            if count == len(dungeon_data["creatures"]["main_creatures"]) - 1:
                count = 0
            else:
                count += 1
        # Тест распределения main creatures
        print("Main creatures locations: " + " " + ", ".join(map(str, target_areas)))
        for num, content in Dungeon.areas.items():
            if "main_creature" in content:
                print(f"{num}: {content['main_creature'].kind}")

        # Случайно распределяем additional creatures по кол-ву total - 1 для small и total - 2 для large
        if dungeon_data["size"] == "small":
            n = -1
        elif dungeon_data["size"] == "large":
            n = -2
        additional_creatures_num = len(dungeon_data["creatures"]["additional_creatures"]) + n
        # Для малых подземелий num может быть 0 или даже -1, фиксим:
        if additional_creatures_num <= 0:
            additional_creatures_num = 1
        target_areas = random.sample(range(1, len(Dungeon.areas) + n), additional_creatures_num)
        count = 0
        for i in target_areas:
            Dungeon.areas[i]["additional_creature"] = dungeon_data["creatures"]["additional_creatures"][count]
            # Когда main creatures заканчиваются - идем по списку сначала
            if count == len(dungeon_data["creatures"]["additional_creatures"]) - 1:
                count = 0
            else:
                count += 1
        # Тест распределения additional creatures
        print("Additional creatures locations: " + " " + ", ".join(map(str, target_areas)))
        for num, content in Dungeon.areas.items():
            if "additional_creature" in content:
                print(f"{num}: {content['additional_creature'].kind}")


        # Случайно распределяем ловушки
        traps_num = len(dungeon_data["traps"])
        target_areas = random.sample(range(1, len(Dungeon.areas)), traps_num)
        count = 0
        for i in target_areas:
            Dungeon.areas[i]["trap"] = dungeon_data["traps"][count]
        # Тест распределения ловушек
        print("Traps locations: " + " " + ", ".join(map(str, target_areas)))
        for num, content in Dungeon.areas.items():
            if "trap" in content:
                print(f"{num}: {content['trap']}")


        # Случайно распределяем основные предметы
        # Случайно распределяем объекты кол-ву total - 1 для small и total - 2 для large
        # Если есть пустые комнаты:
            # Добавляем в них оставшихся additional creatures, предметы и возможно ловушки
        # Перемешиваем комнаты случайным образом, чтобы теперь был определенный порядок
        # Добавляем комнату с боссом (не раньше n позиции)


