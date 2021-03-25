"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W).
You also have several balls in your hand.

Each time, you may choose a ball in your hand,
and insert it into the row (including the leftmost place and rightmost place).
Then, if there is a group of 3 or more balls in the same color touching, remove these balls.
Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
1 <= board.length <= 16
1 <= hand.length <= 5
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.


Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty

Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

16*15*14*13*12*5*4*3*2

greedily only put ball next to same color, default to putting ball on the right to simplify
once we put a ball, we can run a check to remove like colors (could be recursively)

to find minimal balls, better to run BFS, number of times switching layer is number of balls

to get to a state, we need a unique number of balls, but we need to track balls used to get to the next level
-> explored set is state of the map
"""
from collections import Counter

class Solution:
    def compress_board(self, board):
        board = list(board)
        for i in range(len(board)):
            j = i + 1
            while j < len(board) and board[j] == board[i]:
                j += 1
            if j <= len(board) and j-i >= 3:
                for k in range(i,j):
                    board[k] = ""

        return "".join(board)

    def recursive_compress(self, board):
        current_board = board
        new_board = self.compress_board(current_board)
        while new_board != current_board:
            current_board = new_board
            new_board = self.compress_board(current_board)

        return new_board

    def findMinStep(self, board: str, hand: str) -> int:
        visited = set()
        result = 0
        q = [(board, hand)]
        # import pudb; pu.db # Debug
        while q:
            next_q = []
            result += 1
            while q:
                current_board, current_hand = q.pop()
                # print(current_board, current_hand)
                for j in range(len(current_hand)):
                    color = current_hand[j]
                    for i in range(len(current_board)):
                        # Removing the greedy approach for a corner edge case
                        if True or current_board[i] == color and (i+1 == len(current_board) or current_board[i+1] != color):
                            next_board = current_board[:i+1] + color + current_board[i+1:]
                            next_board = self.recursive_compress(next_board)

                            if next_board == "":
                                return result
                            if next_board not in visited:
                                visited.add(next_board)
                                next_q.append((next_board, current_hand[:j]+current_hand[j+1:]))

            q = next_q

        return -1

import unittest
class Test(unittest.TestCase):

    def test_1(self):
        cases = [
            ["WRRBBW", "RB", -1],
            ["WWRRBBWW", "WRBRW", 2],
            ["G", "GGGGG", 2],
            ["RBYYBBRRB", "YRBGB", 3],
            ["RRWWRRBBRR", "WB", 2]
        ]
        sol = Solution()
        for board, hand, answer in cases:
            self.assertEqual(sol.findMinStep(board, hand), answer)
    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.compress_board("WRRRBBW"), "WBBW")

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.recursive_compress("BRBYYYBBRRBB"), "")
if __name__ == '__main__':
    unittest.main()



