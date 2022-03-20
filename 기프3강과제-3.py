i,j,heartnum=0,0,0 
num,ch,heartstr="","",""
##2019038073 신승용##

num=input("숫자를 여러개 입력하세요 : ") 
print("")
##2019038073 신승용##
i=0
ch=num[i] 
##2019038073 신승용##
while i<len(num) :
    ch=num[i]
    heartnum=int(ch)
    heartstr=""
    for j in range(0,heartnum) :
        heartstr += "\u2665"
        j+=1
    print(heartstr)
    i+=1
##2019038073 신승용##
