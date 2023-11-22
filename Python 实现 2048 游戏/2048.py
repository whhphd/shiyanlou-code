import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_code = [ord(ch) for ch in "WASDRQwasdrq"]

actions_dict = dict(zip(letter_code, actions * 2))

action = ''

def main(stdscr):
    def init():
        # 初始化棋盘
        return 'Game'


    def not_game(state):
        #展示游戏结束界面，判断action
        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        #画棋盘，获取action
        if action == 'Restart':
            return "Init"
        if action == 'Exit':
            return "Exit"
        #if 成功移动了一步：
            if 游戏胜利了:
                return "Win"
            if 游戏失败了:
                return 'Gameover'
        return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
    }

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

def get_user_action(keyboard):
    char = ''
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

class GameField(object):
    def __int__(self,height=4,width=4,win=2048):
        self.height = height
        self.width = width
        self.win_value=2048
        self.score = 0
        self.highscore = 0
        self.restart()

    def restart(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    def spawn(self):
        new_element = 4 if randrange(100)>89 else 2

        (i,j) = choice([(i,j) for i in range(self.height) for j in range(self.width) if self.field[i][j] == 0])

        self.field[i][j] = new_element