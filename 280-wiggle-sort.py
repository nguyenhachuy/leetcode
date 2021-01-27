class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If index is even, the number must be less than its next element, if it is not, we swap
        # If index is odd, the number must be larger than its next element, if it is not, we swap
        for i in range(len(nums)):
            if i+1 < len(nums) and ((i%2==0 and nums[i]>nums[i+1]) or (i%2==1 and nums[i] < nums[i+1])):
                nums[i], nums[i+1] = nums[i+1], nums[i]


"""
sort array in place, then swap elements pair wise starting from index 1 O(nlogn), O(1)

"""
