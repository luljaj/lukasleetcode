import itertools
from itertools import takewhile
import time
'''
1+1=0 with carry 1
1+0=1 with carry 0
0+1=1 with carry 0
0+0=0 with carry 0
Imp:1+1=1 with carry 1 if previous carry was 1.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carryover = 0
        alist = list(map(int,a))
        blist = list(map(int,b))
        alist.reverse()
        blist.reverse()
        aiter = iter(alist)
        biter = iter(blist)
        clist = []
        ca = next(aiter)
        cb = next(biter)
        while  carryover > 0 or (ca or cb == 0,1):
            print(f'{ca}A{cb}B', end=" ")
            if (ca and cb) == 1:
                print(f'1 and 1', end="")
                clist.append(1)
                print(clist)
                carryover += 1
            if (ca ^ cb):
                print('1 and 0', end="")
                clist.append(1) 
                print(clist)
            if (ca ^ cb):
                print('0 and 0', end="")
                clist.append(0)
                print(clist)
            print(f'{ca},{cb},{carryover}')
            try:
                ca = next(aiter)
            except StopIteration:
                ca = 0
            try:
                cb = next(aiter)
            except StopIteration:
                cb = 0
            time.sleep(0.5)
        clist.reverse()
        return clist
            


solve = Solution()

result = solve.addBinary(a = "1", b = "0")

print(result)