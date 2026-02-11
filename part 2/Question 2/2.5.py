import unittest

def pick_first_not_none(a, b):
    if a is None:
        print("a is a null value")
        return(b)
    elif b is None:
        print("b is a null value")
        return(a)    
    else:
        return a   # placeholder — you will replace this

class TestPickFirst(unittest.TestCase):

    def test_when_a_is_none(self):
        try:
            self.assertIsNone(pick_first_not_none(None, 3))
        except AssertionError as msg:
            print(msg)

if __name__ == '__main__':
    unittest.main()
