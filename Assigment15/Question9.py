from functools import reduce

def main():
    data = list(map(int, input("Enter numbers: ").split()))

    product = reduce(lambda x, y: x * y, data)

    print("Product:", product)

if __name__ == "__main__":
    main()