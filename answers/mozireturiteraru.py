# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
n = int(input())  # nは入力回数
str_list = [input() for _ in range(n)]
flag=False
for stri in str_list:
    sf = False
    out = ''
    for s in stri:
        if s == '"' and sf == False:
            sf = True
        elif s == '"' and sf == True:
            sf = False
            print(out)
            out = ''
        elif sf == True:
            out += s