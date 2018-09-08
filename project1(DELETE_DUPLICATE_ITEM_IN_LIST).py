# Python Code for Deleting Duplicate values in a user defined List
Empty_list = []
size = int(input("Enter the size of List"))
for i in range(size):
    numbers = int(input('Enter position element in list'))
    Empty_list.append(numbers)
Empty_list.sort()
j=len(Empty_list) - 1
while j > 0:
    if Empty_list[j] == Empty_list[j-1]:
        Empty_list.pop(j)
    j = j-1
print(Empty_list)



