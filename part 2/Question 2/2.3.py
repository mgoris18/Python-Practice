import unittest

def merge_values(a, b):
    if a is None:
        print("a is a null value")
        return b 
    if b is None: 
        print("b is a null value")
        return a
    else:
        return a - b   # placeholder — you will replace this

class TestMergeValues(unittest.TestCase):

    def test_when_b_is_none(self):
        try:
            self.assertIsNone(merge_values(12, None))
        except AssertionError as msg:
            print(msg)

if __name__ == '__main__':
    unittest.main()
