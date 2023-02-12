# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N = 5
K = [list(map(int, input().split())) for l in range(N)]

for k in K:
    if k[0] <= k[1]:
        print('Yes')
    else:
        print('No')
