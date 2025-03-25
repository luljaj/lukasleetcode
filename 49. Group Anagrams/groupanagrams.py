class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dc = {}
        rc= []
        for pos, s in enumerate(strs):
            s = sorted(s)
            srs = "".join(s)
            print(s)
            if dc.get(srs) is not None:
                print(f'{srs} is alr at {pos}')
                dc[srs].append(pos)
            elif dc.get(srs) == None:
                print(f'{srs} starting with {pos}')
                dc[srs] = list()
                dc[srs].append(pos)
        for l,s in dc.items():
            print(f'l,s is {l},{s}')
            ca = list()
            #if rc.count(l)== 0:
            #    ca = list()
            #elif rc.count(l)> 0:
            #    ca = rc[ca]
            try:
                for pos,sl in enumerate(s):
                    print(sl)
                    print(f's,i is {sl},{pos}')
                    print(f'word for {sl} is {strs[s[pos]]}')
                    ca.append(strs[s[pos]])
            except TypeError:
                print(f'word for {s} is {strs[s]}')
                ca.append(strs[s])
            rc.append(ca)
            print(f'{l},{s} done')
        print(f'dc is {dc}')
        return rc


solve = Solution()

result = solve.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

print(result)