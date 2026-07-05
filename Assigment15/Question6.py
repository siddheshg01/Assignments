from functools import reduce

def main():
    data = list(map(int, input("Enter numbers: ").split()))

    minimum = reduce(lambda x, y: x if x < y else y, data)

    print("Minimum:", minimum)

if __name__ == "__main__":
    main()