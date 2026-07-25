import schedule
import time
import datetime

def CreateLog():
    name = "MarvellousLog_" + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(name, "w") as file:
        file.write("Log file created successfully.\n")
        file.write("Creation Time : " +
                   datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

    print("Log file created:", name)

def main():
    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()