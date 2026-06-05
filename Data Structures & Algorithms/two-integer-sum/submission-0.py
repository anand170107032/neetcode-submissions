class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        mp[nums[0]] = 0
        for i in range(1, len(nums)):
            comp = target-nums[i]

            if comp in mp:
                return [mp[comp], i]

            else:
                mp[nums[i]] = i


        return 

        