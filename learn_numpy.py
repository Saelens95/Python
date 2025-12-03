# Learning Numpy
# 10/02/25

import numpy as np

# list = [1,2,3,4,5]
# print(list[1])

# list2 = ["John", "Sue", 1, 2]
# print(list2[1])


# Numpy = Numeric Python
# ndarray = n-dimensional array
# np1 = np.array([0,1,2,3,4,5,6,7,8,9])
# print(np1)
# print(np1.shape) # tells us how many elements are in the array

# np2 = np.arange(10)
# print(np2)

# Step
# np3 = np.arange(0,10,2)
# print(np3)

# Zeros 
# np4 = np.zeros(10)
# print(np4)

# Multidimensioanl zeros
# np5 = np.zeros((2,10))
# print(np5)

# Full 
# np6 = np.full((10), 6)
# print(np6)

# Multidimensional Full
# np7 = np.full((2,10), 6)
# print(np7)

# Convert Python lists to np
# my_list = [1,2,3,4,5]
# np8 = np.array(my_list)
# print(np8)
# print(np8[0])
# print(np8[2])

# --------------------

# 10/3/25
# Slicing w/ numpy

# my_array = np.array([1,2,3,4,5,6,7,8,9])
# print(my_array[1:5]) # Return 2,3,4,5 from list

# Return from something to the end of the array
# print(my_array[3:]) # third item to the end of list

# Return Negative Slices
# 7, 8
# print(my_array[-3:-1])

# Steps
# print(my_array[1:5]) # 2-5
# print(my_array[1:5:2]) # 2-5 in steps of 2

# Steps on the entire array
# print(my_array[::2]) # stepping through whole array by 2
# print(my_array[::3]) # stepping through whole array by 3
# print(my_array[::-1]) # stepping through whole array backwards by (negative) 1

# my_array2 = np.array([[1,2,3,4,5], 
#                       [6,7,8,9,10]])

# Pull out a single item
# print(my_array2[1,2]) # two brackets in array with indices 0 & 1 --> so '1' in print statement for bracket with 6,7,8,9,10 and '2' for the second (third) item in that brakcet--> 8

# Slicing a 2-3 array 2,3
# print(my_array2[0:1, 1:3]) # 0:1 tells us all numbers in first bracket 1-5 -- 1:3 tells us which numbers to pull from that bracket i.e. indices 1-3 but not including 3 --> so 2,3

# Slice from both rows
# print(my_array2[0:2, 1:3]) # 0-2 will return bracket indices 0-2 but not including 2 --> so both brackets will be returned, but this time we want indices 1:3 not including 3 to be returned from BOTH brakcets, i.e 2,3 & 7,8

#-----------------------

# Universal Functions in Numpy (UFunc)
# new_array = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
# print(new_array)

#Square Root of Each Element
# print(np.sqrt(new_array))

# Absolute Value
# print(np.absolute(new_array)) # Makes all elements positive

# Exponents
# print(np.exp(new_array))

# Min/Max
# print(np.max(new_array))
# print(np.min(new_array))

# Sign positive or negative
# print(np.sign(new_array)) # returns -1 for negatives ; 0 for 0 ; 1 for positives

# Trig Funcs. --> Sin, Cos, Tan, Log
# print(np.sin(new_array))
# print(np.cos(new_array))
# print(np.tan(new_array))
# print(np.log(new_array))

#------------------------------
# Copy Vs. View
# Copy is copy of array ; view is copy of array but still connected to orig. array

# array0 = np.array([0,1,2,3,4,5])

# Create a view
# array1 = array0.view()

# print(f'Original Array0 {array0}')
# print(f'Original Array1 {array1}')

# array0[0] = 41

# print(f'Original Array0 {array0}')
# print(f'Original Array1 {array1}')

# Create a Copy
# array1 = array0.copy()
# print(f'Original Array0 {array0}')
# print(f'Original Array1 {array1}')

# array1[0] = 41

