class Solution:
    def convert(self, s: str, numRows: int) -> str:
        complete = {

        }
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

        for l,s in zip(slist,nlist):
            print(f'{l} is in row {s}')
            try:
                complete.update({s:(complete[s]) + l})
            except KeyError:
                complete.update({s:l})
        
        returnstring = ""
        for i in complete.keys():
            print(numRows)
            print(i)
            print(complete)
            returnstring += complete[i]




        return returnstring
        

solve = Solution()

result = solve.convert("A",2)

print(result)