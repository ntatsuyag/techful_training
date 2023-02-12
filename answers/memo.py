# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N = int(input())
s_list = list(input().split())  # n個の文字列がリストに格納される
M = int(input())
t_list = list(input().split())  # n個の文字列がリストに格納される

count = 0
for s in s_list:
    match = False
    for t in t_list:
        if s == t:
            match = True
    if match == False:
        count+=1
print(count)