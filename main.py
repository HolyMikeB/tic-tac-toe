from game import Game

game = Game()

playing = True
winner = False
players = input('Would you like to play against the AI or another human? AI/Human ').lower()

while playing:
    game.start_game()
    while not winner:
        if players == 'ai':
            game.player_1_move()
            if game.check_victory():
                winner = True
                break
            else:
                game.comp_move()
            if game.check_victory():
                winner = True
        else:
            game.player_1_move()
            if game.check_victory():
                winner = True
                break
            else:
                game.player_2_move()
            if game.check_victory():
                winner = True
    keep_playing = input('Would you like to play again? y/n ').lower()
    if keep_playing == 'y':
        game.reset_board()
        winner = False
    else:
        print('Thank you for playing.')
        playing = False


