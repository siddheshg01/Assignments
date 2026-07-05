def main():
    largest = lambda a, b, c: a if a >= b and a >= c else (b if b >= c else c)

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    result = largest(num1, num2, num3)

    print("Largest =", result)

if __name__ == "__main__":
    main()