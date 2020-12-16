a=int(input("Enter a value:"))
b=int(input("Enter b value:"))

#logic for GCD
if(a<b):
    small=a
else:
    small=b
for i in range(1,small+1):
    if(a%i==0 and b%i==0):
        gcf=i

#logic for LCM
lcm=(a*b)/gcf

print("GCM of a and b is",gcf)
print("LCM of a and b is",lcm)
