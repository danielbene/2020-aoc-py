from util import iohandler
import re

# --- solution ---


def multiplied_corner_tiles(input_file):
    data_list = [str(row.strip()) for row in input_file]
    terrain = Terrain()

    tile = None
    for row in data_list:
        if re.match(r"^Tile [0-9]{4}:$", row):
            tile = Tile(int(row.split(' ')[1][:-1]))
        elif row != '':
            tile.rows.append(row)
        else:
            terrain.tiles.append(tile)

    return terrain.find_corners()


def mirror(text):
    return text[::-1]


# not my cleanest solution, but can be extended for part2 if needed
class Terrain:
    left_sides = list()
    right_sides = list()
    top_sides = list()
    bottom_sides = list()
    all_sides_with_rotation = list()

    def __init__(self):
        self.tiles = list()

    def collect_sides(self):
        for tile in self.tiles:
            self.left_sides.append(tile.get_left_side())
            self.right_sides.append(tile.get_right_side())
            self.top_sides.append(tile.get_top())
            self.bottom_sides.append(tile.get_bottom())

        # extend takes out the list elements, and adds them, while append will put the list object in
        self.all_sides_with_rotation.extend(self.left_sides + self.right_sides
                                            + self.top_sides + self.bottom_sides)
        self.all_sides_with_rotation.extend(
            [mirror(side) for side in self.all_sides_with_rotation])

    def find_corners(self):
        multiplied_ids = 1
        self.collect_sides()
        for tile in self.tiles:
            unmatched_sides = 0
            if self.all_sides_with_rotation.count(tile.get_left_side()) == 1:
                unmatched_sides += 1
            if self.all_sides_with_rotation.count(tile.get_right_side()) == 1:
                unmatched_sides += 1
            if self.all_sides_with_rotation.count(tile.get_top()) == 1:
                unmatched_sides += 1
            if self.all_sides_with_rotation.count(tile.get_bottom()) == 1:
                unmatched_sides += 1

            if unmatched_sides > 1:
                multiplied_ids *= tile.tile_id
                tile.is_corner = True

        return multiplied_ids


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
