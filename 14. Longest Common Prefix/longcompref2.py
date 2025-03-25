class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def length
        wordslisted = {
        }
        for pos, entry in enumerate(strs):
            wordslisted[pos] = list(entry)
        prefix = ""
        lw= max(wordslisted.values(),key=len)
        for pos,i in enumerate(lw):
            try:
                case = all(word[pos] == lw[pos] for word in wordslisted.values())
                if case == True: 
                    prefix = prefix + lw[pos]
                    print(f'prefix is at {prefix}')
                else:
                    return prefix
            except IndexError:
                print('not all reached that point')
                break
        return prefix




solve = Solution()
result = solve.longestCommonPrefix(('flower','flower'))
print(f'result:{result}')