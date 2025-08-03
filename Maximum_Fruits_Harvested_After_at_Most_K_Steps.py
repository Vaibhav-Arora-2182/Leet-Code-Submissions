import time
from typing import List
from bisect import bisect_left

class Solution:
    """
    You are given an array `fruits` where `fruits[i] = [position_i, amount_i]`. 
    You are at `startPos` and can take at most `k` steps (left or right).
    At each position you visit, you collect all fruits available there.

    Return the maximum number of fruits you can collect by walking at most `k` steps.
    """

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # Bound fruits within relevant step range
        low_idx = bisect_left(fruits, [startPos - k, 0])
        high_limit = bisect_left(fruits, [startPos + k + 1, 0])  # Exclusive upper bound

        fruits = fruits[low_idx:high_limit]  # Truncate to window of interest
        n = len(fruits)
        
        left = 0
        total = 0
        max_fruits = 0

        for right in range(n):
            total += fruits[right][1]
            # Check if current window is within step budget
            while left <= right:
                l_pos = fruits[left][0]
                r_pos = fruits[right][0]

                min_steps = min(
                    abs(startPos - l_pos) + (r_pos - l_pos),  # go left first, then right
                    abs(startPos - r_pos) + (r_pos - l_pos)   # go right first, then left
                )

                if min_steps <= k:
                    break
                total -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total)

        return max_fruits

if __name__ == "__main__":
    test_cases = [
        {"fruits": [[2,8],[6,3],[8,6]], "startPos": 5, "k": 4, "ans": 9},
        {"fruits": [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], "startPos": 5, "k": 4, "ans": 14},
        {"fruits": [[0,3],[6,4],[8,5]], "startPos": 3, "k": 2, "ans": 0},
        {"fruits": [[3,2],[4,3],[6,5]], "startPos": 5, "k": 2, "ans": 5},
        {"fruits": [[0,10000]], "startPos": 200000, "k": 200000, "ans": 10000}
    ]

    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.maxTotalFruits(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed, \nTest Case = {test_case} (Time: {elapsed_ms:.4f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.4f} ms)")
