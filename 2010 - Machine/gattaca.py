import sys


def gattaca(N, code, M, genome):
    return genome.find(code)


if __name__ == '__main__':
    N = int(raw_input())
    code = raw_input()
    M = int(raw_input())
    genome = raw_input()

    print gattaca(N, code, M, genome)
