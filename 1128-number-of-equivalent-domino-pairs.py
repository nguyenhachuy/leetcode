class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = {}
        result = 0
        for domino in dominoes:
            domino = tuple(sorted(domino))
            if domino in freq:
                result += freq[domino]
            # if domino[::-1] in freq:
            #     result += freq[domino[::-1]]
            freq[domino] = freq[domino] + 1 if domino in freq else 1
        return result