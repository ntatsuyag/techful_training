# input.txtに記述した内容を標準入力として受け取り実行する
# 提出する時にはこの部分は含めない
import io,sys
with open("input.txt") as txt_opend:
    TXT_INPUT = txt_opend.read()
sys.stdin=io.StringIO(TXT_INPUT)
# --------------------------------------------------------
N,M,K = map(int, input().split())  # 特定個の数字の入力を受け取る
A_list = [int(input()) for _ in range(N)]

A_list.sort(reverse=True)
flag = True
for s in range(N):
    A_target_list = A_list[s:]
    k_count = 0
    sum = 0
    for i in range(N-s):
        if sum + A_target_list[i] < M:
            if k_count+1 == K:
                # print('No')
                break
            else:
                sum += A_target_list[i]
                k_count += 1
        elif sum + A_target_list[i] == M:
            if k_count+1 <= K:
                print('Yes')
                flag = False
                break
            else:
                break
        # elif A_target_list[i] == A_target_list[-1]:
        #     print('No')
        elif sum + A_target_list[i] > M:
            continue
    if flag == False:
        break

if flag == True:
    print('No')



# sumの値と残りのKの値からとりうる値の組み合わせを列挙する
# print(A_list[i:])
# print(list(itertools.combinations(A_list[i:],K-k_count)))
# if flag==True:
#     suml = []
#     for tup in list(itertools.combinations(A_list[i:],K-k_count)):
#         sumtup = 0
#         for t in tup:
#             sumtup+=t
#         suml.append(sumtup)

#     for s in suml:
#         if sum+s == M:
#             print('Yes')
#             break
#         elif s == suml[-1]:
#             print('No')
#         else:
#             continue


