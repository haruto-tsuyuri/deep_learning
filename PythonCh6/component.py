# xがyを持っている（has-a関係の場合）はコンポジションや集約の方が理にかなっていることがある
from collections import namedtuple


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')


duck_tuple = namedtuple('Duck2', 'bill tail')
duck2 = duck_tuple('wide orange', 'long')
print(duck2.bill)
parts = {'bill': 'wide orange maybe', 'tail': 'long'}
duck3 = duck_tuple(**parts)
print(duck3.bill)
