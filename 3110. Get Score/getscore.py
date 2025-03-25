class Solution:
    def scoreOfString(self, s: str) -> int:
        print(str)
        bank = 0
        for n in range(len(s)):
            try:
                first = s[n]
                second = s[n+1]
                bank += abs(ord(first) - ord(second))
            except IndexError:
                next
        return(bank)


solution = Solution()
result = solution.scoreOfString('Hello')