import schedule
import time
import shutil

source = input("Enter source file name: ")
destination = input("Enter backup file name: ")

def Backup():
    try:
        shutil.copy(source, destination)
        print("Backup completed.")
    except FileNotFoundError:
        print("Source file not found.")

def main():
    schedule.every(1).hours.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()