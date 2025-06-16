from typing import List


class Solution:
    """
    Given a 0-indexed integer array nums of size n,
    find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]),
    such that 0 <= i < j < n and nums[i] < nums[j].

    Return the maximum difference. If no such i and j exists, return -1.
    """

    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1

        for i in range(1, len(nums)):
            val = nums[i]
            if val > min_val:
                diff = val - min_val
                if diff > max_diff:
                    max_diff = diff
            else:
                min_val = val

        return max_diff
