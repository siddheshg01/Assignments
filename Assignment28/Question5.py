def main():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        if word in data:
            print("Word found.")
        else:
            print("Word not found.")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()