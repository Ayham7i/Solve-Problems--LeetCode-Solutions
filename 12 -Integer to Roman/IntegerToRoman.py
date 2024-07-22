def IntToRoman(num):

    Roman = {
        1:    'I',
        4:    'IV',
        5:    'V',
        9:    'IX',
        10:   'X',
        40:   'XL',
        50:   'L',
        90:   'XC',
        100:  'C',
        400:  'CD',
        500:  'D',
        900:  'CM',
        1000:  'M'
    }
    result = ""
    for key , val in reversed(list(Roman.items())):
        if num // key:
            count = num // key
            result += (val * count)
            num = num % key

    return result

num = 1914

print(IntToRoman(num))
