import math

def main():
    r = float(input())
    area = round(math.pi * r ** 2, 6)
    circumference_length = round(2 * math.pi * r, 6)
    print(area, circumference_length)

if __name__ == '__main__':
    main()