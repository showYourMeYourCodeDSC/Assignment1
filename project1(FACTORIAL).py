#Factorial of a Number
factIn = int(input("Enter a the number for it's factorial "))
a = 1
for i in range(1, factIn+1):
    a = a * i
print(a)