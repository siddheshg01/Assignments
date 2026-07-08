import threading

def Small(text):
    count = 0

    for ch in text:
        if ch.islower():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase letters :", count)


def Capital(text):
    count = 0

    for ch in text:
        if ch.isupper():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase letters :", count)


def Digits(text):
    count = 0

    for ch in text:
        if ch.isdigit():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", count)


def main():

    str1 = input("Enter a string : ")

    t1 = threading.Thread(target=Small, args=(str1,), name="Small")
    t2 = threading.Thread(target=Capital, args=(str1,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(str1,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()