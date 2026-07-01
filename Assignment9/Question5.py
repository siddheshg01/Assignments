# write a program to accept a number and check wheather it is divisible by 3 and 5.

a = int(input("Enter a number"))

if (a % 3 == 0 and a % 5== 0):
    print("the number is divisible by 3 and 5")
else:
    print("the number is not divisible by 3 and 5")