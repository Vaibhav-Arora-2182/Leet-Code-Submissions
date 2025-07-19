import time
from typing import List


class Solution:
    """
    Given a list of folders **folder**, return the folders after removing all sub-folders in those folders.

    A folder[i] is a sub-folder of folder[j] if it starts with folder[j] + '/'.
    You may return the answer in any order.

    Constraints:
        - 1 <= folder.length <= 4 * 10^4
        - 2 <= folder[i].length <= 100
        - folder[i] contains only lowercase letters and '/'
        - Each folder starts with '/'
        - All folder names are unique
    """

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for path in folder:
            if not res or not path.startswith(res[-1] + "/"):
                res.append(path)
        return res


# Test harness
if __name__ == "__main__":
    testcases = {
        "Example 1": {
            "params": {"folder": ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]},
            "expected": ["/a", "/c/d", "/c/f"],
        },
        "Example 2": {
            "params": {"folder": ["/a", "/a/b/c", "/a/b/d"]},
            "expected": ["/a"],
        },
        "Example 3": {
            "params": {"folder": ["/a/b/c", "/a/b/ca", "/a/b/d"]},
            "expected": ["/a/b/c", "/a/b/ca", "/a/b/d"],
        },
    }

    solution = Solution()
    for name, tc in testcases.items():
        start = time.perf_counter()
        result = solution.removeSubfolders(**tc["params"])
        end = time.perf_counter()

        expected = tc["expected"]
        result_set = set(result)
        expected_set = set(expected)
        assert (
            result_set == expected_set
        ), f"{name} failed: expected {expected_set}, got {result_set}"
        print(f"{name} passed in {end - start:.6f} ms.")
