# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
K = int(input())  # nは入力回数
int_list = list(map(int, input().split()))  # n個の数字の入力を受け取る

sum = 0
ans = 0
for l in int_list:
    sum+=l
    ans = sum%10
print(int(ans))