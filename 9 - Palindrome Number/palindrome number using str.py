def strpalindromenum(num):
    num = str(num)
    return num == num[::-1]# when you want to reverse the string use [::-1]


num = 121

print(strpalindromenum(num))