# 1. Number
# int - 5000
# float - 5.98
# complex - 3c + 10
# 2. Boolean
# 3. Sequence
# list - 
# 4. Mapping
# 5. set

# a = [1, 1.3, "abc", 6, 90.10]
# A = ["Ram", 21, 21,21,2.1]
# print (type(a))
# print(id(A))

# import keyword
# print(keyword.kwlist)

# indexing we get element print(my_list[3])
# through slicing alos print(my_list[2:6])


my_list = [1, 2, 3, 123, 10.5, 60, 100, 300, 400]
# print("original list: ", my_list)
# my_list.append(500)
# print("list after append", my_list)
# my_list.extend((555,333,[111,222]))
# print("after extend", my_list)
# print(my_list.sublist[1])

# pop
# removed_item = my_list.pop()
# print("removed item: ", removed_item)
# print("after pop the list is: ", my_list)

# print(my_list.index(555))

my_list = [1,2,3,4]
my_list[0] = 100
print(my_list)
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 12, [11, 22, 33, 44])
tup[-1][1] = 600
print(tup[-1][1])
