def main():
    while True:
        h, w = map(int, input().split())
        if h == w == 0:
            break
        for i in range(1, h+1):
            if i == 1 or i == h:
                print('#' * w)
            else:
                print('#' + '.'*(w-2) + '#')
        print()

if __name__ == '__main__':
    main()