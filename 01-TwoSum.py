 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(0,i):
                if(nums[i]+nums[j]==target):
                    return [i,j]
                
#Runtime: 2224 ms, faster than 31.20% of Python online submissions for Two Sum.
#Memory Usage: 12.6 MB, less than 77.88% of Python online submissions for Two Sum.


class Solution:
    def twoSum(self, nums, target):
        num_set = {}
        for num_index, num in enumerate(nums):
            if (target-num) in num_set:
                return [num_set[target-num], num_index]
            num_set[num] = num_index
            
#Runtime: 36 ms, faster than 97.15% of Python3 online submissions for Two Sum.
#Memory Usage: 14.3 MB, less than 38.44% of Python3 online submissions for Two Sum.
#使用enumerate枚举，并用num_set记录已遍历过的元素index，判断成功后return
