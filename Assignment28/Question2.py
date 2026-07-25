def main():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        words = data.split()

        print("Total number of words:", len(words))

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()