import math
import random
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        rlist = []
        rlist.append(nums)
        pl = math.factorial(len(nums))
        tl = pl / len(nums)
        for i in range(pl):
            nums[i] 
       
        
solve = Solution()

result = solve.permute([1,2,3])

print(result)