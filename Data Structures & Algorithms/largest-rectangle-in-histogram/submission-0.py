class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)

        for i in range(len(heights)):

            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = height * (i - index)
                maxArea = max(area,maxArea)
                start = index
            
            stack.append([start,heights[i]])
        
        return maxArea