import psutil

def ShowProcesses():

    print("-" * 65)
    print("{:<30} {:<10} {:<20}".format("Process Name", "PID", "Username"))
    print("-" * 65)

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            pname = proc.info['name'] or "N/A"
            pid = proc.info['pid']
            user = proc.info['username'] or "N/A"

            print("{:<30} {:<10} {:<20}".format(pname, pid, user))

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            continue

def main():
    ShowProcesses()

if __name__ == "__main__":
    main()