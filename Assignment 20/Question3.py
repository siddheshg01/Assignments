import threading

def EvenList(arr):
    print("Even Numbers:")
    for i in arr:
        if(i % 2 == 0):
            print(i)


def OddList(arr):
    print("Odd Numbers:")
    for i in arr:
        if(i % 2 != 0):
            print(i)


def main():

    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        no = int(input("Enter element : "))
        data.append(no)

    t1 = threading.Thread(target=EvenList, args=(data,))
    t2 = threading.Thread(target=OddList, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()