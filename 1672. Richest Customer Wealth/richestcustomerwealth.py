class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        banks = {

        }
        for pos, a in enumerate(accounts):
            print(f'{pos} bank')
            wealth = 0
            for num in a:
                wealth += num
            banks[pos] = wealth
            print(f'{pos} bank has {wealth} dollars')
        return max(banks.values())
            


solve = Solution()

result = solve.maximumWealth([[1,2,3],[5,4,2]])
print (result)