def main():
    data = list(map(int, input("Enter numbers: ").split()))

    even = list(filter(lambda x: x % 2 == 0, data))

    print("Even numbers:", even)

if __name__ == "__main__":
    main()