'''
1+1=0 with carry 1
1+0=1 with carry 0
0+1=1 with carry 0
0+0=0 with carry 0
Imp:1+1=1 with carry 1 if previous carry was 1.
'''

import itertools

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        al = list(map(int,a))
        bl = list(map(int,b))
        al.reverse()
        bl.reverse()
        cr = 0
        cl = list(itertools.zip_longest(al,bl,fillvalue=0))
        print(cl)
        fl = []
        for a,b in cl:
            if a == b == 1:
                print('1 and 1')
                if cr >= 1:
                    fl.append(1)
                if cr == 0:
                    fl.append(0)
                    cr += 1
            if a == b == 0:
                print('0 and 0')
                if cr >= 1:
                    print('carrying 1')
                    fl.append(1)
                    cr -= 1
                else:
                    fl.append(0)
            if a != b:
                if cr >= 1:
                    print('carrying 1')
                    fl.append(0)
                else:
                    fl.append(1)
        fl.extend(itertools.repeat(1,cr))
        fl.reverse()
        fl = "".join(map(str,fl))
        return fl

                
            




solve = Solution()

result = solve.addBinary(a = "1111", b = "1111")

print(result)