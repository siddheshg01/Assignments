def main():
    multiply = lambda a, b: a * b

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = multiply(num1, num2)

    print("Multiplication =", result)

if __name__ == "__main__":
    main()