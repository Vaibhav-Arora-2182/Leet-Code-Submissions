import time


class Solution:
    """
    Problem:
    --------
    Given a positive integer n, return the smallest number x >= n
    such that the binary representation of x contains only set bits (i.e., all 1's).

    Example:
    --------
    Input: n = 5
    Output: 7
    Explanation: 7 in binary is "111".

    Input: n = 10
    Output: 15
    Explanation: 15 in binary is "1111".

    Input: n = 3
    Output: 3
    Explanation: 3 in binary is "11".
    """

    def smallestNumberWithAllSetBits(self, n: int) -> int:
        """
        Approach:
        ----------
        - The number with all bits set up to a certain length `m`
          is of the form (1 << m) - 1.
        - We need the smallest such number >= n.
        - So, find the smallest `m` such that (1 << m) - 1 >= n.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        m = 1
        while (1 << m) - 1 < n:
            m += 1
        return (1 << m) - 1


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 5, "ans": 7},
        {"n": 10, "ans": 15},
        {"n": 3, "ans": 3},
        {"n": 1, "ans": 1},
        {"n": 8, "ans": 15},
        {"n": 16, "ans": 31},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.smallestNumberWithAllSetBits(**params)
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
