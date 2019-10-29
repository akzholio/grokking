'''
Grokking Algorithms
'''

'''
CHAPTER 1

Binary Search algorithm
Time complexity: O(logn)
'''

def binary_search(arr, keyword):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 # remainder-free division
        guess = arr[mid]

        if guess == keyword: # return the guess
            return mid
        if guess > keyword: # if guess is greater than keyword,
            high = mid - 1  # assign a new high
        else:               # if guess is smaller than keyword,
            low = mid + 1   # assign a new low
    
    return None

# my_list = [1,3,5,7,9]

# print(binary_search(my_list, 3)) # => 1
# print(binary_search(my_list, 10)) # => None


'''
EXERCISES

Q: You have a list of 128 names, what is the maximum checks required?
A: Take log2 of 128 = 7

Q: Suppose the number of names in a list doubled (256). How will the number of checks change?
A: It will increase by 1 (8) 

Bonus
Q: Suppose the list is 4 times bigger now (512), what is number of checks?
A: It will increase by 1 again (9)

It would suffice to say that the number of steps will increase by log2(factor) 
where factor is by how much the original list has increased
'''

'''
NOTES

Big Oh always tells us the worst possible case.

Typical examples of Big Oh:

1. O( log(n) ) - logarithmic time. Example: Binary Search
2. O( n ) - linear time. Example: Linear Search
3. O( n * log(n) ) Effective sorting algorithms. Example: Quicksort
4. O( n^2 ) Slow sorting algorithms. Example: Selection Sort
5. O( n! ) Very slow sorting algorithms. Example: The Salesman Problem

'''

'''
REVISION

- Algorithm speed is not calculated in seconds, but rather in the rate of increase in number of operations.

'''

'''
EXERCISES

Give complexity in Big Oh notation for each task.

Q: We have a surname, we need a phone number in phone journal.
A: O(log(n)) - Binary Search

Q: We know a number, we need a surname.
A: O(n) - Linear Search

Q: We need to read all phone numbers in phone book.
A: O(n)

Q: We need all phone numbers of people whose surname starts with "A".
A: O(n)


The Salesman Problem

Our Salesman needs to travel to 5 cities, using the shortest route possible.
One way to solve this problem would be to find all possible combinations of routes to determine the shortest one.

O(n!) - complexity of finding the shortest path.


EXTRA: Chapter 11, Binary Search Tree

Everytime a user enters a new username, Facebook has to search billions of other usernames to check if entered username has been taken.
Wouldn't it be good to insert a new username so that we don't have to sort the massive array again?

Turns out, Binary Search Tree has same Big Oh complexity as an Array, but excels at Inserting and Deleting operations.

                    Search      Insert      Delete
Array               O(log(n))   O(n)        O(n)
Binary Search Tree  O(log(n))   O(log(n))   O(log(n))

The above is an AVERAGE case, BST has issues with getting an arbitrary element.
GETTING an element will depend on how balanced BST is.

There are BSTs that can self-balance, i.e. Red-Black BSTs.

B-Tree is a form of BST used to store data in database.

Search more for: B-Tree, Red-Black Trees, Heaps, Splay Trees

'''
