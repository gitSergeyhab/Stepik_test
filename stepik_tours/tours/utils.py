from random import shuffle
from .data import *


# рандомные тэги и отели
def random_tags_hotels(list_values, num):
    ran = list(range(1, len(list_values)))
    shuffle(ran)
    return [list_values[lv] for lv in range(len(list_values)) if lv in ran[:num]]


# расчет минимальной и максимальной цены/дней
def minimax(tours_from_one_city, category):
    some_min, some_max = 1_000_000_000, -1
    for i in tours_from_one_city.values():
        if i[category] > some_max:
            some_max = i[category]
        if i[category] < some_min:
            some_min = i[category]
    return (some_min, some_max)


# dict туров для конкретного города !!
def fun_one_city_tours(slug):
    one_city_tours = {}
    for number, data in tours.items():
        if data["departure"] == slug:
            one_city_tours[number] = data
    return one_city_tours

