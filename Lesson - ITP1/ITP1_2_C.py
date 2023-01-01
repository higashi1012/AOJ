def main():
    a = sorted((map(int, input().split())))
    print(*a)
    
    '''
    a, b, c = map(int, input().split())
    if a <= b <= c:
        print(a, b, c)
    elif a <= c <= b:
        print(a, c, b)
    elif b <= a <= c:
        print(b, a, c)
    elif b <= c <= a:
        print(b, c, a)
    elif c <= a <= b:
        print(c, a, b)
    else:
        print(c, b, a)
    '''
    
    '''
    a, b, c = sorted((map(int, input().split())))
    print(a, b, c)
    '''
    
    '''
    a = sorted(list(map(int, input().split())))
    print(*a)
    '''
    
    '''
    a = sorted(tuple(map(int, input().split())))
    print(*a)
    '''
    
    '''
    a = list(map(int, input().split()))
    a.sort()
    print(*a)
    '''

if __name__ == '__main__':
    main()