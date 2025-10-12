# Numpy advanced - add remove stack split matrics


'''
np.insert(array, index ,value,axis=none)
array - origional array
index - 
value - 
axis - 0 , row wise 
1 column wise 
'''

import numpy as np

# ar = np.array([1,2,34,55,66,88])
# print(ar)
# newarr = np.insert(ar,0,7)
# print(newarr)

# ===================================
# HOW TO INSERT IN 2D 


# ar = np.array([[1,2,55],
#               [77,66,88]])
# print(ar)/

# newarr = np.insert(ar,1,[108,1 ,9], axis = 0)
# print(newarr)


# ======================================
# APPEND , CONCATINATE AND REMOVE 
# ======================================

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4,5,6])
# new = np.concatenate((arr1,arr2))
# new2 = np.append((arr1,arr2))
# print(new)
# print(new2)

'''
np.delete(array, index, axis= none)
flattern array
'''

# arr =np.array([[1, 2 , 3],[4, 5, 6]])
# new_arr = np.delete(arr, 0 , axis = 0)
# print(new_arr)


# ==========================================
# # STACKING (HORIZONTALLY AND VERTICALLY)
# ==========================================

'''
vertically , horizontally 
vstack() and hstack()
'''

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4,5,6])
# print(np.vstack((arr1,arr2)))
# print(np.hstack((arr1, arr2)))



# =====================================
# split 
# =====================================

'''
np.split()
equal

np.vsplit()
np.hsplit()
'''

# ar = np.array([1,2,34,55,66,88])
# print(np.split(ar, 3))