def main():
    data = list(map(int, input("Enter numbers: ").split()))

    even = list(filter(lambda x: x % 2 == 0, data))

    print("Count of even numbers:", len(even))

if __name__ == "__main__":
    main()