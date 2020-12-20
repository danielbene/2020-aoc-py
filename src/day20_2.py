from util import iohandler
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

    terrain.tiles[0].print_tile()
    terrain.tiles[0].remove_borders()
    print('---')
    terrain.tiles[0].print_tile()
    return ''


def mirror(text):
    return text[::-1]


class Terrain:
    def __init__(self):
        self.tiles = list()
        self.terrain_tile = list()

    def build_terrain(self):
        # contrariwise of part1 matrix positions is must have here
        pass


class Tile:
    is_corner = False

    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.rows = list()

    def remove_borders(self):
        del self.rows[0]
        del self.rows[len(self.rows) - 1]
        self.rows = [row[1:len(row) - 1] for row in self.rows]

    def print_tile(self):
        for row in self.rows:
            print(row)


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(get_monsterlessness(iohandler.begin(__file__))))
