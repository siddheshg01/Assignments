import schedule
import time
import datetime
import os

filename = input("Enter file name: ")

def MonitorFile():
    with open("FileSizeLog.txt", "a") as log:

        if os.path.exists(filename):
            size = os.path.getsize(filename)

            log.write("File : " + filename + "\n")
            log.write("Size : " + str(size) + " bytes\n")
            log.write("Time : " +
                      datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") +
                      "\n\n")

            print("File size recorded.")
        else:
            print("File does not exist.")

def main():
    schedule.every(30).seconds.do(MonitorFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()