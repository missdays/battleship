import random
class BattleShip:
    """
    Battle between player and computer.
    """

    def __init__(self):
        self.Field_Size = ''
        self.Ships_Qt = ''
        self.Player_Board = []
        self.PC_Board = []
        self.User_Name = ''
        self.User_Score = 0
        self.PC_Score = 0
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

    def get_user_guess(self):
        """Get the user's guess for row and column."""
        while True:
            try:
                x = int(input(f"Guess row (0-{self.Field_Size - 1}): "))
                y = int(input(f"Guess column (0-{self.Field_Size - 1}): "))
                if 0 <= x < self.Field_Size and 0 <= y < self.Field_Size:
                    return x, y
                else:
                    print("Please enter valid coordinates.\n")
            except ValueError:
                print("Please enter valid coordinates.\n")

    def get_pc_guess(self):
        x = random.randint(0, self.Field_Size - 1)
        y = random.randint(0, self.Field_Size - 1)
        return x, y
    
    def user_attacks(self, x, y):
        if self.PC_Board[x][y] == 'S':
            print("Congratulations! You sunk the opponent's ship!\n")
            #must be replaced with board that will be shown to user
            self.PC_Board[x][y] = 'X'
            self.User_Score += 1
        else:
            print("You missed!")

    def pc_attacks(self, x, y):
        if self.Player_Board[x][y] == 'S':
            print("Computer found one of your ships!\n")
            self.Player_Board[x][y] = 'X'
            self.PC_Score += 1
        else:
            print("Computer missed!\n")

    def check_winner(self, board):
        for row in board:
            for element in row:
                if element == "S":
                    return False
        return True

    def print_score(self):
        print("#### SCORE ###\n")
        print(f'{self.User_Name}: {self.User_Score}\n')
        print(f'Computer: {self.PC_Score}\n')

    def play_game(self):
        user_name = input("Enter your name:\n")

        if user_name == "":
            self.User_Name = "Player"
        else:
            self.User_Name = user_name

        self.Field_Size = int(input("Enter grid size:\n"))
        self.Ships_Qt = int(input("Enter ships quantity:\n"))
        self.create_board()

        #Place player's ships
        self.place_ships(self.Player_Board)
        
        #Place computer's ships
        self.place_ships(self.PC_Board)

        #PC = C , PLAYER = P
        player_turn = 'P'
        while True:
            
            if player_turn == 'P':
                self.print_score()
                x, y = self.get_user_guess()
                self.user_attacks(x,y)
                player_turn = 'C'
            else:
                x, y = self.get_pc_guess()
                self.pc_attacks(x,y)
                player_turn = 'P'

            #Check if there's a winner
            if self.check_winner(self.PC_Board):
                print("You Win!")
                self.print_score()
                break
            elif self.check_winner(self.Player_Board):
                print("You lose!")
                self.print_score()
                break


battle = BattleShip()
battle.play_game()
battle.print_player_board()
battle.print_PC_board()