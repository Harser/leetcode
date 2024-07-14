class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        check = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != check:
                check = nums[i]
            else:
                nums[i] = 101
                k += 1
        nums.sort()
        return len(nums) - k