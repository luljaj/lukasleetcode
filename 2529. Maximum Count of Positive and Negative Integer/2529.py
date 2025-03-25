class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos = 0
        neg = 0
        for i in nums:
            if i>0:
                pos += 1
            if i<0:
                neg+= 1
            if i==0:
                next
        return max(pos,neg)

solve = Solution()

result = solve.maximumCount([-2,-1,-1,2,3,4,5])

print(result)