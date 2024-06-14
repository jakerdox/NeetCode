from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(2):
            for j in range(len(nums)):
                answer.append(nums[j])
        return answer