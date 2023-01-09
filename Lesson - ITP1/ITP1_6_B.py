def main():
    mark = ['S', 'H', 'C', 'D']
    num = [i for i in range(1, 14)]
    card = [j+' '+str(k) for j in mark for k in num]
    n = int(input())
    for _ in range(n):
        a = input()
        card.remove(a)
        
    for l in card:
        print(l)


if __name__ == '__main__':
    main()