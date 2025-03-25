class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        current = 0
        
        for i in nums:
            findnum = target - i
            print(f"looking for {findnum}")
            try:
                foundnum = nums.index(findnum)
                print(f"found at {foundnum}")
                if foundnum == current:
                    next
                    print(f"they are the same")
                else:
                    return foundnum, current
            except: 
                next
            current += 1
        print(target)


    


solution = Solution()

result = solution.twoSum([4,3,0,0],0)

print(result)