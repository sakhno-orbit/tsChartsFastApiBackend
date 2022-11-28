from random import randint
from typing import List
FAKEDATA_STEPS = 15

NAME_A = 'Anika'
NAME_B = 'Tom'
NAME_C = 'Nikki'

NAMES = [NAME_A, NAME_B, NAME_C]


def gen_fake(header, page, max_val=100, steps=FAKEDATA_STEPS):
    year = 2022 - steps
    chart_labels: List[str] = []
    data_a = []
    data_b = []
    data_c = []

    for x in range(steps):
        chart_labels.append("%s" % year)

        data_a.append(randint(int(randint(30, 50) * max_val / 100), max_val))
        data_b.append(randint(int(randint(30, 50) * max_val / 100), max_val))
        data_c.append(randint(int(randint(30, 50) * max_val / 100), max_val))
        year += 1

    datasets = [
        {"data": data_a, 'label': NAME_A},
        {"data": data_b, 'label': NAME_B},
        {"data": data_c, 'label': NAME_C},
    ]

    return {
        "header": header,
        "page": page,
        "datasets": datasets,
        "labels": chart_labels
    }


FAKE_DATA = [
    gen_fake("Ice creams per year", page=1, max_val=100),
    gen_fake("Steps per year", page=2, max_val=1000000),
    gen_fake("Sold per year", page=3, max_val=100),
    gen_fake("Bought pencils per year", page=4, max_val=100),
    gen_fake("Sold cars per year", page=5, max_val=300),
    gen_fake("Coffee cups per year", page=6, max_val=900),
    gen_fake("Miles per year", page=7, max_val=30000),
    gen_fake("Spend per year", page=8, max_val=100000),
    gen_fake("Visited cities", page=9, max_val=10),
    gen_fake("Spend per year", page=10, max_val=100),
]

