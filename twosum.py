def twosum(nums,target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen: # NOT seen.key() cause seen i
            return [seen[diff],i]
        else:
            seen[nums[i]]= i

nums = [2,4,5,3,5]
target = 8

print(twosum(nums,target))


#### Twosum
####  ======================== OK ====================