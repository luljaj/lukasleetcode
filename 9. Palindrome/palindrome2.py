class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            xlist = [int(x) for x in str(x)]
        except:
            return False
        print(xlist)
        for pos, i in enumerate(xlist, start=1):
            print(len(xlist))
            frs = xlist[len(xlist)- pos]
            print(frs)
            print(pos)
            if frs == i:
                next
            else:
                return False
        return True

solve = Solution()

result = solve.isPalindrome(12121)

print(result)
