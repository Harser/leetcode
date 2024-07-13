class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(len(nums1) - m):
            nums1.remove(0)
        nums1.extend(nums2)
        nums1.sort()