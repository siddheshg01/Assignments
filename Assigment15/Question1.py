def main():
    data = list(map(int, input("Enter numbers: ").split()))

    square = list(map(lambda x: x * x, data))

    print("Squares:", square)

if __name__ == "__main__":
    main()