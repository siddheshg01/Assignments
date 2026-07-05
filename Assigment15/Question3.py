def main():
    data = list(map(int, input("Enter numbers: ").split()))

    odd = list(filter(lambda x: x % 2 != 0, data))

    print("Odd numbers:", odd)

if __name__ == "__main__":
    main()