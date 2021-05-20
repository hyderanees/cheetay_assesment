def activities(s, f, n):
    i = 0
    lst = [i]
    for j in range(0, n):
        if s[j] >= f[i]:
            lst.append(j)
            i = j
    return lst

if __name__ == '__main__':
    print(activities([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9], 6))   # parameters (start, end, N)