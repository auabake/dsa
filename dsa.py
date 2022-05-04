# def str(ab):
#     ab = sorted(ab)
#     for i in range(len(ab)-1):
#         if (ab[i]== ab[i+1]):
#             print(ab,'has duplicates')
#             return False
#     print(ab,'is unique')
#     return True
#
# ab = 'abcdef'
# str(ab)

# def unique(xy):
#     a = len(xy)-1
#     print(a)
# xy='abcd'
# unique(xy)


# def pm(arr):
#     k = len(arr)
#     for i in range(arr):
#         arr.count(0)        
#         if i < 0:
#             arr.count(i)
#         if i > 0:
#             arr.count(i)
# arr=[1,2,3,0]
# pm(arr)


# arr=[0,1,2,3,1]
# k = arr.count(1)
# j=len(arr)
# print(j, 'lenght')
# print(k, 'count')
# print(j/k, 'ration')


# def pm(arr):
#     k=len(arr)
#     p, n, z = 0,0,0
#     num = 0
#     for num in arr:
#         if num == 0:
#             z =1
#         if num >= 0:
#             p +=1
#         else: 

#             n -=1
# if __name__=='__main__':
#     arr=[0,1,2,3]   
#     pm(arr)  
#     print (p)
#     print (n)
#     print (z)
# def pm(k):

#     pos_count, neg_count = 0, 0

#     for num in k:
#         if num >= 0:
#             pos_count += 1
#             print("Positive numbers in the list: ", pos_count)

#         else:
#             neg_count += 1
#             print("Negative numbers in the list: ", neg_count)

# k = [10, -21, 4, -45, 66, -93, 1] 
# pm(k)

# Python3 program to find the ratio of positive,
# negative, and zero elements in the array.

# Function to find the ratio of
# positive, negative, and zero elements

# def positiveNegativeZero(arr):

# 	# Store the array length into the variable len.
# 	length = len(arr);

# 	# Initialize the postiveCount, negativeCount, and
# 	# zeroCountby 0 which will count the total number
# 	# of positive, negative and zero elements
# 	positiveCount = 0;
# 	negativeCount = 0;
# 	zeroCount = 0;

# 	# Traverse the array and count the total number of
# 	# positive, negative, and zero elements.
# 	for i in range(length):
# 		if (arr[i] > 0):
# 			positiveCount += 1;
# 		elif(arr[i] < 0):
# 			negativeCount += 1;
# 		elif(arr[i] == 0):
# 			zeroCount += 1;

# 	# Print the ratio of positive,
# 	# negative, and zero elements
# 	# in the array up to four decimal places.
# 	print("positive ratio","{0:.6f}".format((positiveCount / length)), end="\n");
# 	print("negative ratio","%1.6f "%(negativeCount / length), end="\n");
# 	print("zero ratio","%1.6f "%(zeroCount / length), end="\n");
# 	print();

# # Driver Code.
# if __name__ == '__main__':

# 	# Test Case 1:
# 	a1 = [ 2, -1, 5, 6, 0, -3 ];
# 	positiveNegativeZero(a1);

# 	# Test Case 2:
# 	a2 = [ 4, 0, -2, -9, -7, 1 ];
# 	positiveNegativeZero(a2);

# # This code is contributed by Rajput-Ji

# arr = (1,2,3)
# print(sum(arr))


# from pygorithm.sorting import bubble_sort
# my_list = [12, 4, 2, 14, 3, 7, 5]
# k = bubble_sort.sort(my_list)
# print(k)


from pygorithm.data_structures.stack import Stack

r = Stack()
print(r.get_code())


# from pygorithm.sorting import merge_sort

# my_list = [12, 4, 2, 14, 3, 7, 5]
# k = merge_sort.sort(my_list)
# print(k)
# print(merge_sort.get_code())


from pygorithm.data_structures.linked_list import DoublyLinkedList
x = DoublyLinkedList()
print (x.get_code())


























