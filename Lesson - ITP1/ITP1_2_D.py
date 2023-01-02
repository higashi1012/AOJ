def main():
    w, h, x, y, r = list(map(int, input().split()))
    if 0 <= x-r and x+r <= w and 0 <= y-r and y+r <= h:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()