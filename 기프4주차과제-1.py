num=[0xa37b,0x23cc,0x88d9,0xbb8f,0x3a9a]

print('정렬전 데이터 : ',hex(num[0]),hex(num[1]),hex(num[2]),hex(num[3]),hex(num[4]))

##2019038073 신승용##

 

for i in range(0,5):
##2019038073 신승용##
    for j in range(i+1,5):

        if num[i]>num[j]:

            temp=num[i]

            num[i]=num[j]

            num[j]=temp

##2019038073 신승용##            

        j+=j

    i+=i

 

##2019038073 신승용## 

    

print('정렬후 데이터 : ',hex(num[0]),hex(num[1]),hex(num[2]),hex(num[3]),hex(num[4]))
