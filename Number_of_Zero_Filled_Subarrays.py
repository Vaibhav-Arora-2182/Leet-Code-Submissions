import time
from typing import List


class Solution:
    """
    Given an integer array nums, return the number of subarrays filled with 0.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example:
    Input: nums = [1,3,0,0,2,0,0,4]
    Output: 6
    """

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Approach:
        - Maintain a running counter `count` of consecutive zeros.
        - Each zero contributes `count` new subarrays ending at that position.
        - Reset `count` when a non-zero is found.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count = 0
        result = 0

        for num in nums:
            if num == 0:
                count += 1
                result += count
            else:
                count = 0

        return result


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, 3, 0, 0, 2, 0, 0, 4], "ans": 6},
        {"nums": [0, 0, 0, 2, 0, 0], "ans": 9},
        {"nums": [2, 10, 2019], "ans": 0},
        {"nums": [0], "ans": 1},
        {"nums": [0, 0, 0, 0], "ans": 10},  # (4*5)/2 subarrays
        {"nums": [0] * 100000, "ans": 100000 * 100001 // 2},  # Large test
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.zeroFilledSubarray(**params)
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
