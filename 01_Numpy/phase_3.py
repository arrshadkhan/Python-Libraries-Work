import numpy as np
# import matplotlib as plt
import matplotlib.pyplot as plt

# Data structure years =(resturent id ,2021,2022,2023,2024)

# sales_data = np.array(
#     [
#         [1, 1, 2, 3, 4],
#         [2, 5, 6, 7, 8],
#         [3, 9, 0, 3, 1],
#         [4, 1, 9, 2, 3],
#         [5, 1, 5, 5, 4],
#     ]
# )
# print("\n====== Resturents sales analysis ======\n")
# # print(sales_data.shape,"\n")
# total_2021 = np.sum(sales_data[:,1], axis=0)
# print(f"total sale of 2021 is: {total_2021} cr in india.")
# total_2022 = np.sum(sales_data[:,2], axis=0)
# print(f"total sale of 2022 is: {total_2022} cr in india.")
# total_2023 = np.sum(sales_data[:,3], axis=0)
# print(f"total sale of 2023 is: {total_2023} cr in india.")
# total_2024 = np.sum(sales_data[:,4], axis=0)
# print(f"total sale of 2024 is: {total_2024} cr in india.\n")
# print("MIN SALE")
# min_sale =np.min(sales_data[:,0:2],axis=0)
# print(min_sale)
# print("\nMAX SALE")
# max_sale = np.max(sales_data[:,1:],axis=0)
# print(max_sale)
# print("\nAVG SALE")
# avg_sale = np.mean(sales_data[:,1:],axis=0)
# print(avg_sale)

# cumsun = np.cumsum(sales_data[:,1:],axis=1)
# print(cumsun)

# plt.plot(np.mean(cumsun,axis=1))
# plt.figure(figsize=(8,6))
# plt.title("Average cumulative sales accross all resturents ")
# plt.xlabel("years")
# plt.ylabel("sales")
# plt.grid(True)
# plt.show()

#vector add,mul,dot
# vector1=np.array([1,2,3,4,5])
# vector2=np.array([6,7,8,9,10])
# print("Addition: ",vector1 + vector2)
# print("\nMultiplication: ",vector1 * vector2)
# print("\nAddition: ",np.dot(vector1 , vector2))

#Vectorized upper character
resturant_menu = np.array(['biryani','chikan','dal','rice','piazza','salat'])
vectorized_upper=np.vectorize(str.upper)
print("Upper vector: ",vectorized_upper(resturant_menu))