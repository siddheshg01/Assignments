def main():
    addition = lambda a, b: a + b

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = addition(num1, num2)

    print("Addition =", result)

if __name__ == "__main__":
    main()