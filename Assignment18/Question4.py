def Frequency(arr, value):
    count = 0

    for i in arr:
        if(i == value):
            count = count + 1

    return count

def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        no = int(input("Enter element: "))
        data.append(no)

    search = int(input("Enter element to search: "))

    ans = Frequency(data, search)

    print("Frequency =", ans)

if __name__ == "__main__":
    main()