class Solution:
    def myAtoi(self, s: str) -> int:
        strs = s.strip()
        if strs == '' :
            return 0
        if strs[0].isalpha():
            return 0 

        lst = [x for x in strs.split() if not x.isalpha()]
        lst = lst[0]
        temp=''
        isNeg = False

           
        if '+' in lst[0]:
            lst=lst[1:]
           
        elif '-' in lst[0]:
            isNeg = True
            lst=lst[1:]
        
        for i in lst:
            if i.isnumeric() or i == '.':
                temp+=i
            else: break

        if temp == '':
            return 0
        if '.' in temp: temp = float(temp)
        if isNeg:
            temp = '-' + temp
        temp = int(temp)
        if temp > 2**31-1: return 2**31-1                
        if temp < -2**31: return -2**31

        return temp 

strs = '  046s'

solve = Solution()
result = solve.myAtoi(strs)
print(result)