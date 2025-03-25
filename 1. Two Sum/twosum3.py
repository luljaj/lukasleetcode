class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numdict = dict()
        for ind, num in enumerate(nums):
            search = target - num
            print(search)
            if search in numdict and numdict[search] != ind:
                return numdict[search], ind
            else:
                numdict[num] = ind
                next
        
        



solve = Solution()
result = solve.twoSum([3,3],6)
print(result)