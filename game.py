import random

class Game:

    def __init__(self):
        self.TL = ' '
        self.TM = ' '
        self.TR = ' '
        self.ML = ' '
        self.M = ' '
        self.MR = ' '
        self.BL = ' '
        self.BM = ' '
        self.BR = ' '
        self.open_spaces = ['TL', 'TM', 'TR', 'ML', 'M', 'MR', 'BL', 'BM', 'BR']


    def show_board(self):
        print(f' {self.TL} | {self.TM} | {self.TR} \n-----------\n {self.ML} | {self.M} | {self.MR} \n-----------\n '
              f'{self.BL} | {self.BM} | {self.BR}')

    def start_game(self):
        print('Welcome to Tic Tac Toe. When asked, please respond with which space you wish to play with a 1 or 2 '
              'letter abbreviation. For example, if you want to play the top left square, say "TL". Player 1 will be X'
              ' and they will start.')
        self.show_board()

    def player_1_move(self):
        choice = input('Player one, please make your move. ').upper()
        if choice not in self.open_spaces:
            print("Sorry, either that space has been taken, or you provided an invalid option. Please try again.")
            self.player_1_move()
        else:
            if choice == 'TL':
                self.TL = 'x'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'TM':
                self.TM = 'x'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'TR':
                self.TR = 'x'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'ML':
                self.ML = 'x'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'M':
                self.M = 'x'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'MR':
                self.MR = 'x'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'BL':
                self.BL = 'x'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'BM':
                self.BM = 'x'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'BR':
                self.BR = 'x'
                self.open_spaces.remove(choice)
                self.show_board()

    def player_2_move(self):
        choice = input('Player two, please make your move. ').upper()
        if choice not in self.open_spaces:
            print("Sorry, either that space has been taken, or you provided an invalid option. Please try again.")
            self.player_2_move()
        else:
            if choice == 'TL':
                self.TL = 'o'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'TM':
                self.TM = 'o'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'TR':
                self.TR = 'o'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'ML':
                self.ML = 'o'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'M':
                self.M = 'o'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'MR':
                self.MR = 'o'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'BL':
                self.BL = 'o'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'BM':
                self.BM = 'o'
                self.open_spaces.remove(choice)
                self.show_board()
            elif choice == 'BR':
                self.BR = 'o'
                self.open_spaces.remove(choice)
                self.show_board()

    def comp_move(self):
        choice = random.choice(self.open_spaces)
        print(f"The computer's move is {choice}.")
        if choice == 'TL':
            self.TL = 'o'
            self.open_spaces.remove(choice)
            self.show_board()
        elif choice == 'TM':
            self.TM = 'o'
            self.open_spaces.remove(choice)
            self.show_board()
        elif choice == 'TR':
            self.TR = 'o'
            self.open_spaces.remove(choice)
            self.show_board()
        elif choice == 'ML':
            self.ML = 'o'
            self.open_spaces.remove(choice)
            self.show_board()
        elif choice == 'M':
            self.M = 'o'
            self.open_spaces.remove(choice)
            self.show_board()
        elif choice == 'MR':
            self.MR = 'o'
            self.open_spaces.remove(choice)
            self.show_board()
        elif choice == 'BL':
            self.BL = 'o'
            self.open_spaces.remove(choice)
            self.show_board()
        elif choice == 'BM':
            self.BM = 'o'
            self.open_spaces.remove(choice)
            self.show_board()
        elif choice == 'BR':
            self.BR = 'o'
            self.open_spaces.remove(choice)
            self.show_board()

    def check_victory(self):
        if self.TL == self.TR == self.TM == 'x' or self.ML == self.M == self.MR == 'x'\
                or self.BL == self.BM == self.BR == 'x' or self.TL == self.ML == self.BL == 'x'\
                or self.TL == self.M == self.BR == 'x' or self.TM == self.M == self.BM == 'x'\
                or self.TR == self.MR == self.BR == 'x' or self.TR == self.M == self.BL == 'x':
            print('Player 1 wins!')
            return True
        elif self.TL == self.TR == self.TM == 'o' or self.ML == self.M == self.MR == 'o'\
                or self.BL == self.BM == self.BR == 'o' or self.TL == self.ML == self.BL == 'o'\
                or self.TL == self.M == self.BR == 'o' or self.TM == self.M == self.BM == 'o'\
                or self.TR == self.MR == self.BR == 'o' or self.TR == self.M == self.BL == 'o':
            print('Player 2 wins!')
            return True
        elif not self.open_spaces:
            print('Tie!')
            return True
        else:
            return False

    def reset_board(self):
        self.TL = ' '
        self.TM = ' '
        self.TR = ' '
        self.ML = ' '
        self.M = ' '
        self.MR = ' '
        self.BL = ' '
        self.BM = ' '
        self.BR = ' '
        self.open_spaces = ['TL', 'TM', 'TR', 'ML', 'M', 'MR', 'BL', 'BM', 'BR']



