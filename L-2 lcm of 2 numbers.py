a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

# Logic
if a >= b:
    lar = a
    sm = b
else:
    lar = b
    sm = a
dup = lar
while True:
    # checking 
    if (dup % sm == 0):
        ans = dup
        break
    # increasing 
    dup += lar
