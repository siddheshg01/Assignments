import psutil
import os
import sys
from datetime import datetime

def CreateProcessLog(folder):

    if not os.path.exists(folder):
        os.mkdir(folder)

    logfile = os.path.join(
        folder,
        "ProcessLog_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".log"
    )

    with open(logfile, "w") as file:

        file.write("=" * 60 + "\n")
        file.write("RUNNING PROCESS REPORT\n")
        file.write("=" * 60 + "\n\n")

        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:

                file.write(f"Process : {proc.info['name'] or 'N/A'}\n")
                file.write(f"PID     : {proc.info['pid']}\n")
                file.write(f"User    : {proc.info['username'] or 'N/A'}\n")
                file.write("-" * 40 + "\n")

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                continue

    print("Log created successfully.")
    print(logfile)

def main():

    if len(sys.argv) != 2:
        print("Usage : python ProcessLogger.py FolderName")
        return

    CreateProcessLog(sys.argv[1])

if __name__ == "__main__":
    main()