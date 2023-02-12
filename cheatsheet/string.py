# 文字列操作のチートシート
# 指定インデックスの文字列を書き換える方法
# 参考 https://qiita.com/tamago324/items/ea39fb541ef9f2cada7f

#一度list化してしてして、指定箇所に文字を代入し、再びstring化する
N='101'
N=list(N)
N[-1] = '0'
print("".join(N))


# ルールに従った文字列ソート
n = int(input())  # nは入力回数
str_list = list(input().split())
# dictや関数で優先順位を記述
rule = {
    'rule1':1,
    'rule2':2
    }
# lamda関数を使ってそのルールを適応させる
l = sorted(str_list,key=lambda s:rule[s])
output = ' '.join(list(map(str,l)))
print(output)
