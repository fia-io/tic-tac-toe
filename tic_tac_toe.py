#! /usr/bin/python3

def main():
    print("Main called.")

class TicTacToe:
    def __init__(self):
        self.size = 3
        self.state = [' '] * (self.size * self.size)

    def GetPosition(self, row, col):
        return self.state[row * self.size + col]

    def SetPosition(self, value, row, col):
        self.state[row * self.size + col] = value

    def Winner(self):
        winx = False 
        wino = False
        if ((self.state[0]== 'X' and self.state[1]== 'X' and self.state[2]== 'X') or
           (self.state[3]== 'X' and self.state[4]== 'X' and self.state[5]== 'X') or
           (self.state[6]== 'X' and self.state[7]== 'X' and self.state[8]== 'X') or
           (self.state[0]== 'X' and self.state[3]== 'X' and self.state[6]== 'X') or
           (self.state[1]== 'X' and self.state[4]== 'X' and self.state[7]== 'X') or
           (self.state[2]== 'X' and self.state[5]== 'X' and self.state[8]== 'X') or
           (self.state[0]== 'X' and self.state[4]== 'X' and self.state[8]== 'X') or
           (self.state[2]== 'X' and self.state[4]== 'X' and self.state[6]== 'X')):
           winx = True
        if ((self.state[0]== 'O' and self.state[1]== 'O' and self.state[2]== 'O') or
           (self.state[3]== 'O' and self.state[4]== 'O' and self.state[5]== 'O') or
           (self.state[6]== 'O' and self.state[7]== 'O' and self.state[8]== 'O') or
           (self.state[0]== 'O' and self.state[3]== 'O' and self.state[6]== 'O') or
           (self.state[1]== 'O' and self.state[4]== 'O' and self.state[7]== 'O') or
           (self.state[2]== 'O' and self.state[5]== 'O' and self.state[8]== 'O') or
           (self.state[0]== 'O' and self.state[4]== 'O' and self.state[8]== 'O') or
           (self.state[2]== 'O' and self.state[4]== 'O' and self.state[6]== 'O')):
           wino = True
        if (winx and wino) or  (not winx and not wino):
            return None
        elif winx:
            return 'X'
        else: 
            return 'O'

    def GameOver(self):
        if self.Winner():
            return True
        for v in self.state:
            if v == ' ':
                return False
        return True

    def RenderBoard(self):
        board = (
            "   |   |   \n"
            " {0} | {1} | {2} \n"
            "   |   |   \n"
            "---+---+---\n"
            "   |   |   \n"
            " {3} | {4} | {5} \n"
            "   |   |   \n"
            "---+---+---\n"
            "   |   |   \n"
            " {6} | {7} | {8} \n"
            "   |   |   \n".format(*self.state))
        return board
 
if __name__ == '__main__':
    main()
