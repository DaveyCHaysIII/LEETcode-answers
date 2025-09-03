"""
4. Median of two sorted arrays

Given two sorted arrays nums1 and nums2 of size m and n
respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        allNums = nums1 + nums2
        allNums.sort()
        allNums_len = len(allNums)
        m0 = allNums_len // 2
        if allNums_len % 2 != 0:
            return allNums[m0]
        else:
            m1 = allNums[m0]
            m2 = allNums[m0 -1]
            return (m1 + m2) / 2.0

"""
Hard parts: once again, relearning python. The difference between
division and floor division, python methods, etc. Otherwise the
actual algorithm was pretty simple, I only had to reference how to
write it.

Answer: pretty close to optimal, though the actual most optimal I
could find is pretty neat in its efficiency

Time complexity: O(log(m+n))

Better solution: more clever use of modulo

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        num.sort()
        n = len(num)

        if n % 2 != 0:
            return float(num[n // 2])
        else:
            return (num[n // 2 - 1] + num[n // 2]) / 2.0
"""
