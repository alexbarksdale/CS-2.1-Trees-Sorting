#!python
from typing import List


def counting_sort(numbers: List[int]):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    # FIXME: Improve this to mutate input instead of creating new output list

    min_val = min(numbers)
    # Create list of counts with a slot for each number in input range
    freq_count = [0] * (max(numbers) - min_val + 1)

    # Loop over given numbers and increment each number's count
    for i in range(len(numbers)):
        freq_count[numbers[i] - min_val] += 1

    # Loop over counts and append that many numbers into output list
    ....

    print(freq_count)


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


T1 = [0, 1, 5, 9, 4, 2, 6, 5]
print('Starting values:', T1)
counting_sort(T1)
