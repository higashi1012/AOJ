def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(min(a), max(a), sum(a))

if __name__ == '__main__':
    main()