 class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        for x in s:
            if(x=="I"):
                value += 1
            elif(x=="V"):
                value += 5
            elif(x=="X"):
                value += 10
            elif(x=="L"):
                value += 50
            elif(x=="C"):
                value += 100
            elif(x=="D"):
                value += 500
            elif(x=="M"):
                value += 1000
        if("IV" in s or "IX" in s):
            value -= 2
        if("XL" in s or "XC" in s):
            value -= 20
        if("CD" in s or "CM" in s):
            value -= 200
        return value
    
#Runtime: 56 ms, faster than 97.02% of Python3 online submissions for Roman to Integer.
#Memory Usage: 13.3 MB, less than 47.86% of Python3 online submissions for Roman to Integer.

#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
