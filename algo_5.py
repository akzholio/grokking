'''
Grokking Algorithms
'''

'''
CHAPTER 5

Hash Tables


GIST: just use Python's built in hash function.

Avoid collisions!
Coefficient of fill = number of elements / total number of cells

The lower coefficient - the better.

Complexity:

            Average         Worst
Search      O(1)            O(n)
Insert      O(1)            O(n)
Delete      O(1)            O(n)


Python's dict() is an implementation of hash table.
'''

phone_book = dict()
# or
phone_book = {}

