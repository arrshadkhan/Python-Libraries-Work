import numpy as np
# array_1 =np.array([1,2,3,4,7])
# print("array1 ",array_1)
# array_2=np.array([[9,76,543,0],[1,2,3,4]])
# print("array2 ",array_2)

#multiplication in list vs array
list=[1,2,3]
print("List ",list*2)
array=np.array([1,2,3])
print("Array1 ",array*2)

#time efficiancy
# import time
# start =time.time()
# list=[i*2 for i in range(100000)]
# print("time taken in list",time.time()-start)
# start=time.time()
# array=np.arange(100000)*2           #array more efficiant
# print("time taken in array",time.time()-start)

#creating array from scratch as we have func to use
# zeros =np.zeros((3,3))
# print("Zeros func \n",zeros)
# one=np.ones((2,3))
# print("one \n",one)
# full=np.full((2,3),7)
# print("full matrix with 7\n",full)
# random=np.random.random((2,3))
# print(random)
# arange=np.arange(1,11)
# print("generate 1 to 10",arange)

#Vector , Matrix,Tensor
# vector=np.array([1,2,3,4,5])
# print("Vector\n",vector)
# matrix=np.array([[1,2,3,4,5],[6,7,8,9,0]]) #2d
# print("Matrix\n",matrix)
# tensor=np.array([[[1,2,3],[4,5,6]],  
#                  [[7,8,9],[0,1,1]]])
# print("tensor\n",tensor)

# Array properties
# arr= np.array([[1,2,3],[7,8,9]])
# print("Array shape",arr.shape)
# print("Array Dimensions",arr.ndim)
# print("Array size",arr.size)
# print("Array type",arr.dtype)

#Array reshaped
# arr=np.arange(1,12+1)
# print(arr)
# reshape=arr.reshape((3,4))
# print(reshape)
# flatten=reshape.flatten() #return copy array
# print(flatten)
# ravel=reshape.ravel() # return origanal array
# print(ravel)
# transpose=reshape.T
# print(transpose)