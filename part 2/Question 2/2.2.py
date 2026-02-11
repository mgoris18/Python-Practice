import unittest

def choose_value(x, y):
    if x is None:
        print("x is a null value")
        return y
    if y is None:
        print("y is a null value")
        return x
    else:
        return x * y   # placeholder — you will replace this

class TestChooseValue(unittest.TestCase):

    def test_when_x_is_none(self):
        try:
            self.assertIsNone(choose_value(None, 8))
        except AssertionError as msg:
            print(msg)

if __name__ == '__main__':
    unittest.main()
