def main():
    n = int(input())
    for i in range(1, n+1):
        if i % 3 == 0 or '3' in str(i):
            print('',i, end='')

if __name__ == '__main__':
    main()