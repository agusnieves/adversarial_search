# -*- coding: utf-8 -*-
import unittest
from context import adversarial_search
utils = adversarial_search.utils

class Test_utils(unittest.TestCase):
    """ Testcases for .utils
    """

    def test_coord(self):
        """ Testing juegos.utils.coord_id(column, row)
        """
        coord_id = utils.coord_id
        COLUMNS = [l for l in utils.__COLUMNS__]
        for i, col in zip(range(len(COLUMNS)), COLUMNS):
            self.assertEqual(col + str(i + 1), coord_id(i, i))

    def test_print_board(self):
        """ Testing print_boardjuegos.utils.print_board(board, rows, cols, row_sep, col_sep, joint_sep, row_fmt)
        """
        print_board = utils.print_board
        self.assertEqual('A\n', print_board('A', 1, 1, '!', '!', '!'))
        self.assertEqual('AB\nCD\n', print_board('ABCD', 2, 2))
        self.assertEqual('A|B\n--\nC|D\n', print_board('ABCD', 2, 2, '-', '|'))
        self.assertEqual('A|B\n-+-\nC|D\n', print_board('ABCD', 2, 2, '-', '|', '+'))
        self.assertEqual('A|B\nC|D\n', print_board('ABCD', 2, 2, '', '|', '+'))
        self.assertEqual('|AB|\n|CD|\n', print_board('ABCD', 2, 2, row_fmt='|%s|\n'))
        self.assertEqual('|AB|\n|--|\n|CD|\n', print_board('ABCD', 2, 2, '-', '', '', row_fmt='|%s|\n'))
        self.assertEqual('AB\nCD\nEF\n', print_board('ABCDEF', 3, 2))
        self.assertEqual('ABC\nDEF\n', print_board('ABCDEF', 2, 3))

    def test_board_orths(self):
        """ Testing orthogonal lines (functions board_rows, board_columns, 
            board_orths).
        """
        board_rows = utils.board_rows
        board_columns = utils.board_columns
        board_orths = utils.board_orths

        def _test_orths(board, row_num, col_num, rows, cols):
            self.assertEqual(rows, board_rows(board, row_num, col_num))
            self.assertEqual(cols, board_columns(board, row_num, col_num))
            self.assertEqual(rows + cols, list(board_orths(board, row_num, col_num)))

        _test_orths('A', 1, 1, ['A'], ['A'])
        _test_orths('ABCD', 2, 2, ['AB', 'CD'], ['AC', 'BD'])
        _test_orths('ABCDEFGHI', 3, 3, ['ABC', 'DEF', 'GHI'], ['ADG', 'BEH', 'CFI'])
        _test_orths('ABCDEF', 3, 2, ['AB', 'CD', 'EF'], ['ACE', 'BDF'])
        _test_orths('ABCDEF', 2, 3, ['ABC', 'DEF'], ['AD', 'BE', 'CF'])
        _test_orths('ABCDEF', 1, 6, ['ABCDEF'], ['A', 'B', 'C', 'D', 'E', 'F'])
        _test_orths('ABCDEF', 6, 1, ['A', 'B', 'C', 'D', 'E', 'F'], ['ABCDEF'])

    def test_board_diags(self):
        """ Testing diagonal lines (functions board_pdiags, board_ndiags, 
            board_diags).
        """
        board_pdiags = utils.board_pdiags
        board_ndiags = utils.board_ndiags
        board_diags = utils.board_diags

        def _test_diags(board, row_num, col_num, pdiags, ndiags):
            self.assertEqual(pdiags, list(board_pdiags(board, row_num, col_num)))
            self.assertEqual(ndiags, list(board_ndiags(board, row_num, col_num)))
            self.assertEqual(pdiags + ndiags, list(board_diags(board, row_num, col_num)))

        _test_diags('A', 1, 1, ['A'], ['A'])
        _test_diags('ABCD', 2, 2, ['A', 'BC', 'D'], ['C', 'AD', 'B'])
        _test_diags('ABCDEFGHI', 3, 3, ['A', 'BD', 'CEG', 'FH', 'I'], ['G', 'DH', 'AEI', 'BF', 'C'])
        _test_diags('ABCDEF', 3, 2, ['A', 'BC', 'DE', 'F'], ['E', 'CF', 'AD', 'B'])
        _test_diags('ABCDEF', 2, 3, ['A', 'BD', 'CE', 'F'], ['D', 'AE', 'BF', 'C'])
        _test_diags('ABCDEF', 6, 1, ['A', 'B', 'C', 'D', 'E', 'F'], ['F', 'E', 'D', 'C', 'B', 'A'])
        _test_diags('ABCDEF', 1, 6, ['A', 'B', 'C', 'D', 'E', 'F'], ['A', 'B', 'C', 'D', 'E', 'F'])


if __name__ == "__main__":
    unittest.main()
