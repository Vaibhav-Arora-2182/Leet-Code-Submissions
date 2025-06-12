from typing import List


class Solution:
    """
    Given a circular array nums, find the maximum absolute difference between adjacent elements.

    Note: In a circular array, the first and last elements are adjacent.
    """

    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(
            abs(nums[0] - nums[-1]), max(abs(a - b) for a, b in zip(nums, nums[1:]))
        )
