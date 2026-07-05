def main():
    maximum = lambda a, b: a if a > b else b

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = maximum(num1, num2)

    print("Maximum =", result)

if __name__ == "__main__":
    main()