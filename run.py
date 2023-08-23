import random
class BattleShip:
    """
    Battle between player and computer.
    """

    def __init__(self):
        self.Field_Size = ''
        self.Ships_Qt = ''
        #self.Ships_Types = []
        self.Player_Board = []
        self.PC_Board = []
        print("Works")

    def create_board(self):
        for _ in range(self.Field_Size):
            self.Player_Board.append(['O'] * self.Field_Size)

        for _ in range(self.Field_Size):
            self.PC_Board.append(['O'] * self.Field_Size)
    
    def print_player_board(self):
        """Print the game board."""
        print("####### PLAYER BOARD #######")
        for row in self.Player_Board:
            print(" ".join(row))
    
    def print_PC_board(self):
        """Print the game board."""
        print("####### COMPUTER BOARD #######")
        for row in self.PC_Board:
            print(" ".join(row))

    def place_ships(self, board):
        for _ in range(self.Ships_Qt):
            while True:
                x = random.randint(0, len(board) - 1)
                y = random.randint(0, len(board) - 1)

                if board[x][y] == 'O':
                    board[x][y] = 'S'
                    break

    def play_game(self):
        self.Field_Size = int(input("Enter grid size:\n"))
        self.Ships_Qt = int(input("Enter ships quantity:\n"))
        self.create_board()
        #Place player's ships
        self.place_ships(self.Player_Board)
        #Place computer's ships
        self.place_ships(self.PC_Board)



battle = BattleShip()
battle.play_game()
battle.print_player_board()
battle.print_PC_board()