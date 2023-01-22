# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N,M,X = map(int, input().split())  # 特定個の数字の入力を受け取る
A = [list(map(int, input().split())) for l in range(N)]

def calc_now(old, brain):
    if old < brain:
        return brain
    else:
        return old+1

for Ai in A:
    X = calc_now(X,max(Ai))
print(X)