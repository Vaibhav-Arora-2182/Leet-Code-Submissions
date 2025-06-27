from collections import Counter, deque


class Solution:
    """
    You are given a string s of length n, and an integer k.

    You are tasked to find the longest subsequence repeated k times in string s.

    A subsequence is a string that can be derived from another string by
        deleting some or no characters without changing the order of the remaining characters.

    A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s,
        where seq * k represents a string constructed by concatenating seq k times.

    For example, "bba" is repeated 2 times in the string "bababcba",
        because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".

    Return the longest subsequence repeated k times in string s.

    If multiple such subsequences are found, return the lexicographically largest one.

    If there is no such subsequence, return an empty string.
    """

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        # Only characters that appear at least k times can be part of the result
        chars = [c for c in freq if freq[c] >= k]
        chars.sort(reverse=True)  # to get lexicographically larger candidates first

        # Check if string t * k is a subsequence of s
        def is_k_subseq(t):
            it = iter(s)
            return all(all(c in it for c in t) for _ in range(k))

        queue = deque([""])
        best = ""
        while queue:
            curr = queue.popleft()
            for c in chars:
                nxt = curr + c
                if len(nxt) * k > len(s):  # prune impossible candidates
                    continue
                if is_k_subseq(nxt):
                    queue.append(nxt)
                    if len(nxt) > len(best) or (len(nxt) == len(best) and nxt > best):
                        best = nxt
        return best
        return best
