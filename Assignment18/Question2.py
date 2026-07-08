def Maximum(arr):
    max = arr[0]

    for i in arr:
        if(i > max):
            max = i

    return max

def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        no = int(input("Enter element: "))
        data.append(no)

    ans = Maximum(data)

    print("Maximum =", ans)

if __name__ == "__main__":
    main()