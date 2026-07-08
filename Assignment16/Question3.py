def Add(a, b):
    return a + b

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    ans = Add(num1, num2)
    print("Addition =", ans)

if __name__ == "__main__":
    main() 
#Accepts: Two numbers
#Returns: Addition