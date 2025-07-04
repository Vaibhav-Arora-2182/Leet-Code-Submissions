import time
from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        lengths = [1] * (n + 1)
        for i in range(n):
            if operations[i] == 0:
                lengths[i + 1] = lengths[i] * 2
            else:
                lengths[i + 1] = lengths[i] * 2
            if lengths[i + 1] > k:
                lengths[i + 1] = k + 1

        shift = 0
        for i in range(n - 1, -1, -1):
            if k <= lengths[i]:
                continue
            else:
                k -= lengths[i]
                if operations[i] == 1:
                    shift += 1

        base_char = "a"
        final_char = chr((ord(base_char) - ord("a") + shift) % 26 + ord("a"))
        return final_char


if __name__ == "__main__":
    test_cases = [
        {"k": 5, "operations": [0, 0, 0], "ans": "a"},
        {"k": 10, "operations": [0, 1, 0, 1], "ans": "b"},
        {"k": 1, "operations": [1, 0], "ans": "a"},
    ]
    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        start = time.time()
        ans = sol.kthCharacter(k=test_case["k"], operations=test_case["operations"])
        end = time.time()
        elapsed_ms = (end - start) * 1000
        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} failed, \nTest Case = {test_case} (Time: {elapsed_ms:.2f} ms)"
            )
        else:
            print(f"Test Case - {ind + 1} passed (Time: {elapsed_ms:.2f} ms)")
