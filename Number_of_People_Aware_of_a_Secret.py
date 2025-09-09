import time

MOD = 10**9 + 7


class Solution:
    """
    On day 1, one person discovers a secret.
    Each person starts sharing after `delay` days, and forgets after `forget` days.
    Return the number of people who know the secret at the end of day n.
    """

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        """
        Approach:
        - dp[i] = number of people who learn the secret on day i.
        - On day 1: dp[1] = 1.
        - Each person who learns on day i contributes dp[i] to dp[j] for j in [i+delay, i+forget-1].
        - Use a running prefix sum to efficiently distribute contributions.
        - Final answer = sum of dp[i] for i in [n - forget + 1, n] (people who haven't forgotten yet).
        """
        dp = [0] * (n + 1)
        dp[1] = 1

        share_add = [0] * (n + 2)
        share_add[1 + delay] += 1
        share_add[1 + forget] -= 1

        active = 0
        for day in range(2, n + 1):
            active = (active + share_add[day]) % MOD
            dp[day] = active
            if dp[day] > 0:
                if day + delay <= n:
                    share_add[day + delay] = (share_add[day + delay] + dp[day]) % MOD
                if day + forget <= n:
                    share_add[day + forget] = (share_add[day + forget] - dp[day]) % MOD

        ans = sum(dp[max(1, n - forget + 1) : n + 1]) % MOD
        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 6, "delay": 2, "forget": 4, "ans": 5},
        {"n": 4, "delay": 1, "forget": 3, "ans": 6},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.peopleAwareOfSecret(**params)
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
