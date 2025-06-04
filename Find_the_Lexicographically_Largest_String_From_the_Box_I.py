class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        window = len(word) - numFriends + 1
        res = -1
        maxScore = ""
        for idx in range(len(word)):
            if word[idx: idx + window] > maxScore:
                maxScore = word[idx: idx + window]
                res = idx
        return word[res: res + window]
