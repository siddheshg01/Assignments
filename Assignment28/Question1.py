def main():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            count = 0

            for line in file:
                count += 1

        print("Total number of lines:", count)

    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()