import time


class Solution:
    """
    Dynamic Programming with Sliding Window.

    dp[i] = probability of reaching exactly i points.
    Transition:
        dp[i] = (sum of dp[i-1], dp[i-2], ..., dp[i-maxPts]) / maxPts
    where indices are valid and < k (since drawing stops at >= k).

    Final answer = sum of dp[i] for k <= i <= n.
    """

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            else:
                result += dp[i]

            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return result


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 10, "k": 1, "maxPts": 10, "ans": 1.0},
        {"n": 6, "k": 1, "maxPts": 10, "ans": 0.6},
        {"n": 21, "k": 17, "maxPts": 10, "ans": 0.73278},
        {"n": 10000, "k": 5000, "maxPts": 10000, "ans": None},  # performance test
    ]

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.new21Game(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if test_case["ans"] is not None:
            if abs(ans - test_case["ans"]) > 1e-5:
                print(
                    f"Test Case - {ind+1} FAILED\n"
                    f"Expected: {test_case['ans']}, Got: {ans:.5f}\n"
                    f"(Time: {elapsed_ms:.4f} ms)\n"
                )
            else:
                print(f"Test Case - {ind+1} PASSED (Time: {elapsed_ms:.4f} ms)")
        else:
            print(
                f"Test Case - {ind+1} COMPLETED (Result: {ans:.5f}, Time: {elapsed_ms:.4f} ms)"
            )
