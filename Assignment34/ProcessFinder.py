import psutil
import sys

def SearchProcess(process_name):

    found = False

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:

            pname = proc.info['name']

            if pname and pname.lower() == process_name.lower():

                found = True

                print("\nProcess Found")
                print("-" * 35)
                print("Name     :", proc.info['name'])
                print("PID      :", proc.info['pid'])
                print("Username :", proc.info['username'])

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            continue

    if not found:
        print("Process not found.")

def main():

    if len(sys.argv) != 2:
        print("Usage : python ProcessFinder.py ProcessName")
        return

    SearchProcess(sys.argv[1])

if __name__ == "__main__":
    main()