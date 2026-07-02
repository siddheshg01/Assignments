# write a program which accept one character and check whether it is vowel or consonant.


a = input("Enter a character: ")
if a in "aeiou" or a in "AEIOU":
    print("The character is a vowel.")
else:
    print("The character is a consonant.")