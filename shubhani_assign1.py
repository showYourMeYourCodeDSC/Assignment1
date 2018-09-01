print("prime number upto a range as input by the user")
x=int(input("enter the lower bound:"))
y=int(input("enter the upper bound:"))
for n in range(x,y+1):
    k=0
    for i in range(2,n//2+1):
        if (n%i)==0:
            k=k+1
    if(k<=0):
        print(n)


print ("fibonacci series upto a range input by the user")
x=int(input("enter the lower bound"))
y=int(input("enter the upper bound:"))
a = 0
b = 1
if x==1 and y>1:
    print(a,"\n",b)
if x==1 and y==1:
    print(a)

while(1):
    c=a+b
    if(x<c and c<y):
       print(c)
    a=b
    b=c
    if(c>y):
        break


print("factorial of number input by the user")
num=int(input("enter the number whose factorial is to be calculated:"))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print(fact)

print("convert an integer input by user into binary and vice versa")
print("convert in binary")
res=0
count=0
sum=0
flag=0
a=[]
y=int(input("enter the number in binary:"))
flag=y
while(flag>0):
    res=flag%10
    count=count+1
    flag=flag//10
for i in range (0,count):
    dig=(y%10)*(2**i)
    sum=sum+dig
    y=y//10
print(sum)
print("convert in integer")
y=int(input("enter the integer:"))
while(1):
    quo=y//2
    rem=y%2
    a.append(rem)
    y=quo
    if(y==0):
        break
a.sort(reverse=True)
print(a)

print("program to delete duplicate values in a list without using inbuilt function")
x=[1,2,1]
x.sort()
i = len(x) - 1
while i > 0:
    if x[i] == x[i - 1]:
        x.pop(i)
    i -= 1
print(x)
