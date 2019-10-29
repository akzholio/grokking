'''
Grokking Algorithms
'''

'''
CHAPTER 3

Recursion
'''

'''

Recursive function is the one that calls itself.

In every recursive function you will need to specify 'base case' and 'recursive case'.

In Recursive Case, function calls itself.
In Base Case, function does not call itself to prevent infinite loop.

'''

def countdown(i):
    print(i)
    if i <= 0: # <--- Base Case
        return
    else:
        countdown(i-1) # <--- Recursive Case

# countdown(10)


'''
STACK


'''

def greet2(name):
    print('how are you, ' + name + '?')

def bye():
    print('ok bye!')

def greet(name):
    print('hello, ' + name + '!')
    greet2(name)
    print('gettin read to say bye...')
    bye()

# greet('Akzhol')

'''
Let's see our stack in action with factorials
'''

def factorial(x):
    print('*'*x)
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

# print(factorial(5))

'''

2 options to optimize:

    1. Re-write as a loop
    2. Use 'Tail Recursion'

'''