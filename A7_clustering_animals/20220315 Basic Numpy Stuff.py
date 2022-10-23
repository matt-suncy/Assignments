'''
   20220315
   
   Robin Dawes
   
   NumPy has a HUGE range of functions that are designed to improve on the standard
   mathematical functionality of Python.  But in this assignment we aren't going to use
   much of that.
   
   NumPy also offers an alternative to the Python list structure: the ndarray.  You access its contents
   just like a list (i.e. you use square brackets "[" and "]" to identify particular locations), and
   if you print it, it looks like a list.  One difference is that NumPy interprets a list of lists
   as a 2-dimensional array (and prints it like one), which is one of the most useful structures
   ever invented - it's basically a table.
   
   You can also have arrays that are 3-dimensional, 4-dimensional, etc. - but 2-dimensional
   arrays are far more common.
   
   NumPy arrays have some limitations:
      - in a 2-dimensional (or higher-dimensional) array, all the rows must have the same 
        number of elements.  This is not the case in a standard list of lists.
      - all of the elements in a NumPy array must have the same type (certainly not the
        case in a standard Python list)
   
   So why use a structure that has more limitations than a standard Python list?
   
   The answer is ... SPEED!  Python lists let us do all sorts of cool things (like adding
   new elements at the end, or in the middle, and removing values from the middle of
   the list, etc etc) but these fancy operations come at the cost of slowing down the program.
   
   So if you don't need to do any of those things - for example if you are reading in a whole
   pile of data that forms a table, and then you are going to work on that data without needing
   to append or insert new elements or delete elements - then a NumPy array is the way to go.
   
   In this demo program we're going to look at 
   - a bunch of options for reading data from a text file into a NumPy array
   - a couple of ways to initialize an array so that we can modify the data later
   - a few of the built-in operations on arrays
'''


import numpy as np
import random

# variations of using the np.loadtxt() function to create a 2-dimensional array from a file

# See the test.txt file: each row of the array is on a separate line

# load the file as an array of integers
table_1 = np.loadtxt("test.txt", dtype=int)
# The default type is float, but we use dtype to override this
print("\ntable_1")
print(table_1)
print("table_1 is of type ", type(table_1))

# use skiprows to ignore lines at the top of the file
# use usecols to select specific columns
table_2 = np.loadtxt("test.txt", dtype=int, skiprows=1, usecols=(0, 2, 4, 5))
print("\ntable_2")
print(table_2)

# we can use a range() to select the columns we want
table_3 = np.loadtxt("test.txt", dtype=int, usecols=range(3, 6))
print("\ntable_3")
print(table_3)

# create an array from a set of values using the np.array() function

# NB - this function takes ONE parameter.  The values/rows of the table
# must be enclosed in parentheses

# create a one-dimensional array
table_4 = np.array([4, 6, 1, 2, 3])
print("\ntable_4")
print(table_4)

# create a two-dimensional array
table_5 = np.array([
    [1, 2, 3, 4],
    [8, 7, 6, 5],
    [10, 10, 10, 10]
]
)
print("\ntable_5")
print(table_5)

# create an array initialized to all 0's
# Note that the entries are floats (0.) because we didn't specify integers
table_6 = np.zeros((5, 4))
print("\ntable_6")
print(table_6)

# create an array initialized to all 1's
# Note that the entries are integers because we specified the dtype
table_7 = np.ones((3, 4), dtype=int)
print("\ntable_7")
print(table_7)

# create an array initialized to whatever was in the memory addresses
# being used - why would you ever use this??
table_8 = np.empty((2, 5))
print("\ntable_8")
print(table_8)

print("\ntable_5 again")
print(table_5)

# we can find the shape of an array
print("\ntable_5.shape")
print(table_5.shape)

# we can sum the elements of an array
print("\nsum(table_5)")
print(np.sum(table_5))

# we can sum a single row of an array
print("\nsum(table_5[1])")
print(np.sum(table_5[1]))

# we can access/change a single value in an array
table_5[2, 3] = 99       # row 2, column 3
print("\ntable_5 with one element changed")
print(table_5)

# we can iterate over the rows of an array
print("\nsum each row in table_5")
for r in table_5:
    print(np.sum(r))

# we can multiply (or add, subtract, divide) an array by a value
print("\nmultiplying all elements of table_5 by 10")
table_9 = table_5*10
print(table_9)

# we can add (multiply, subtract, divide) two tables together   ...
print("\nadding table_7 and table_9")
table_10 = table_7 + table_9
print(table_10)

# ... but only if they have the same shape
#~ print("\ntrying to add table_1 and table_2")
# ~ table_11 = table_1 + table_2                          # fails because they have different shape
#~ print(table_11)

# numpy has hundreds of pre-defined operations - we are just
# scratching the surface here.  You should check out the online
# documentation!
