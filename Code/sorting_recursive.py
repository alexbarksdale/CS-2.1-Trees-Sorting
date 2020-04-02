#!python
from sorting_iterative import insertion_sort


def merge(items1=list, items2=list) -> list:
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # 1,4,8,9       2,4,5,6 = [1,2,4,4,5,6,8,9]
    merged_items = []

    # There's gotta be a better way
    while len(items1) > 0 and len(items2) > 0:
        if items1[0] > items2[0]:
            merged_items.append(items2.pop(0))
        else:
            merged_items.append(items1.pop(0))

        # Checks if the list is empty
        if not items1:
            merged_items.extend(items2)  # O(k) k being the len of list
        if not items2:
            merged_items.extend(items1)  # O(k) k being the len of list
    return merged_items


def split_sort_merge(items=list) -> list:
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Split items list into approximately equal halves
    mid_index = len(items)//2
    first_half = items[:mid_index]
    second_half = items[mid_index:]
    # Sort each half using any other sorting algorithm
    sorted_f_half = insertion_sort(first_half)
    sorted_s_half = insertion_sort(second_half)
    # Merge sorted halves into one list in sorted order
    return merge(sorted_f_half, sorted_s_half)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


if __name__ == '__main__':
    T1 = [1, 4, 8, 9]
    T2 = [2, 4, 5, 6]
    T3 = [1, 4, 8, 9, 2, 4, 5, 6]
    # print(merge(T1, T2))
    print(split_sort_merge(T3))
