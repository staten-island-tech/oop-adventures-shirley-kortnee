import os

# Define maze layout
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', 'E', '#', '#']
]

# Initial player position (row, col)
player_pos = [1, 1]

# Function to print the maze
def print_maze():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for each update
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if [r, c] == player_pos:
                print('P', end=' ')  # Print the player icon
            else:
                print(maze[r][c], end=' ')  # Print the maze structure
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
            print("Thanks for playing!")
            break
        elif move in ['W', 'A', 'S', 'D']:
            move_player(move)
        else:
            print("Invalid input! Use W, A, S, D to move.")
        
        # Check if player has reached the end
        if player_pos == [8, 8]:  # End position is at (8, 8)
            print("You reached the end of the maze!")
            break

# Run the game
game_loop()
