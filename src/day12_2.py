from util import iohandler
from enum import Enum

# --- solution ---

position = [0, 0]  # basic graph dimensions - north, east are pos, south, and west are neg
waypoint = [1, 10]
facing = 2
dir_vectors = {
    '1': [1, 0],
    '2': [0, 1],
    '3': [-1, 0],
    '4': [0, -1]
}


def get_manhattan_distance_with_waypoint(input_actions):
    for action in input_actions:
        do_some_action(action.strip())
        print(position)
        print(waypoint)

    return abs(position[0]) + abs(position[1])


def do_some_action(act):
    global facing
    action = act[0]
    value = int(act[1:])

    if action == 'N':
        waypoint[0] += value
    elif action == 'S':
        waypoint[0] -= value
    elif action == 'E':
        waypoint[1] += value
    elif action == 'W':
        waypoint[1] -= value
    elif action == 'L':
        turns = value / 90
        if (facing == 1 and turns > 2) or (facing == 2 and turns < 3) or\
                (facing == 3 and turns > 2) or (facing == 4 and turns < 3):
            waypoint[0] *= -1
            waypoint[1] *= -1

        if turns % 2 != 0:
            waypoint[0], waypoint[1] = waypoint[1], waypoint[0]

        facing -= int(turns)
        if facing < 1:
            facing += 4

    elif action == 'R':
        turns = value / 90
        if (facing == 1 and turns > 2) or (facing == 2 and turns < 3) or \
                (facing == 3 and turns > 2) or (facing == 4 and turns < 3):
            waypoint[0] *= -1
            waypoint[1] *= -1

        if turns % 2 != 0:
            waypoint[0], waypoint[1] = waypoint[1], waypoint[0]

        facing += int(turns)
        if facing > 4:
            facing -= 4

    elif action == 'F':
        position[0] += waypoint[0] * value
        position[1] += waypoint[1] * value


# NOP - refact later
class Directions(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(get_manhattan_distance_with_waypoint(iohandler.begin(__file__))))
