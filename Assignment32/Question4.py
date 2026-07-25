import schedule
import time
import os
import shutil

source = input("Enter source directory: ")
destination = input("Enter destination directory: ")

def CopyFiles():
    if not os.path.isdir(source) or not os.path.isdir(destination):
        print("Invalid directory.")
        return

    with open("CopyLog.txt", "a") as log:
        for file in os.listdir(source):

            if file.endswith(".txt"):
                src = os.path.join(source, file)
                dest = os.path.join(destination, file)

                try:
                    shutil.copy(src, dest)
                    log.write(file + " copied successfully\n")

                except Exception:
                    log.write(file + " could not be copied\n")

    print("Copy operation completed.")

def main():
    schedule.every(10).minutes.do(CopyFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()