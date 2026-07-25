def main():
    filename = input("Enter file name: ")
    word = input("Enter string: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        count = data.count(word)
        print("Frequency:", count)

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()