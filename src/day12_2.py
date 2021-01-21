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
        rotate_x_times(int(value/90), 'cw')
    elif action == 'R':
        rotate_x_times(int(value/90), 'ccw')
    elif action == 'F':
        position[0] += waypoint[0] * value
        position[1] += waypoint[1] * value


def rotate_x_times(counter, direction):
    d = 0 if direction == 'cw' else 1
    for _ in range(counter):
        waypoint[d] *= -1
        waypoint[0], waypoint[1] = waypoint[1], waypoint[0]


# NOP - refact later
class Directions(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(get_manhattan_distance_with_waypoint(iohandler.begin(__file__))))
