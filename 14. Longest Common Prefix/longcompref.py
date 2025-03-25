class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        letters = {
        }
        prefix = {
        }
        for word in strs:
            wordlist = list(word)  
            for pos, letter in enumerate(wordlist):
                print(pos,letter)
                if pos not in letters:
                    print(f'nothing there yet, adding {letter} at {pos}')
                    letters[pos] = letter
                if letters[pos] != letter:
                    print(f'{letter} isnt at {pos}')
                    if pos == 0:
                        return ""
                    break
                if letters[pos] == letter:
                    print(f'found {letter} at {pos}')
                    prefix[word] = pos
                    continue    
        print(letters)
        print(prefix)
        try:
            answer = list(letters.values())[0:min(prefix.values())+1]
        except ValueError:
            return ""
        return "".join(answer)

    

solve = Solution()
result = solve.longestCommonPrefix(["","b"])
print(result)