import time
from typing import List


class Solution:
    """
    Problem:
    --------
    Given a positive integer `n`, there exists a 0-indexed array called `powers`,
    composed of the minimum number of powers of 2 that sum to `n`. The array is sorted
    in non-decreasing order, and there is only one way to form the array.

    You are given a 0-indexed 2D integer array `queries`, where queries[i] = [lefti, righti].
    Each queries[i] represents a query where you have to find the product of all
    powers[j] with lefti <= j <= righti.

    Return an array `answers`, where answers[i] is the answer to the ith query.
    Since answers may be large, return them modulo 10^9 + 7.

    Examples:
    ---------
    Example 1:
        Input: n = 15, queries = [[0,1],[2,2],[0,3]]
        Output: [2,4,64]
        Explanation: powers = [1,2,4,8]

    Example 2:
        Input: n = 2, queries = [[0,0]]
        Output: [2]
        Explanation: powers = [2]

    Constraints:
    ------------
    1 <= n <= 10^9
    1 <= queries.length <= 10^5
    0 <= lefti <= righti < len(powers)
    """

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        bins, rep = [], 1
        while n > 0:
            if n % 2 == 1:
                bins.append(rep)
            n //= 2
            rep *= 2

        m = len(bins)
        results = [[0] * m for _ in range(m)]
        for i in range(m):
            cur = 1
            for j in range(i, m):
                cur = cur * bins[j] % mod
                results[i][j] = cur

        ans = []
        for left, right in queries:
            ans.append(results[left][right])
        return ans


# ------------------------
# Test cases
# ------------------------
if __name__ == "__main__":
    test_cases = [
        {"n": 15, "queries": [[0, 1], [2, 2], [0, 3]], "ans": [2, 4, 64]},
        {"n": 2, "queries": [[0, 0]], "ans": [2]},
        {"n": 9, "queries": [[0, 0], [0, 1]], "ans": [1, 8]},
    ]

    sol = Solution()

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.productQueries(**params)
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
