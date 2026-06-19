class MedianFinder:

    def __init__(self):

        # on left i will have Max heap (0th element is max)
        self.left = []
        
        # on right I will have Min heap (0th element is min)
        self.right = []
        

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, -num)
            return
        
        # [1, 2] v [3, 4] add(3)
        if num >= -self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if abs(len(self.left) - len(self.right)) == 2:
            if len(self.left) > len(self.right):
                n = -heapq.heappop(self.left)
                heapq.heappush(self.right, n)
            else:
                n = -heapq.heappop(self.right)
                heapq.heappush(self.left, n)
      


    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (self.right[0] - self.left[0]) / 2

