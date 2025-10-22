import time
from collections import Counter
from typing import List


class Solution:
    """
    You are given an integer array nums and two integers k and numOperations.

    You must perform an operation numOperations times on nums, where in each operation:
      - Select an index i that was not selected in any previous operations.
      - Add an integer in the range [-k, k] to nums[i].

    Return the maximum possible frequency of any element in nums after performing the operations.

    Approach:
    - Each number v can be transformed to any integer t in [v - k, v + k] (inclusive).
    - For a target integer t, the elements that can be made equal to t are those whose interval covers t.
    - Count how many intervals cover t (coverage) and how many elements are already equal to t (exact_count).
      Required operations to make all covered elements equal to t = coverage - exact_count.
      But we can only use at most numOperations operations, so achievable frequency:
        exact_count + min(numOperations, coverage - exact_count).
    - Coverage as a function of t is a step function; it only changes at interval endpoints.
      We add events +1 at (v - k) and -1 at (v + k + 1) and sweep these events, evaluating coverage
      at all relevant integer positions (endpoints and original values).
    - Time: O(n log n) due to sorting event positions. Space: O(n).
    """

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        if not nums:
            return 0
        if numOperations == 0 and k == 0:
            ctr = Counter(nums)
            return max(ctr.values())

        exact = Counter(nums)

        events = {}
        for v in nums:
            start = v - k
            endp1 = v + k + 1
            events[start] = events.get(start, 0) + 1
            events[endp1] = events.get(endp1, 0) - 1

        positions = sorted(set(events.keys()) | set(exact.keys()))

        current_coverage = 0
        res = 0
        for pos in positions:
            if pos in events:
                current_coverage += events[pos]
            cov = current_coverage
            eq = exact.get(pos, 0)
            can_add = min(numOperations, cov - eq)
            freq = eq + can_add
            if freq > res:
                res = freq

        return res


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, 4, 5], "k": 1, "numOperations": 2, "ans": 2},
        {"nums": [5, 11, 20, 20], "k": 5, "numOperations": 1, "ans": 2},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.maxFrequency(**params)
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
