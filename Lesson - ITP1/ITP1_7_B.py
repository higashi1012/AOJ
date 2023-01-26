def main():

    cnt = 0
    while True:
        n, x = map(int, input().split())
        cnt = 0
        if n == x == 0: break
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                k = x - i - j
                if j < k <= n:
                    cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()