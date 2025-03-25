class Solution:
    def romanToInt(self, s: str) -> int:
        converted = list(s)
        values = {
            "I": 1, "V": 5, "X": 10,  "L": 50, "C": 100, "D": 500, "M": 1000
        }
        final = 0
        for pos, n in enumerate(converted):
            val = values[n]
            try:
                if val >= values[converted[pos+1]]:
                    print('add')
                    final += val
                else:
                    print('subtract')
                    final -= val
            except IndexError:
                final += val
        return final


solve = Solution()
result = solve.romanToInt('LVII')

print(result)