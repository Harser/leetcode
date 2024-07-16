class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        nums1 = nums.copy()
        if len(nums) >= k:
            nums1 = nums1[-k:] + nums1[:-k]
        else:
            for i in range(k):
                nums1 = nums1[-1:] + nums1[:-1]
        for i in range(len(nums)):
            nums[i] = nums1[i]