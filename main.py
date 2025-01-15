import os

class Item:
    def __init__(self, name, description, quantity=1):
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (x{self.quantity}): {self.description}"

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def add_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory.append
        else:        
            if item.name in self.inventory:
                self.inventory[item.name].quantity += quantity

    def show_inventory(self):
        if not self.inventory:
            print(f"{self.name}'s inventory is empty.")
        else:
            print(f"{self.name}'s inventory:")
            for item in self.inventory.values():
                print(f" - {item}")

key = Item("key", "i can open stuff woah", 1)


#maze thing
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', '1', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', 'E', '#', '#']
]


player_pos = [1, 1]


# maze
def print_maze():
    os.system('cls' if os.name == 'nt' else 'clear')  
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if [r, c] == player_pos:
                print('P', end=' ')  
            else:
                print(maze[r][c], end=' ')
        print()
#moviing stuff
def move_player(direction):
    global player_pos
    row, col = player_pos


    if direction == 'W':  
        if row > 0 and maze[row - 1][col] != '#':
            player_pos[0] -= 1
    elif direction == 'S':
        if row < len(maze) - 1 and maze[row + 1][col] != '#':
            player_pos[0] += 1
    elif direction == 'A':
        if col > 0 and maze[row][col - 1] != '#':
            player_pos[1] -= 1
    elif direction == 'D':  
        if col < len(maze[row]) - 1 and maze[row][col + 1] != '#':
            player_pos[1] += 1

def game_loop():
    while True:
        print_maze()
        move = input("use WASD to move (w = up, a = left, s = down, d = right, q = quit): ").upper()
        if move == 'Q':
            print("wow so u hate me")
            print(player_pos)
            break
        elif player_pos == [5, 5]:
            print(player_pos)
            break
        elif move in ['W', 'A', 'S', 'D']:
            move_player(move)
            print(player_pos)

        elif player_pos == [8, 8]:  
            print("woah u did it")
            print(player_pos)
            break
        else:
            input("wtf thats not wasd r u slow. do it again ")
            print(player_pos)


def puzzle_one():
    if player_pos == [5, 5]:
        print("what has hands but cannot clap?")
        answer_one = "a clock".upper()
        user_input = input("your answer: ").upper()
        if user_input == answer_one:
            print("what is not living, but can die?")
            if user_input != answer_one:
                print("try again smh")
                answer_two = "a battery".upper()
                user_input = input("your answer: ").upper()
                if user_input == answer_two:
                    print("i have keys but no locks. i have space but no room. you can enter but you can't go outside. what am i?")
                    if user_input != answer_two:
                        print("try again smh")
                        answer_three = "a keyboard".upper()
                        user_input = input("your answer: ").upper()
                        if user_input == answer_three:
                            print("wowie, first puzzle done!")
                            player.add_item(key)
                            print(f"you now got a: {key}")
                            player.show_inventory()
                            if user_input != answer_three:
                                print("try again smh)")

game_loop()
puzzle_one()
