class Solution:
    def isValid(self, s: str) -> bool:
        answer = []
        closeToOpen = {"}": "{", "]": "[", ")": "("}
        for c in s:
            if c not in closeToOpen:
                answer.append(c)
                continue
            if not answer or answer[-1] != closeToOpen[c]:
                return False
            answer.pop()
        return not answer