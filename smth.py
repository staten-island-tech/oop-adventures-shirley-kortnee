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
    ['#', '#', '#', '#', '#', '#', '#', '#', 'E', '#', '#'],
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
    row, col = player_pos

    if direction == 'W' and row > 0 and maze[row - 1][col] != '#':  
        player_pos[0] -= 1
    elif direction == 'S' and row < len(maze) - 1 and maze[row + 1][col] != '#':
        player_pos[0] += 1
    elif direction == 'A' and col > 0 and maze[row][col - 1] != '#':
        player_pos[1] -= 1
    elif direction == 'D' and col < len(maze[row]) - 1 and maze[row][col + 1] != '#':
        player_pos[1] += 1


def puzzle_one(player):
    print("What has hands but cannot clap?")
    questions = [
        ("A CLOCK", "what is not living, but can die?"),
        ("A BATTERY", "i have keys but no locks. I have space but no room. you can enter but you can't go outside. what am I?"),
        ("A KEYBOARD", "wowie, first puzzle done!"),
    ]

    for answer, next_question in questions:
        user_input = input("Your answer: ").strip().upper()
        while user_input != answer:
            print("Try again, smh.")
            user_input = input("Your answer: ").strip().upper()
        print(next_question)

    player.add_item(key)
    print(f"You now have: {key}")
    player.show_inventory()


def game_loop(player):
    while True:
        print_maze()
        move = input("Use WASD to move (W = up, A = left, S = down, D = right, Q = quit): ").strip().upper()
        if move == 'Q':
            print("You quit the game.")
            break
        elif move in ['W', 'A', 'S', 'D']:
            move_player(move)

            if player_pos == [5, 5]:
                puzzle_one(player)
            elif player_pos == [8, 8]:
                print("Woah, you did it! You escaped the maze!")
                break
        else:
            print("Invalid input. Use WASD to move.")


# Initialize and start the game
player = Player("Adventurer")
game_loop(player)
