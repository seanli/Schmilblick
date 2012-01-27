from multi_array import MultiArray

class BaseMatrix(object):
    
    def __init__(self, numRows, numCols):
        assert numRows >= 0
        assert numCols >= 0
        super(BaseMatrix, self).__init__()
        self._numRows = numRows
        self._numCols = numCols
    
    def getNumRows(self):
        return self._numRows
    
    numRows = property(
        fget = lambda self: self.getNumRows())
    
    def getNumCols(self):
        return self._numCols
    
    numCols = property(
        fget = lambda self: self.getNumCols())

class Matrix(BaseMatrix):
    
    def __init__(self, rows, cols):
        super(Matrix, self).__init__(rows, cols)
        self._array = MultiArray(rows, cols)
    
    def __getitem__(self, (i, j)):
        return self._array[i, j]
    
    def __setitem__(self, (i, j), value):
        self._array[i, j] = value
    
    def __mul__(self, mat):
        assert self.numCols == mat.numRows
        result = Matrix(self.numRows, mat.numCols)
        for i in xrange(self.numRows):
            for j in xrange(mat.numCols):
                row_sum = 0
                for k in xrange(self.numCols):
                    row_sum += self[i,k] * mat[k, j]
                result[i, j] = row_sum
        return result