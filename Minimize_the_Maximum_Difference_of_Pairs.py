from typing import List


class Solution:
    """
    You are given a 0-indexed integer array nums and an integer p.
    Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized.
    Also, ensure no index appears more than once amongst the p pairs.
    Note that for a pair of elements at the index i and j,
    the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
    Return the minimum maximum difference among all p pairs.
    We define the maximum of an empty set to be zero.

    """

    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        n = len(nums)

        # Early exit: exactly enough elements to form p non-overlapping adjacent pairs
        if p * 2 == n:
            return max(nums[i + 1] - nums[i] for i in range(0, n, 2))

        # Binary search for minimal maximum difference
        def can_form(dmax: int) -> bool:
            count, i = 0, 1
            while i < n:
                if nums[i] - nums[i - 1] <= dmax:
                    count += 1
                    i += 2  # skip both indices to avoid overlap
                else:
                    i += 1  # try next element
                if count >= p:
                    return True  # early exit
            return False

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if can_form(mid):
                right = mid
            else:
                left = mid + 1

        return left
