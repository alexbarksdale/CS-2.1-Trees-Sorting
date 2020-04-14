#!python

from sorting import random_ints
from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort
from sorting_recursive import split_sort_merge, merge_sort, quick_sort, merge, partition
from sorting_integer import counting_sort, bucket_sort
import unittest


class IsSortedTest(unittest.TestCase):
    def test_is_sorted_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert is_sorted([]) is True  # Empty lists are vacuously sorted
        assert is_sorted([3]) is True  # Single item is trivially sorted
        assert is_sorted([3, 3]) is True  # Duplicate items are in order
        assert is_sorted([3, 5]) is True
        assert is_sorted([3, 5, 7]) is True
        assert is_sorted([20, 50, 51, 100, 102]) is True
        assert is_sorted([-40, -1, 0, 70, 90]) is True
        assert is_sorted([-120, -50, -20, 25, 42]) is True

    def test_is_sorted_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        assert is_sorted([5, 3]) is False
        assert is_sorted([3, 5, 3]) is False
        assert is_sorted([7, 5, 3]) is False
        assert is_sorted([20, 50, 49, 100, 102]) is False
        assert is_sorted([-40, 1, 0, 70, 90]) is False
        assert is_sorted([-120, -50, -60, 25, 42]) is False

    def test_is_sorted_on_sorted_strings(self):
        # Positive test cases (examples) with lists of sorted strings
        assert is_sorted(['A']) is True  # Single item is trivially sorted
        assert is_sorted(['A', 'A']) is True  # Duplicate items are in order
        assert is_sorted(['A', 'B']) is True
        assert is_sorted(['A', 'B', 'C']) is True
        assert is_sorted(['C', 'F', 'H']) is True
        assert is_sorted(['N', 'O', 'Y', 'Z']) is True
        assert is_sorted(['K', 'P', 'Q', 'U']) is True

    def test_is_sorted_on_unsorted_strings(self):
        # Negative test cases (counterexamples) with lists of unsorted strings
        assert is_sorted(['B', 'A']) is False
        assert is_sorted(['A', 'B', 'A']) is False
        assert is_sorted(['C', 'B', 'A']) is False
        assert is_sorted(['Z', 'F', 'H']) is False
        assert is_sorted(['N', 'Y', 'Q', 'Z']) is False
        assert is_sorted(['R', 'G', 'Q', 'A']) is False

    def test_is_sorted_on_sorted_tuples(self):
        # Positive test cases (examples) with lists of sorted tuples
        assert is_sorted([(3, 5)]) is True  # Single item
        assert is_sorted([(3, 'A')]) is True  # Single item
        assert is_sorted([('A', 3)]) is True  # Single item
        assert is_sorted([('A', 'B')]) is True  # Single item
        assert is_sorted([(3, 5), (3, 5)]) is True  # Duplicate items
        assert is_sorted([(3, 'A'), (3, 'A')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('A', 3)]) is True  # Duplicate items
        assert is_sorted([('A', 'B'), ('A', 'B')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('B', 5)]) is True  # Both items sorted
        assert is_sorted([('A', 3), ('B', 3)]) is True  # First item sorted
        assert is_sorted([('A', 3), ('A', 5)]) is True  # Second item sorted
        assert is_sorted([(3, 'A'), (5, 'B')]) is True  # Both items sorted
        assert is_sorted([(3, 'A'), (5, 'A')]) is True  # First item sorted
        assert is_sorted([(3, 'A'), (3, 'B')]) is True  # Second item sorted
        assert is_sorted([(0, 'Z'), (2, 'H')]) is True
        assert is_sorted([(3, 'W'), (5, 'G')]) is True
        assert is_sorted([(1, 'O'), (2, 'U')]) is True

    def test_is_sorted_on_unsorted_tuples(self):
        # Negative test cases (counterexamples) with lists of unsorted tuples
        assert is_sorted([(5, 'B'), (3, 'A')]) is False  # Both items unsorted
        assert is_sorted([(5, 'A'), (3, 'B')]) is False  # First item unsorted
        assert is_sorted([(3, 'B'), (3, 'A')]) is False  # Second item unsorted
        assert is_sorted([('B', 5), ('A', 3)]) is False  # Both items unsorted
        assert is_sorted([('B', 3), ('A', 5)]) is False  # First item unsorted
        assert is_sorted([('A', 5), ('A', 3)]) is False  # Second item unsorted
        assert is_sorted([(12, 'W'), (5, 'I')]) is False
        assert is_sorted([(8, 'A'), (4, 'E')]) is False
        assert is_sorted([(6, 'T'), (6, 'F')]) is False


