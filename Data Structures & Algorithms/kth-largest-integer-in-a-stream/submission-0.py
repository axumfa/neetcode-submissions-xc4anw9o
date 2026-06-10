class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeaps = nums
        self.k = k
        heapq.heapify(self.minHeaps)
        while len(self.minHeaps) > k:
            heapq.heappop(self.minHeaps)


    def add(self, val: int) -> int:
        
        heapq.heappush(self.minHeaps, val)
        if len(self.minHeaps) > self.k:
            heapq.heappop(self.minHeaps)
        
        return self.minHeaps[0]
