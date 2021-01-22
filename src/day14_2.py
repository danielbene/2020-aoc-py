from util import iohandler
from itertools import combinations

# --- solution ---


def sum_of_memory_with_floating_bits(input_file):
    memory = dict()
    current_mask = ''
    memory_sum = 0

    for line in input_file:
        record = line.strip().split(' = ')

        if record[0] == 'mask':
            current_mask = record[1]
        else:
            memory_index = record[0][4:-1]
            bin_address = "{0:036b}".format(int(memory_index))

            for address in str_mask(bin_address, current_mask):
                memory.update({address: record[1]})

    for mem in memory.values():
        memory_sum += int(mem)

    return memory_sum


# TODO: optimize this
def str_mask(value, mask):
    masked = ''
    floating_bit_cnt = 0
    floating_addresses = set()

    for index in range(36):
        bit = mask[index]
        if bit == '0':
            masked += value[index]
        elif bit == '1':
            masked += '1'
        elif bit == 'X':
            masked += 'X'
            floating_bit_cnt += 1

    if floating_bit_cnt != 0:
        comb_array = []
        for _ in range(floating_bit_cnt):
            comb_array.append(1)
            comb_array.append(0)

        combs = set(combinations(comb_array, floating_bit_cnt))

        for comb in combs:
            tmp = masked
            for c in comb:
                tmp = tmp.replace('X', str(c), 1)
            floating_addresses.add(int(tmp, 2))

    return floating_addresses


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(
        sum_of_memory_with_floating_bits(iohandler.begin(__file__))))
