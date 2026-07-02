def reverse(n):
   
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10  
        
    return rev


def main():
  a = int(input("Enter a number: "))
  c= reverse(a)
  print("Reversed number:", c)


if __name__ == "__main__":
    main()