# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N = int(input())
a_list = list(map(int, input().split()))  # n個の数字の入力を受け取る

a_list.sort(reverse=True)

tech = a_list[0::2]
ful = a_list[1::2]

count = 0
for i in range(N):
    if ful[0] > tech[0]:
        tech.pop(0)
        ful.pop(0)
        count += 1
    else:
        tech.pop(0)
        ful.pop(-1)

print(count)

# max()を使うとTLEになってしまったsortしたからindex=0が最大なのはmax使わずともわかる