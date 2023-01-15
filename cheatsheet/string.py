# 文字列操作のチートシート
# 指定インデックスの文字列を書き換える方法
# 参考 https://qiita.com/tamago324/items/ea39fb541ef9f2cada7f

#一度list化してしてして、指定箇所に文字を代入し、再びstring化する
N='101'
N=list(N)
N[-1] = '0'
print("".join(N))