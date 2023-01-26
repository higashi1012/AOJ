def main():

    while True:
        x = input()
        if x == '0': break
        print(sum([int(i) for i in x]))

    '''
    while True:
        x = input()
        s = 0
        if x == '0': break
        for i in x:
            s += int(i)
        print(s)
    '''

if __name__ == '__main__':
    main()