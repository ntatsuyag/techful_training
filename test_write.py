# かきこむのがめんどい時につかうやつ
import io,sys

# 書き込みたい内容
s = ""
sl=[]
to = 10**4
for i in range(1,to+1):
    sl.append(str(i))
s = " ".join(sl)

# write
with open("input.txt",mode='w') as txt_opend:
    txt_opend.write(str(to)+'\n'+s)
# sys.stdin=io.StringIO(TXT_INPUT)