import unittest
import Minesweeper

class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.game = Minesweeper.minesweeper()

    def test_creatField(self):
        self.game.crratField(2,2)
        self.assertEqual(self.game.row,2)
        self.assertEqual(self.game.col,2)


    def test_layMine(self):
        self.creat_field(4,4)
        self.game.layMine(1,1)
        self.assertEqual(self.game.miner[1][1],'*')

    def test_play(self):
        self.creat_field(4,4)
        self.game.layMine(0,1)
        self.game.layMine(1,0)
        self.game.play(0,0)
        self.assertEqual(self.game.showIndexs,[[0,0]])


    def test_status_Playing(self):
        self.creat_field_lay_mins(1, 1)
        self.creat_field_lay_mins(0, 0)
        self.game.play(1,1)
        self.assertEqual(self.game.stat.name,Minesweeper.GameStatus.PLAYING.name)

    def test_status_lost(self):
        self.creat_field_lay_mins(1,1)
        self.game.play(1,1)
        self.assertEqual(self.game.stat.name,Minesweeper.GameStatus.LOST.name)

    def test_status_win(self):
        self.creat_field_lay_mins(0,0)
        self.game.play(0,2)
        self.assertEqual(self.game.stat.name,Minesweeper.GameStatus.WIN.name)

    def creat_field(self,row,col):
        self.game.crratField(row,col)

    def creat_field_lay_mins(self,row,col):
        self.creat_field(4, 4)
        self.game.layMine(row,col)


if __name__ == '__main__':
    unittest.main()