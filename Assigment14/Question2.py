def main():
    cube = lambda x: x ** 3

    num = int(input("Enter a number: "))
    result = cube(num)

    print("Cube =", result)

if __name__ == "__main__":
    main()