"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar,
 and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles,
 however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column,
 and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting
 puzzle grid and its solution grid.

 A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
 although it may be necessary to employ "guess and test" methods in order to eliminate
 options (there is much contested opinion over this). The complexity of the search
 determines the difficulty of the puzzle; the example above is considered easy because
 it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'),
contains fifty different Su Doku puzzles ranging in difficulty, but all with
unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found
in the top left corner of each solution grid; for example, 483 is the 3-digit
number found in the top left corner of the solution grid above.
"""
counter = 0
sudoku = list()
sudokuList = list()

with open("0096_sudoku.txt", "r", encoding="utf-8") as file:
    for row in file:
        if row.startswith("Grid"):
            continue

        if row.endswith("\n"):
            row = row[:-1]

        rowList = list(row)
        for i in range(len(rowList)):
            rowList[i] = int(rowList[i])

        counter += 1
        sudoku.append(rowList)
        if counter == 9:
            sudokuList.append(sudoku)
            counter = 0
            sudoku = list()


class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def isErrorRow(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    continue
                for k in range(j + 1, 9):
                    if self.sudoku[i][j] == self.sudoku[i][k]:
                        return True
        return False

    def isErrorColumn(self):
        for j in range(9):
            for i in range(9):
                if self.sudoku[i][j] == 0:
                    continue

                for k in range(i + 1, 9):
                    if self.sudoku[i][j] == self.sudoku[k][j]:
                        return True
        return False

    def isErrorBox(self):
        box = list()
        for a in range(3):
            for b in range(3):
                for i in range(0 + a * 3, 3 + a * 3):
                    for j in range(0 + b * 3, 3 + b * 3):
                        box.append(self.sudoku[i][j])

                for i in range(9):
                    if box[i] == 0:
                        continue

                    for k in range(i+1, 9):
                        if box[i] == box[k]:
                            return True
                box.clear()
        return False

    def isError(self):
        return self.isErrorRow() or self.isErrorColumn() or self.isErrorBox()

    def isSolved(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    return False
        return True

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    for x in range(1, 10):
                        self.sudoku[i][j] = x
                        if self.isError():
                            self.sudoku[i][j] = 0
                            continue

                        if self.isSolved():
                            return True

                        if self.solve():
                            return True
                    self.sudoku[i][j] = 0
                    return False

    def firstThreeNumber(self):
        return self.sudoku[0][0] * 100 + self.sudoku[0][1] * 10 + self.sudoku[0][2]

    def printSudoku(self):
        for i in range(9):
            print(self.sudoku[i])
"""
sudoku = Sudoku(sudokuList[9])
sudoku.printSudoku()
print("-------------")
sudoku.solve()
sudoku.printSudoku()
"""

total = 0
for i in range(50):
    sudoku = Sudoku(sudokuList[i])
    sudoku.solve()
    total += sudoku.firstThreeNumber()

print(total)






















