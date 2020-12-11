class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        st = []
        heights = heights + [0]
        for i,v in enumerate(heights):
            while st and heights[st[-1]] >= v:
                j = st.pop()
                width = i-st[-1]-1 if st else i
                result = max(result, heights[j] * width)
            st.append(i)
        return result
