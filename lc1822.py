class Solution:
    def arraySign(self, nums: List[int]) -> int:
        k = 0
        if (0 in nums):
            return 0
        for n in nums: 
            if (n < 0):
                k += 1
        if (k % 2 == 0):
            return 1
        else: return -1