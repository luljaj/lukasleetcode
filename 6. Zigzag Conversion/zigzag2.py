class Solution:
    def convert(self, s: str, numRows: int) -> str:
        complete = {}
        slist = list(s)
        nlist = []
        current = 1
        direction = 1
        for _ in range(len(slist)):
            nlist.append(numRows - current + 1)
            if current == numRows:
                print(f'{current} current and {numRows} rows')
                direction = -1
                current = current+direction
                continue
            if current == 1:
                print(f'current is {current}, direction is {direction}')
                print(current,direction)
                direction = 1
                current = current+direction
                continue
            else:
                current = current+direction
                continue
            
        print (nlist)

        if numRows == 1:
            return s
        print (nlist)



    
        cRow = numRows
        for l in range(numRows):
            print(f' checking {cRow}')
            for l,s in zip(slist,nlist):
                {f'{l} is in row {s}'}
                if cRow == s:
                    
                    complete.append(l)
                    print(f' adding {l} bc its in {cRow}')
                    continue
                else:
                    print(f'{l}not {cRow} its {s}')
                    continue
            cRow -= 1
            print(f' movin to  {cRow}')

    

        return "".join(complete)
        

solve = Solution()

result = solve.convert("AB",1)

print(result)