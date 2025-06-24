from typing import List


class Solution:
    """
    You are given a 0-indexed integer array nums and two integers key and k.
    A k-distant index is an index i of nums for which there exists at least one index j such that
        |i - j| <= k and nums[j] == key.

    Return a list of all k-distant indices sorted in increasing order.
    """

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        intervals = []

        for i, val in enumerate(nums):
            if val == key:
                # Create a valid range around key
                start = max(0, i - k)
                end = min(n - 1, i + k)
                intervals.append((start, end))

        # Merge overlapping intervals and collect indices
        result = []
        intervals.sort()
        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= prev_end + 1:  # overlapping
                prev_end = max(prev_end, end)
            else:
                result.extend(range(prev_start, prev_end + 1))
                prev_start, prev_end = start, end

        # Add the last interval
        result.extend(range(prev_start, prev_end + 1))

        return result
