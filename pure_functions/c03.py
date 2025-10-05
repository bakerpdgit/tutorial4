mat = [[0, 0], [0, 0]]


def determinant():
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def identity():
    global mat
    mat = [[1, 0], [0, 1]]


def square():
    global mat
    mat = [[
        mat[0][0] ** 2 + mat[1][0] * mat[0][1],
        mat[0][0] * mat[0][1] + mat[0][1] * mat[1][1]], [
        mat[0][0] * mat[1][0] + mat[1][0] * mat[1][1],
        mat[0][1] * mat[1][0] + mat[1][1] ** 2
    ]]


# All reads or modifications to global state should be moved here
identity()
mat[0][1] = determinant()
for i in range(5):
    square()
print(mat)
