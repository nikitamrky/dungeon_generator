from dungeon_generation.pre_generation.pre_generation import Creature

import random
import math


def areas_scheme(dungeon_data: dict) -> dict[int, dict]:
    # Создаем словарь областей, каждая из которых также является словарем;
    # количество областей на 1 меньше, поскольку область с боссом не участвует в распределении
    # и будет добавлена позднее
    # Если есть босс - уменьшаем количество областей на 1, чтобы добавить область с боссом позже
    if dungeon_data["boss"]:
        n = 0  # Потому что range() не включает последний элемент
    else:
        n = 1
    # TODO: сделать свойством экземпляра!
    areas = {i: dict() for i in range(1, dungeon_data["area_limit"] + n)}
    return areas


class Dungeon:

    def __init__(self, dungeon_data: dict):
        self.id = 1  # В будущем придумать, как назначать id
        self.areas = areas_scheme(dungeon_data)
        self.set_areas(dungeon_data)

    def set_areas(self, dungeon_data: dict) -> None:
        """
        Создать dict областей в параметре .areas. Каждая область является dict.
        :param dungeon_data: Контент подземелья, сгенерированный функциями из helpers.
        """
        # Распределяем main creatures по областям
        self.distribute_main_creatures(dungeon_data)
        # Распределяем additional creatures по областям
        self.distribute_additional_creatures(dungeon_data)
        # Распределяем traps по областям
        self.distribute_traps(dungeon_data)
        # Случайно распределяем основные предметы
        self.distribute_main_items(dungeon_data)
        # Случайно распределяем объекты кол-ву total - 1 для small и total - 2 для large
        self.distribute_objects(dungeon_data)
        # Если есть пустые комнаты, добавляем в них или additional creature,
        # или trap, или additional item
        self.fill_empty_areas(dungeon_data)
        # TODO: добавить опцию перемешать порядок комнат кнопкой?
        # Если есть босс, добавляем комнату с боссом и наградой,
        # если нет, добавляем 1-ю награду
        self.add_boss_area(dungeon_data)
        # Добавляем 2-ю награду, если есть
        self.add_reward(dungeon_data, 2)

    def distribute_main_creatures(self, dungeon_data: dict) -> None:
        """Случайно распределяем main creatures по областям без повторений, каких-то должно быть мин. 2
            :param dungeon_data: контент подземелья, сгенерированный функциями из helpers
        """
        main_creatures_num = len(dungeon_data["main_creatures"]) + 1  # Заменить +1 на формулу
        target_areas = random.sample(range(1, len(self.areas) + 1), main_creatures_num)
        count = 0
        for i in target_areas:
            self.areas[i]["main_creature"] = dungeon_data["main_creatures"][count]
            # Когда main creatures заканчиваются - идем по списку сначала
            if count == len(dungeon_data["main_creatures"]) - 1:
                count = 0
            else:
                count += 1
        # Тест распределения main creatures
        # print("Main creatures locations: " + " " + ", ".join(map(str, target_areas)))
        # for num, content in self.areas.items():
        #     if "main_creature" in content:
        #         print(f"{num}: {content['main_creature'].kind}")

    def distribute_additional_creatures(self, dungeon_data: dict) -> None:
        """Случайно распределяем additional creatures по кол-ву total - 1 для small и total - 2 для large
        :param dungeon_data: контент подземелья, сгенерированный функциями из helpers
        """
        if dungeon_data["size"] == "small":
            n = 0  # Потому что для корректной работы range() должно быть +1
        elif dungeon_data["size"] == "large":
            n = -1
        additional_creatures_num = len(dungeon_data["additional_creatures"]) + n
        # Для малых подземелий num может быть 0 или даже -1, фиксим:
        if additional_creatures_num <= 0:
            additional_creatures_num = 1
        target_areas = random.sample(range(1, len(self.areas) + n), additional_creatures_num)
        count = 0
        for i in target_areas:
            self.areas[i]["additional_creature"] = dungeon_data["additional_creatures"][count]
            # Когда main creatures заканчиваются - идем по списку сначала
            if count == len(dungeon_data["additional_creatures"]) - 1:
                count = 0
            else:
                count += 1

    def distribute_traps(self, dungeon_data: dict) -> None:
        """Случайно распределяем ловушки
        :param dungeon_data: контент подземелья, сгенерированный функциями из helpers
        """
        if not dungeon_data["traps"]:
            return
        traps_num = len(dungeon_data["traps"])
        target_areas = random.sample(range(1, len(self.areas) + 1), traps_num)
        count = 0
        for i in target_areas:
            self.areas[i]["trap"] = dungeon_data["traps"][count]
        # Тест распределения ловушек
        # print("Traps locations: " + " " + ", ".join(map(str, target_areas)))
        # for num, content in self.areas.items():
        #     if "trap" in content:
        #         print(f"{num}: {content['trap']}")

    def distribute_main_items(self, dungeon_data: dict) -> None:
        """Случайно распределяем основные предметы
        :param dungeon_data: контент подземелья, сгенерированный функциями из helpers
        """
        main_items_num = len(dungeon_data["items"][0])
        target_areas = random.sample(range(1, len(self.areas) + 1), main_items_num)
        count = 0
        for i in target_areas:
            self.areas[i]["main_item"] = dungeon_data["items"][0][count]
            count += 1
        # Тест распределения основных предметов
        # print("Main items locations: " + " " + ", ".join(map(str, target_areas)))
        # for num, content in self.areas.items():
        #     if "main_item" in content:
        #         print(f"{num}: {content['main_item']}")

    def distribute_objects(self, dungeon_data: dict) -> None:
        """Случайно распределяем объекты*
        :param dungeon_data: контент подземелья, сгенерированный функциями из helpers
        """
        objects_num = len(dungeon_data["objects"])
        if dungeon_data["size"] == "small":
            n = 0  # Потому что для корректной работы range() должно быть +1
        elif dungeon_data["size"] == "large":
            n = -1
        target_areas = random.sample(range(1, len(self.areas) + n), objects_num)
        count = 0
        for i in target_areas:
            self.areas[i]["object"] = dungeon_data["objects"][count]
            count += 1

    def fill_empty_areas(self, dungeon_data: dict) -> None:
        """Добавляем в пустые комнаты или additional creature, или trap,
        или additional item
        :param dungeon_data: контент подземелья, сгенерированный функциями из helpers
        """
        # Если есть пустые комнаты...
        if any(not v for v in self.areas.values()):
            # ... добавляем в них случайно или additional creature (с конца списка),
            # или trap, или additional item
            additional_creatures_count = 0
            # Для каждого пустого словаря (area)
            for i in (k for k in self.areas if not self.areas[k]):
                # Проверяем, есть ли в подземелье ловушки:
                if dungeon_data["traps"]:
                    r = random.choice((1, 2, 3))
                else:
                    r = random.choice((1, 3))
                if r == 1:
                    additional_creatures_count += 1
                    self.areas[i]["additional_creature"] = (
                        dungeon_data["additional_creatures"][-additional_creatures_count]
                    )
                elif r == 2:
                    self.areas[i]["trap"] = (
                        dungeon_data["traps"][random.choice(range(0, len(dungeon_data["traps"])))]
                    )
                else:
                    self.areas[i]["additional_item"] = (
                        dungeon_data["items"][1][random.choice(range(0, len(dungeon_data["items"][1])))]
                    )

    def add_boss_area(self, dungeon_data: dict) -> None:
        """Если есть босс - добавляем комнату с боссом и наградой случайно
        в одну из последних комнат (33% последних, но не больше 3-х с конца)
        :param dungeon_data: контент подземелья, сгенерированный функциями из helpers
        """
        if not dungeon_data["boss"]:
            # Если нет босса, добавляем награду и выходим
            self.add_reward(dungeon_data, 1)
            return
        length = dungeon_data["area_limit"]
        a = math.floor(length * 0.33 + 0.5)  # Для округления половины до верхнего значения
        if a > 3:
            a = 3
        r = random.randint(1, a)

        # Сдвигаем все ключи на 1
        new_area = length + 1 - a
        last_but_one_area = length - 1
        if new_area > last_but_one_area:
            self.areas[length] = {
                "boss": dungeon_data["boss"],
                "rewards": dungeon_data["rewards"],
            }
        else:
            self.insert_boss_area(
                last_but_one_area,
                new_area,
                self.areas,
                dungeon_data["boss"],
                dungeon_data["rewards"]
            )

    def insert_boss_area(
        self,
        current_area_key: int,
        new_area_key: int,
        areas: dict,
        boss: Creature,
        rewards: str
    ) -> None:
        """Рекурсивный метод для сдвигания номеров областей и вставки области с боссом
        :param current_area_key: last but one area ordinal number to work with
        :param new_area_key: ordinal number of a new area with boss and reward
        :param areas: dictionary with areas {int: [area content]}, starts with 1
        :param boss: boss creature object (Creature)
        :param rewards: reward str
        """
        # Base case
        if current_area_key == new_area_key:
            areas[current_area_key + 1] = areas[current_area_key]
            areas[current_area_key] = {"boss": boss, "rewards": rewards[0]}
            return
        # Recursive case
        areas[current_area_key + 1] = areas[current_area_key]
        self.insert_boss_area(
            current_area_key - 1,
            new_area_key,
            areas,
            boss,
            rewards
        )

    def add_reward(self, dungeon_data: dict, iteration: int) -> None:
        """
        Добавляем награду в случайную комнату.

        Для 1-й итерации - в 25% последних комнат (не более 2-х последних).
        Для 2-й итерации - в одну из двух центральных комнат.
        :param dungeon_data: Контент подземелья, сгенерированный функциями из helpers
        :param iteration: Порядковый номер добавляемой награды (с конца подземелья)
        """
        length = dungeon_data["area_limit"]
        if iteration == 1:
            reward_index = 0  # Индекс в dungeon_data['reward']
            a = math.floor(length * 0.25 + 0.5)  # Для округления половины до верхнего значения
            if a > 2:
                a = 2
            r = random.randint(1, a)
            r_key = length + 1 - r
        elif iteration == 2:
            if len(dungeon_data["rewards"]) < 2:
                return
            reward_index = 1
            # Выбираем случайно одну из двух центральных комнат
            # или между центральной и центральной + 1
            middle_key = math.ceil(length / 2)
            r_key = random.randint(middle_key, middle_key + 1)
        self.areas[r_key]["reward"] = dungeon_data["rewards"][reward_index]

    def get_areas(self):
        return self.areas
