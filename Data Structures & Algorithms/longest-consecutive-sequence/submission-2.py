class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        seen = set(nums)
        res = 0
        for i in range(n):
            currLen = 0
            curr = nums[i]

            while curr in seen:
                currLen += 1
                curr +=1

            res = max(res, currLen)

        return res
        