class IntegerSortTest(unittest.TestCase):

    def test_sort_on_empty_list(self):
        items = []
        sort(items)
        assert items == []  # List should not be changed

    def test_sort_on_small_lists_of_integers(self):
        items1 = [3]
        sort(items1)
        assert items1 == [3]  # List should not be changed
        items2 = [5, 3]
        sort(items2)
        assert items2 == [3, 5]  # List should be in sorted order
        items3 = [5, 7, 3]
        sort(items3)
        assert items3 == [3, 5, 7]
        items4 = [65, 24, 90, -5]
        sort(items4)
        assert items4 == [-5, 24, 65, 90]
        items5 = [123, 302, -120, 5]
        sort(items5)
        assert items5 == [-120, 5, 123, 302]
        items6 = [102, -50, 90, -24]
        sort(items6)
        assert items6 == [-50, -24, 90, 102]

    def test_sort_on_small_lists_of_integers_with_duplicates(self):
        items1 = [3, 3]
        sort(items1)
        assert items1 == [3, 3]  # List should not be changed
        items2 = [3, 5, 3]
        sort(items2)
        assert items2 == [3, 3, 5]  # List should be in sorted order
        items3 = [5, 5, 3, 5, 3]
        sort(items3)
        assert items3 == [3, 3, 5, 5, 5]
        items4 = [7, 5, 3, 7, 5, 7, 5, 3, 7]
        sort(items4)
        assert items4 == [3, 3, 5, 5, 5, 7, 7, 7, 7]
        items5 = [-20, 50, -20, 201, 201, 201]
        sort(items5)
        assert items5 == [-20, -20, 50, 201, 201, 201]
        items6 = [-1, -1, -1, 50, 50, 14, 14]
        sort(items6)
        assert items6 == [-1, -1, -1, 14, 14, 50, 50]
        items7 = [-901, 502, 502, 124, 124, 50, 50]
        sort(items7)
        assert items7 == [-901, 50, 50, 124, 124, 502, 502]

    def test_sort_on_lists_of_random_integers(self):
        # Generate list of 10 random integers from range [1...20]
        items1 = random_ints(10, 1, 20)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 20 random integers from range [1...50]
        items2 = random_ints(20, 1, 50)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 30 random integers from range [1...100]
        items3 = random_ints(30, 1, 100)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3

    def test_sort_on_lists_of_random_integers_with_duplicates(self):
        # Generate list of 20 random integers from range [1...10]
        items1 = random_ints(20, 1, 10)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 50 random integers from range [1...20]
        items2 = random_ints(50, 1, 20)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 100 random integers from range [1...30]
        items3 = random_ints(100, 1, 30)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3


class StringSortTest(unittest.TestCase):

    def test_sort_on_small_lists_of_strings(self):
        items1 = ['A']
        sort(items1)
        assert items1 == ['A']  # List should not be changed
        items2 = ['B', 'A']
        sort(items2)
        assert items2 == ['A', 'B']  # List should be in sorted order
        items3 = ['B', 'C', 'A']
        sort(items3)
        assert items3 == ['A', 'B', 'C']
        items4 = ['X', 'G', 'I', 'P', 'L']
        sort(items4)
        assert items4 == ['G', 'I', 'L', 'P', 'X']
        items5 = ['B', 'Z', 'Y', 'E', 'I', 'F', 'K']
        sort(items5)
        assert items5 == ['B', 'E', 'F', 'I', 'K', 'Y', 'Z']
        items6 = ['J', 'K', 'L', 'F', 'Y', 'D', 'U', 'J', 'D', 'D']
        sort(items6)
        assert items6 == ['D', 'D', 'D', 'F', 'J', 'J', 'K', 'L', 'U', 'Y']

    def test_sort_on_fish_book_title(self):
        items = 'one fish two fish red fish blue fish'.split()
        sorted_items = sorted(items)  # Create a copy of list in sorted order
        sort(items)  # Call mutative sort function to sort list items in place
        assert items == sorted_items

    def test_sort_on_seven_dwarf_names(self):
        items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
        sorted_items = sorted(items)  # Copy
        sort(items)  # Mutate
        assert items == sorted_items


