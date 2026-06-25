class MedianFinder:

    def __init__(self):
        # in left one first element should be highest one which means i need to use max heap
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        # finding the median is not the hardest part 
        # Thoughts: I will divide array in to 2 list -> left and right
        # initial condition if there is nothing on both arrays it will go to left 

        if(not self.left or -self.left[0] >= num):
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if(len(self.left) - len(self.right)) == 2:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        if(len(self.right) - len(self.left) == 2):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        