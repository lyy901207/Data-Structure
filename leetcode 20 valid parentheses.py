# leetcode 20 valid Parentheses

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        lower = {'(':0, '[':1, '{':2}
        upper = {")":0, ']':1, '}':2}
        if s=='': return True
        if len(s)%2 != 0:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in lower.keys():
                stack.append(s[i])

            else:
                if stack:
                    out = stack.pop()              
                    if upper[s[i]] != lower[out]:
                        return False
                else:
                    return False
        if len(stack) == len(s) or len(stack)!=0:
            return False

        return True
                