import time
from typing import List


class Solution:
    """
    Given an integer array `nums` and integer `k`, check if there exist two *adjacent*
    subarrays of length `k` that are both strictly increasing.

    Adjacent means:
      - First subarray starts at index `a`
      - Second subarray starts at index `b = a + k`

    Approach:
    1. Precompute a helper array `inc[i]` = length of current strictly increasing streak ending at i.
    2. For each possible adjacent pair (a, a + k):
        - Check if subarray [a..a+k-1] is strictly increasing → requires inc[a+k-1] >= k
        - Check if subarray [a+k..a+2k-1] is strictly increasing → requires inc[a+2k-1] >= k
    3. If both hold for any a, return True.

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def hasTwoIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        inc = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        for a in range(0, n - 2 * k + 1):
            if inc[a + k - 1] >= k and inc[a + 2 * k - 1] >= k:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [2, 5, 7, 8, 9, 2, 3, 4, 3, 1], "k": 3, "ans": True},
        {"nums": [1, 2, 3, 4, 4, 4, 4, 5, 6, 7], "k": 5, "ans": False},
        {"nums": [1, 2, 3, 4, 5, 6, 7, 8, 9], "k": 2, "ans": True},
        {"nums": [9, 8, 7, 6, 5, 4, 3, 2], "k": 2, "ans": False},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.hasTwoIncreasingSubarrays(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        expected = test_case["ans"]
        if ans != expected:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {expected}, Got: {ans}\n"
                f"Input: {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
