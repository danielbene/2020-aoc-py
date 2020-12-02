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
