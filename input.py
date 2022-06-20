def takingInput():
    x, y = input().split()
    print(f"Our input value is {x} and {y}")
    print("Formatting string with modules %2.2f" % 120)
    result = [0 for i in range(6)]
    print(result)


if __name__ == '__main__':
    takingInput()
