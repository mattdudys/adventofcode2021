import fileinput
from dataclasses import dataclass

class BingoBoard:

    def __init__(self, board_id, rows):
        self.board_id = board_id
        self.num_to_position = {}
        for r, row in enumerate(rows):
            for c, num in enumerate(row):
                self.num_to_position[num] = (r, c)
        self.row_marks = [0] * 5
        self.col_marks = [0] * 5
        self.completed = False
        self.completed_move = None
        self.completed_num = None
        self.completed_score = None

    def mark(self, num, move):
        if num in self.num_to_position:
            r, c = self.num_to_position[num]
            self.row_marks[r] += 1
            self.col_marks[c] += 1
            del self.num_to_position[num]
            if not self.completed and self.is_complete():
                self.completed = True
                self.completed_move = move
                self.completed_num = num
                self.completed_score = self.sum_unmarked() * num
                return True
        return False

    def is_complete(self):
        return self.completed or max(self.row_marks) == 5 or max(self.col_marks) == 5

    def sum_unmarked(self):
        return sum(self.num_to_position.keys())

    def __repr__(self):
        return str(self.row_marks) + ' ' + str(self.col_marks)


def read_input():
    board_row = 0
    boards = []
    board_id = 0
    for i, line in enumerate(fileinput.input()):
        line = line.strip()
        if i == 0:
            numbers = [int(num) for num in line.split(',')]
            continue
        print(i, line)
        if line != '':
            board_row = board_row % 5
            if board_row == 0:
                rows = []
            row = [int(num) for num in line.split()]
            rows.append(row)
            if board_row == 4:
                print(rows)
                board = BingoBoard(board_id, rows)
                boards.append(board)
                board_id += 1
            board_row += 1

    return numbers, boards

numbers, boards = read_input()
print(numbers)

for move, num in enumerate(numbers):
    print(move, 'num', num)
    for board in boards:
        if board.mark(num, move):
            print('completed', 'board_id', board.board_id, 'score', board.completed_score)
