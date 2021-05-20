import math

def candy_store(lst, k, n):
    lst = sorted(lst)
    temp = int(math.ceil(n / k))
    return sum(lst[:temp]), sum(lst[-temp:])

if __name__ == '__main__':
    print(candy_store([3, 2, 1, 4], 4, 5))  # parameters (list, k, n)