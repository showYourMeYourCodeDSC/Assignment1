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


