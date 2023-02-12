# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N = list(input()) #文字列で受け取る
# N以下の整数で最大となる10の倍数を出力してください。
N[-1] = '0'
print("".join(N))

# 解答について
# 整数型で受け取るとオーバーフローした時に処理できないことを考慮する必要があるという問題