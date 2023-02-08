# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
x,y = map(int, input().split())

def sell(x,y):
    return y*2+x
# sell(x,yt*2)
yn = y
for i in range(10):
    yn = sell(x,yn)
print(str(x) + ' ' + str(yn))