def main():
    S = int(input())
    h = S // 3600
    m = (S % 3600) // 60
    s = S % 60
    print(f'{h}:{m}:{s}')
    # print('{}:{}:{}'.format(h,m,s))
    
if __name__ == '__main__':
    main()