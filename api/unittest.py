import unittest
from app import views

class TestCorrectness(unittest.TestCase):

    def test_authenticate(self):
        # test the correctness of autheticate method with edge cases
        pass
    
    def test_authorize(self):
        # test the correctness of authorize method with edge cases
        pass
    
    def test_upload(self):
        # test the correctness of upload method with edge cases
        pass
    
    def test_moodsDistribution(self):
        # test the correctness of moodsDistribution method with edge cases
        pass
    
    def test_getProximity(self):
        # test the correctness of getProximity method with edge cases
        pass
    
class TestRobustness(unittest.TestCase):
    """test all the methods above with large throuput"""

class TestLatency(unittest.TestCase):
    """test all the methods above with a contrant on the latency"""

if __name__ == '__main__':
    unittest.main()
