from random import shuffle
from .data import *


# рандомные тэги и отели
def random_tegs_hotels(list_val, num):
    ran = list(range(1, len(list_val)))
    shuffle(ran)
    return [list_val[lv] for lv in range(len(list_val)) if lv in ran[:num]]


# расчет минимальной и максимальной цены/дней
def minimax(tours_from_one_city, category):
    minc, maxc = 1_000_000_000, -1
    for i in tours_from_one_city.values():
        if i[category] > maxc:
            maxc = i[category]
        if i[category] < minc:
            minc = i[category]
    return (minc, maxc)


# dict туров для конкретного города !!
def fun_tours_x(rp):
    tours_x = {}
    for tk, tv in tours.items():
        if tv["departure"] == rp:
            tours_x[tk] = tv
    return tours_x
#
# # !!
def bad_re(rp):
    import re
    return re.findall(pattern=r"\/[^\/]+\/$", string=rp)[-1][1:-1]
