def main():
    data = input("Enter strings: ").split()

    result = list(filter(lambda x: len(x) > 5, data))

    print("Strings:", result)

if __name__ == "__main__":
    main()