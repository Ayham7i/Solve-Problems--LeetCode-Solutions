def capital_index(str):
    index = []
    
    for indx , char in enumerate(str):
        if char.isupper():
            index.append(indx)
    
    print(index)



capital_index("HeLo")