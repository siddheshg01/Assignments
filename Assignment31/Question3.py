import schedule
import time
import datetime
import os

directory = input("Enter directory path: ")

def ScanDirectory():
    files = 0
    folders = 0

    for item in os.listdir(directory):
        path = os.path.join(directory, item)

        if os.path.isfile(path):
            files += 1
        elif os.path.isdir(path):
            folders += 1

    print("Directory Scanned :", directory)
    print("Total Files :", files)
    print("Total Subdirectories :", folders)
    print("Scan Time :", datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(ScanDirectory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()