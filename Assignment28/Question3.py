def main():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            for line in file:
                print(line, end="")

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()