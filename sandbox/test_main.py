import unittest
from main import binary_search, bubble_sort

class TestAlgorithms(unittest.TestCase):

    def test_binary_search(self):
        # Element found in the middle
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        # Element found at the beginning
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)
        # Element found at the end
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)
        # Element not found
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0), -1)
        # Empty array
        self.assertEqual(binary_search([], 1), -1)
        # Single element array (found)
        self.assertEqual(binary_search([1], 1), 0)
        # Single element array (not found)
        self.assertEqual(binary_search([1], 2), -1)

    def test_bubble_sort(self):
        # Already sorted array
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        # Reverse sorted array
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        # Random array with duplicates
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 25, 90]), [11, 12, 22, 25, 25, 34, 64, 90])
        # Empty array
        self.assertEqual(bubble_sort([]), [])
        # Single element array
        self.assertEqual(bubble_sort([1]), [1])
        # Array with negative numbers
        self.assertEqual(bubble_sort([-5, 3, -1, 0, 2]), [-5, -1, 0, 2, 3])

if __name__ == "__main__":
    unittest.main()
