

#Prime Numbers

N = int(input("Enter the numbers till where you want Prime Numbers"))
for i in range(1 , N):
    fact = 0
    for j in range(1 ,N):
        if i % j == 0:
            fact = fact+1
    if fact == 2:
        print(i)
