class Solution:
    def removeSpaces(i):
        return not i.isspace()
    def lengthOfLastWord(self, s: str) -> int:
        words = list(s.split())
        words = list(filter(Solution.removeSpaces, words))
        return len(words[-1])


solve = Solution()

result = solve.lengthOfLastWord('   fly me   to   the moon  ')

print(result)