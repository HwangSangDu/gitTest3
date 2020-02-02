import unittest


def add_digit(no):
    return sum(map(int, ' '.join(str(no)).split()))

# exMap = (map(int, ['1','2','3']))
# print(list(exMap))

# exJoin = ' '.join('1234dg').split()
# print(exJoin)

# res = add_digit(91)
# print(res)


class GeneratorTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, add_digit(200))

if __name__ == "__main__":
    unittest.main()
