import bisect
import time
from typing import List


class Solution:
    """
    Successful Pairs of Spells and Potions (LeetCode 2300)

    You are given:
    - spells[i]: power of ith spell
    - potions[j]: strength of jth potion
    - success: threshold for successful pair (spell * potion >= success)

    Goal:
    Return an array pairs[] where pairs[i] = count of potions that form
    successful pairs with spells[i].

    Approach:
    1. Sort potions.
    2. For each spell s:
         - Find the minimum potion strength needed: ceil(success / s)
         - Use binary search to find its index in sorted potions.
         - Count = total potions - index.
    """

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []
        for s in spells:
            threshold = (success + s - 1) // s  
            idx = bisect.bisect_left(potions, threshold)
            ans.append(m - idx)
        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "spells": [5, 1, 3],
            "potions": [1, 2, 3, 4, 5],
            "success": 7,
            "ans": [4, 0, 3],
        },
        {"spells": [3, 1, 2], "potions": [8, 5, 8], "success": 16, "ans": [2, 0, 2]},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.successfulPairs(**params)
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
