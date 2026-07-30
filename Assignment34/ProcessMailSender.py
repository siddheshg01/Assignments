import psutil
import os
import sys
import smtplib
from datetime import datetime
from email.message import EmailMessage

SENDER_EMAIL = "*******"
APP_PASSWORD = "***********"

def GenerateLog(folder):

    if not os.path.exists(folder):
        os.mkdir(folder)

    logfile = os.path.join(
        folder,
        "ProcessLog_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".log"
    )

    with open(logfile, "w") as file:

        file.write("Running Process Report\n")
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

    return logfile


def SendEmail(receiver, logfile):

    message = EmailMessage()

    message["Subject"] = "Running Process Report"
    message["From"] = SENDER_EMAIL
    message["To"] = receiver

    message.set_content("Please find the attached process log.")

    with open(logfile, "rb") as file:
        data = file.read()

    message.add_attachment(
        data,
        maintype="application",
        subtype="octet-stream",
        filename=os.path.basename(logfile)
    )

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(message)
    server.quit()

    print("Email sent successfully.")

def main():

    if len(sys.argv) != 3:
        print("Usage : python ProcessMailSender.py FolderName EmailID")
        return

    logfile = GenerateLog(sys.argv[1])

    SendEmail(sys.argv[2], logfile)

if __name__ == "__main__":
    main()