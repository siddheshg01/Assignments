def main():
    Power = lambda no: 2 ** no

    value = int(input("Enter number : "))

    ret = Power(value)

    print("Output :", ret)

if __name__ == "__main__":
    main()