def determinant(matrix):
    a,b=matrix[0][0],matrix[0][1]
    c,d=matrix[1][0],matrix[1][1]
    determinant=a*d-b*c
    return determinant
print(determinant([[4,2],[3,4]]))
