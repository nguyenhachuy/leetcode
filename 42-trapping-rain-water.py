class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        st = []
        for i in range(len(height)):
            while st and height[i] > height[st[-1]]:
                mid = st.pop()
                # No left column to support
                if not st:
                    break
                left = st[-1]
                bounded_height = min(height[i], height[left]) - height[mid]
                distance = i - left - 1
                result += bounded_height * distance
            st.append(i)
        return result

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        peak = 0
        for i in range(len(height)):
            if height[i] > height[peak]:
                peak = i

        result = 0
        left = 0
        max_left = height[left]
        while left < peak:
            max_left = max(max_left, height[left])
            result += min(max_left, height[peak]) - height[left]
            left += 1
        right = len(height) - 1
        max_right = height[right]
        while right > peak:
            max_right = max(max_right, height[right])
            result += min(max_right, height[peak]) - height[right]
            right -= 1

        return result
