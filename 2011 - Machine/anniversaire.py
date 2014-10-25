import sys


def anniversaires(n, b):
    tot=0
    reste=0
    for i in range(len(b)):
        print "reste:",reste
        if i==0:
            print "init on fabrique",b[i]," ballons"
            tot+=b[i]
            reste=b[i]/2
        elif b[i]>reste:
            print "anniv suivant > reste, on fabrique:",b[i]-reste,"ballons"
            tot+=b[i]-reste
            reste=b[i]/2
        else:
            print "on a assez de ballons, on en prend",b[i],"il en reste",reste-b[i]
            reste-=b[i]
    return tot


if __name__ == '__main__':
    n = int(raw_input())
    b = [int(_) for _ in raw_input().split()]

    print anniversaires(n, b)
