# 21 game (by Bazinga)

# imports
import random 
import HarmonicWare
import ColorWare as cl

player = input(f'{cl.yellow}Nickname: {cl.reset}')
bot = ''.join(HarmonicWare.Generate('Cvcv Cv Cvc', 1))

player_session = []
bot_session = []

player_score = 0
bot_score = 0

game_won = False

def bot_play():
    global bot_session, bot_score

    t = random.randrange(1, 11)
    bot_session.append(t)
    bot_score += t

def player_play():
    global player_session, player_score

    t = random.randrange(1, 11)
    player_session.append(t)
    player_score += t

def do_checks():
    global player_session, player_score
    global bot_session, bot_score
    global game_won

    if bot_score > player_score:
        print(f'{bot} is {cl.green}winning{cl.reset} by {bot_score-player_score} points! Score: {bot_score} | Plays: {len(bot_session)}')
        print(f'► {player} is {cl.red}losing{cl.reset} by {player_score-bot_score} points! Score: {player_score} | Plays: {len(player_session)}')
    if player_score > bot_score:
        print(f'► {player} is {cl.green}winning{cl.reset} by {player_score-bot_score} points! Score: {player_score} | Plays: {len(player_session)}')
        print(f'{bot} is {cl.red}losing{cl.reset} by {bot_score-player_score} points! Score: {bot_score} | Plays: {len(bot_session)}')
    
    if bot_score == 21:
        print(f'{bot} got {cl.yellow}21{cl.reset} points!')
    if player_score == 21:
        print(f'► {player} got {cl.yellow}21{cl.reset} points!')

    if player_score > 21:
        print('---------------------')
        print(f'{cl.red}YOU LOSE!{cl.reset} {bot} won the game!')
        print('---------------------')
        game_won = True
    if bot_score > 21:
        print('---------------------')
        print(f'► {cl.yellow}YOU WON!{cl.reset} {player} won the game!')
        print('---------------------')
        game_won = True


who_playing = 0 # 0: player | 1: bot

while True:
    if who_playing == 0:
        opt = input(f'---------------------\nPress {cl.green}enter{cl.reset} to roll a new card or {cl.red}S{cl.reset} to stop: ').lower().strip()
        if opt == '':
            print(f'{cl.black}You\'ve chosen to continue playing.{cl.reset}')
            player_play()
            print(f'Rolled {cl.cyan}{player_session[-1]}{cl.reset}!')
        elif opt == 's':
            print(f'{cl.black}You\'ve chosen to stop playing, the bot will roll 1 more time.{cl.reset}')
            bot_play()
            print(f'Bot rolled a {cl.blue}{bot_session[-1]}{cl.reset}')
        
        do_checks()
        if game_won: break
        who_playing = 1
    else:
        print(f'---------------------\n{cl.black}Bot playing...{cl.reset}')
        bot_play()
        print(f'Bot rolled a {cl.blue}{bot_session[-1]}{cl.reset}')
        do_checks()
        if game_won: break
        who_playing = 0
