import os
import random


class Game:
    def __init__(self, grid=None, score=0, step=0):
        if grid:
            self.grid = grid
        else:
            self.grid = [[0 for i in range(4)] for j in range(4)]
        self.score = score
        self.step = step

    def random_field(self):
        lst = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        x, y = random.choice([(i, j) for (i, j) in lst for k in range(10)])
        # Px(2)=0.8, Px(4)=0.2
        num = random.randint(1, 10000)
        p_2 = 80
        if num <= p_2*100:
            self.grid[x][y] = 2
        else:
            self.grid[x][y] = 4

    def print_screen(self):
        # linux: clear, windows: cls
        os.system("cls")
        # "\b" is backspace (BS)
        print("\b", end='')
        print("Score: {score}".format(score=self.score))
        print("-" * 29)
        for row in self.grid:
            print("|{}|".format("|".join([str(col or " ").center(6) for col in row])))
            print("-" * 29)

    @staticmethod
    def up(grid):
        add_score = 0
        res = [[0 for i in range(4)] for j in range(4)]
        col_list = []
        for k in range(4):
            col_k = [grid[0][k], grid[1][k], grid[2][k], grid[3][k]]
            col_list.append(col_k)
        for j in range(4):
            new_col = ([n for n in col_list[j] if n] + [0, 0, 0, 0])[:4]
            if new_col[0] and new_col[1] and new_col[0] == new_col[1]:
                add_score += new_col[0] + new_col[1]
                new_col[0] = new_col[0] + new_col[1]
                new_col[1] = 0
                new_col = ([n for n in new_col if n] + [0, 0, 0, 0])[:4]
            if new_col[1] and new_col[2] and new_col[1] == new_col[2]:
                add_score += new_col[1] + new_col[2]
                new_col[1] = new_col[1] + new_col[2]
                new_col[2] = 0
                new_col = ([n for n in new_col if n] + [0, 0, 0, 0])[:4]
            if new_col[2] and new_col[3] and new_col[2] == new_col[3]:
                add_score += new_col[2] + new_col[3]
                new_col[2] = new_col[2] + new_col[3]
                new_col[3] = 0
                new_col = ([n for n in new_col if n] + [0, 0, 0, 0])[:4]
            for i in range(4):
                res[i][j] = new_col[i]
        return res, add_score

    @staticmethod
    def down(grid):
        add_score = 0
        res = [[0 for i in range(4)] for j in range(4)]
        col_list = []
        for k in range(4):
            col_k = [grid[0][k], grid[1][k], grid[2][k], grid[3][k]]
            col_list.append(col_k)
        for j in range(4):
            new_col = ([0, 0, 0, 0] + [n for n in col_list[j] if n])[-4:]
            if new_col[-1] and new_col[-2] and new_col[-1] == new_col[-2]:
                add_score += new_col[-1] + new_col[-2]
                new_col[-1] = new_col[-1] + new_col[-2]
                new_col[-2] = 0
                new_col = ([0, 0, 0, 0] + [n for n in new_col if n])[-4:]
            if new_col[-2] and new_col[-2] and new_col[-2] == new_col[-3]:
                add_score += new_col[-2] + new_col[-3]
                new_col[-2] = new_col[-2] + new_col[-3]
                new_col[-3] = 0
                new_col = ([0, 0, 0, 0] + [n for n in new_col if n])[-4:]
            if new_col[-3] and new_col[-4] and new_col[-3] == new_col[-4]:
                add_score += new_col[-3] + new_col[-4]
                new_col[-3] = new_col[-3] + new_col[-4]
                new_col[-4] = 0
                new_col = ([0, 0, 0, 0] + [n for n in new_col if n])[-4:]
            for i in range(4):
                res[i][j] = new_col[i]
        return res, add_score

    @staticmethod
    def left(grid):
        add_score = 0
        res = []
        for row in grid:
            new_row = ([n for n in row if n] + [0, 0, 0, 0])[:4]
            if new_row[0] and new_row[1] and new_row[0] == new_row[1]:
                add_score += new_row[0] + new_row[1]
                new_row[0] = new_row[0] + new_row[1]
                new_row[1] = 0
                new_row = ([n for n in new_row if n] + [0, 0, 0, 0])[:4]
            if new_row[1] and new_row[2] and new_row[1] == new_row[2]:
                add_score += new_row[1] + new_row[2]
                new_row[1] = new_row[1] + new_row[2]
                new_row[2] = 0
                new_row = ([n for n in new_row if n] + [0, 0, 0, 0])[:4]
            if new_row[2] and new_row[3] and new_row[2] == new_row[3]:
                add_score += new_row[2] + new_row[3]
                new_row[2] = new_row[2] + new_row[3]
                new_row[3] = 0
                new_row = ([n for n in new_row if n] + [0, 0, 0, 0])[:4]
            res.append(new_row)
        return res, add_score

    @staticmethod
    def right(grid):
        add_score = 0
        res = []
        for row in grid:
            new_row = ([0, 0, 0, 0] + [n for n in row if n])[-4:]
            if new_row[-1] and new_row[-2] and new_row[-1] == new_row[-2]:
                add_score += new_row[-1] + new_row[-2]
                new_row[-1] = new_row[-1] + new_row[-2]
                new_row[-2] = 0
                new_row = ([0, 0, 0, 0] + [n for n in new_row if n])[-4:]
            if new_row[-2] and new_row[-3] and new_row[-2] == new_row[-3]:
                add_score += new_row[-2] + new_row[-3]
                new_row[-2] = new_row[-2] + new_row[-3]
                new_row[-3] = 0
                new_row = ([0, 0, 0, 0] + [n for n in new_row if n])[-4:]
            if new_row[-3] and new_row[-4] and new_row[-3] == new_row[-4]:
                add_score += new_row[-3] + new_row[-4]
                new_row[-3] = new_row[-3] + new_row[-4]
                new_row[-4] = 0
                new_row = ([0, 0, 0, 0] + [n for n in new_row if n])[-4:]
            res.append(new_row)
        return res, add_score

    @staticmethod
    # 0 means "not end"
    def is_end(grid):
        min_value = min(min(grid[0]), min(grid[1]), min(grid[2]), min(grid[3]))
        if min_value == 0:
            return 0
        else:
            possible_add_score = max([Game.up(grid)[1], Game.down(grid)[1], Game.left(grid)[1], Game.right(grid)[1]])
            if possible_add_score > 0:
                return 0
            else:
                max_value = max(max(grid[0]), max(grid[1]), max(grid[2]), max(grid[3]))
                return max_value

    # control is one of op in ["w", "a", "s", "d"]
    def update_grid(self, control):
        operator = {"w": Game.up, "a": Game.left, "s": Game.down, "d": Game.right}
        grid, add_score = operator[control](self.grid)
        if grid != self.grid:
            self.grid = grid
            self.score += add_score
            return True
        else:
            return False

    def game_process(self):
        self.random_field()
        self.random_field()
        while not Game.is_end(self.grid):
            game.print_screen()
            print("input w/a/s/d: (up, left, down, right) or input 1/2: (start another game, quit the game)")
            action = input()
            if action == "1":
                return 1
            elif action == "2":
                return 0
            elif action in ["w", "a", "s", "d"]:
                if self.update_grid(action):
                    self.random_field()
            else:
                pass


if __name__ == '__main__':
    print("-" * 20)
    print("|{}|".format("1: New game".center(18)))
    print("-" * 20)
    print("|{}|".format("2: Quit".center(18)))
    print("-" * 20)
    op = input()
    while op != "1" and op != "2":
        op = input()
    if op == "1":
        t = os.system("cls")
        print("\b", end='')
        game = Game()
        while game.game_process():
            game = Game()
