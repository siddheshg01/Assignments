def main():
    odd = lambda x: x % 2 != 0

    num = int(input("Enter a number: "))

    result = odd(num)

    print(result)

if __name__ == "__main__":
    main()