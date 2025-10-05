from copy import deepcopy

mat = [[1, 0], [0, -1]]


def transpose():
    temp = mat[0][1]
    mat[0][1] = mat[1][0]
    mat[1][0] = temp


def identity():
    global mat
    mat = [[1, 0], [0, 1]]
    return mat


def is_orthogonal():
    temp = deepcopy(mat)
    transpose()
    product = [[
        mat[0][0] * temp[0][0] + temp[1][0] * mat[0][1],
        mat[0][0] * temp[0][1] + mat[0][1] * temp[1][1]], [
        temp[0][0] * mat[1][0] + temp[1][0] * mat[1][1],
        temp[0][1] * mat[1][0] + mat[1][1] * temp[1][1]
    ]]
    return product == identity()


print(is_orthogonal())
mat = [[2, 0], [0, 2]]
print(is_orthogonal())
print(is_orthogonal())
