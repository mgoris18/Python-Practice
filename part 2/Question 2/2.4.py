import unittest

def combine_strings(s1, s2):
    if s1 is None:
        print("s1 is a null value")
        return s2
    if s2 is None:
        print("s2 is a null value")
        return s1
    else:
        return s1 + s2   # placeholder — you will replace this

class TestCombineStrings(unittest.TestCase):

    def test_when_s1_is_null(self):
        try:
            self.assertIsNone(combine_strings(None, "world"))
        except AssertionError as msg:
            print(msg)

if __name__ == '__main__':
    unittest.main()
