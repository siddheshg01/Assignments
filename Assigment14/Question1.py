def main():
    square = lambda x: x * x

    num = int(input("Enter a number: "))
    result = square(num)

    print("Square =", result)

if __name__ == "__main__":
    main()