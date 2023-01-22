# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
nv_dict = {}

while (True):
    i = input().split()
    if i[0] == "#END":
        break
    else:
        if (i[0] in nv_dict) == False:
            nv_dict[i[0]] = int(i[1])
        elif (i[0] in nv_dict) == True:
            nv_dict[i[0]] = int(nv_dict[i[0]]) + int(i[1])
for p in sorted(list(nv_dict.values()),reverse=True):
    print(p, end=" ")

# dict使って存在をinで判定して処理を分岐する