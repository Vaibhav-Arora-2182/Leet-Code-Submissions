from typing import List


class Solution:
    """
    The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

    For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
    Given an array nums, return the sum of all XOR totals for every subset of nums.

    Note: Subsets with the same elements should be counted multiple times.

    An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
    """

    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        total = 0
        n = len(nums)

        for i in range(31):
            mask = 1 << i
            count = 0

            for num in nums:
                if num & mask:
                    count += 1
            if count > 0:
                total += mask * (1 << (n - 1))
                
        return total
