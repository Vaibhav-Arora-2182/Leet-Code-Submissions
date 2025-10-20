import time
from collections import deque


class Solution:
    """
    You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

    You can perform two operations any number of times and in any order:
        1. Add a to all digits at odd indices (0-indexed). If a digit exceeds 9, it wraps around (mod 10).
        2. Rotate the string to the right by b positions.

    Your task is to return the lexicographically smallest string you can obtain after any sequence of operations.

    Example 1:
        Input: s = "5525", a = 9, b = 2
        Output: "2050"

    Example 2:
        Input: s = "74", a = 5, b = 1
        Output: "24"

    Example 3:
        Input: s = "0011", a = 4, b = 2
        Output: "0011"
    """

    def find_lex_smallest_string(self, s: str, a: int, b: int) -> str:
        """
        Approach:
        1. We can perform two reversible operations: add on odd indices and rotate.
        2. Since the number of possible strings is finite (each digit can take 10 values and string length ≤ 100),
           we can use BFS (or DFS) to explore all possible transformations.
        3. We track visited strings to avoid cycles.
        4. For each state:
            - Generate string after applying the "add" operation.
            - Generate string after applying the "rotate" operation.
            - Continue exploring until all reachable strings are visited.
        5. Return the lexicographically smallest string encountered.

        Time Complexity: O(10 * n^2) worst-case (bounded by 10 * number of rotations)
        Space Complexity: O(n)
        """

        visited = set()
        queue = deque([s])
        smallest = s

        while queue:
            curr = queue.popleft()
            if curr < smallest:
                smallest = curr

            arr = list(curr)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            added = "".join(arr)

            rotated = curr[-b:] + curr[:-b]

            for nxt in (added, rotated):
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return smallest


if __name__ == "__main__":

    sol = Solution()

    test_cases = [
        {"s": "5525", "a": 9, "b": 2, "ans": "2050"},
        {"s": "74", "a": 5, "b": 1, "ans": "24"},
        {"s": "0011", "a": 4, "b": 2, "ans": "0011"},
        {"s": "43987654", "a": 7, "b": 3, "ans": "00553311"},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.find_lex_smallest_string(**params)
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
