def NameLength(name):
    return len(name)

def main():
    name = input("Enter your name: ")

    ans = NameLength(name)
    print("Length =", ans)

if __name__ == "__main__":
    main()