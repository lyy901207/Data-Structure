# leetcode 167 majority element

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ref = {i:0 for i in set(nums)}
        for i in nums:
            ref[i] += 1
        return [key for key in ref.keys() if ref[key]==max(ref.values())][0]