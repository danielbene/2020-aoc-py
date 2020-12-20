from util import iohandler
import re

# --- solution ---


def multiplied_corner_tiles(input_file):
    data_list = [str(row.strip()) for row in input_file]
    title = re.compile("^Tile [0-9]{4}:$")
    tiles_obj = Tiles()

    tile = None
    for row in data_list:
        if title.match(row):
            if tile is not None:
                tiles_obj.tiles.append(tile)
            tile = Tile(int(row.split(' ')[1][:-1]))
        elif row != '':
            tile.rows.append(row)

    tiles_obj.find_corners()
    return ''


class Tiles:
    left_sides = list()
    right_sides = list()
    top_sides = list()
    bottom_sides = list()

    def __init__(self):
        self.tiles = list()

    def collect_sides(self):
        for tile in self.tiles:
            self.left_sides.append(tile.get_left_side())
            self.right_sides.append(tile.get_right_side())
            self.top_sides.append(tile.get_top())
            self.bottom_sides.append(tile.get_bottom())

    def find_corners(self):
        self.collect_sides()
        print(self.left_sides)
        print(self.right_sides)
        for tile in self.tiles:
            unmatched_sides = 0
            if self.left_sides.count(tile.get_right_side()) == 0:
                unmatched_sides += 1
            if self.right_sides.count(tile.get_left_side()) == 0:
                unmatched_sides += 1
            if self.top_sides.count(tile.get_bottom()) == 0:
                unmatched_sides += 1
            if self.bottom_sides.count(tile.get_top()) == 0:
                unmatched_sides += 1

            if unmatched_sides > 1:
                print(tile.tile_id)
                print(unmatched_sides)
                tile.is_corner = True


class Tile:
    is_corner = False

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
        return self.rows[len(self.rows)-1]

    def print_tile(self):
        for row in self.rows:
            print(row)


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(multiplied_corner_tiles(iohandler.begin(__file__))))
