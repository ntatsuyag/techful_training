# かきこむのがめんどい時につかうやつ
import io,sys

# 書き込みたい内容
s = ""
sl=[]
to = 10**5
for i in range(1,to+1):
    sl.append(str(i))
s = " ".join(sl)

s2 = ""
sl2=[]
for i in range(to,0,-1):
    sl2.append(str(i))
s2 = " ".join(sl2)

# write
with open("input.txt",mode='w') as txt_opend:
    txt_opend.write(str(to)+'\n'+s)
# sys.stdin=io.StringIO(TXT_INPUT)