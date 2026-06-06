class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        heap = []
        for n, c in count.items():
            heapq.heappush(heap, (-c, n))

        out = []
        while k:
            out.append(heapq.heappop(heap)[1])
            k-=1
        return out


        