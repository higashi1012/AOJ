def main():
    a, b = map(int, input().split())
    d = a // b
    r = a % b
    f = round((a / b), 5)
    print(d, r, f)

if __name__ == '__main__':
    main()