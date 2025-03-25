""" def binaryToDecimal(s):
    value = 0
    b = enumerate(list(map(int,s)))
    for pos, i in b:
        print(f'{pos} position {i} value')
        value += (2**pos) * i
    return value
"""
#def decToBinary(num):

def finishcarry(carry,cont):
    for _ in range(carry):
        carry -= 1
        cont.append(1)
    return cont

def attachend(d,l,ol):
    


    return newlist
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        alist = list(map(int,a))
        blist = list(map(int,b))
        combinedlist = list(zip(alist,blist))
        difference = len(alist) - len(blist)
        if difference > 0:
            longerlist = alist
        if difference < 0:
            longerlist = blist
        print(f'{difference} diff')
        crt = []
        carryover=0
        for a,b in reversed(combinedlist):
            if a == b == carryover == 0:
                crt.append(0)
                continue
            if a != b and carryover == 0:
                crt.append(1)
                continue
            if a == b == 1 and carryover == 0:
                crt.append(0)
                carryover += 1
                continue
            if a == b == 0 and carryover >=1:
                crt.append(1)
                carryover -= 1
                continue
            if a != b and carryover >= 1:
                crt.append(1)
                carryover -= 1
                continue
            if a == b == 1 <= carryover:
                crt.append(1)
                carryover -= 1
                continue
        print(crt)
        crt = finishcarry(carryover,crt)
        crt.reverse()
        if difference != 0:
            crt = attachend(diff,longerlist,crt)
        print (crt)


solve = Solution()

result = solve.addBinary(a = "10", b = "101110")

print (result)