import time
from typing import List


class Solution:
    """
    Given an integer n, return any array containing n unique integers such that they add up to 0.

    Problem:
    - You must return an array of n unique integers.
    - The sum of the array should be exactly 0.

    Example:
    Input: n = 5
    Output: [-2, -1, 0, 1, 2]   (or any valid permutation)

    Input: n = 3
    Output: [-1, 0, 1]
    """

    def sumZero(self, n: int) -> List[int]:
        """
        Approach:
        - If n is odd, include 0 in the list.
        - Add pairs of positive and negative integers (e.g., -1 and 1, -2 and 2, ...).
        - This guarantees uniqueness and ensures that the total sum is 0.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        mid = [0] if n & 1 else []
        right = [i for i in range(1, n // 2 + 1)]
        left = [-i for i in right]
        return left + mid + right


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 5, "ans": 0},
        {"n": 3, "ans": 0},
        {"n": 1, "ans": 0},
        {"n": 6, "ans": 0},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        arr = sol.sumZero(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        result_sum = sum(arr)
        if (
            result_sum != test_case["ans"]
            or len(arr) != params["n"]
            or len(arr) != len(set(arr))
        ):
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected sum: {test_case['ans']}, Got sum: {result_sum}\n"
                f"Array: {arr}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(
                f"Test Case - {ind + 1} PASSED (Array: {arr}) (Time: {elapsed_ms:.4f} ms)"
            )
