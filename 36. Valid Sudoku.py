'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = sum(([(c, i), (j, c), (i//3, j//3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'), [])
        return seen

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        d = {}
        known = {}
        for i,row in enumerate(board):
            for j,c in enumerate(row):
                if c != '.':
                    known[i,j] = c
        unknown = {}
        for i in list(range(9)):
            for j in list(range(9)):
                if (i,j) not in known:
                    unknown[i,j] = set('123456789')



        column = {}
        box = {}
        row = {}
        for i in list(range(9)):
            column[i] = set()
            row[i] = set()
        for i in list(range(3)):
            for j in list(range(3)):
                box[i,j] = set()

        for i,j in known:
            column[j].add(known[i,j])
            row[i].add(known[i,j])
            box[i//3,j//3].add(known[i,j])

        while len(unknown) > 40:
            self.loopunknown(unknown,known,column,box,row)
        return known

    def addknown(self,i,j,known,column,box,row):
        column[j].add(known[i,j])
        box[i//3,j//3].add(known[i,j])
        row[i].add(known[i,j])

    def loopunknown(self,unknown,known,column,box,row):
        for i,j in list(unknown.keys()):
            check = row[i].union(column[j],box[i//3,j//3])
            unknown[i,j] -= check
            if len(unknown[i,j]) == 1:
                temp = unknown.pop((i,j))
                known[i,j] = temp.pop()
                self.addknown(i,j,known,column,box,row)
        return unknown



board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

a=Solution()
b=a.solveSudoku(board)
print(b)
print(len(b))