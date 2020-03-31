#!python


def is_sorted(items=list) -> bool:
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(0, len(items)-1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items=list) -> list:
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    for i in range(0, len(items) - 1):
        # Inner loop is responsible for the switching/checking
        # We remove i at the end because we know that the last item is already sorted
        for j in range(0, len(items) - 1 - i):
            if items[j] > items[j + 1]:
                # Swaps the location of the items
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


if __name__ == '__main__':
    T1 = [1, 4, 3, 2, 5]
    print(is_sorted(T1))
    print(bubble_sort(T1))
