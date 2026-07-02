def factorial():
    a = int(input("enter first number "))
    multi = 1
    for i in range(1,a+1):
        multi = i * multi
        
    
    print(multi)



def main():
    factorial()

if __name__ == "__main__":
    main()