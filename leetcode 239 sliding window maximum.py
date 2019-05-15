from collections import deque

class Solution(object):

    def maxSlidingWindow(self, nums, k): 
        que = [ (-1000000,1000000) ]
        ans = []
        for i in range( len(nums) ) : 
            print('i:',i, '; que:', que, '; ans:',ans)
            # 当que and window的宽度k>=k, 删掉头部元素
            while len(que)>0 and i-que[0][0] >= k : 
                print('del')
                del que[0]
            #当que and 队尾元素小于当前值，
            while len(que)>0 and que[-1][1]<=nums[i] :
                print('pop')
                que.pop();

            que.append( (i,nums[i]) )
            if i>=k-1 :
                ans.append(que[0][1])


if __name__ == '__main__':
	s = Solution()
	nums = [1,3,-1,-3,5,3,6,7]
	k = 3
	ans = s.maxSlidingWindow(nums, k)
	print(ans)
