#1)Print prime numbers upto a range input by user

x=int(input("Enter  Lower Number:"))
y=int(input("Enter  Upper Number:"))
print("PRIME NUMBERS:")
for i in range(x,y+1):
    count=0
    for j in range(2,i//2+1):
        if (i%j)==0:
            count=count+1
    if(count<=0):
        print(i)


#2)Print Fibonacci series upto a range input by user

n=int(input("Enter start range:"))
m=int(input("Enter end range:"))
a=0
b=1
if(n==0 and m==1):
    print(a)
    print(b)
    print(b)
elif(n==0 and m==0):
    print(a)
elif(n==1 and m==1):
    print(b)
    print(b)

elif(m>=2):
    if(n==0 ):
        print(a)
    print(b)
    while(1):
        c=a+b
        if(n <= c and c<=m):
            print(c)
        a=b
        b=c
        if (c>m):
            break


#3)Print factorial of number input by user

n=int(input("ENTER NUMBER: "))
f=1
for i in range(n):
    f=f*(i+1)

print("Factorial of",n,"is",f)







#4)Convert an integer input by user into binary equivalent and vice versa

#BINARY TO INTEGER
count=0
INTEGER=0
i=0

x=int(input("Enter Binary Number:"))
i=x
while(i>0):
    count=count+1
    i=i//10
for j in range (count):
    dig=(x%10)*(2**j)
    INTEGER=INTEGER+dig
    x=x//10
print("INTEGER:",INTEGER)





#INTEGER TO BINARY
x=[]
y=int(input("Enter the Integer:"))
while(1):
    q=y//2
    r=y%2
    x.append(r)
    y=q
    if(y==0):
        break
x.sort(reverse=True)
b=''.join(str(i) for i in x)
print(b)


#5)Write a program to delete duplicate values in a list without using inbuilt function

x=[1,5,1,7,5,8,7,6,5]
x.sort()
y=len(x)
i=y-1
while(i>0):
    if (x[i]==x[i-1]):
        x=x[ :i] + x[i+1: ]
        i=i-1
    else:
        i=i-1
        continue

print(x)
