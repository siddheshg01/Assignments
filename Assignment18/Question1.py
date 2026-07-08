def Addition(arr):
    sum = 0

    for i in arr:
        sum = sum + i

    return sum

def main():
    size = int(input("Enter number of elements: "))

    data = []

    for i in range(size):
        no = int(input("Enter element: "))
        data.append(no)

    ans = Addition(data)

    print("Addition =", ans)

if __name__ == "__main__":
    main()