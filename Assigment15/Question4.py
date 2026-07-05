from functools import reduce

def main():
    data = list(map(int, input("Enter numbers: ").split()))

    total = reduce(lambda x, y: x + y, data)

    print("Addition:", total)

if __name__ == "__main__":
    main()