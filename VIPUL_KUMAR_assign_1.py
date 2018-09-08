#Factorial of a Number
factIn = int(input("Enter a the number for it's factorial "))
a = 1
for i in range(1, factIn+1):
    a = a * i
print(a)


# Integer to Binary
def intToBinary(n):
    k = ""
    while n > 0:
        k = k+str(n%2)
        n = int(n/2)
    return k
def reverse(a):
  str = ""
  for i in a:
    str = i + str
  return str
inp=int(input("Enter the number to be Converted into Binary"))
s = intToBinary(inp)
print(reverse(s))


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





# FIBONACCI
nterms = int(input("Enter the range of Fabonacci series"))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
    print("Please enter a valid range")
elif nterms == 1:
    print("0")
else:
    while count < nterms:
        print(n1 , end=' , ')
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1




#Prime Numbers

N = int(input("Enter the numbers till where you want Prime Numbers"))
for i in range(1 , N):
    fact = 0
    for j in range(1 ,N):
        if i % j == 0:
            fact = fact+1
    if fact == 2:
        print(i)
