import time
from typing import List


class Solution:
    """
    A word is valid if:
      1. Length is at least 3.
      2. All characters are ASCII letters or digits.
      3. At least one vowel exists.
      4. At least one consonant exists.

    Vowels: a, e, i, o, u (case-insensitive)
    Consonants: A-Z or a-z letters that are not vowels.
    """

    vowels = set("aeiouAEIOU")

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in self.vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"word": "b3", "ans": False},
        {"word": "a3$e", "ans": False},
        {"word": "Umbrella9", "ans": True},
        {"word": "Aei123", "ans": False},
        {"word": "125", "ans": False},
        {"word": "z1o", "ans": True},
    ]

    for i, tc in enumerate(test_cases, 1):
        start = time.time()
        result = sol.isValid(**{k: v for k, v in tc.items() if k != "ans"})
        elapsed = (time.time() - start) * 1000
        status = "Passed" if result == tc["ans"] else "Failed"
        print(f"Test Case {i}: {status} (Time: {elapsed:.2f} ms)")
        if status == "Failed":
            print(f"  Input    : {tc['word']!r}")
            print(f"  Expected : {tc['ans']}")
            print(f"  Got      : {result}")
