import math
import keyword


def Main():
    num = int(input())
    print(fabNumber(num))
    showKeywords()


def output(arg):
    print(65 + arg)


def fabNumber(num):
    return math.fabs(num)


def showKeywords():
    print(keyword.kwlist)


if __name__ == "__main__":
    Main()
