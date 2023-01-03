def main():
    '''
    cnt = 1
    x = 0
    while True:
        x = int(input())
        if x == 0: break
        print(f'Case {cnt}: {x}')
        cnt += 1
    '''
    for i in range(1, 10001):
        x = int(input())
        if x == 0: break
        print(f'Case {i}: {x}')

if __name__ == '__main__':
    main()