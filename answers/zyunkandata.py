# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N, M = map(int, input().split(" "))  # 特定個の数字の入力を受け取る
s_list = input()

data = [0 for _ in range(N)]
cursor = 0 #indexとの差に注意
for s in s_list:
    if s == 'R':
        if cursor == N-1:
            cursor = 0
        else:
            cursor += 1
    elif s == 'L':
        if cursor == 0:
            cursor = N-1
        else:
            cursor -= 1
    elif s == '+':
        data[cursor] += 1
    elif s == '-':
        data[cursor] -= 1

print(' '.join(list(map(str,data))))