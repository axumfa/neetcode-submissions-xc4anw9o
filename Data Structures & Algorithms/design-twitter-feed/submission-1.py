class Twitter:

    def __init__(self):
        self.followeeMap = defaultdict(set) # it is for userid -> (followed ids)
        self.twitterMap = defaultdict(list) #  it is verry for each user we will have list of tweetids
        self.time = 0
        # in twitterMap we need to keep track of the time for getNewsFeed        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitterMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []

        self.followeeMap[userId].add(userId)
        for followeeId in self.followeeMap[userId]:
            if followeeId in self.twitterMap:
                idx = len(self.twitterMap[followeeId]) - 1
                time, tweetId = self.twitterMap[followeeId][idx]
                minHeap.append([time, tweetId, followeeId, idx - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.twitterMap[followeeId][idx]
                heapq.heappush(minHeap, [time, tweetId, followeeId, idx - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)
        
        
