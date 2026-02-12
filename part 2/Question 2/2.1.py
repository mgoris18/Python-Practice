import unittest

def check_value(a, b):
    if a is None:
        print("a is a null value")
        return(b)
    elif b is None:
        print("b is a null value")
        return(a)    
    else:
        return a + b   # placeholder — you will replace this

class TestNoneCheck(unittest.TestCase):

    def test_when_b_is_none(self):
        try:
            self.assertIsNone(check_value(10, None))
        except AssertionError as msg:
            print(msg)

if __name__ == '__main__':
    unittest.main()


#12 check if string contains numbers
#7 assert is none
#24 least privelage