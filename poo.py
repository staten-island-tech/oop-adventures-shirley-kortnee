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

# Function to move player
def move_player(direction):
    global player_pos
    row, col = player_pos

    if direction == 'W':  # Move Up
        if row > 0 and maze[row - 1][col] != '#':
            player_pos[0] -= 1
    elif direction == 'S':  # Move Down
        if row < len(maze) - 1 and maze[row + 1][col] != '#':
            player_pos[0] += 1
    elif direction == 'A':  # Move Left
        if col > 0 and maze[row][col - 1] != '#':
            player_pos[1] -= 1
    elif direction == 'D':  # Move Right
        if col < len(maze[row]) - 1 and maze[row][col + 1] != '#':
            player_pos[1] += 1

# Main game loop
def game_loop():
    while True:
        print_maze()  # Print the current state of the maze
        move = input("Use WASD to move (W = up, A = left, S = down, D = right, Q = quit): ").upper()

        if move == 'Q':
            print("wow so u hate me")
            break
        elif move in ['W', 'A', 'S', 'D']:
            move_player(move)
        else:
            input("wtf thats not wasd r u slow. do it again ")

        # Check if player has reached the end
        if player_pos == [8, 8]:  # End position is at (8, 8)
            print("woah u did it")
            break

        if player_pos == [6, 4]:
            print("what has hands but cannot clap?")
            answer_one = "a clock".upper()
        if user_input = answer_one:
            print("what has life, but can die?")
            answer_two = "a battery".upper()
        if user_input = answer_two:
            print("i have keys but no locks. i have space but no room. you can enter but you can't go outside. what am i?")
            answer_three = "a keyboard".upper()
        if user_input = answer_three:
            print(wowie first puzzle done!)





# Run the game
game_loop()