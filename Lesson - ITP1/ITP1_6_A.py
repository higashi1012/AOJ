def main():
    n = int(input())
    a = reversed(list(map(int, input().split())))
    print(*a)

if __name__ == '__main__':
    main()