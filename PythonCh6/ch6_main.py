from PythonCh6 import duck
from PythonCh6 import component


def main():
    duck.Duck('Howard')
    bill = component.Bill('wide orange')
    tail = component.Tail('very long')
    ducks = component.Duck(bill, tail)
    ducks.about()


if __name__ == '__main__':
    main()
