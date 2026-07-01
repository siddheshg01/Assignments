# write a program that contain one function chkGreater() that accepts two number and prints the grater number.
#input :10,20
#output: 20 is greater

def chkGreater():
    a = int(input("enter first number "))
    b = int(input("enter second number"))
    if(a > b ):
        print(a,"is grater")
    else:
        print(b,"is grater")



def main():
    chkGreater()

if __name__ == "__main__":
    main()