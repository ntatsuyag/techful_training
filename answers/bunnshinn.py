# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
x1, x2, x3 = map(int, input().split())
N, M = map(int, input().split())

count = 0
for i in range(N+1):
    for j in range(N+1-i):
        if x1*i+x2*j+x3*(N-i-j) == M:
            count += 1
print(count)