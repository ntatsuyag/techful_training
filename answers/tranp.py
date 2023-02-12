# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
# from collections import deque
n = int(input())  # nは入力回数
str_list = list(input().split())

num_dict = {
    '03D':1,
    '03C':2,
    '03H':3,
    '03S':4,
    '04D':5,
    '04C':6,
    '04H':7,
    '04S':8,
    '05D':9,
    '05C':10,
    '05H':11,
    '05S':12,
    '06D':13,
    '06C':14,
    '06H':15,
    '06S':16,
    '07D':17,
    '07C':18,
    '07H':19,
    '07S':20,
    '08D':21,
    '08C':22,
    '08H':23,
    '08S':24,
    '09D':25,
    '09C':26,
    '09H':27,
    '09S':28,
    '10D':29,
    '10C':30,
    '10H':31,
    '10S':32,
    '0JD':33,
    '0JC':34,
    '0JH':35,
    '0JS':36,
    '0QD':37,
    '0QC':38,
    '0QH':39,
    '0QS':40,
    '0KD':41,
    '0KC':42,
    '0KH':43,
    '0KS':44,
    '0AD':45,
    '0AC':46,
    '0AH':47,
    '0AS':48,
    '02D':49,
    '02C':50,
    '02H':51,
    '02S':52
}
l = sorted(str_list,key=lambda s:num_dict[s])
output = ' '.join(list(map(str,l)))
print(output)

# --------------------------------
# もう少しスマートに解くなら
num = {
    '03':1,
    '04':2,
    '05':3,
    '06':4,
    '07':5,
    '08':6,
    '09':7,
    '010':8,
    '0J':9,
    '0Q':10,
    '0K':11,
    '0A':12,
    '02':13,
}

fig = {
    'D':1,
    'C':2,
    'H':3,
    'S':4,
}
l = sorted(str_list,key=lambda s:(num[''.join([s[0],s[1]])],fig[str(s[2])]))
output = ' '.join(list(map(str,l)))
print(output)
# ---------------------------------


# def DCHS_sort(s1,s2,l):
#     s1f = s1[2]
#     s2f = s2[2]
#     if 'D' in s1f:
#         l.appendleft(s1f)
#         l.appendleft(s2f)
#     elif 'D' in s2f:
#         l.appendleft(s2f)
#         l.appendleft(s1f)
#     elif s1f < s2f:
#         l.appendleft(s1f)
#         l.appendleft(s2f)
#     else:
#         l.appendleft(s2f)
#         l.appendleft(s1f)


# 2はrotate