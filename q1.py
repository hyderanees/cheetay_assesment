# THIS FUNCTION WAS NOT MENTIONED IN THE DESCRIPTION BUT I
# DID IT TO CREATE THIS TASK MORE GENERIC AND LESS HARD CODED
# IT JUST CREATE A MATRIX ACCORDING TO NO. OF ROWS AND COLUMNS
def create_matrix(r, c):
    lst = []
    count = 1
    for i in range(0, r):
        temp = [i for i in range(count, count + c)]
        lst.append(temp)
        count += c
    return lst

def spiral(matrix, r, c):
    k, l, lst = 0, 0, []
    while k < r and l < c:
        for i in range(l, c):
            lst.append(matrix[k][i])
        k += 1
        for i in range(k, r):
            lst.append(matrix[i][c - 1])
        c -= 1
        if k < r:
            for i in range(c - 1, (l - 1), -1):
                lst.append(matrix[r - 1][i])
            r -= 1
        if l < c:
            for i in range(r - 1, k - 1, -1):
                lst.append(matrix[i][l])
            l += 1
    return lst

if __name__ == '__main__':
    R, C = 4, 4
    print(spiral(create_matrix(R, C), R, C))    # parameters (matrix, rows, cols)