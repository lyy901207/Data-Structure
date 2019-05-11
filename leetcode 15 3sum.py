# currently no better solution;
# will be update later

def threeSum(nums):
    
    res = []
    
    if sum(nums)==0 and len(nums)==3:
        res.append(nums)
        return res
    
    if len(set(nums))==1 and sum(nums)==0 and len(nums)>3:
        res.append([0,0,0])
        return res
    
    nums = sorted(nums)
    neg = [x for x in nums if x<0]
    pos = [x for x in nums if x>0]
    if 0 in nums:
        for i in set(neg):
            if -i in pos:
                res.append([i,0,-i])

    sum_neg = [[neg[i],neg[j]] for i in range(len(neg)) for j in range(len(neg)) if i!=j]
    sum_pos = [[pos[i],pos[j]] for i in range(len(pos)) for j in range(len(pos)) if i!=j]
    print(sum_neg, sum_pos)
    for i in sum_neg:
        new = -sum(i)
        if new in pos:
            item = sorted(i+[new])
            res.append(item)
            
    for j in sum_pos:
        new1 = -sum(j)
        if new1 in neg:
            item1 = sorted(j+[new1])
            res.append(item1)
    return [list(item) for item in set(tuple(row) for row in res)]

