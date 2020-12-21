from util import iohandler
from math import sqrt
import re

# --- solution ---


def get_monsterlessness(input_file):
    data_list = [str(row.strip()) for row in input_file]
    terrain = Terrain()

    tile = None
    for row in data_list:
        if re.match(r"^Tile [0-9]{4}:$", row):
            tile = Tile(int(row.split(' ')[1][:-1]))
        elif row != '':
            tile.rows.append(row)
        else:
            # double nl at eof is important
            terrain.tiles.append(tile)

    terrain.get_terrain_width()
    return ''


def mirror_sting(text):
    return text[::-1]


def rotate_matrix(matrix):
    return zip(*matrix[::-1])


class Terrain:
    def __init__(self):
        self.tiles = list()
        self.assembled = list()
        self.dimensions = 0

    def get_terrain_width(self):
        self.dimensions = int(sqrt(len(self.tiles)))

    def rubic(self):
        pass


class Tile:
    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.rows = list()

    def get_left_side(self):
        ret = ''
        for row in self.rows:
            ret += row[0]
        return ret

    def get_right_side(self):
        ret = ''
        for row in self.rows:
            ret += row[len(row) - 1]
        return ret

    def get_top(self):
        return self.rows[0]

    def get_bottom(self):
        return self.rows[len(self.rows) - 1]

    def rotate_clockwise(self):
        self.rows = rotate_matrix(self.rows)

    def print_tile(self):
        for row in self.rows:
            print(row)


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(get_monsterlessness(iohandler.begin(__file__))))
