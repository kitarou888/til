n, q = map(int, input().split())
print(n, q)


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


# ナップサック問題（再帰呼び出し）
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


# 迷路問題（再帰呼び出し）

def maze(start, map):
    i, j = start

    if i < 0 or len(map[0]) <= i or j < 0 or len(map) <= j:
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

print(maze(start, map))


# 最短経路問題（動的計画法）

def maze(start, map):
    dp = map
    height = len(map)
    width = len(map[0])
    x, y = start
    if dp[y][x] == 'G': return True
    dp[y][x] = 0

    k = 1
    while True:
        flg_continued = False
        for j in range(height):
            for i in range(width):
                if dp[j][i] == k - 1:
                    if i > 0 and dp[j][i - 1] == 'G': return True
                    if j > 0 and dp[j - 1][i] == 'G': return True
                    if i < width - 1 and dp[j][i + 1] == 'G': return True
                    if j < height - 1 and dp[j + 1][i] == 'G': return True

                    if i > 0 and dp[j][i - 1] == 'o':
                        dp[j][i - 1] = k
                        flg_continued = True
                    if j > 0 and dp[j - 1][i] == 'o':
                        dp[j - 1][i] = k
                        flg_continued = True
                    if i < width - 1 and dp[j][i + 1] == 'o':
                        dp[j][i + 1] = k
                        flg_continued = True
                    if j < height - 1 and dp[j + 1][i] == 'o':
                        dp[j + 1][i] = k
                        flg_continued = True
        print(dp)
        if flg_continued == False: return False
        k += 1

map = [
    ['o','o','o','o','o','x','o','x','o','o','o','x','o','o','o','o',],
    ['o','x','o','x','x','x','o','x','o','x','o','x','o','x','o','x',],
    ['o','x','o','o','o','o','o','x','o','x','o','o','o','x','o','o',],
    ['o','o','x','x','o','x','x','x','o','x','x','x','x','x','x','o',],
    ['x','o','x','x','o','x','o','o','o','o','o','o','o','x','o','o',],
    ['o','o','o','x','o','x','x','x','x','x','x','o','x','o','o','x',],
    ['x','o','x','x','o','x','o','x','o','x','x','o','x','o','x','x',],
    ['o','o','o','o','o','o','o','o','o','x','o','o','x','o','o','G',],
]
start = (6, 4)
print(maze(start, map))


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


# 動的計画法（部分和問題）
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


# ナップサック問題（動的計画法）
def knapsack(wv, c):
dp_table = [[0 for i in range(c + 1)] for j in range(len(wv))]
print(dp_table)

for i in range(len(wv)):
    for j in range(c + 1):
        if wv[i][0] > j:
            if i > 0:
                dp_table[i][j] = dp_table[i - 1][j]
        else:
            if i > 0:
                no_put_value = dp_table[i - 1][j]
                put_value = wv[i][1] + dp_table[i - 1][j - wv[i][0]]
                dp_table[i][j] = max(no_put_value, put_value)
            else:
                dp_table[i][j] = wv[i][1]
print(dp_table)
return dp_table[len(wv) - 1][c]

# 参考）ナップサック問題（再帰呼び出し）
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

"""
