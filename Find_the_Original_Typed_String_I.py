# git add . && git commit -m "Find the Original Typed String I" && git push  
class Solution:
    """
    Alice is attempting to type a specific string on her computer. 
    However, she tends to be clumsy and may press a key for too long, 
        resulting in a character being typed multiple times.

    Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

    You are given a string word, which represents the final output displayed on Alice's screen.

    Return the total number of possible original strings that Alice might have intended to type.

    """
    def __init__(self):
        pass
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        transformations = set()
        transformations.add(word) 

        i = 0
        while i < n:
            j = i
            while j + 1 < n and word[j + 1] == word[i]:
                j += 1

            group_len = j - i + 1

            if group_len >= 2:
                for reduce_to in range(1, group_len):
                    new_word = word[:i] + word[i] * reduce_to + word[j+1:]
                    transformations.add(new_word)

            i = j + 1

        return len(transformations)


        
    

if __name__ == "__main__":
    test_cases = [
        {"word": 'abbcccc', "ans": 5},
        {"word": 'abcd', "ans": 1},
        {"word": 'aaaa', "ans": 4}
    ]
    sol = Solution()
    for ind, test_case in enumerate(test_cases):
        ans = sol.possibleStringCount(test_case["word"])
        if ans != test_case["ans"]:
            print(f"Test Case - {ind + 1} failed, \nTest Case = {test_case}")
        else:
            print(f"Test Case - {ind + 1} passed")