# print(f'Original Array0 {array0}')
# print(f'Original Array1 {array1}')

#---------------------------------------
# Shape and Re-shape

# Create 1-D Numpy Array and Get Shape (rows, columns (elements))
# np_1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(np_1)
# print(np_1.shape)

# Create 2-D Array and get Shape, (rows/columns)
# np_2 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
# print(np_2)
# print(np_2.shape)

# Reshape 2-D
# np_3 = np_1.reshape(3,4)
# print(np_3)
# print(np_3.shape)

# Reshape 3-D
# np_4 = np_1.reshape(2,3,2) # reshapes into 2 arrays with 3 rows and 2 columns EACH!
# print(np_4)
# print(np_4.shape)

# # Flatten to 1-D
# np_5 = np_4.reshape(-1)
# print(np_5)
# print(np_5.shape)

#----------------------------------------------
# 10/05-25
# Iterating Through Numpy Arrays

# 1_D Numpy Array
# np_1 = np.array([1,2,3,4,5,6,7,8,9,10])
# for x in np_1:
#     print(x)

# 2-D Numpy Array
# np_2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# for x in np_2:
#     # print(x)
#     for y in x:
#         print(y)

# 3-D Numpy Array
# np_3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

# for x in np_3:
#     # print(x)
#     for y in x:
#         # print(y)
#         for z in y:
#             print(z)

# Better Way! --> Use np.nditer()
# for x in np.nditer(np_3):
#     print(x)

#-------------------

# Sorting Numpy Arrays

# np.sort()
# np1 = np.array([6,7,8,4,9,0,2,1])
# print(np1)
# print(np.sort(np1))

# Alphabetical
# np2 = np.array(["John", "Tina", "Aaron", "Zed"])
# print(np2)
# print(np.sort(np2))

# Boolean False = 0 ; True = 1
# np3 = np.array([True, False, False, True])
# print(np3)
# print(np.sort(np3))

# Return a copy not change the original
# print(np1)
# print(np.sort(np1))
# print(np1) # See how orig does NOT get changed

# 2-D Array --> sorts elements in each row low to high, not entire thing
# np4 = np.array([[6,7,1,9], [8,3,5,0]])
# print(np4)
# print(np.sort(np4))

#------------------------------------k

# Searching Through Numpy Arrays
# np1 = np.array([1,2,3,4,5,6,7,8,9,10, 3])
# x = np.where(np1 == 3)
# print(np1)
# print(x[0]) # returns 0th item of tuple i.e. where the # that we're interested in is located -->  i.e. [2] and [10] indices
# print(np1[x[0]]) # this simply prints the # of those indices --> i.e. it prints [3 3]

# Prints even indices
# y = np.where(np1 % 2 == 0)
# print(np1)
# print(y[0])

# Prints odd indices
# z = np.where(np1 % 2 == 1)
# print(np1)
# print(z[0])

#------------------------------------------------

# Filtering Numpy Arrays With Boolean Index Lists

# np1 = np.array([1,2,3,4,5,6,7,8,9,10])
# x = [True, True, False, False, False, False, False, False, False, False]

# Filters out False indices
# print(np1)
# print(np1[x])

# Somewhat Better Way!

# filtered = []
# for thing in np1:
#     if thing % 2 ==0:
#         filtered.append(True)
#     else:
#         filtered.append(False)

# print(np1)
# print(filtered)
# print(np1[filtered]) # prints just even indices

# for thing in np1:
#     if thing > 5:
#         filtered.append(True)
#     else:
#         filtered.append(False)

# print(np1)
# print(filtered)
# print(np1[filtered]) # prints indices only greater than 5

# Best Way --> Shortcut!
# filtered = np1 % 2 == 0
# print(np1)
# print(filtered)
# print(np1[filtered]) # filtering for even numbers

# filtered = np1 > 5
# print(np1)
# print(filtered)
# print(np1[filtered]) # prints indices only greater than 5