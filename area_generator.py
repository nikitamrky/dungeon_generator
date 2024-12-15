from helpers import Creature

import random


class Dungeon:

    def __init__(self, dungeon_data: dict):
        self.id = 1  # В будущем придумать, как назначать id
        self.content = self.set_areas(dungeon_data)

    def set_areas(self, dungeon_data: dict) -> list:
        # TODO: разбить функцию на части
        # Создаем словарь областей, каждая из которых также является словарем;
        # количество областей на 1 меньше, поскольку область с боссом не участвует в распределении
        # и будет добавлена позднее

        # Если есть босс - уменьшаем количество областей на 1, чтобы добавить область с боссом позже
        if dungeon_data["creature"]["boss"]:
            n = 0  # Потому что range() не включает последний элемент
        else:
            n = 1
        Dungeon.areas = {i: dict() for i in range(1, dungeon_data["areas_num"] + n)}

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
            n = 0  # Потому что для корректной работы range() должно быть +1
        elif dungeon_data["size"] == "large":
            n = -1
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
        # Проверяем, что ловушки есть
        if dungeon_data["traps"]:
            traps_num = len(dungeon_data["traps"])
            target_areas = random.sample(range(1, len(Dungeon.areas) + 1), traps_num)
            count = 0
            for i in target_areas:
                Dungeon.areas[i]["trap"] = dungeon_data["traps"][count]
            # Тест распределения ловушек
            print("Traps locations: " + " " + ", ".join(map(str, target_areas)))
            for num, content in Dungeon.areas.items():
                if "trap" in content:
                    print(f"{num}: {content['trap']}")


        # Случайно распределяем основные предметы
        main_items_num = len(dungeon_data["main_items"])
        target_areas = random.sample(range(1, len(Dungeon.areas) + 1), main_items_num)
        count = 0
        for i in target_areas:
            Dungeon.areas[i]["main_item"] = dungeon_data["main_items"][count]
            count += 1
        # Тест распределения основных предметов
        print("Main items locations: " + " " + ", ".join(map(str, target_areas)))
        for num, content in Dungeon.areas.items():
            if "main_item" in content:
                print(f"{num}: {content['main_item']}")


        # Случайно распределяем объекты кол-ву total - 1 для small и total - 2 для large
        objects_num = len(dungeon_data["objects_list"])
        if dungeon_data["size"] == "small":
            n = 0  # Потому что для корректной работы range() должно быть +1
        elif dungeon_data["size"] == "large":
            n = -1
        target_areas = random.sample(range(1, len(Dungeon.areas) + n), objects_num)
        count = 0
        for i in target_areas:
            Dungeon.areas[i]["object"] = dungeon_data["objects_list"][count]
            count += 1
        # Тест распределения объектов
        print("Objects locations: " + " " + ", ".join(map(str, target_areas)))
        for num, content in Dungeon.areas.items():
            if "object" in content:
                print(f"{num}: {content['object']}")


        # Если есть пустые комнаты...
        if any(not v for v in Dungeon.areas.values()):
            # ... добавляем в них случайно или additional creature (с конца списка),
            # или trap, или additional item
            additional_creatures_count = 0
            # Для каждого пустого словаря (area)
            for i in (k for k in Dungeon.areas if not Dungeon.areas[k]):
                # Проверяем, есть ли в подземелье ловушки:
                if dungeon_data["traps"]:
                    r = random.choice((1, 2, 3))
                else:
                    r = random.choice((1, 3))
                if r == 1:
                    additional_creatures_count += 1
                    Dungeon.areas[i]["additional_creature"] = (
                        dungeon_data["creatures"]["additional_creatures"][-additional_creatures_count]
                    )
                elif r == 2:
                    Dungeon.areas[i]["trap"] = (
                        dungeon_data["traps"][random.choice(range(0, len(dungeon_data["traps"])))]
                    )
                else:
                    Dungeon.areas[i]["additional_item"] = (
                        dungeon_data["additional_items"][random.choice(range(0, len(dungeon_data["additional_items"])))]
                    )
        # Тестируем донаполнение комнат и смотрим всё вместе
        counter = 1
        for (k, v) in Dungeon.areas.items():
            content_list = [item for item in v.values()]
            # Если в контенте комнаты есть существо - меняем значение с объекта на название вида существа
            for index in range(len(content_list)):
                if isinstance(content_list[index], Creature):
                    content_list[index] = content_list[index].kind
            # Выводим контент каждой комнаты
            print(f"#{counter}: {content_list}")
            counter += 1

        # TODO: добавить опцию перемешать порядок комнат кнопкой?
        # Если есть босс - добавляем комнату с боссом и наградой (не раньше n позиции)
        # в одну из 25% последних комнат (не более 3-х комнат для рандома)
        if dungeon_data["creature"]["boss"]:
            n = len(Dungeon.areas)
            a = n * 0.25
            if a > 3:
                a = 3
            r = random.randint(1, a)
            r_area_index = -r
            # TODO: сдвинуть все последующие ключи на 1
            # TODO: добавить новый ключ и комнату с боссом и наградой в качестве значения

        # Если нет босса - добавляем награду в одну из 25% последних комнат (не более 3-х комнат для рандома)

