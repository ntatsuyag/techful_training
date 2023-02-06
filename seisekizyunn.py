# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N = int(input())  # nは入力回数
A_list = [[i+1,int(input())] for i,_ in enumerate(range(N))]
ans = sorted(A_list, reverse=True, key=lambda l: l[1])

for a in ans:
    print(a[0])

# output = ' '.join(list(map(str,[l[0] for l in ans])))
# print(output)