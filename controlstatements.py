temperature = 45

if temperature > 25:
    print("It is too hot")
else:
    print("It is too cold")

#A program that checks three numbers and returns the smallest value

num1 = 78
num2 = 15
num3 = 90

if num1 < num2 and num3 < num2:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest  number")
else:
    print(num2, "is the smallest number")
