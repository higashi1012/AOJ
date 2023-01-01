def main():
    a, b, c = map(int, input().split())
    print('Yes' if a<b<c else 'No')
    
    '''
    if a < b < c:
        print('Yes')
    else:
        print('No')
    '''

if __name__ == '__main__':
    main()