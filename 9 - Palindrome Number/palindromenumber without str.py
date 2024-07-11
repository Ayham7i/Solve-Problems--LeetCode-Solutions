def palindromenumber(num):  #1221

    if num<0 or (num!=0 and num % 10 == 0 ):
        return False
    
    half = 0
    while num>half:
        half = (half * 10) + (num % 10)
        num = num // 10
    
    return num == half or num == half // 10

num = 1221
print(palindromenumber(num))
