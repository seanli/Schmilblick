from copy import copy
from array import Array
from matrix import Matrix

if __name__ == '__main__':
    arr = Array(5)
    for i in xrange(0, 5):
        arr[i] = i
    barr = copy(arr)
    print barr.getData()
    mat1 = Matrix(2, 2)
    mat1[0, 0] = 1
    mat1[0, 1] = 2
    mat1[1, 0] = 3
    mat1[1, 1] = 4
    mat2 = Matrix(2, 2)
    mat2[0, 0] = 1
    mat2[0, 1] = 2
    mat2[1, 0] = 3
    mat2[1, 1] = 4
    matr = mat1 * mat2
    for row in xrange(matr.numRows):
        for col in xrange(matr.numCols):
            print "%d\t" % matr[row, col],
        print ''