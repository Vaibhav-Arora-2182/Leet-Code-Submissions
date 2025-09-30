import time
from typing import List


class Solution:
    """
    Given an array of digits (0–9), repeatedly replace it with pairwise sums
    modulo 10 until only one element remains. Return that final triangular sum.

    Approach:
    - Observed that the process is equivalent to computing:
        result = Σ (C(n-1, i) * nums[i]) % 10
      where C(n-1, i) are binomial coefficients.
    - Use iterative formula to compute binomial coefficients efficiently.
    - This gives O(n) time and O(1) extra space.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        coeff = 1
        for i in range(n):
            res = (res + coeff * nums[i]) % 10
            if i < n - 1:
                coeff = coeff * (n - 1 - i) // (i + 1)
        return res


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, 2, 3, 4, 5], "ans": 8},
        {"nums": [5], "ans": 5},
        {"nums": [9, 9, 9], "ans": 6},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.triangularSum(**params)
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
