string2=''
##2019038073 신승용##
if __name__=='__main__':
    string=input("문자열을 입력하세요 : ")
    for i in range(0,len(string)):
        if string[i].isupper()==False:
            string2+=string[i].upper()
        else:
            string2+=string[i].lower()
    print('대소문자 변환 결과 -->',string2)
##2019038073 신승용##
    

