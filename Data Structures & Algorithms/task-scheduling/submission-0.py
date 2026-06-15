class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = Counter(tasks)
        timing = 0
        maxHeap = [-s for s in t.values()]
        queue = deque()

        heapq.heapify(maxHeap)

        while queue or maxHeap:
            timing += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: 
                    queue.append((cnt, timing + n))
     
            if queue and queue[0][1] == timing:
                num = queue.popleft()[0]
                heapq.heappush(maxHeap, num)
        
        return timing
