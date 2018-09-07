#1)Print prime numbers upto a range input by user
x= int(input("Enter the number from which prime numbers are to be printed:"))
y = int(input("Enter the number upto which prime numbers are to be printed:"))

'''First for loop gives number from 2 to the number given by user,while the
second loop checks if that number is prime or not'''
print('Prime Numbers:')
for i in range(x, y+1):
    k = 0  # A random variable
    for j in range(2, i//2+1):
        if (i % j) == 0:
            k = k+1
    if(k <= 0):
        print(i)

#2)Print Fibonacci series upto a range input by user
x = int(input("Range upto which Fibonacci are to be printed:"))
a = 0
b = 1
sum = 0
print('Fibonacci Series:')
for i in range(x):
    print(a)
    sum = a+b
    a = b
    b = sum

#3)Print factorial of number input by user
x = int(input("Range upto which Factorial are to be printed:"))
f = x
y = 1
fact = 1
for i in range(x):
    fact = fact*f
    f -= 1
print("Factorial of "+str(x)+" is "+str(fact))

#4)Convert an integer input by user into binary equivalent and vice versa
while True:
    print("Options:")
    print("Enter 1 to convert digit to binary")
    print("Enter 2 to convert binary to digit")
    print("Enter 3 to quit")
    user_input = input(': ')

    if user_input == '3':
        break
    elif user_input == '1':
        digit = int(input("Enter the Digit:"))
        binary = 0
        i = 0
        while(1):
            quot = digit//2
            rem = digit % 2
            pot = 10**i
            i = i+1
            binary = rem*pot+binary
            digit = quot
            if(digit == 0):
                break
        print("Binary to the Digit is "+str(binary))

    elif user_input == '2':
        binary = int(input("Enter the Binary:"))
        digit = 0
        i = 0
        while(1):
            quot = binary//10
            rem = binary % 10
            po2 = 2**i
            i = i+1
            digit = rem*po2+digit
            binary = quot
            if(b == 0):
                break
        print("Digit to the Binary is "+str(digit))


#5)Write a program to delete duplicate values in a list without using inbuilt function

old = [1,2,3,1,5,6,2,6,5]
new = []
for i in old:
    if i not in new:
        new.append(i)
    else:
        continue

print(new)
