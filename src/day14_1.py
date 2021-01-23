from util import iohandler
# import numpy as np  # this is where I found out about numpy efficiency o_O

# --- solution ---

# NOTE: VSCode runtimes looks slower than PyCharm's

# for reference only
# str type is only 1 char | U36 = 36 unicode char
# memory = np.zeros(36, dtype='U36')


def sum_of_memory(input_file):
    memory = dict()
    current_mask = ''

    for cmd, value in [line.strip().split(' = ') for line in input_file]:
        if cmd == 'mask':
            current_mask = value
        else:
            mem_value = bin(int(value))[2:].zfill(36)
            memory.update({cmd[3:-1]: int(str_mask(mem_value, current_mask), 2)})

    return sum(memory.values())


def str_mask(value, mask):
    masked = ''
    for index in range(len(mask)):
        masked += value[index] if mask[index] == 'X' else mask[index]

    return masked


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(sum_of_memory(iohandler.begin(__file__))))
