'''
CISC-121 2022W
  
This program includes radix sort and quick sort and two tests that
compare the correctiness and effciency of each algorithm through a
seres of tests.

Quick sort from https://www.programiz.com/dsa/quick-sort

Name: Matthew Sun
Student Number: 20273229
Email: matt.suncy@gmail.com

I confirm that this assignment solution is my own work and conforms to 
Queen's standards of Academic Integrity
'''

import random
import copy
import time


def radix_sort(arr):
    '''
    The iterative version of radix sort. Sorts without comparison but sorting
    using the digit in each ones, tens, hundredds, etc place. 

    Parameters: arr - a list of integers

    Return: sorted_arr - the sorted version of arr
    '''

    longest_length = len(str(max(arr)))

    sorted_arr = arr

    for i in range(longest_length):
        # gotta be careful with loop var names
        # 10 digits so 10 buckets
        buckets = []
        for j in range(10):
            buckets.append([])

        for x in sorted_arr:

            try:
                index = int(str(x)[-1 - i])
            except IndexError:
                index = 0

            buckets[index].append(x)

        sorted_arr = []
        for j in range(len(buckets)):
            for x in buckets[j]:
                sorted_arr.append(x)

    return sorted_arr


'''
print('radix with iteration:', radix_sort(
    [842, 952, 17, 199, 59, 33, 13, 3006, 904]))
'''


# For the testing I will be using the recursive version

def radix_sort_rec(arr):
    '''
    The recursive version of radix sort. Sorts without comparison but sorting
    using the digit in each ones, tens, hundredds, etc place. 

    Parameters: arr - a list of integers

    Return: sort_buckets - a function that sorts the arr using buckets
    '''

    longest_length = len(str(max(arr)))

    return sort_buckets(arr, 0, longest_length)


def sort_buckets(arr, counter, longest_length):
    '''
    Sorts integers based on the digit in a specified position. Does that for
    longest_length number of rounds. For each specified position the number
    is added to bucket based on the digit in that position and then all
    numbers are addded to a list.

    Parameters: arr - a list of integers
    counter - a counter to keep track of how many times the function iterates
    longest_length - number of times the function will iterate

    Returns: arr - a sorted version of the inputed array
    '''

    if counter == longest_length:
        return arr

    else:
        buckets = []
        for i in range(10):
            buckets.append([])

        for x in arr:

            try:
                # This is referencing the last digit then the second last...
                index = int(str(x)[-1 - counter])
            except IndexError:
                index = 0

            buckets[index].append(x)

        sorted_arr = []
        # Add all elements to sorted_arr from buckets in order from the 0 bucket to the 9 bucket
        for i in range(len(buckets)):
            for x in buckets[i]:
                sorted_arr.append(x)

    return sort_buckets(sorted_arr, counter + 1, longest_length)


'''
print('radix with recursion:', radix_sort_rec(
    [842, 952, 17, 199, 59, 33, 13, 3006, 904]))
'''


# now gotta do either merge or quick now probably quick


def partition_2(arr, low, high):
    '''
    Takes an array and makes sure that every thing to the left of the pviot
    is smaller and everything on the right is larger. This is done using a 
    pointer that moves from left to right and compares elements to the pivot.

    Parameters: arr - a list
    low - the lowest position
    high - the highest position

    Returns: None
    '''
    pivot = arr[high]
    i = low - 1
    # Comparing from right to left
    for j in (range(low, high)):
        if arr[j] <= pivot:

            i = i + 1
            # Swapping values
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the larger element that's in position i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Return the pos of the partition
    return (i + 1)


def quick_sort_rec_2(arr, low, high):
    '''
    Insures the quick sort algorithm stop when everything is sorted.

    Parameters: arr - a list
    low - the lowest position of the list
    high - the highest position of the list

    Returns: None
    '''

    if low < high:

        p_index = partition_2(arr, low, high)
        # Does the partition with the each of the two sides of the array
        quick_sort_rec_2(arr, low, p_index - 1)
        quick_sort_rec_2(arr, p_index + 1, high)


def quick_sort_2(arr):
    '''
    Initializes the quick sort algorithm.

    Parameters: arr - a list

    Returns: None
    '''
    quick_sort_rec_2(arr, 0, len(arr) - 1)


'''
list_for_quick = [842, 952, 17, 199, 59, 33, 13, 3006, 904]
quick_sort_2(list_for_quick)
print('quick sort:', list_for_quick)
'''


# Testing part 1


def testing_part1():
    '''
    Testing the correctness of the algorithms.
    '''

    list_of_lists_1 = []
    for i in range(100):
        temp_list = []
        for i in range(100):
            temp_list.append(random.randint(1, 10000))

    # I made a deepcopy just in case the sorting interferes with the original lists
    list_of_lists_2 = copy.deepcopy(list_of_lists_1)

    # I will apply bucket sort to list_of_lists_1 and quick sort to the other
    # Just a reminder that bucket sort returns the sorted list the quick sort does not return anything

    # Bucket sorting
    for i in range(len(list_of_lists_1)):
        list_of_lists_1[i] = radix_sort_rec(list_of_lists_1[i])

    # Quick sorting
    for i in range(len(list_of_lists_2)):
        quick_sort_2(list_of_lists_2[i])

    # Comparing the lists of lists
    if list_of_lists_1 == list_of_lists_2:
        print('\nAll sorted lists are equal.\n')
    else:
        print('\nThere was an error.\n')


testing_part1()


def testing_part2():
    '''
    Testing the efficiency of the alogrithms. 
    '''

    bucket_sort_times = []
    bucket_wins = 0
    quick_sort_times = []
    quick_wins = 0

    n_trials = 200
    for i in range(n_trials):
        testing_list_1 = []
        for i in range(10000):
            testing_list_1.append(random.randint(100000, 999999))

        testing_list_2 = copy.deepcopy(testing_list_1)

        # Bucket sort first
        start = time.time()
        testing_list_1 = radix_sort_rec(testing_list_1)
        end = time.time()
        bucket_time = end - start
        bucket_sort_times.append(bucket_time)

        # Next is quick sort
        start = time.time()
        quick_sort_2(testing_list_2)
        end = time.time()
        quick_time = end - start
        quick_sort_times.append(quick_time)

        # Checking who won
        if bucket_time < quick_time:
            bucket_wins += 1
        elif bucket_time > quick_time:
            quick_wins += 1

    avg_bucket = sum(bucket_sort_times) / len(bucket_sort_times)
    avg_quick = sum(quick_sort_times) / len(quick_sort_times)

    print('\nHere are the results after', n_trials, 'trials:\n')

    print('The average time for bucket sort:', avg_bucket, 'seconds.')
    print('The average time for quick sort:', avg_quick, 'seconds.')
    print()
    print('Bucket sort won', bucket_wins, 'times.')
    print('Quick sort won', quick_wins, 'times.')
    print('In', 200 - bucket_wins - quick_wins,
          'occurences, the difference in their times were indistinguishable.')


testing_part2()
