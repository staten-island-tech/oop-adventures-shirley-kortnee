import os

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
        move = input("Use WASD to move (W = up, A = left, S = down, D = right, Q = quit): ").upper()
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
        user_input = input("Your answer: ").upper()
        if user_input == answer_one:
            print("what is not living, but can die?")
            answer_two = "a battery".upper()
            user_input = input("Your answer: ").upper()
            if user_input == answer_two:
                print("i have keys but no locks. I have space but no room. You can enter but you can't go outside. What am I?")
                answer_three = "a keyboard".upper()
                user_input = input("Your answer: ").upper()
                if user_input == answer_three:
                    print("wowie, first puzzle done!")
 

# Run the game

game_loop()
puzzle_one()