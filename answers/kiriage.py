# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N,M = map(int, input().split())

for k in range(10000000):
    if -(-k//N) >= M:
        print(k)
        break
