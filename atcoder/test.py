def knapsack(wv, c):
    if len(wv) == 0:
        return 0

    sliced_wv = wv[1:]

    if wv[0][0] > c:
        max_value = knapsack(sliced_wv, c)
    else:
        no_put_value = knapsack(sliced_wv, c)
        put_value = wv[0][1] + knapsack(sliced_wv, c - wv[0][0])
        max_value = max(no_put_value, put_value)

    return max_value

C = 5
WV = [[2, 2], [2, 4], [3, 3]]

print(knapsack(WV, C))

# h, w = map(int, input().split())
# MAP = []
# for _ in range(h):
#     MAP.append(list(input()))
# n = int(input())
# portion = []
# for _ in range(n):
#     portion.append(list(map(int, input().split())))

# print(A)
# print(B)

# def step(map)



# n = int(input())
# A = []
# for _ in range(n):
#     A.append(list(map(int, input().split())))

# d = {}

# max = 0
# for i in A:
#     if str(i[1]) in d:
#         d[str(i[1])] = min(d[str(i[1])], i[0])
#     else:
#         d[str(i[1])] = i[0]

# max_key, max_value = '', 0
# for k, v in d.items():
#     if v > max_value:
#         max_key = k
#         max_value = v

# print(max_value)

# n = int(input())
# A = []
# for _ in range(n):
#     A.append(list(map(int, input().split())))

# for point in A:
#     max_d = 0
#     target = 0
#     for i, v in enumerate(A):
#         d = (v[0] - point[0]) ** 2 + (v[1] - point[1]) ** 2
#         if d > max_d:
#             target = i + 1
#             max_d = d
#     print(target)



# 動的計画法（ナップサック問題）
# def knapsack():
#     a


"""

# AtCoder用（標準入力受付け）
s = input() # str型で受け取る
n = int(input()) # int型で受け取る
f = # float型(小数)で受け取る
n, k = map(int, input().split()) # 複数の整数を受け取る
arr = list(map(int, input().split())) # list型で整数を受け取る
# N行データを受け取る
N, M = map(int, input().split())
A = []
for _ in range(M):
    A.append(int(input()))

print("{} {}".format(a+b+c, s))


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


# 動的計画法（部分話問題）
def find_max_dp(num_list, limit):
    list_len = len(num_list)
    dp_table = [
        [0 for j in range(limit + 1)] for i in range(list_len)
    ]

    for j in range(limit + 1):
        if num_list[0] <= j:
            dp_table[0][j] = num_list[0]

    for i in range(1, list_len):
        for j in range(limit + 1):
            if num_list[i] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                tmp_choice = dp_table[i - 1][j - num_list[i]] + num_list[i]
                dp_table[i][j] = max(dp_table[i - 1][j], tmp_choice)

    return dp_table[list_len - 1][limit]

num_list = [3, 5, 7]
limit = 10
list_total_with_limit = find_max_dp(num_list, limit)

if limit == list_total_with_limit:
    print('Yes')
else:
    print('No')


"""
