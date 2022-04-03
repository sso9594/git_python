def hexatrans(number):
##2019038073신승용##	
    strings = "0123456789ABCDEF"
    
    if number < 16:
    	return strings[number]
	
    else:
    	return hexatrans(number // 16) + strings[number % 16]
##2019038073신승용##
def binarytrans(n):
    if (n<1):
        return '0'
    elif(n==1):
        return '1'
    if (n%2==0):
        return binarytrans(int(n/2))+'0'
    elif(n%2==1):
        return binarytrans(int(n/2))+'1'
##2019038073신승용##
def octaltrans(n):
    if(n<8):
        return n
    else:
        return n%8+(octaltrans(n//8)*10)
##2019038073신승용##
if __name__=="__main__":

    num=int(input("10진수 입력-->"))

    print('2진수 : ',binarytrans(num))
    print('8진수 : ',octaltrans(num))
    print('16진수 : ',hexatrans(num))
        
