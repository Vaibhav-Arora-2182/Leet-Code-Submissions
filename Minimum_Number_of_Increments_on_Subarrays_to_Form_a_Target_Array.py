import time
from typing import List


class Solution:
    """
    Problem:
    --------
    You are given an integer array `target`.
    You start with an array `initial` of the same length filled with zeros.

    In one operation, you can choose any subarray of `initial` and increment each value by 1.

    Return the minimum number of operations required to make `initial` equal to `target`.

    Example:
    --------
    Input: target = [1,2,3,2,1]
    Output: 3

    Input: target = [3,1,1,2]
    Output: 4

    Input: target = [3,1,5,4,2]
    Output: 7

    Constraints:
    ------------
    1 <= target.length <= 10^5
    1 <= target[i] <= 10^5
    """

    def minNumberOperations(self, target: List[int]) -> int:
        """
        Approach:
        ----------
        - Each time the target value increases compared to the previous element,
          that increase requires new operations (since we can increment subarrays).
        - If it decreases or stays the same, we don’t need extra operations.

        - Therefore, the total operations = target[0] + sum(max(target[i] - target[i-1], 0))

        Example:
        target = [1,2,3,2,1]
        => operations = 1 (first element)
                      + (2-1) + (3-2) + max(2-3,0) + max(1-2,0)
                      = 1 + 1 + 1 + 0 + 0 = 3

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        operations = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        return operations


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"target": [1, 2, 3, 2, 1], "ans": 3},
        {"target": [3, 1, 1, 2], "ans": 4},
        {"target": [3, 1, 5, 4, 2], "ans": 7},
        {"target": [1, 1, 1, 1], "ans": 1},
        {"target": [5], "ans": 5},

    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.minNumberOperations(**params)
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
