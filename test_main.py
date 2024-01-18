import unittest
from main import checklist
class TestChecklistFunction(unittest.TestCase):

    def test_valid_list(self):
        # Test when the length of the list is a multiple of 10
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result_list = checklist(my_list)
        self.assertEqual(len(result_list) % 10, 0)

    def test_invalid_list_length(self):
        # Test when the length of the list is not a multiple of 10
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        with self.assertRaises(ValueError):
            checklist(my_list)

    def test_removal_of_elements(self):
        # Test if elements at positions that are multiples of 2 or 3 are removed
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        result_list = checklist(my_list)
        self.assertNotIn(2, result_list)
        self.assertNotIn(3, result_list)
        self.assertNotIn(4, result_list)
        self.assertNotIn(6, result_list)

    def test_empty_list(self):
        # Test when an empty list is provided
        my_list = []
        result_list = checklist(my_list)
        self.assertEqual(result_list, [])

if __name__ == '__main__':
    unittest.main()
