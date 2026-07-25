import schedule
import time
import datetime

def WriteData():
    with open("Marvellous.txt", "a") as file:
        file.write("Task executed at : " +
                   datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") +
                   "\n")

    print("Data written successfully.")

def main():
    schedule.every(5).minutes.do(WriteData)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()