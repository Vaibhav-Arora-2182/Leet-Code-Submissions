import time


class Solution:
    """
    Alice and Bob play a game on string s:
    - Alice removes substrings with odd number of vowels
    - Bob removes substrings with even number of vowels
    - The first unable to move loses.

    Return True if Alice wins, else False.
    """

    def doesAliceWin(self, s: str) -> bool:
        """
        Approach:
        - Count vowels in s
        - If there are 0 vowels, Alice cannot start => False
        - Otherwise, Alice can always guarantee a win => True
        """
        return sum(s.count(v) for v in "aeiou") > 0


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"s": "leetcoder", "ans": True},
        {"s": "bbcd", "ans": False},
        {"s": "aeiou", "ans": True},
        {"s": "bcdfg", "ans": False},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.doesAliceWin(**params)
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
