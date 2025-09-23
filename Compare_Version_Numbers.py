import time


class Solution:
    """
    Given two version strings, version1 and version2, compare them.

    A version string consists of revisions separated by '.'.
    - Revisions are integers (ignore leading zeros).
    - Missing revisions are treated as 0.

    Return:
    -1 if version1 < version2
     1 if version1 > version2
     0 if equal

    Example 1:
    Input: version1 = "1.2", version2 = "1.10"
    Output: -1

    Example 2:
    Input: version1 = "1.01", version2 = "1.001"
    Output: 0

    Example 3:
    Input: version1 = "1.0", version2 = "1.0.0.0"
    Output: 0
    """

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Approach:
        - Split both version strings by '.' into revision lists.
        - Convert each revision to int (handles leading zeros).
        - Pad the shorter list with zeros.
        - Compare element by element:
          - If v1[i] > v2[i] return 1
          - If v1[i] < v2[i] return -1
        - If all equal, return 0

        Time Complexity: O(n + m), where n and m are the number of revisions.
        Space Complexity: O(n + m) for storing revisions.
        """
        rev1 = list(map(int, version1.split(".")))
        rev2 = list(map(int, version2.split(".")))

        max_len = max(len(rev1), len(rev2))
        rev1.extend([0] * (max_len - len(rev1)))
        rev2.extend([0] * (max_len - len(rev2)))

        for a, b in zip(rev1, rev2):
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"version1": "1.2", "version2": "1.10", "ans": -1},
        {"version1": "1.01", "version2": "1.001", "ans": 0},
        {"version1": "1.0", "version2": "1.0.0.0", "ans": 0},
        {"version1": "1.0.1", "version2": "1", "ans": 1},
        {"version1": "7.5.2.4", "version2": "7.5.3", "ans": -1},
        {"version1": "3.4.5", "version2": "3.4.5", "ans": 0},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.compareVersion(**params)
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
