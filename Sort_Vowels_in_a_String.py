import time
from typing import List


class Solution:
    """
    Given a string s, permute vowels such that:
    - Consonants remain in their original positions
    - Vowels appear in sorted ASCII order
    Return the resulting string.
    """

    def sortVowels(self, s: str) -> str:
        """
        Approach:
        1. Extract all vowels from s
        2. Sort them by ASCII
        3. Rebuild string, replacing vowels in order
        """
        vowels = set("aeiouAEIOU")
        vowel_list = sorted([ch for ch in s if ch in vowels])

        res = []
        idx = 0
        for ch in s:
            if ch in vowels:
                res.append(vowel_list[idx])
                idx += 1
            else:
                res.append(ch)

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"s": "lEetcOde", "ans": "lEOtcede"},
        {"s": "lYmpH", "ans": "lYmpH"},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.sortVowels(**params)
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
