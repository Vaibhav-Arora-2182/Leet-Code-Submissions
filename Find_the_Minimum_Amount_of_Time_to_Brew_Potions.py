import time
from typing import List


class Solution:
    """
    Minimum Brewing Time for Sequential Potions and Wizards.

    Each potion must pass through all wizards in order.
    Wizard i takes skill[i] * mana[j] time on potion j.
    Wizards and potions must be synchronized (like a flow shop scheduling).

    Approach:
    Dynamic flow propagation using cumulative 'done' array.
    """

    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        done = [0] * (n + 1)

        for j in range(m):
            for i in range(n):
                done[i + 1] = max(done[i + 1], done[i]) + skill[i] * mana[j]
            for i in range(n - 1, 0, -1):
                done[i] = done[i + 1] - skill[i] * mana[j]

        return done[n]


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"skill": [1, 5, 2, 4], "mana": [5, 1, 4, 2], "ans": 110},
        {"skill": [1, 1, 1], "mana": [1, 1, 1], "ans": 5},
        {"skill": [1, 2, 3, 4], "mana": [1, 2], "ans": 21},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.minTime(**params)
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
