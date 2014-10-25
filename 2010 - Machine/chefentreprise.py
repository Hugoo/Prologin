import sys


def benefices(numbers):
    print max(numbers), min(numbers)
    return


if __name__ == '__main__':
    numbers = [int(_) for _ in raw_input().split()]

    benefices(numbers)
