# My solution that I came up with 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        ans = 0
        l = len(nums1)
        if l % 2 == 1:
            ans = float(nums1[l//2])
        else:
            ans = (nums1[l//2] + nums1[(l//2)-1]) / 2
        return ans