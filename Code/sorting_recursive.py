#!python
from sorting_iterative import insertion_sort
from typing import List


def merge(items1: List[int], items2: List[int]) -> List[int]:
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n) it iterates of (n) items given
    Memory usage: O(n) (maybe) we're storing (n) merged items in a new array."""
    merged_items = []
    i, j = 0, 0  # These values "point" to the next item

    while len(items1) > i and len(items2) > j:
        if items1[i] > items2[j]:
            merged_items.append(items2[j])
            j += 1
        else:  # items1[i] < items2[j]
            merged_items.append(items1[i])
            i += 1

    # Depending on which list is empty it'll add the remaining items
    if len(items1) == i:
        merged_items.extend(items2[j:])  # O(k) k being the len of list
    else:  # if len(items2) == j:
        merged_items.extend(items1[i:])  # O(k) k being the len of list
    return merged_items


def split_sort_merge(items: List[int]) -> List[int]:
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: avg O(n^2) because of insertion_sort 
    Memory usage: O(n) because we're creating an array of (n) elements to merge"""
    # Split items list into approximately equal halves
    mid_index = len(items)//2
    first_half, second_half = items[:mid_index], items[mid_index:]
    # Sort each half using any other sorting algorithm
    insertion_sort(first_half)
    insertion_sort(second_half)
    # Merge sorted halves into one list in sorted order
    got_back = merge(first_half, second_half)  # (n)
    items[:] = got_back


def merge_sort(items: List[int]) -> None:
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(nlogn) for both because merge_sort is splitting the items in
    half each time and merge is taking both lists so (n) elements.
    Memory usage: O(n) because in each recursive call it creates a new array
    which take no more than (n) elements and after the merge it is deleted.
    """
    # Check if list is so small it's already sorted (base case)
    if len(items) > 1:
        # Split items list into approximately equal halves
        mid_index = len(items)//2
        first_half, second_half = items[:mid_index], items[mid_index:]

        # Sort each half by recursively calling merge sort
        merge_sort(first_half)  # T(n/2)
        merge_sort(second_half)  # T(n/2)

        # Merge sorted halves into one list in sorted order
        got_back = merge(first_half, second_half)  # (n)

        items[:] = got_back  # O(n) to copy n items
        print(items)


# def merge_sort(items: List[int]) -> List[int]:
#     '''This version returns a new merged list'''
#     # Check if list is so small it's already sorted (base case)
#     if len(items) == 1:
#         return items

#     # Split items list into approximately equal halves
#     mid_index = len(items)//2
#     first_half, second_half = items[:mid_index], items[mid_index:]

#     print(f'First half: {first_half} Second half: {second_half}')

#     # Sort each half by recursively calling merge sort
#     sorted_f_half = merge_sort(first_half)
#     sorted_s_half = merge_sort(second_half)

#     # Merge sorted halves into one list in sorted order
#     print('Sending:', sorted_f_half, sorted_s_half)
#     got_back = merge(sorted_f_half, sorted_s_half)
#     print(f'Got Back: {got_back} \n')

#     return got_back


def partition(items: List[int], low: int, high: int) -> int:
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    # TODO: Choose a pivot any way and document your method in docstring above
    TODO: Memory usage: ??? Why and under what conditions?"""
    pivot = items[low]
    i, j = low, high

    while i < j:
        while items[i] <= pivot:
            i += 1
        while items[j] > pivot:
            j -= 1
        if (i < j):  # If j > than i we don't swap because it's in the right spot
            items[i], items[j] = items[j], items[i]
    items[low], items[j] = items[j], items[low]
    return j  # returns the index of the partition

    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items: List[int], low=None, high=None):
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
    T1 = [19, 5, 14, 8, 5]
    T2 = [17, 17, 11, 13, 20]
    T3 = [19, 5, 14, 8, 5, 17, 17, 11, 13, 20]
    print('Starting list:', T3, '\n')
    print(split_sort_merge(T3))
    merge_sort(T3)
    # print(v2_merge_sort(t3))
