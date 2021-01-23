from util import iohandler
import numpy as np

# --- solution ---

req_position = 30000000


def init(input_file):
    return big_memory_game_position_value(input_file.readline().strip())


def big_memory_game_position_value(input_nums):
    nums = np.array([int(num) for num in input_nums.split(',')])
    current_turn = len(nums) + 1
    prog = 0

    while current_turn < req_position + 1:
        occurencies = np.where(nums == nums[current_turn - 2])[0]
        add = 0 if len(occurencies) == 1 else occurencies[-1] - occurencies[-2]
        nums = np.append(nums, add)

        current_turn += 1

        # this probably cannot be calculated in reasonable time
        # find math solution
        if current_turn % 300000 == 0:
            prog += 1
            print(prog)

    return nums[req_position - 1]


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(init(iohandler.begin(__file__))))
