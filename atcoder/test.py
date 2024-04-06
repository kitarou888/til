# -*- coding: utf-8 -*-

fib_list = [0] * 101

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if fib_list[n] == 0:
        fib_list[n] = fib(n - 1) + fib(n - 2)
    
    return fib_list[n]

print(fib(50))

"""

# ナップサック問題
CAPACITY = 5
values = [2, 4, 3]
weight = [2, 2, 3]
n = len(values)

def knapsack(i, capacity):
    if i >= n:
        return 0

    if weight[i] > capacity:
        max_value = knapsack(i + 1, capacity)
    else:
        no_put_value = knapsack(i + 1, capacity)
        put_value = values[i] + knapsack(i + 1, capacity)
        max_value = max(no_put_value, put_value)

    return max_value

def main():
    print(knapsack(0, CAPACITY))

if __name__ == '__main__':
    main()

# 迷路問題
map = [
    ['o','o','o','o','o','x','o','x','o','o','o','x','o','o','o','o',],
    ['o','x','o','x','x','x','o','x','o','x','o','x','o','x','o','x',],
    ['o','x','o','o','o','o','o','x','o','x','o','o','o','x','o','o',],
    ['o','o','x','x','o','x','x','x','o','x','x','x','x','x','x','o',],
    ['x','o','x','x','o','o','o','o','o','o','o','o','o','x','o','o',],
    ['o','o','o','x','o','x','x','x','o','x','x','o','x','o','o','x',],
    ['x','o','x','x','o','x','o','x','o','x','x','o','x','o','x','x',],
    ['o','o','o','o','o','o','o','o','o','x','o','o','x','o','o','G',],
]

WIDTH = len(map[0])
HEIGHT = len(map)

def maze(start, map):
    i, j = start

    if i < 0 or WIDTH <= i or j < 0 or HEIGHT <= j:
        return False
    if map[j][i] =='p':
        return False
    if map[j][i] =='x':
        return False
    if map[j][i] =='G':
        return True

    map[j][i] = 'p'

    is_goaled_left = maze((i - 1, j), map)
    is_goaled_right = maze((i + 1, j), map)
    is_goaled_up = maze((i, j + 1), map)
    is_goaled_down = maze((i, j - 1), map)

    if is_goaled_left or is_goaled_right or is_goaled_up or is_goaled_down:
        return True
    else:
        return False

def main():
    start = (2,2)
    isGoal = maze(start, map)
    print('OK') if isGoal else print('NG')

if __name__ == '__main__':
    main()

# 線形探索
def linear_search(data, key):
    position = 0
    end = len(data) - 1
    steps = 1
    while position <= end:
        if data[position] == key:
            return steps,position
        steps += 1
        position += 1
    return steps,-1

# 二分木探索
def binary_search(data, key):
    start = 0
    end = len(data) - 1
    steps = 1
    while start <= end:
        middle = (start + end) // 2
        if data[middle] == key:
            return steps,middle
        elif data[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
        steps += 1
    return steps,-1

# 探索の実行と最大ステップ数を求める処理
def search(title, data, func):
    print(title)
    max_steps = 1
    for key in data:
        steps,pos = func(data, key)
        if max_steps < steps:
            max_steps = steps
        print("key:{} position:{} steps:{}".format(key,pos,steps))
    print("最大ステップ数:{}\n".format(max_steps))
    return

if __name__ == '__main__':
    data = [1, 3, 7, 13, 17, 21, 74]
    length = len(data)
    print("探索データ:{}\n長さ:{}\n".format(data,length))
    search("線形探索",data,linear_search)
    search("二分木探索",data,binary_search)



a = int(input())
arr = list(map(int, input().split()))
b,c = arr
s = input()

print(a)
print(arr)
print(b)
print(c)
print(s)

print("{} {}".format(a+b+c, s))

"""
