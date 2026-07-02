# Accept : 2 Parameters (Integers)
# Return : Nothing

def Arithmetic(No1, No2):
    print("Addition is:", No1 + No2)
    print("Subtraction is:", No1 - No2)
    print("Multiplication is:", No1 * No2)
    print("Division is:", No1 / No2)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    Arithmetic(a, b)


if __name__ == "__main__":
    main()