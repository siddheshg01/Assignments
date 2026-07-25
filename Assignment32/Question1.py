import schedule
import time
import datetime

def CreateFile():
    filename = "File_" + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(filename, "w") as file:
        file.write("Filename : " + filename + "\n")
        file.write("Creation Date : " + datetime.datetime.now().strftime("%d-%m-%Y") + "\n")
        file.write("Creation Time : " + datetime.datetime.now().strftime("%I:%M:%S %p"))

    print("File created:", filename)

def main():
    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()