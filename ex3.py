import unittest

class Number:
    # 생성자
    def __init__(self, num):
        self.num = list(str(num))
    # Functor
    def __getitem__(self, index):
        try : return int(self.num[index])
        except IndexError: return 0
    
    def __len__(self):
        return len(self.num)


class Adder:
    def __init__(self):
        self.carries = [0]*10
    def add(self, src, target):
        # 자릿수
        for i in range(1, max(len(src), len(target)) + 1):
            if src[-i] + target[-i] + self.carries[-i] >= 10:
                self.carries[-i-1] = 1
    def carryCount(self):
        return self.carries.count(1)


class CarryTest(unittest.TestCase):
    def test1(self):
        adder = Adder()
        adder.add(Number(1), Number(1))
        self.assertEquals(0, adder.carryCount())
    def test2(self):
        adder = Adder()
        adder.add(Number(9), Number(1))
        self.assertEquals(1, adder.carryCount())


import sys
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(CarryTest))
unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)

'''
1. suite = unittest.TestSuite()
2. suite.addTest()
3. 
'''
