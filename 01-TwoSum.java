class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i,j;
        int[] array = new int[2];
        for(i=0;i<nums.length;i++){
            for(j=0;j<i;j++){
                if(nums[i]+nums[j]==target){
                    array[0] = i;
                    array[1] = j;
                }
            }
        }
        return array;
    }
}

//Runtime: 37 ms, faster than 15.19% of Java online submissions for Two Sum.
//Memory Usage: 37.2 MB, less than 98.78% of Java online submissions for Two Sum.
