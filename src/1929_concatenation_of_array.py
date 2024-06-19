from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums) * 2):
            answer.append(nums[i % len(nums)])
        return answer
