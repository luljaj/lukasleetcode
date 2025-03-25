import math
import random
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        rlist = []
        #print(nums)
        #print(math.factorial(len(nums)))
        iterationcount = 0
        while len(rlist) < (math.factorial(len(nums))):
            iterationcount += 1
            current=nums.copy()
            nlist = []
            random.shuffle(current)
            if current in rlist:
                random.shuffle(current)
                continue
            else:
                rlist.append(current)
        print(iterationcount)
        return rlist
solve = Solution()

result = solve.permute([1,2,3])

print(result)
