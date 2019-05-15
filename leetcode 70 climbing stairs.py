class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        ret = [1,2]
        if n > 2:
            i = 3
            while i <= n:
                add = ret[i-2]+ret[i-3]
                ret.append(add)
                i+=1
        return ret[n-1]
        