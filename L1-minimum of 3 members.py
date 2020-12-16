num1 = float(input("ENTER THE FIRST NUMBER:"))
num2 = float(input("ENTER THE SECOND NUMBER:"))
num3 = float(input("ENTER THE THIRD NUMBER:"))

#LOGIC
if(num1<num2) and (num1<num3):
    minimum = num1
elif(num2<num1) and (num2<num3):
    minimum = num2
else:
    minimum = num3
print("The minimum of 3 numbers:",minimum)
