def main():
    minimum = lambda a, b: a if a < b else b

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = minimum(num1, num2)

    print("Minimum =", result)

if __name__ == "__main__":
    main()