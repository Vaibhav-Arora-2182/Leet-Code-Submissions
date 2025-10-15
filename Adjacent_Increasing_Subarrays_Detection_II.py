import time
from typing import List


class Solution:
    """
    Given an array nums of n integers, find the maximum value of k for which there exist
    two adjacent subarrays of length k each, such that both are strictly increasing.

    Specifically, there must exist indices a and b = a + k such that:
      - nums[a..a+k-1] and nums[b..b+k-1] are strictly increasing.
      - These two subarrays are adjacent.

    Example:
        Input: nums = [2,5,7,8,9,2,3,4,3,1]
        Output: 3

        Explanation:
        The subarray [7,8,9] and its adjacent [2,3,4] are both strictly increasing.
    """

    def max_adjacent_increasing_subarrays(self, nums: List[int]) -> int:
        """
        Compute the maximum length `k` such that there exist two adjacent subarrays
        of length `k` each in `nums`, both of which are strictly increasing.

        The two subarrays must be contiguous and non-overlapping, meaning that if the
        first subarray starts at index `a`, the second one starts exactly at `b = a + k`.

        Algorithm:
            1. Maintain two counters:
               - `up`: the length of the current strictly increasing run ending at the current index.
               - `preUp`: the length of the previous increasing run before the current run began.

            2. Traverse the array from left to right:
               - If `nums[i] > nums[i - 1]`, the current run continues → increment `up`.
               - Otherwise, store the previous run length (`preUp = up`) and reset `up = 1`.

            3. At each step, determine the possible `k` values:
               - `min(preUp, up)`: maximum adjacent `k` if two increasing runs exist back-to-back.
               - `up // 2`: maximum adjacent `k` if a single long increasing run can contain
                            two adjacent subarrays of length `k` each.
               - The candidate for this step is `max(min(preUp, up), up // 2)`.

            4. Track the maximum candidate across all indices as the final result.

        Time Complexity:
            O(n) — The array is scanned once.

        Space Complexity:
            O(1) — Constant extra space is used.

        Parameters
        ----------
        nums : list[int]
            The input list of integers.

        Returns
        -------
        int
            The maximum possible value of `k` for which two adjacent strictly
            increasing subarrays of length `k` exist.

        Examples
        --------
        >>> sol = Solution()
        >>> sol.max_adjacent_increasing_subarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1])
        3
        >>> sol.max_adjacent_increasing_subarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7])
        2

        """
        n = len(nums)
        up, preUp, res = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up += 1
            else:
                preUp = up
                up = 1
            half = up >> 1
            m = min(preUp, up)
            candidate = max(half, m)
            if candidate > res:
                res = candidate
        return res


if __name__ == "__main__":

    sol = Solution()

    test_cases = [
        {"nums": [2, 5, 7, 8, 9, 2, 3, 4, 3, 1], "ans": 3},
        {"nums": [1, 2, 3, 4, 4, 4, 4, 5, 6, 7], "ans": 2},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.max_adjacent_increasing_subarrays(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
