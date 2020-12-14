from util import iohandler
from functools import reduce

# --- solution ---


def init(input_file):
    return [str(row.strip()) for row in input_file][1]


# based on Chinese Remainder Theory - i dont like math theories :,)
# https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8
def get_earliest_matching_departs(data_list):
    bus_ids = [str(bus_id) for bus_id in data_list.split(',')]
    ids_by_delay = dict()
    for index in range(len(bus_ids)):
        bus_id = bus_ids[index]
        if bus_id != 'x' and index != 0:
            ids_by_delay.update({int(bus_id): int(bus_id) - index})
        elif index == 0:
            ids_by_delay.update({int(bus_id): 0})

    return chinese_remainder(ids_by_delay.keys(), ids_by_delay.values())


def chinese_remainder(n, a):  # n - mod (bus_id), a - remainder (ts delay)
    sum_val = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum_val += a_i * mul_inv(p, n_i) * p
    return sum_val % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1

    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0

    return x1


# --- solution ---

if __name__ == '__main__':
    input_ids = init(iohandler.begin(__file__))
    iohandler.end(str(get_earliest_matching_departs(input_ids)))
