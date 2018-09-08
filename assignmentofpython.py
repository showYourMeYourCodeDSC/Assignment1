#Printing prime nos. 
r=int(input("Enter upper limit: "))
for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)

#Fibonacci series
print("Fibonacci series is")
x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y


#Print factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

#Decimal to binary
def decimalTobinary(n):
    if(n>1):
        decimalTobinary(n//2)
    print(n%2)

n=int(input())    

if __name__=='__main__':

    result=decimalTobinary(n)


#To duplicate 

b = [10,20,30,20,10,50,60,40,80,50,40]

dup = set()
uniq = []
for x in a:
    if x not in dup:
        uniq.append(x)
        dup.add(x)

print(dup)
