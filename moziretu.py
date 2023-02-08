# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
S = input()
str_list = list(input().split())

for i,s in enumerate(S):
    if s not in str_list:
        print('No')
        break
    elif i+1 == len(S):
        print('Yes')
