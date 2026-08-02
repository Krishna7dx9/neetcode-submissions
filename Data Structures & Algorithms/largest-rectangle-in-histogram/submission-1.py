class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        max_area = 0

        for left in range(n):
            min_height = float('inf')

            for right in range(left, n):
                min_height = min(min_height, heights[right])
                width = right - left + 1
                area = min_height * width
                max_area = max(max_area, area)

        return max_area