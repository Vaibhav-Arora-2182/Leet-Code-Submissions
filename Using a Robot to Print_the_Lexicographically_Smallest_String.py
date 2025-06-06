class Solution:

    def robotWithString(self, s: str) -> str:
        """
        You are given a string s and a robot that currently holds an empty string t.
        Apply one of the following operations until s and t are both empty:
        Remove the first character of a string s and give it to the robot.
        The robot will append this character to the string t.
        Remove the last character of a string t and give it to the robot.
        The robot will write this character on paper.
        Return the lexicographically smallest string that can be written on the paper.
        """
        min_char = min(s)
        min_char_count = s.count(min_char)

        res, stack, last_idx = "", [], len(s) - 1
        for idx, char in enumerate(s):
            if char == min_char:
                res += char
                min_char_count -= 1
                if min_char_count == 0:
                    if idx >= last_idx:
                        break
                    min_char = min(s[idx + 1 :])
                    min_char_count = s[idx + 1 :].count(min_char)
                    while stack and stack[-1] <= min_char:
                        res += stack.pop()
            else:
                stack.append(char)

        return res + "".join(stack[::-1])
