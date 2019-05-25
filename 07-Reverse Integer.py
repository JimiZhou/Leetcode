 class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            digits = str(x)
            if(x>=0):
                reverse_digits = digits[::-1]
            else:
                digits_unsign = digits[1:]
                digits_unsign = digits_unsign[::-1]
                reverse_digits = "-" + digits_unsign
                
            if(int(reverse_digits)>= 2**31-1 or int(reverse_digits)<=-2**31): return 0
            else: return int(reverse_digits)
            
#Runtime: 36 ms, faster than 95.28% of Python3 online submissions for Reverse Integer.
#Memory Usage: 13.3 MB, less than 44.12% of Python3 online submissions for Reverse Integer.

#Note: 
#1.list[::-1]可把list逆序
#2.将int转为string便于使用list处理
#3.带负号的string可以直接int()转成int
