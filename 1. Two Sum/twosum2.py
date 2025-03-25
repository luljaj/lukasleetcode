class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        current = 0
        
        for i in nums:
            findnum = target - i
            print(f"looking for {findnum}")

            if findnum in nums:
                foundspot = nums.index(findnum)
                if foundspot == current:
                    next
                else:
                    return foundspot, current
            else:
                next
                
            current += 1
        print(target)


solution = Solution()

result = solution.twoSum([4,3,0,0],0)

print(result)