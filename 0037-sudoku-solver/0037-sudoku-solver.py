class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def solve():
            if not empty:
                return True

            # Find cell with minimum choices
            best = 0
            best_choices = None

            for k in range(len(empty)):
                r, c = empty[k]
                b = (r // 3) * 3 + c // 3

                choices = []
                for num in "123456789":
                    if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                        choices.append(num)

                if best_choices is None or len(choices) < len(best_choices):
                    best = k
                    best_choices = choices

                if len(best_choices) == 1:
                    break

            r, c = empty.pop(best)
            b = (r // 3) * 3 + c // 3

            for num in best_choices:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                if solve():
                    return True

                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)

            empty.insert(best, (r, c))
            return False

        solve()