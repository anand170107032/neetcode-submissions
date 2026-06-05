class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        return heapq.nlargest(k, count.keys(), key=lambda x: count[x])


        