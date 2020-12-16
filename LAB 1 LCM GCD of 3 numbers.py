a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

# Calculation of GCD 
gcd1 = gcd(a,b)
gcd2 = gcd(gcd1,c) # GCD of 3 numbers

# Calculation of LCM
lcm1 = a*b//gcd1
lcm2 = c*lcm1//gcd(c,lcm1) # GCD of 3 numbers

# Printing the answer
print("The GCD of 3 numbers is " + str(gcd2) + " and the LCM is "+ str(lcm2))
