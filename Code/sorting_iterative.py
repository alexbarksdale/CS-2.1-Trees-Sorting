#!python


def is_sorted(items=list) -> bool:
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(0, len(items)-1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items=list, print_sorting=False) -> list:
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    for i in range(0, len(items) - 1):
        swapped = False

        # Inner loop is responsible for the switching/checking
        # We remove i at the end because we know that the last item is already sorted
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


def selection_sort(items=list, print_sorting=False) -> list:
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(0, len(items) - 1):
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


def visualize_sort(items=list) -> None:
    '''Prints the sorting algorithm in action'''
    print(items)


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


if __name__ == '__main__':
    T1 = [1, 5, 6, 2, 8, 0, 10]
    print(is_sorted(T1))
    # bubble_sort(T1, print_sorting=True)
    selection_sort(T1, print_sorting=True)
