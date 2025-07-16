import time
from typing import List


class Solution:
    """
    Given an integer array nums, a subsequence is valid if:
    (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... for all adjacent pairs.

    A valid subsequence has either:
      - All elements of the same parity (even-even or odd-odd → sum % 2 == 0), or
      - Alternating parity (even-odd-even... or odd-even-odd... → sum % 2 == 1).

    Return the length of the longest such valid subsequence.
    """

    def maximumLength(self, nums: List[int]) -> int:
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 == 1]

        same_parity_max = max(len(evens), len(odds))

        alt1 = self._max_alternating(nums, start_parity=0)
        alt2 = self._max_alternating(nums, start_parity=1)

        return max(same_parity_max, alt1, alt2)

    def _max_alternating(self, nums: List[int], start_parity: int) -> int:
        expected = start_parity
        count = 0
        for x in nums:
            if x % 2 == expected:
                count += 1
                expected ^= 1  # Flip parity
        return count


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"nums": [1, 2, 3, 4], "ans": 4},
        {"nums": [1, 2, 1, 1, 2, 1, 2], "ans": 6},
        {"nums": [1, 3], "ans": 2},
        {"nums": [1, 8, 4, 2, 4], "ans": 4},
        {"nums": [2, 2, 2, 2], "ans": 4},
        {"nums": [1, 1, 2, 2, 1], "ans": 3},
        {"nums": [1, 1, 1, 1, 1, 1], "ans": 6},
        {"nums": [2, 1, 2, 1, 2], "ans": 5},
        {"nums": [1, 2], "ans": 2},
    ]

    for i, tc in enumerate(test_cases, 1):
        start = time.time()
        result = sol.maximumLength(**{k: v for k, v in tc.items() if k != "ans"})
        elapsed = (time.time() - start) * 1000
        status = "Passed" if result == tc["ans"] else "Failed"
        print(f"Test Case {i}: {status} (Time: {elapsed:.2f} ms)")
        if status == "Failed":
            print(f"  Input    : {tc['nums']}")
            print(f"  Expected : {tc['ans']}")
            print(f"  Got      : {result}")
