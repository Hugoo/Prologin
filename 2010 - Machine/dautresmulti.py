import sys


def autres_mults(n, m, numbers):
    nearest = [abs(n-numbers[0]*numbers[1]),numbers[0]*numbers[1]]
    i = 0
    while i!=m:
        for i2 in range(i+1,m):
            temp = n-numbers[i]*numbers[i2]
            if abs(temp)<nearest[0]:
                nearest[0]=abs(temp)
                nearest[1]=temp+n
        i+=1
    return nearest[1]


if __name__ == '__main__':
    n = int(raw_input())
    m = int(raw_input())
    numbers = [int(_) for _ in raw_input().split()]

    print autres_mults(n, m, numbers)
