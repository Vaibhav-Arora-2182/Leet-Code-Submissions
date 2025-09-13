import time
from collections import Counter


class Solution:
    """
    Given a string s consisting of lowercase English letters:
    - Find the vowel with the maximum frequency.
    - Find the consonant with the maximum frequency.
    Return the sum of the two frequencies.

    If no vowels or consonants exist, their frequency is considered 0.
    """

    def maxFreqSum(self, s: str) -> int:
        """
        Approach:
        - Count all characters using Counter.
        - Separate into vowels and consonants.
        - Take the maximum frequency from both groups.
        - Return their sum.
        """
        freq = Counter(s)
        vowels = {ch: cnt for ch, cnt in freq.items() if ch in "aeiou"}
        consonants = {ch: cnt for ch, cnt in freq.items() if ch not in "aeiou"}

        max_vowel = max(vowels.values()) if vowels else 0
        max_consonant = max(consonants.values()) if consonants else 0

        return max_vowel + max_consonant


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "s": "successes",
            "ans": 6,
        },
        {
            "s": "aeiaeia",
            "ans": 3,
        },
        {"s": "zzz", "ans": 3},
        {"s": "a", "ans": 1},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.maxFreqSum(**params)
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
