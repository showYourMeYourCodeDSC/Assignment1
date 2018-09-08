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

