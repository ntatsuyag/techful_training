# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
import math
N,P = map(int, input().split())
ans = math.factorial(N) % P
print(ans)

f = 1
for n in range(1,N+1):
    f *= n
    f %= P
print(f)
