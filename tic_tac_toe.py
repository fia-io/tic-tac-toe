#! /usr/bin/python3

import mysql.connector

def database_proof_of_concept():
    db = mysql.connector.connect(host = 'localhost',
                    user = 'mb1a',
                    password = '',
                    db = 'c9')
    if db.is_connected():
        print('We win!')
    else:
        print("We is phucked, yo!")
    cursor = db.cursor()
    query = ("SELECT * FROM hello_world")
    insert = ("INSERT INTO hello_world (name) VALUES ('Thorson')")
    cursor.execute(insert)
    db.commit()
    cursor.execute(query)
    for x in cursor:
        print(x)
    
    db.close()


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
        for i in range(3):
            if (self.GetPosition(i, 0) == 'X' and
                self.GetPosition(i, 1) == 'X' and
                self.GetPosition(i, 2) == 'X'):
                    winx = True
            if (self.GetPosition(0, i) == 'X' and
                self.GetPosition(1, i) == 'X' and
                self.GetPosition(2, i) == 'X'):
                    winx = True
        if self.GetPosition(0, 0) == 'X' and self.GetPosition(1, 1) == 'X' and self.GetPosition(2, 2) == 'X':
            winx = True
        if self.GetPosition(0, 2) == 'X' and self.GetPosition(1, 1) == 'X' and self.GetPosition(2, 0) == 'X':
            winx = True
            
        for i in range(3):
           if (self.GetPosition(i, 0) == 'O' and
                self.GetPosition(i, 1) == 'O' and
                self.GetPosition(i, 2) == 'O'):
                    wino = True
           if (self.GetPosition(0, i) == 'O' and
                self.GetPosition(1, i) == 'O' and
                self.GetPosition(2, i) == 'O'):
                    wino = True
        if self.GetPosition(0, 0) == 'O' and self.GetPosition(1, 1) == 'O' and self.GetPosition(2, 2) == 'O':
            wino = True
        if self.GetPosition(0, 2) == 'O' and self.GetPosition(1, 1) == 'O' and self.GetPosition(2, 0) == 'O':
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
