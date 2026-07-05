def main():
    data = list(map(int, input("Enter numbers: ").split()))

    result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, data))

    print("Numbers:", result)

if __name__ == "__main__":
    main()