import schedule
import time
import datetime
import os

directory = input("Enter directory path: ")

def CountFiles():
    count = 0

    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            count += 1

    with open("DirectoryCountLog.txt", "a") as file:
        file.write("Directory : " + directory + "\n")
        file.write("Files : " + str(count) + "\n")
        file.write("Time : " +
                   datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") +
                   "\n\n")

    print("Information written successfully.")

def main():
    schedule.every(5).minutes.do(CountFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()