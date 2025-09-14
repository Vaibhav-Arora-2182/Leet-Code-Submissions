import time
from collections import defaultdict
from typing import List


class Solution:
    """

    Given a wordlist and a list of queries:
    - If the query matches exactly, return the exact match.
    - Else if the query matches case-insensitively, return the first such match.
    - Else if the query matches by replacing vowels with a placeholder,
      return the first such match.
    - Otherwise, return an empty string.

    Constraints:
    - 1 <= len(wordlist), len(queries) <= 5000
    - Each word/query is non-empty and consists of English letters only.
    """

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        Approach:
        - Maintain:
          1. exact set for exact matches
          2. lowercase dict for case-insensitive matches
          3. vowel-hashed dict for vowel error matches
        - Process queries in O(L) time each (L = word length).
        """

        def case_hash(s: str) -> str:
            return s.lower()

        def vowel_hash(s: str) -> str:
            return (
                s.lower()
                .replace("e", "a")
                .replace("i", "a")
                .replace("o", "a")
                .replace("u", "a")
            )

        exact = set(wordlist)
        case = {}
        vowl = {}

        for w in wordlist:
            c = case_hash(w)
            if c not in case:
                case[c] = w
            v = vowel_hash(w)
            if v not in vowl:
                vowl[v] = w

        def correct(w: str) -> str:
            if w in exact:
                return w
            c = case_hash(w)
            if c in case:
                return case[c]
            v = vowel_hash(w)
            if v in vowl:
                return vowl[v]
            return ""

        return [correct(q) for q in queries]


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "wordlist": ["KiTe", "kite", "hare", "Hare"],
            "queries": [
                "kite",
                "Kite",
                "KiTe",
                "Hare",
                "HARE",
                "Hear",
                "hear",
                "keti",
                "keet",
                "keto",
            ],
            "ans": ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"],
        },
        {
            "wordlist": ["yellow"],
            "queries": ["YellOw"],
            "ans": ["yellow"],
        },
        {
            "wordlist": ["abc", "ABC", "aBc"],
            "queries": ["aBC", "Abc", "xyz"],
            "ans": ["abc", "abc", ""],
        },
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.spellchecker(**params)
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
