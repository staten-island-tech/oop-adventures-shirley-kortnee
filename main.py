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
            self.inventory[item.name].quantity += quantity
        else:
            self.inventory[item.name] = item

    def show_inventory(self):
        if not self.inventory:
            print(f"{self.name}'s inventory is empty.")
        else:
            print(f"{self.name}'s inventory:")
            for item in self.inventory.values():
                print(f" - {item}")

key = Item("key", "i can open stuff woah", 1)

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

def print_maze():
    os.system('cls' if os.name == 'nt' else 'clear')
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if [r, c] == player_pos:
                print('P', end=' ')
            else:
                print(maze[r][c], end=' ')
        print()

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

def check_key():
    if "key" in player.inventory and player.inventory["key"].quantity > 0:
        print("did u get the key from the obvious 1 yet")
        use_key = input("ya wanna use the key? (dont be stupid pls)")
        if use_key == "yes".upper():
            player.inventory["key"].quantity -= 1
            if player.inventory["key"].quantity == 0:
                del player.inventory["key"]
                print("u finished kortnees super bad maze woah do i get 100")
        if use_key == "no".upper():
            print("ur so stupid oml")
        if "key" in player.inventory and player.inventory["key"].quantity < 0:
            print("u dont gotta key u should go to 1")

puzzle_one_solved = False

def game_loop():
    global puzzle_one_solved
    while True:
        print_maze()
        move = input("use WASD to move (w = up, a = left, s = down, d = right, q = quit): ").upper()
        if move == 'Q':
            print(player_pos)
            print("wow so u hate me")
            break
        elif player_pos == [5, 5]:
            print(player_pos)
            if not puzzle_one_solved:
                puzzle_one()
        elif print("u did this alr did u forget"):
            input("press enter to continue")
            continue
        elif move in ['W', 'A', 'S', 'D']:
            print(player_pos)
            move_player(move)
        elif player_pos == [8, 8]:
            print(player_pos)
            print("woah u did it")
            check_key()
            break
    else:
        print(player_pos)
        input("wtf thats not wasd r u slow. do it again ")

player = Player("kortnee")

def puzzle_one():
    global puzzle_one_solved
    answer_one = "a clock".upper()
    answer_two = "a battery".upper()
    answer_three = "a keyboard".upper()
    if player_pos == [5, 5]:
        print("what has hands but cannot clap?")
        user_input = input("your answer: ").upper()
        while user_input != answer_one:
            print("try again smh")
            user_input = input("your answer: ").upper()

        print("what is not living, but can die?")
        user_input = input("your answer: ").upper()
        while user_input != answer_two:
            print("try again smh")
            user_input = input("your answer: ").upper()

        print("i have keys but no locks. i have space but no room. you can enter but you can't go outside. what am i?")
        user_input = input("your answer: ").upper()
        while user_input != answer_three:
            print("try again smh")
            user_input = input("your answer: ").upper()

        print("wowie, first puzzle done!")
        player.add_item(key)
        print(f"you now got a: {key}")
        player.show_inventory()
        input("press enter to go back to where u came from") 
        os.system('cls' if os.name == 'nt' else 'clear')

game_loop()
