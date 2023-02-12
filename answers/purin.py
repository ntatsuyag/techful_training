# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N = int(input())  # nは入力回数
S_list = [int(input()) for _ in range(N)]
S_list.sort(reverse=True)

max = 0
sum = 0
for s in S_list:
    if s>max:
        sum += s-max
        max = s
    else:
        sum += 1
print(sum)