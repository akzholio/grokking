'''
Grokking Algorithms
'''

'''
CHAPTER 4

Quick Sort
'''

'''
Divide & Conquer Strategy.


Imagine you are a farmer that owns some land.

1680x640 meters

You want to evenly divide the land into similar square regions.
The regions should be as big as possible.

Using divide & conquer in creating a sum function.


'''

def sum(arr):
    if len(arr) == 0:
        return 0 # base case
    elif len(arr) == 1:
        return arr[0] # base case
    else:
        return arr[0] + sum(arr[1:]) # recursive case
    

# print(sum([2,4,6]))
# print(sum([]))

# remember the stack of calls, none of the functions will end until base case is returned

def element_counter(arr, count=0):
    if len(arr) == 0: # base case
        return count
    elif len(arr) == 1: # base case
        return count + 1
    else:
        count += 1
        return count + element_counter(arr[1:], count) # recursive case

# print(element_counter([1,2,3,4,5]))

def find_max(arr, max_num=0):
    if len(arr) == 0: # base case
        return 0
    elif len(arr) == 1: # base case, but check if max_num is less than the only element in array
        if max_num < arr[0]:
            max_num = arr[0]
        return max_num
    else:
        if max_num < arr[0]:
            max_num = arr[0]
        return find_max(arr[1:], max_num) # recursive case

# print(find_max([1,2,9,4,5,20,11]))

'''
Quick sort
'''
import random

def quicksort(arr):
    if len(arr) < 2:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

array = [5,1,4,2,7,6,10,8]

print(quicksort(array))

def merge(arr1, arr2):
    min_value = 0
    max_value = 0
    min_value = min(arr1[0], arr2[0])
    max_value = max(arr1[1], arr2[1])
    result = []
    result[0] = min_value
    result[3] = max_value
    
    return result


def mergesort(arr):
    if len(arr) < 2:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    else:
        left = [i for i in arr[:len(arr)//2]]
        right = [i for i in arr[len(arr)//2:]]
        if len(left) == 2:
            if left[0] > left[1]:
                left[0], left[1] = left[1], left[0]
        if len(right) == 2:
            if right[0] > right[1]:
                right[0], right[1] = right[1], right[0]
            
        return mergesort(left) + mergesort(right)

print(mergesort(array))

'''

RESUME



'''