class MergeSortTest(unittest.TestCase):
    # merge() assumes two lists are sorted already
    def test_merge_on_small_list_with_decimal(self):
        T1 = [5, 6]
        T2 = [9, 10]
        result = merge(T1, T2)
        assert result == [5, 6, 9, 10]
        T3 = [20, 25, 76]
        T4 = [80, 89, 95]
        result = merge(T3, T4)
        assert result == [20, 25, 76, 80, 89, 95]
        T5 = [-20, 20, 25.5, 30]
        T6 = [35.2, 35.5, 40]
        result = merge(T5, T6)
        assert result == [-20, 20, 25.5, 30, 35.2, 35.5, 40]

    def test_merge_on_large_list_with_negatives(self):
        T1 = [1, 1, 1, 5, 6, 7, 8]
        T2 = [9, 15, 16, 20]
        result = merge(T1, T2)
        assert result == [1, 1, 1, 5, 6, 7, 8, 9, 15, 16, 20]
        T3 = [-15, -10, 0, 5, 6]
        T4 = [12, 15, 20, 25, 30]
        result = merge(T3, T4)
        assert result == [-15, -10, 0, 5, 6, 12, 15, 20, 25, 30]

    def test_sort_on_decimal_with_negative_list(self):
        T1 = [9.2, -5.3, 2.3, 7.5]
        merge_sort(T1)
        assert T1 == [-5.3, 2.3, 7.5, 9.2]
        T2 = [6.2, -12.12, 75.3, 12.12]
        merge_sort(T2)
        assert T2 == [-12.12, 6.2, 12.12, 75.3]
        T3 = [-9.5, 5.6, -89.1, 12.2]
        merge_sort(T3)
        assert T3 == [-89.1, -9.5, 5.6, 12.2]

    def test_sort_on_small_list(self):
        T1 = [39, 6, 8, 12, 10]
        merge_sort(T1)
        assert T1 == [6, 8, 10, 12, 39]
        T2 = [73, 61, 5, 12]
        merge_sort(T2)
        assert T2 == [5, 12, 61, 73]
        T3 = [20, 20, 91, 24]
        merge_sort(T3)
        assert T3 == [20, 20, 24, 91]

    def test_sort_on_large_list(self):
        T1 = [5, 1, 6, 78, 5, 1, 2, 5, 1]
        merge_sort(T1)
        assert T1 == [1, 1, 1, 2, 5, 5, 5, 6, 78]
        T2 = [5, 1, 2, 56, 2, 6, 78, 8, 90, 124]
        merge_sort(T2)
        assert T2 == [1, 2, 2, 5, 6, 8, 56, 78, 90, 124]
        T3 = [56, 1, 3, 634, 7, 8, 2, 123, 1, 2]
        merge_sort(T3)
        assert T3 == [1, 1, 2, 2, 3, 7, 8, 56, 123, 634]


class PartitionTest(unittest.TestCase):
    def test_partition_small(self):
        T1 = [19, 5, 14, 8, 5]
        partition(T1, 0, len(T1) - 1)
        assert T1 == [5, 5, 14, 8, 19]
        T2 = [56, 12, 12, 8]
        partition(T2, 0, len(T2) - 1)
        assert T2 == [8, 12, 12, 56]
        T3 = [5, 2, 3, 5]
        partition(T3, 0, len(T2) - 1)
        assert T3 == [5, 2, 3, 5]

    def test_partition_with_negative(self):
        T1 = [-10, -5, -50, 40]
        partition(T1, 0, len(T1) - 1)
        assert T1 == [-50, -10, -5, 40]
        T2 = [-25, -9, 56, 20]
        partition(T2, 0, len(T2) - 1)
        assert T2 == [-25, -9, 56, 20]
        T3 = [-4, 20, -15, 50]
        partition(T3, 0, len(T2) - 1)
        assert T3 == [-15, -4, 20, 50]

    def test_sort_on_decimal_with_negative_list(self):
        T1 = [9.2, -5.3, 2.3, 7.5]
        quick_sort(T1)
        assert T1 == [-5.3, 2.3, 7.5, 9.2]
        T2 = [6.2, -12.12, 75.3, 12.12]
        quick_sort(T2)
        assert T2 == [-12.12, 6.2, 12.12, 75.3]
        T3 = [-9.5, 5.6, -89.1, 12.2]
        quick_sort(T3)
        assert T3 == [-89.1, -9.5, 5.6, 12.2]

    def test_sort_on_small_list(self):
        T1 = [39, 6, 8, 12, 10]
        quick_sort(T1)
        assert T1 == [6, 8, 10, 12, 39]
        T2 = [73, 61, 5, 12]
        quick_sort(T2)
        assert T2 == [5, 12, 61, 73]
        T3 = [20, 20, 91, 24]
        quick_sort(T3)
        assert T3 == [20, 20, 24, 91]

    def test_sort_on_large_list(self):
        T1 = [5, 1, 6, 78, 5, 1, 2, 5, 1]
        quick_sort(T1)
        assert T1 == [1, 1, 1, 2, 5, 5, 5, 6, 78]
        T2 = [5, 1, 2, 56, 2, 6, 78, 8, 90, 124]
        quick_sort(T2)
        assert T2 == [1, 2, 2, 5, 6, 8, 56, 78, 90, 124]
        T3 = [56, 1, 3, 634, 7, 8, 2, 123, 1, 2]
        quick_sort(T3)
        assert T3 == [1, 1, 2, 2, 3, 7, 8, 56, 123, 634]


def get_sort_function():
    """Read command-line argument and return sort function with that name."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort_function'.format(script))
        print('Example: {} bubble_sort'.format(script))
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
            return sort_function
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if 'sort' in name:
                    print('    {}'.format(name))
            return


# If using PyTest, change this variable to the sort function you want to test
sort = counting_sort


if __name__ == '__main__':
    # Get sort function from command-line argument
    # FIXME: This is causing unittest to throw an error
    # sort = get_sort_function()
    unittest.main()
