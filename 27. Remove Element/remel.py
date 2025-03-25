class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)):
            while nums[i] == val:
                nums.pop(i)
                nums.append('_')
                print('skipped')
            else:
                print(nums[i])
        print (nums)

solve = Solution()

result = solve.removeElement([0,1,2,2,3,0,4,2],2)