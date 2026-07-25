import sys

def main():
    if len(sys.argv) != 2:
        print("Usage : python program.py ABC.txt")
        return

    source = sys.argv[1]
    destination = "Demo.txt"

    try:
        with open(source, "r") as src:
            data = src.read()

        with open(destination, "w") as dest:
            dest.write(data)

        print("Contents copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")

if __name__ == "__main__":
    main()