def main():
    div5 = lambda x: x % 5 == 0

    num = int(input("Enter a number: "))

    result = div5(num)

    print(result)

if __name__ == "__main__":
    main()