#!python


def is_sorted(items=list):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) we're iterating over all elements
    Memory usage: O(1) we're not creating new memory"""
    for i in range(0, len(items)-1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items=list, print_sorting=False):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: avg O(n^2) because we have an outer loop iterating over all
    elements and an inner loop iterating over elements n - 1 - i
    Memory usage: O(1) we're never creating new memory and doing it in place."""

    for i in range(len(items)):
        swapped = False

        # Inner loop is responsible for the switching/checking
        # We remove i at the end because we know that the last item is already sorted
        # because we're pushing the largest value up each time
        for j in range(0, len(items) - 1 - i):
            if items[j] > items[j + 1]:
                # Swaps the location of the items
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            return items
        if print_sorting:
            visualize_sort(items)
    return items


def selection_sort(items=list, print_sorting=False):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) we have two loops iterating over all the elements
    Memory usage: O(1) we're never creating new memory and doing it in place."""
    for i in range(len(items)):
        min_val = i

        for j in range(i, len(items)):
            # Checks to see if the current value is less than min_val
            if items[j] < items[min_val]:
                min_val = j

        # Swaps the location of the items
        items[i], items[min_val] = items[min_val], items[i]

        if print_sorting:
            visualize_sort(items)

    return items


def insertion_sort(items=list, print_sorting=False):
    # S/O to https://youtu.be/yCxV0kBpA6M for the help
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) because we have one loop iterating over all elements
    and a nested loop that also iterates over n-1 elements.
    Memory usage: O(1) we're never creating new memory and doing it in place."""
    for i in range(1, len(items)):
        extr_val = items[i]
        extr_loc = i - 1

        while extr_loc >= 0 and items[extr_loc] > extr_val:
            # Moves the greater value to the rigth
            items[extr_loc + 1] = items[extr_loc]
            extr_loc -= 1
        items[extr_loc + 1] = extr_val

        if print_sorting:
            visualize_sort(items)
    return items


def visualize_sort(items=list):
    '''Prints the sorting algorithm in action if enabled'''
    print(items)


if __name__ == '__main__':
    T1 = [2, 1, 0, 4, 5]
    print('STARTING VALUES:', T1, '\n')
    print('Sorted?', is_sorted(T1))
    # bubble_sort(T1, True)
    # selection_sort(T1, True)
    insertion_sort(T1, True)
