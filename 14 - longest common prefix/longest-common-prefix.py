def longestCommonPrefix(strs):
    
    first = strs[0]
    for i in range(len(first)):
        for word in strs[1:]:
            if i == len(word) or word[i] != first[i]:
                return first[0:i]
    return first


strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))



