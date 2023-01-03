def main():
    while True:
        a, op, b = input().split()
        if op == '+':
            print(int(a)+int(b))
        if op == '-':
            print(int(a)-int(b))
        if op == '*':
            print(int(a)*int(b))
        if op == '/':
            print(int(a)//int(b))
        if op == '?':
            break

if __name__ == '__main__':
    main()