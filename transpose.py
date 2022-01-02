n = 4

def transpose(MatrixA, MatrixB):
    for i in range(n):
        for j in range(n):
            MatrixB[i][j] = MatrixA[j][i]

MatrixA = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

MatrixB = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
transpose(MatrixA,MatrixB)

print('The transpose version of the matrix is: ')
for i in range(n):
    for j in range(n):
        print(MatrixB[i][j], "", end='')
    print()

