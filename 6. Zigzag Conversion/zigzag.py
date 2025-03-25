class Solution:
    def convert(self, s: str, numRows: int) -> str: 

        slist = list(s)
        olist = []
        r1s = 2*numRows - 2

        def fzigcount(xs):
            start = 0
            for x in xs:
                if start%r1s != 0:
                    print(f'not {x} bc {start} and {r1s}')
                    start += 1
                    continue
                if start%r1s == 0:
                    print(f'IS {x} bc {start} and {r1s}')
                    start += 1
                    yield (x)
                    continue
            
        def midcount(xs):
            start = 0
            for x in xs:
                if start%r1s != 0:
                    print(f'IS {x} bc {start} and {r1s}')
                    yield(x)
                    start +=1
                    continue
                if start%r1s == 0:
                    print(f'not {x} bc {start} and {r1s}')
                    start += 1
                    continue
            
        
        def tzigcount(xs):
            start = numRows-1
            for x in xs:
                if start%r1s != 0:
                    print(f'not {x} bc {start} and {r1s}')
                    start += 1
                    continue
                if start%r1s == 0 or start==numRows:
                    print(f'IS {x} bc {start} and {r1s}')
                    start += 1
                    yield (x)
                    continue

            


        for l in fzigcount(slist):
           olist.append(l)

        print('first done')

        for l in midcount(slist):
           olist.append(l)

        print('second done')

        for l in tzigcount(slist):
           olist.append(l)

        return "".join(olist)


solve = Solution()

result = solve.convert('PAYPALISHIRING',4)

print(result)

# the 2nd letter will always be at position 2n-1 for N rows.
#PAHNAPLSIIGYIR at 3
#PINALSIGYAHRPI at 4