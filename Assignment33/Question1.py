import os
import hashlib
import schedule
import time
import datetime

# Calculate checksum of a file
def Checksum(path):
    hashobj = hashlib.md5()

    with open(path, "rb") as file:
        while True:
            data = file.read(1024)

            if not data:
                break

            hashobj.update(data)

    return hashobj.hexdigest()


# Find duplicate files
def FindDuplicate(directory):
    duplicate = {}

    for folder, subfolder, files in os.walk(directory):

        for file in files:

            filepath = os.path.join(folder, file)

            try:
                value = Checksum(filepath)

                if value in duplicate:
                    duplicate[value].append(filepath)
                else:
                    duplicate[value] = [filepath]

            except Exception:
                pass

    return duplicate


# Delete duplicate files
def DeleteDuplicate(directory):

    duplicates = FindDuplicate(directory)

    logfile = open("DuplicateLog.txt", "a")

    logfile.write("\n---------------------------------\n")
    logfile.write(str(datetime.datetime.now()) + "\n")

    for value in duplicates.values():

        if len(value) > 1:

            logfile.write("\nDuplicate Files:\n")

            for file in value:
                logfile.write(file + "\n")

            for file in value[1:]:
                try:
                    os.remove(file)
                    logfile.write("Deleted : " + file + "\n")
                except Exception:
                    logfile.write("Unable to delete : " + file + "\n")

    logfile.close()

    print("Scanning Completed...")


# Main Function
def main():

    directory = input("Enter directory path : ")

    if not os.path.isdir(directory):
        print("Invalid Directory")
        return

    schedule.every(10).minutes.do(DeleteDuplicate, directory)

    print("Automation Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()  