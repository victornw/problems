class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        module = 10**9 +7
        min = 0
        max = len(nums) - 1
        while min <=  max:
            if nums[min] + nums[max] <= target:
                result = (result +pow(2,max-min, module)) % module
                min += 1
            else:
                max -= 1        
        return result