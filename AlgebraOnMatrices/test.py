import unittest

from Algebra_Matrix import Matrix


class TestMatrixClass(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix([[12,7,3],[4 ,5,6],[7 ,8,9]])

#     def test_initialization(self): 
#         self.assertEqual(self.gaussian.mean, 25, 'incorrect mean')
#         self.assertEqual(self.gaussian.stdev, 2, 'incorrect standard deviation')

    def test_add(self):
        self.assertEqual(self.matrix.addition([[5,8,1],[6,7,3],[4,5,9]]),[[17, 15, 4], [10, 12, 9], [11, 13, 18]], 'function does not give expected result')
        
    def test_sub(self):
        self.assertEqual(self.matrix.subtraction([[5,8,1],[6,7,3],[4,5,9]]),[[7, -1, 2], [-2, -2, 3], [3, 3, 0]],'function does not give expected result')
        
    def test_mult(self):
        self.assertEqual(self.matrix.multiplication([[5,8,1,2],[6,7,3,0], [4,5,9,1]]),                 [[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]],'function does not give expected result')
        
    def test_trans(self):
        self.assertEqual(self.matrix.transpose(),[[12, 4, 7],[7, 5, 8],[3,6,9]],'function does not give expected result')

      
if __name__ == '__main__':
    unittest.main()