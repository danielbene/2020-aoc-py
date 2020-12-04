from unittest import TestCase


class Test(TestCase):
    def test_find_entry_pair(self):
        from src.day1_1 import find_entry_pair
        input_list = [1721, 979, 366, 299, 675, 1456]
        correct_answer = 514579
        self.assertTrue(find_entry_pair(input_list) == correct_answer)

    def test_find_entry_triplet(self):
        from src.day1_2 import find_entry_triplet
        input_list = [1721, 979, 366, 299, 675, 1456]
        correct_answer = 241861950
        self.assertTrue(find_entry_triplet(input_list) == correct_answer)

    def test_sum_of_correct_passwords(self):
        from src.day2_1 import sum_of_correct_passwords
        input_list = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        correct_answer = 2
        self.assertTrue(sum_of_correct_passwords(input_list) == correct_answer)

    def test_sum_of_correct_passwords_by_pos(self):
        from src.day2_2 import sum_of_correct_passwords_by_pos
        input_list = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        correct_answer = 1
        self.assertTrue(sum_of_correct_passwords_by_pos(input_list) == correct_answer)

    def test_sum_of_trees_in_the_slope(self):
        from src.day3_1 import sum_of_trees_in_the_slope
        input_list = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#']
        correct_answer = 7
        self.assertTrue(sum_of_trees_in_the_slope(input_list) == correct_answer)

    def test_multiplied_tree_probabilities(self):
        from src.day3_2 import multiplied_tree_probabilities
        input_list = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#']
        correct_answer = 336
        self.assertTrue(multiplied_tree_probabilities(input_list) == correct_answer)

    def test_num_of_valid_passports(self):
        from src.day4_1 import num_of_valid_passports
        input_list = [
            'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n',
            'byr:1937 iyr:2017 cid:147 hgt:183cm\n',
            '\n',
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n',
            'hcl:#cfa07d byr:1929\n',
            '\n',
            'hcl:#ae17e1 iyr:2013\n',
            'eyr:2024\n',
            'ecl:brn pid:760753108 byr:1931\n',
            'hgt:179cm\n',
            '\n',
            'hcl:#cfa07d eyr:2025 pid:166559648\n',
            'iyr:2011 ecl:brn hgt:59in\n',
            '\n']
        correct_answer = 2
        self.assertTrue(num_of_valid_passports(input_list) == correct_answer)
