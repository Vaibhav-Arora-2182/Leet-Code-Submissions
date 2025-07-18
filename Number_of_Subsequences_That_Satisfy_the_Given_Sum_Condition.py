from typing import List


class Solution:
    """
    You are given an array of integers nums and an integer target.

    Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target.

    Since the answer may be too large, return it modulo 109 + 7.
    """

    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2 up to n
        power = [1] * (n)
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        res = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + power[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return res
        return res
