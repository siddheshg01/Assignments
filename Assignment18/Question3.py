def Minimum(arr):
    min = arr[0]

    for i in arr:
        if(i < min):
            min = i

    return min

def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        no = int(input("Enter element: "))
        data.append(no)

    ans = Minimum(data)

    print("Minimum =", ans)

if __name__ == "__main__":
    main()