class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])
            


    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        res = ''
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid][1] == timestamp:
                return arr[mid][0]
            if arr[mid][1] > timestamp:
                right = mid - 1
            else:
                res = arr[mid][0]
                left = mid + 1
        return res
                
    
