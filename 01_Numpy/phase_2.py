#Numpy indexing
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
# print("Basic indexing ",arr[3])
# print("Both value ",arr[1:6])
# print("Skip arr ",arr[1:6:2])
print("Negative indexing ",arr[-2])

# 2d array
# arr=np.array([[1,2,3,4],
#               [5,6,7,8],
#               [1,2,3,4]])
# print(arr[2]) 
# print(arr[1,2])
# print(arr[:,2])
# print(arr[0,3])

# Sorting array
# unsorted_array=np.array([1,5,87,967,44,3,6,8,43,21])
# print(np.sort(unsorted_array))  #Basic sorting 
# array2d=np.array([[3,2,7],[3,4,6]])
# print(np.sort(array2d,axis=0)) #coloum wise sorting
# print(np.sort(array2d,axis=1)) #row wise sorting

# Filter 
# numbers= np.array([1,2,3,4,5,6,7,8,9,10])
# print("Even numbers ",numbers[numbers % 2 ==0])

# Mask #indices #where
# numbers= np.array([1,2,3,4,5,6,7,8,12,10])
# mask=numbers>5
# print(numbers[mask])
# indices=[1,2,4]   #index numbers
# print(numbers[indices])
# where_result =np.where(numbers>5)
# print(where_result)
# print(numbers[where_result]) #index  number

# condition array
# condition=np.where(numbers>5,"True","False")
# print(condition)

# Adding array
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# combined=np.concatenate((arr1,arr2))#Adds the arr
# print(combined)

# add column
# orignal=np.array([[1,2,3],[4,5,6]])
# print(orignal)
# new_row=np.array([[9,5,2]])
# new_row_result=np.vstack((orignal,new_row))#Add vertical(vstack)
# print(new_row_result)
# new_column=np.array([[2,3],[3,1]]) #1st a mat 2nd b mat add coloumn
# new_column_result=np.hstack((orignal,new_column))
# print(new_column_result)

#Delete array
arr=np.array([123,113,223,534,63,6,542])
delete_array=np.delete(arr,[3])
print(delete_array)


#Arr compability
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# c=np.array([7,8,9,10])
# print(a.shape==b.shape) #return true or false accord to size like compare
# print(a.shape==c.shape) #return false

#



