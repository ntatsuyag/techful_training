# 入力のテンプレートをまとめておく用のファイル

a,b,c = input().split()  # 特定個の文字列の入力を受け取る
a,b,c = map(int, input().split())  # 特定個の数字の入力を受け取る
# ---------------------------------------------------------
# 少数をdecimalでうけとる
from decimal import Decimal
A, B = map(Decimal, input().split())
print(int(A*B))

# list
str_list = list(input().split())  # n個の文字列がリストに格納される
int_list = list(map(int, input().split()))  # n個の数字の入力を受け取る

# 行数+1要素入力パターン
n = int(input())  # nは入力回数
str_list = [input() for _ in range(n)]

# 行数+1数字入力のパターン
n = int(input())  # nは入力回数
num_list = [int(input()) for _ in range(n)]

# 行数 + 複数要素のパターン
n = int(input())  # nは入力回数
str_list = [list(input().split()) for _ in range(n)]

# 行数 + 複数数字のパターン 
n = int(input())  # nは入力回数
num_list = [list(map(int, input().split())) for _ in range(n)]

# 入力が列(縦)に並ぶパターン
# N
# x1 y1s
# x2 y2
# :
# xN yN
# x,yにそれぞれ格納
N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
# [x,y]で格納
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

# N,M入力 + 入力のパターン
N, M = map(int, input().split())
#リスト内包表記
x = [int(input()) for _ in range(M)]