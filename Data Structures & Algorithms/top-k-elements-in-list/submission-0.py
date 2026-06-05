class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1
        unique_nums = list(set(nums))
        sorted_unique_nums = sorted(unique_nums, key=lambda x: -count[x])

        return sorted_unique_nums[:k]


        