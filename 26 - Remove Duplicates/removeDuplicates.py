

def removeDuplicates (list):
    Ulist = []

    for i in list:
        if i in Ulist:
            continue
        Ulist.append(i)
        k = len(Ulist)
    return k , Ulist


print(removeDuplicates([1,1,2,1,21,2,1,2,1,1]))



