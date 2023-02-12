# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N = int(input())
Q = int(input())
art = input()

def f(x):
    return x*3

def g(x):
    return x+2

def h(x):
    return f(x)+g(x)

ans = N
for i in art:
    if i == 'F':
        ans = f(ans)
    elif i == 'G':
        ans = g(ans)
    else:
        ans = h(ans)

ans = ans % (10**9+7)
print(int(ans))


#floatを使うときは丸め誤差に注意
#decimalを使おう