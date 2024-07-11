def RomanToInt(s):

    Roman = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }
    total = 0
    for i in range(len(s)-1):
        if Roman[s[i]] < Roman[s[i+1]]:
            total -= Roman[s[i]]
        else:
            total += Roman[s[i]]
    
    return total + Roman[s[-1]]


s='MCMXIV'

print(RomanToInt(s))
