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

    def test_positive_group_answers(self):
        from src.day6_2 import positive_group_answers
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
        correct_answer = 6
        self.assertTrue(positive_group_answers(input_list) == correct_answer)

    def test_containing_bag_num(self):
        from src.day7_1 import containing_bag_num
        input_list = [
            'light red bags contain 1 bright white bag, 2 muted yellow bags.\n',
            'dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n',
            'bright white bags contain 1 shiny gold bag.\n',
            'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n',
            'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n',
            'dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n',
            'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n',
            'faded blue bags contain no other bags.\n',
            'dotted black bags contain no other bags.\n']
        correct_answer = 4
        self.assertEqual(containing_bag_num(input_list), correct_answer)

    def test_contained_bag_num(self):
        from src.day7_2 import contained_bag_num
        input_1 = [
            'light red bags contain 1 bright white bag, 2 muted yellow bags.\n',
            'dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n',
            'bright white bags contain 1 shiny gold bag.\n',
            'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n',
            'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n',
            'dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n',
            'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n',
            'faded blue bags contain no other bags.\n',
            'dotted black bags contain no other bags.\n']
        input_2 = [
            'shiny gold bags contain 2 dark red bags.\n',
            'dark red bags contain 2 dark orange bags.\n',
            'dark orange bags contain 2 dark yellow bags.\n',
            'dark yellow bags contain 2 dark green bags.\n',
            'dark green bags contain 2 dark blue bags.\n',
            'dark blue bags contain 2 dark violet bags.\n',
            'dark violet bags contain no other bags.\n']
        with self.subTest():
            self.assertEqual(contained_bag_num(input_1), 32)
        with self.subTest():
            self.assertEqual(contained_bag_num(input_2), 126)

    def test_get_accumulator_value(self):
        from src.day8_1 import get_accumulator_value
        input_list = [
            'nop +0',
            'acc +1',
            'jmp +4',
            'acc +3',
            'jmp -3',
            'acc -99',
            'acc +1',
            'jmp -4',
            'acc +6']
        correct_answer = 5
        self.assertTrue(get_accumulator_value(input_list) == correct_answer)

    def test_get_fixed_accumulator_value(self):
        from src.day8_2 import get_fixed_accumulator_value
        input_list = [
            'nop +0',
            'acc +1',
            'jmp +4',
            'acc +3',
            'jmp -3',
            'acc -99',
            'acc +1',
            'jmp -4',
            'acc +6']
        correct_answer = 8
        self.assertTrue(get_fixed_accumulator_value(input_list) == correct_answer)

    def test_get_invalid_record(self):
        from src.day9_1 import get_invalid_record
        input_list = [
            '35\n',
            '20\n',
            '15\n',
            '25\n',
            '47\n',
            '40\n',
            '62\n',
            '55\n',
            '65\n',
            '95\n',
            '102\n',
            '117\n',
            '150\n',
            '182\n',
            '127\n',
            '219\n',
            '299\n',
            '277\n',
            '309\n',
            '576\n']
        correct_answer = 127
        preamble_size = 5
        self.assertTrue(get_invalid_record(input_list, preamble_size) == correct_answer)

    def test_sum_of_contiguous_range_edges(self):
        from src.day9_2 import sum_of_contiguous_range_edges
        input_list = [
            '35\n',
            '20\n',
            '15\n',
            '25\n',
            '47\n',
            '40\n',
            '62\n',
            '55\n',
            '65\n',
            '95\n',
            '102\n',
            '117\n',
            '150\n',
            '182\n',
            '127\n',
            '219\n',
            '299\n',
            '277\n',
            '309\n',
            '576\n']
        correct_answer = 62
        preamble_size = 5
        self.assertTrue(sum_of_contiguous_range_edges(input_list, preamble_size) == correct_answer)

    def test_get_multiplied_joltage_differences(self):
        from src.day10_1 import get_multiplied_joltage_differences
        input1 = [
            '16\n',
            '10\n',
            '15\n',
            '5\n',
            '1\n',
            '11\n',
            '7\n',
            '19\n',
            '6\n',
            '12\n',
            '4\n']
        input2 = [
            '28\n',
            '33\n',
            '18\n',
            '42\n',
            '31\n',
            '14\n',
            '46\n',
            '20\n',
            '48\n',
            '47\n',
            '24\n',
            '23\n',
            '49\n',
            '45\n',
            '19\n',
            '38\n',
            '39\n',
            '11\n',
            '1\n',
            '32\n',
            '25\n',
            '35\n',
            '8\n',
            '17\n',
            '7\n',
            '9\n',
            '4\n',
            '2\n',
            '34\n',
            '10\n',
            '3\n']
        with self.subTest():
            self.assertEqual(get_multiplied_joltage_differences(input1), 7 * 5)
        with self.subTest():
            self.assertEqual(get_multiplied_joltage_differences(input2), 22 * 10)

    def test_get_adapter_arrangement_count(self):
        from src.day10_2 import get_adapter_arrangement_count
        input1 = [
            '16\n',
            '10\n',
            '15\n',
            '5\n',
            '1\n',
            '11\n',
            '7\n',
            '19\n',
            '6\n',
            '12\n',
            '4\n']
        input2 = [
            '28\n',
            '33\n',
            '18\n',
            '42\n',
            '31\n',
            '14\n',
            '46\n',
            '20\n',
            '48\n',
            '47\n',
            '24\n',
            '23\n',
            '49\n',
            '45\n',
            '19\n',
            '38\n',
            '39\n',
            '11\n',
            '1\n',
            '32\n',
            '25\n',
            '35\n',
            '8\n',
            '17\n',
            '7\n',
            '9\n',
            '4\n',
            '2\n',
            '34\n',
            '10\n',
            '3\n']
        with self.subTest():
            self.assertEqual(get_adapter_arrangement_count(input1), 8)
        with self.subTest():
            self.assertEqual(get_adapter_arrangement_count(input2), 19208)

    def test_get_occupied_seats(self):
        from src.day11_1 import get_occupied_seats
        input_list = [
            'L.LL.LL.LL\n',
            'LLLLLLL.LL\n',
            'L.L.L..L..\n',
            'LLLL.LL.LL\n',
            'L.LL.LL.LL\n',
            'L.LLLLL.LL\n',
            '..L.L.....\n',
            'LLLLLLLLLL\n',
            'L.LLLLLL.L\n',
            'L.LLLLL.LL\n']
        correct_answer = 37
        self.assertTrue(get_occupied_seats(input_list) == correct_answer)

    def test_get_occupied_seats_by_view(self):
        from src.day11_2 import get_occupied_seats_by_view
        input_list = [
            'L.LL.LL.LL\n',
            'LLLLLLL.LL\n',
            'L.L.L..L..\n',
            'LLLL.LL.LL\n',
            'L.LL.LL.LL\n',
            'L.LLLLL.LL\n',
            '..L.L.....\n',
            'LLLLLLLLLL\n',
            'L.LLLLLL.L\n',
            'L.LLLLL.LL\n']
        correct_answer = 26
        self.assertTrue(get_occupied_seats_by_view(input_list) == correct_answer)

    def test_get_manhattan_distance(self):
        from src.day12_1 import get_manhattan_distance
        input_list = [
            'F10\n',
            'N3\n',
            'F7\n',
            'R90\n',
            'F11\n']
        self.assertEqual(get_manhattan_distance(input_list), 25)

    def test_get_earliest_bus_id(self):
        from src.day13_1 import get_earliest_bus_id
        input_list = [
            '939\n',
            '7,13,x,x,59,x,31,19\n']
        correct_answer = 295
        self.assertTrue(get_earliest_bus_id(input_list) == correct_answer)

    def test_get_earliest_matching_departs(self):
        from src.day13_2 import get_earliest_matching_departs
        with self.subTest():
            self.assertEqual(get_earliest_matching_departs('7,13,x,x,59,x,31,19'), 1068781)
        with self.subTest():
            self.assertEqual(get_earliest_matching_departs('17,x,13,19'), 3417)
        with self.subTest():
            self.assertEqual(get_earliest_matching_departs('67,7,59,61'), 754018)
        with self.subTest():
            self.assertEqual(get_earliest_matching_departs('67,x,7,59,61'), 779210)
        with self.subTest():
            self.assertEqual(get_earliest_matching_departs('67,7,x,59,61'), 1261476)
        with self.subTest():
            self.assertEqual(get_earliest_matching_departs('1789,37,47,1889'), 1202161486)
