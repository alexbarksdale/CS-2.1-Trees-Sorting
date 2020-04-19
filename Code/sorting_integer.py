#!python
from typing import List
from sorting_iterative import insertion_sort


def counting_sort(numbers: List[int]):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n + k) where n is the numbers given and k being the
    possible values/freq_count which is the size of max(n)
    Memory usage: O(k) k being the possible values/freq_count which is the
    size of max(n) n being the numbers given"""

    min_val = min(numbers)
    # Create list of counts with a slot for each number in input range
    freq_count = [0] * (max(numbers) - min_val + 1)

    # Loop over given numbers and increment each number's count
    for i in range(len(numbers)):
        freq_count[numbers[i] - min_val] += 1

    # Loop over counts and mutate the input
    counter = 0
    for i in range(len(freq_count)):
        for _ in range(freq_count[i]):
            numbers[counter] = min_val + i
            counter += 1
    print(numbers)


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n + k) n being the values in the list and k being the 
    bucket's we iterate over.
    Memory usage: O(n + k) n being the values in the list and k being the 
    bucket's we iterate over. """

    num_len, max_num = len(numbers), max(numbers)

    # Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets)]

    # Used to put the elements in the buckets
    divider = (max_num + 1) / num_buckets

    # print(max_num/num_buckets)
    # print('Confused:', int(numbers[7] / (max_num/num_buckets)))
    # print('Witchcraft:', int(numbers[7] / ((max_num + 1)/num_buckets)))
    # print(int(numbers[7]/divider))

    # Loop over given numbers and place each item in appropriate bucket
    for i in range(num_len):
        j = int(numbers[i]/divider)
        buckets[j].append(numbers[i])

    # Sort each bucket using any sorting algorithm (recursive or another)
    for i in range(len(buckets)):
        insertion_sort(buckets[i])

    # Loop over buckets and mutate the input
    counter = 0
    for i in range(len(buckets)):
        for item in buckets[i]:
            numbers[counter] = item
            counter += 1
    print(numbers)


T1 = [10, 1, 5, 9, 4, 2, 6, 5]
# print('Starting values:', T1)
# counting_sort(T1)

T2 = [19, 5, 14, 8, 5]
# T2 = [22, 45, 12, 8, 10, 6, 72, 81, 33, 18, 50, 14]
print('Starting values:', T2)
bucket_sort(T2)
