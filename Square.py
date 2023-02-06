# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N = int(input())

count = 0
for x in range(1,N+1):
    for y in range(1,int(N/x)+1):
        if x != y and x*y <= N:
            count+=1
print(count)