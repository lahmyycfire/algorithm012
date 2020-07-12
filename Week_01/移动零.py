class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                j = j + 1                
            elif j > 0:
                nums[i - j], nums[i] = nums[i], 0

        return nums