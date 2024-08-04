N = int(input())
H = list(map(int, input().split()))

dp = [None] * (N + 1)
dp[0] = 0
dp[1] = 0
dp[2] = abs(H[1] - H[0])

for i in range(3, N+1):
    dp[i] = min(dp[i-1] + abs(H[i-1] - H[i-2]),
                dp[i-2] + abs(H[i-1] - H[i-3]))

print(dp[N])

"""
■入出力（AtCoder用）

S = input() # str型で受け取る
N = int(input()) # int型で受け取る
N, K = map(int, input().split()) # 複数の整数を受け取る
A = list(map(int, input().split())) # list型で整数を受け取る

# N行データを受け取る
A = []
for _ in range(M):
    A.append(int(input()))

# a の要素をつなげて出力する 注）aをstr(a)に予め変換すること
print("".join(a))


■リスト操作

# ２次元配列の初期化（[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]）
A = [[0] * 4 for i in range(3)]

l = [1, 3, -5, 2]
res = all([v > 0 for v in l])    # l に含まれる値が全て正か？
res2 = any([v % 2 == 0 for v in l])    # l に偶数が含まれるか？

# リストのインデックスと値を同時に取得
for i,v in enumerate(l)

# リスト内包表記（all()、any()、map）
all([i > 2 for i in l])
any([i > 2 for i in l])
[i * 2 for i in [1, 6, 9]]

# リスト [0, 1, 2, 3, 4] を作る
a = list(range(5))

# リスト [1, 6] とリスト [1, 8] をつなげて [1, 6, 1, 8] を作る
a = [1, 6] + [1, 8]

# a の i 番目の位置 (a[i-1] と a[i] の間) に x を挿入
a.insert(i, x)

# リスト a と整数 i に対し、 a の i 番目の要素を取得しながら削除
a.pop(i)

# x が a の中に 1 個以上存在するかを判定
x in a

# x が a の中に何個存在するかを取得
a.count(x)

# a の中に x が出現する最初の位置を取得
a.index(x)

# リストをディープコピー
b = a.copy()



■文字列操作

# a の 0 番目の要素を "M" に変更する
a[0] = "M"

print("{} {}".format(a + b + c, s))
print(a + b + c, s) は同じ

# s を逆順にした文字列 "EDCBA" を出力
print(s[::-1])

# "ABABABA" の部分文字列に "BAB" があるか判定する
print("BAB" in s)

# "ABABABA" に現れる最初の部分文字列 "BAB" の位置を求める←1を出力
print(s.index("BAB"))

# "ABABABA" に重ならずに現れる部分文字列 "BAB" の個数を求める
print(s.count("BAB"))

# "AAAAA" に出現する "AA" を "X" に置き換えた文字列 "XXA" を出力する
print("AAAAA".replace("AA", "X"))

★Python の文字列は一度作ると変更することができない→一度listにする。
a = list(s)




■その他
ord(c)・・・文字をコードポイントに
chr(x)・・・コードポイントを文字に

divmod(a, b)・・・aをbで割った商と余りを返す
pow(a, b)・・・aのb乗を返す  ★「**」を使うより高速
pow(a, b, mod)・・・aのb乗をmodで割った余りを返す  ★「%」を使うより高速

exit()・・・プログラムを強制終了させる
"""





"""

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
