import time

MOD = 10**9 + 7


class Solution:
    def _msbf_pow(self, base: int, exp: int) -> int:
        """
        Most Significant Bit First (MSBF) power calculation.
        Efficient modular exponentiation for small exponents (x ≤ 5).

        Args:
            base (int): The base number.
            exp (int): The exponent.

        Returns:
            int: base ** exp (without modulo since n ≤ 300, but for large cases mod is applied).
        """
        if exp == 1:
            return base
        # Manual exponentiation (since x ≤ 5, we could also use pow directly)
        result = base
        for _ in range(exp - 1):
            result *= base
        return result

    def numberOfWays(self, n: int, x: int) -> int:
        """
        Calculate the number of ways to express 'n' as the sum of unique integers each raised to the power 'x'.

        This uses an iterative dynamic programming approach (0/1 knapsack style) where each
        power of an integer is treated as an item that can be used at most once.

        Args:
            n (int): The target integer to be expressed.
            x (int): The exponent.

        Returns:
            int: The number of unique combinations modulo 1_000_000_007.

        Example:
            >>> sol = Solution()
            >>> sol.numberOfWays(10, 2)
            1
            >>> sol.numberOfWays(4, 1)
            2
        """
        # Generate all powers <= n
        powers = []
        num = 1
        while (p := self._msbf_pow(num, x)) <= n:
            powers.append(p)
            num += 1

        # 0/1 knapsack DP
        dp = [0] * (n + 1)
        dp[0] = 1

        for val in powers:
            for s in range(n, val - 1, -1):
                dp[s] += dp[s - val]
                if dp[s] >= MOD:
                    dp[s] -= MOD

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        {"n": 10, "x": 2, "ans": 1},
        {"n": 4, "x": 1, "ans": 2},
        {"n": 160, "x": 3, "ans": 1},
        {"n": 1, "x": 2, "ans": 1},
    ]

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.numberOfWays(**params)
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
