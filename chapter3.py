# indexing and slicing in numpy array
import numpy as np
# ar = np.array([1,2,34,55,66,88])
# print(ar[-1])

# print(ar[0:-1:2]) - start - stop - step 
# note:isme -1 execluded hota hai 

# fancy indexing 
ar = np.array([1,2,34,55,66,88])
# print(ar[5]) 
# it only copy the original arr not impact the main one 

# filtring data 
# conditions -- true or false 

# print(ar[ar>12])


# reshaping and manipulating

# there is a method called reshape(rows , columns) 
# it not create the main arr edit 
ar = np.array([1,2,34,55,66,88])
# print(ar.reshape(3,2))


# ravel ans flatten

# print(ar.ravel()) -- view 
# print(ar.flatten()) -- copy

