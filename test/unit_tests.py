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
            'iyr:2011 ecl:brn hgt:59in\n']
        correct_answer = 2
        self.assertTrue(num_of_valid_passports(input_list) == correct_answer)

    def test_num_of_valid_passports_by_rules(self):
        from src.day4_2 import num_of_valid_passports_by_rules
        invalid_input_list = [
            'eyr:1972 cid:100\n',
            'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926\n',
            '\n',
            'iyr:2019\n',
            'hcl:#602927 eyr:1967 hgt:170cm\n',
            'ecl:grn pid:012533040 byr:1946\n',
            '\n',
            'hcl:dab227 iyr:2012\n',
            'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277\n',
            '\n',
            'hgt:59cm ecl:zzz\n',
            'eyr:2038 hcl:74454a iyr:2023\n',
            'pid:3556412378 byr:2007\n']
        valid_input_list = [
            'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\n',
            'hcl:#623a2f\n',
            '\n',
            'eyr:2029 ecl:blu cid:129 byr:1989\n',
            'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm\n',
            '\n',
            'hcl:#888785\n',
            'hgt:164cm byr:2001 iyr:2015 cid:88\n',
            'pid:545766238 ecl:hzl\n',
            'eyr:2022\n',
            '\n',
            'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719\n']
        with self.subTest():
            self.assertEqual(num_of_valid_passports_by_rules(invalid_input_list), 0)
        with self.subTest():
            self.assertEqual(num_of_valid_passports_by_rules(valid_input_list), 4)

    def test_calculate_binary_seat_partition(self):
        from src.day5_1 import calculate_binary_seat_partition
        values = [['FBFBBFFRLR', 357], ['BFFFBBFRRR', 567], ['FFFBBBFRRR', 119], ['BBFFBBFRLL', 820]]
        for seat in values:
            with self.subTest():
                self.assertEqual(calculate_binary_seat_partition(seat[0]), seat[1])

    def test_positive_answer_count(self):
        from src.day6_1 import positive_answer_count
        input_list = [
            'abc\n',
            '\n',
            'a\n',
            'b\n',
            'c\n',
            '\n',
            'ab\n',
            'ac\n',
            '\n',
            'a\n',
            'a\n',
            'a\n',
            'a\n',
            '\n',
            'b\n']
        correct_answer = 11
        self.assertTrue(positive_answer_count(input_list) == correct_answer)
