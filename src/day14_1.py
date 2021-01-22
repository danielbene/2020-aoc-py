from util import iohandler
# import numpy as np  # this is where I found out about numpy o_O

# --- solution ---

# NOTE: VSCode runtimes looks slower than PyCharm's
# for reference only
# str type is only 1 char | U36 = 36 unicode char
# memory = np.zeros(36, dtype='U36')


def sum_of_memory(input_file):
    memory = dict()
    current_mask = ''
    memory_sum = 0

    for line in input_file:
        record = line.strip().split(' = ')
        if record[0] == 'mask':
            current_mask = record[1]
        else:
            # really nice way to format and padd to binary
            mem_value = "{0:036b}".format(int(record[1]))
            memory.update({record[0][3:-1]: str_mask(mem_value, current_mask)})

    for mem in memory.values():
        memory_sum += int(mem, 2)

    return memory_sum


def str_mask(value, mask):
    masked = ''
    for index in range(len(mask)):
        masked += value[index] if mask[index] == 'X' else mask[index]

    return masked


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(sum_of_memory(iohandler.begin(__file__))))
