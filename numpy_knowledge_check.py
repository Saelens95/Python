import numpy as np

# 1. Numpy stands for numerical python
# 2. A numpy array can be acted on more effeciently through code -- a python list can get bulky and hard to manipulate
# 3. A

# 4. np1 = np.zeros(10)

# 5. np2 = np.full((3,4),2) --> prints a 3 X 4 array filled (full) with 2's
# 6.1 [2:5] returns 30, 40, 50 --> 2nd to the 5th indices but not including 5th
# 6.2 returns [80 60 40 20] it returns in reverse, the even values

# 7. b[0:2, 1:3] prints [1 2] and [7 8] --> does this mean when we go from 0:2 or any number that we don't inlcude 0th index?

# 8. This will return an array of +/- 1 where the index value is +/- and zero where the index is zero
# 9.1 Squareroot of each element in the array
# 9.2 It raises arr to the power of each element
# 9.3 Converts all values to positive

# 10. The copy makes a copy of the original array and doesn't change when updated; and view makes a copy but is still connected to original array
# 11. Output: [99 2 3]
# 12.1 arr2.shape gives the shape of the array --> 3 x 4
# 12.2 there are 12 elements in the array
# 13. arr.reshape(-1) seems to return the same original array [0...11]
# 14. By using np.nditer()
# 15. The first bit of code will only return the x relevant indices in the tuple -- i.e. the brakceted array parts but the second will output the elements in the array
# 16. np.sort() returns a modified array that puts elements in order from low to high
# 17. Indices 0, 4, and 6 will be printed


np1 = np.array([6,7,8,4,9,0,2,1])
print(np1)
print(np.sort(np1))
print(np1)