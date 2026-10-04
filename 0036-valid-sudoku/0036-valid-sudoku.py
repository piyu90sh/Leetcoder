class Solution(object):
    def isValidSudoku(self, board):
        # Check rows
        for row in board:
            nums = []
            for x in row:
                if x != ".":
                    if x in nums:
                        return False
                    nums.append(x)

        # Check columns
        for col in range(9):
            nums = []
            for row in range(9):
                x = board[row][col]
                if x != ".":
                    if x in nums:
                        return False
                    nums.append(x)

        # Check 3x3 boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = []
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        x = board[i][j]
                        if x != ".":
                            if x in nums:
                                return False
                            nums.append(x)

        return True