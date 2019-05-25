#Cheating#
 import os
 class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)

#Runtime: 28 ms, faster than 99.81% of Python3 online submissions for Longest Common Prefix.
#Memory Usage: 13.2 MB, less than 47.77% of Python3 online submissions for Longest Common Prefix.


#My own solution#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        str_min = min(strs,key=len)
        prefix = ""
        for char in str_min:
            temp = False
            for word in strs:
                if word.startswith(prefix+char):
                    temp = True
                else: 
                    temp = False
                    break                   
            if(temp):
                prefix += char
        return prefix
    
#Runtime: 32 ms, faster than 98.75% of Python3 online submissions for Longest Common Prefix.
#Memory Usage: 13.3 MB, less than 35.39% of Python3 online submissions for Longest Common Prefix.
