'''
Grokking Algorithms
'''

'''
CHAPTER 2

Selection Sort
'''


'''

How does memory work?

Suppose you came to a theater and want to leave your belongings in a storage.
There are special boxes to store your items.

Each box can host only one item.
You want to store 2 items so you will need 2 boxes.

That's, in essence, is how the memory in your computer works!
It resembles a huge shelve of boxes, each box having its own address i.e. fe0ffeeb <- address of the memory cell.

Every time you want to save a value in memory, you ask a computer for a memory cell and it gives you an address of that cell.

In case you want to save multiple values, it can be done in 2 ways: either by using an ARRAY or a LIST.


ARRAYS and LINKED LISTS

# ARRAYS

Suppose you are writing a ToDo List App.
You need to store each task in a list in memory.

What will you use - an Array or a LinkedList?

Let's first go with an Array, it's straightforward.
When we use an Array, all our tasks will be next to each other.

        [Task1][Task2][Task3]
        [.....][.....][.....] <- other cells, used by other apps
        [     ][     ][     ] <- empty cells

Now, suppose you want to add a 4th Task.
However, the cell next to 3rd Task is taken!

Imagine you went to cinema with friends and got yourselves some seats.
Another friend of your arrives and now you have to find a place for him/her, next seat is taken :(

Now, you will have to search for a place in memory with empty cells to accommodate your group and move there altogether!

And if another friend arrives, you have to start above search again! This nightmare will continue over and over again!

The simplest solution in this case would be to 'reserve' seats - tell computer to reserve 10 seats if you are expected a group of 10.
Then you can add up to 10 friends and there would be no need in moving.

Here are a couple of drawbacks:
1. Not all of your friends might show up and then the memory will be wasted.
2. If you have more than 10 friends coming, you still need to move.

Seems like a good solution, but LinkedLists might solve the problem.

# LINKED LISTS

When using a LinkedList, items can be stored anywhere in the memory.

Each item has an address of where the next item is stored.


EXERCISES

Q: You are writing an app to accept orders in a restaurant. 
The waiter puts order in the end of queue, the chefs take the orders from the beginning of queue.
What would be the best data structure to use in this case?
A: LinkedList, it allows O(1) add and delete operations.

Q: Suppose Facebook stores list of usernames. What data structure you will use to implement the list, given that people
go to Facebook quite often and there is a need for a quick access to any index of a list, for Binary Search algorithm?
A: A sorted Array.

Q 2.4
A: Array has O(n) complexity for insertion. If we use Binary Search, then the list has to be sorted again and again.
New users can be added to the end of array, but the array will then need to be sorted for Binary Search algorithm.
Or, we can insert it in any place, but we will have to shift remainder of array down.

Q 2.5
A: 
Hybrid data structure will be slower to read compared to an Array, but faster compared to LinkedList.
Hybrid data structure will be faster to insert compared to an Array, but same compared to LinkedList.



Now let's combine all we learned into Selection Sort!


'''

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,6,2,10]))