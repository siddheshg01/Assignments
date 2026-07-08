def ChkNum(no):
    if(no > 0):
        print("Positive Number")
    elif(no < 0):
        print("Negative Number")
    else:
        print("Zero")

def main():
    num = int(input("Enter a number: "))
    ChkNum(num)

if __name__ == "__main__":
    main()

#Accepts: One number
# Returns: Nothing