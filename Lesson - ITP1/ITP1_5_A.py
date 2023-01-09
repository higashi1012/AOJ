def main():
    while True:
        h, w = map(int, input().split())
        if h == w == 0:
            break
        for _ in range(h):
            print('#' * w)
        print()

if __name__ == '__main__':
    main()