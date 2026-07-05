from functools import reduce

def main():
    data = list(map(int, input("Enter numbers: ").split()))

    maximum = reduce(lambda x, y: x if x > y else y, data)

    print("Maximum:", maximum)

if __name__ == "__main__":
    main()