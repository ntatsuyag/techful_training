# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
from collections import deque
N = int(input())  # nは入力回数
A_list = list(map(int, input().split()))  # n個の数字の入力を受け取る
Q = int(input())  # nは入力回数
Q_list = [list(map(int, input().split())) for _ in range(Q)]
aquery = deque()
for a in A_list:
    aquery.append(a)

# def shift(l,n):
#     n = n % len(l)
#     return l[-n:] + l[:-n]

for q in Q_list:
    if q[0] == 1:
        aquery.rotate(q[1])
    else:
        aquery.reverse()

print(' '.join(list(map(str,aquery))))


# メモ
# Aをlistのまま解くとシフトの演算が遅いっぽい、dequにしたら時間制限は引っ掛からなかった