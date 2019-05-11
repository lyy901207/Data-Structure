# leetcode 202

class Solution:
    def sum_2(self, n_list):
        return sum([x*x for x in n_list])
        
    def isHappy(self, n: 'int') -> 'bool':
        res = [1,7,10]
        while True:
            if n in res: 
                return True
            elif n<10:
                return False
            else:
                n_list = [int(i) for i in str(n)]
                n = self.sum_2(n_list)