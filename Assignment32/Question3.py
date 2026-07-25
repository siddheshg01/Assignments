import schedule
import time

filename = input("Enter file name: ")

def DisplayFile():
    try:
        with open(filename, "r") as file:
            data = file.read()

            if data == "":
                print("File is empty.")
            else:
                print(data)

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except OSError:
        print("File cannot be opened.")

def main():
    schedule.every(1).minutes.do(DisplayFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()