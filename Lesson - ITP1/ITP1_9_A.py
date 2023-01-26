def main():

    w = input()
    cnt = 0

    while True:
        t = input()
        if t == 'END_OF_TEXT': break
        cnt += t.lower().split().count(w)

    print(cnt)

if __name__ == '__main__':
    main()