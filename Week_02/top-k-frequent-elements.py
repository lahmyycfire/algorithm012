class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = collections.Counter(nums)
        return heapq.nlargest(k, dt.keys(), key=dt.get)