def main():
    '''
    while True:
        a, b = sorted((map(int, input().split())))
        if a == b == 0: break
        print(a, b)
    '''
    for _ in range(3001):
        a, b = sorted(map(int, input().split()))
        if a == b == 0: break
        print(a, b)

if __name__ == '__main__':
    main()