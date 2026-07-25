import schedule
import time
import os

directory = input("Enter directory path: ")

def DeleteEmptyFiles():
    with open("DeleteLog.txt", "a") as log:

        for folder, subfolders, files in os.walk(directory):

            for file in files:
                path = os.path.join(folder, file)

                try:
                    if os.path.getsize(path) == 0:
                        os.remove(path)
                        log.write(path + " deleted\n")

                except PermissionError:
                    log.write(path + " permission denied\n")

    print("Scan completed.")

def main():
    schedule.every(1).hours.do(DeleteEmptyFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()