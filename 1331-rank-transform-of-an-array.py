class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        sorted_list = sorted(list(set(arr)))
        value_rank_map = { v:i+1 for i,v in enumerate(sorted_list) }
        result = []
        for num in arr:
            result.append(value_rank_map[num])
        return result