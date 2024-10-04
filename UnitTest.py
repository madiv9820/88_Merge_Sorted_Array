from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {
            1: {'nums1': [1,2,3,0,0,0], 'm': 3, 
                'nums2': [2,5,6], 'n': 3,
                'output': [1,2,2,3,5,6]},
            2: {'nums1': [1], 'm': 1, 'nums2': [], 
                'n': 0, 'output': [1]},
            3: {'nums1': [0], 'm': 0, 'nums2': [1], 
                'n': 1,'output': [1]}
        }

        self.__obj = Solution()

        return super().setUp()
    
    def test_Case1(self):
        case = self.__testCases[1]
        nums1, m, nums2, n, output = case.values()
        self.__obj.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, output)

    def test_Case2(self):
        case = self.__testCases[2]
        nums1, m, nums2, n, output = case.values()
        self.__obj.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, output)

    def test_Case3(self):
        case = self.__testCases[3]
        nums1, m, nums2, n, output = case.values()
        self.__obj.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, output)

if __name__ == '__main__':
    unittest.main()