def count_minimum_iterations(expression):
    if expression == expression[::-1]:
        return 0
    else:
        n = len(expression)
        lst = [[0 for i in range(n)] for i in range(n)]
        for i in range(1, n):
            l = 0
            for j in range(i, n):
                if expression[l] == expression[j]:
                    lst[l][j] = lst[l + 1][j - 1]
                else:
                    lst[l][j] = (min(lst[l][j - 1], lst[l + 1][j]) + 1)
                l += 1
    return lst[0][n - 1]

if __name__ == '__main__':
    print(count_minimum_iterations("aabddsfeger"))  # parameters (str)