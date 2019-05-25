 class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            reverse = str(x)[::-1]
            if(x==int(reverse)):
                return True
            else: return False
        
#Runtime: 80 ms, faster than 83.42% of Python3 online submissions for Palindrome Number.
#Memory Usage: 13.3 MB, less than 57.03% of Python3 online submissions for Palindrome Number.

#Note: 
#使用类似07.Reverse Integer的解法，先将integer字符化，利用[::-1]反转，判断原integer和反转后是否相同
#其中负数由于负号原因，不可能成为对称数，因此在程序最开始判断integer是否非负排除此情况
