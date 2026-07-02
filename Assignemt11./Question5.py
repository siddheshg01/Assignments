
def CheckPalindrome(n):

    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    if original == rev:
        return True
    else:
        return False

def main():
    a = int(input("Enter a number: "))

    ret = CheckPalindrome(a)

    if ret == True:
        print(a, "is a Palindrome Number")
    else:
        print(a, "is Not a Palindrome Number")


if __name__ == "__main__":
    main()