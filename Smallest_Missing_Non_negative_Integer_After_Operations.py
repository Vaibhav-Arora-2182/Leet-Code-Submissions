import time
from typing import List


class Solution:
    """
    You are given a 0-indexed integer array nums and an integer value.

    In one operation, you can add or subtract `value` from any element of nums.

    The MEX (minimum excluded value) of an array is the smallest missing
    non-negative integer in it.

    Your task is to find the **maximum possible MEX** after performing any number
    of add/subtract operations on the elements of `nums`.

    Example:
        Input: nums = [1, -10, 7, 13, 6, 8], value = 5
        Output: 4

    Approach:
    -----------
    - Any number x can be transformed into any number `x + k*value` (for integer k).
    - So effectively, each number’s possible values are determined by its remainder
      modulo `value`.
    - Count how many numbers fall into each remainder class (`0..value-1`).
    - Then, to construct the smallest non-negative integers in order, we can
      "consume" one number from each remainder bucket in a cyclic manner.
    - As soon as a bucket becomes empty for the required remainder, that is our MEX.
    """

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """
        Finds the maximum achievable MEX after applying +value or -value operations.

        Steps:
        1. Compute frequency of each remainder (mod value).
        2. Iterate i from 0 upward:
            - For each i, check the remainder i % value.
            - Decrease its count by 1.
            - If any remainder count goes below zero, that `i` is the maximum MEX.
        """
        n = len(nums)
        mod = [0] * value
        for x in nums:
            x %= value
            if x < 0:
                x += value
            mod[x] += 1
        for i in range(n):
            j = i % value
            mod[j] -= 1
            if mod[j] < 0:
                return i
        return n


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, -10, 7, 13, 6, 8], "value": 5, "ans": 4},
        {"nums": [1, -10, 7, 13, 6, 8], "value": 7, "ans": 2},
        {"nums": [0, 1, 2, 3], "value": 2, "ans": 4},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.findSmallestInteger(**params)
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
