import bisect
import time
from typing import List


class Solution:
    """
    Avoid Flood in The City (LeetCode 1488)

    You are given an array 'rains' where:
    - rains[i] > 0 means it rains over lake rains[i].
    - rains[i] == 0 means no rain and you can dry one lake.

    Goal: Prevent floods by scheduling drying days optimally.
    Return an array 'ans' where:
      - ans[i] = -1 if rains[i] > 0
      - ans[i] = lake number to dry if rains[i] == 0
    If impossible, return [].

    Approach:
    - Maintain a map of 'full' lakes and their last fill day.
    - Track available dry days (sorted list).
    - When a lake rains again, find the earliest dry day after its last fill day.
    - Use binary search (bisect) to find and allocate that dry day.
    """

    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        full = {}
        dry_days = []
        ans = [-1] * n

        for i, lake in enumerate(rains):
            if lake == 0:
                bisect.insort(dry_days, i)
                ans[i] = 1
            else:
                if lake in full:
                    last_fill = full[lake]
                    idx = bisect.bisect_right(dry_days, last_fill)
                    if idx == len(dry_days):
                        return []
                    dry_day = dry_days.pop(idx)
                    ans[dry_day] = lake
                full[lake] = i
                ans[i] = -1
        return ans


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"rains": [1, 2, 3, 4], "ans": [-1, -1, -1, -1]},
        {"rains": [1, 2, 0, 0, 2, 1], "ans": [-1, -1, 2, 1, -1, -1]},
        {"rains": [1, 2, 0, 1, 2], "ans": []},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.avoidFlood(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        expected = test_case["ans"]
        if expected == []:
            passed = ans == []
        elif len(ans) == len(expected) and all(
            (e == -1 and a == -1) or (e != -1 and a > 0) for e, a in zip(expected, ans)
        ):
            passed = True
        else:
            passed = False

        if not passed:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {expected}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
