
def Binary(No):
    binary = ""

    while No > 0:
        rem = No % 2
        binary = str(rem) + binary
        No = No // 2

    print("Binary Equivalent:", binary)


def main():
    Value = int(input("Enter a decimal number: "))
    Binary(Value)

if __name__ == "__main__":
    main()