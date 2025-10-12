# properties and calculation 
# -shape size and type 

import numpy as np

# arr = np.array([[1,2,4],
#                 [3,4,5]])

# print(arr.shape)

# output :(2,3)
# expnation : means 2 raws and 3 columns
 
# ============================================

#  2.size
# returns the total no of elements in an array 

# arr = np.array([[1,2,3],
#                [4,5,6]])
# print(arr.size)

# output : 6
# ===================================================



# 3.ndim -- give the dimention of the array 

# arr = np.array([[1,2,3],
#                [4,5,6]])

# print(arr.ndim)

# output : 2 means 2d array 
# ======================================


# 4.dtype -- datatypes of elements in arr 
# arr = np.array([[1,2,3],
#                [4,5,6]])

# print(arr.dtype)

# output : int64

# =============================================



# 5. asdype -- change the datatype an array 
# arr = np.array([[1,2,3],
#                [4,5,6]])
# changed = arr.astype(float)
# print(changed.astype)


# operator 
# -----------------------------------------------------

# arr = np.array([[1,2,3],
#                [4,5,6]])

# print(arr + 3)
# print(arr - 3)
# print(arr * 3)
# print(arr / 3)

# aggregation function 

# function                                       work
# .sum()                                        add all
# .mean()                                       average
# .min()                                        smallest 
# .max()                                        biggest 
# .std()                                        standerd daviation
# .val()                                        varients 