
def Perfect(No):
    sum = 0

    for i in range(1, No):
        if No % i == 0:
            sum = sum + i

    if sum == No:
        return True
    else:
        return False


def main():
    Value = int(input("Enter a number: "))

    ret = Perfect(Value)

    if ret == True:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


if __name__ == "__main__":
    main()