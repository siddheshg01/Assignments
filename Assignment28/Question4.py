def main():
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    try:
        with open(source, "r") as file1:
            data = file1.read()

        with open(destination, "w") as file2:
            file2.write(data)

        print("Contents copied successfully.")

    except FileNotFoundError:
        print("Source file not found.")

if __name__ == "__main__":
    main()