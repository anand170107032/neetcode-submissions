class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        seen = set(nums)
        res = 0
        for i in range(n):
            curr = nums[i]
            if curr-1 in seen:
                continue
            currLen = 0

            while curr in seen:
                currLen += 1
                curr +=1

            res = max(res, currLen)

        return res
        