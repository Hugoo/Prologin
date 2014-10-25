import sys


def multiplications(n, numbers):
    mini = numbers[n]*numbers[n-1]
    maxi = numbers[0]*numbers[1]
    if maxi>mini:
        return maxi
    return mini


if __name__ == '__main__':
    n = int(raw_input())-1
    numbers = [int(_) for _ in raw_input().split()]
    numbers.sort()
    print multiplications(n, numbers)
