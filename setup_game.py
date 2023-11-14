import random

#Size of grid variable
size = int(10)

def create_grid(size):

    #Grid Storage
    grid = [[ '.' for _ in range(size)] for _ in range(size)]
    return grid

#Difculty Variable Creation
difficulty = int(input("What difficulty would you like to play the game at? 1 - 10:     "))

def add_rocks(grid, difficulty):
    #Checks if number is a valid input between 1 and 10
    if 0 < difficulty <= 10:

        # Creates the number of rocks
        rocks_number = 15 - difficulty

        #Creating random position for the rocks to spawn in at
        for i in range(0, rocks_number):
            row_index = random.randint(0, size-1)
            col_index = random.randint(0, size -1)

            grid[row_index][col_index] = "*"

    else:
        print("Please enter a number between 1 - 10.")

    # return the updated grid:
    return grid

player_placed = False

def place_player(grid):

    global player_placed

    if not player_placed:
        for _ in range(size * size):  # Limit the number of attempts to prevent an infinite loop
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)

            if (
                    grid[row][col] != '*' and
                    grid[row][col] != 'M' and
                    (row == 0 or grid[row - 1][col] != '*') and
                    (row == size - 1 or grid[row + 1][col] != '*') and
                    (col == 0 or grid[row][col - 1] != '*') and
                    (col == size - 1 or grid[row][col + 1] != '*')
            ):
                old_player_position = (row, col)  # Save old player position
                grid[row][col] = 'M'
                player_placed = True
                new_player_position = (row, col)  # Store new player position
                return grid, (row, col), old_player_position, new_player_position

        # If no valid position is found after a reasonable number of attempts, handle the error
        raise ValueError("Unable to find a valid position for the merchant ship.")
    else:
        print("Player has already been placed.")
        return grid, -1, -1  # Returning invalid position

    return grid, row, col

#Creates seperate variables used throughout the game
grid, (player_row, player_col), old_player_position, new_player_position = place_player(create_grid(size))

#Creates the player_position variable to use in the player_actions file
player_position = (player_row, player_col)

def place_enemy(grid):

    # Creating random position for the enemy to spawn in at
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)

    while grid[row][col] == '*' or \
            (row > 0 and grid[row - 1][col] == '*') or \
            (row < size - 1 and grid[row + 1][col] == '*') or \
            (col > 0 and grid[row][col - 1] == '*') or \
            (col < size - 1 and grid[row][col + 1] == '*'):
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)

    # Placing the letter "M" at that position
    grid[row][col] = 'P'

    # Player Position
    enemy_position = (row, col)

    # returns two values, the updated grid and the enemy_position:
    return grid, enemy_position

def print_grid(grid):

    if not grid:
        print("The grid is empty")
        return
    
    for row in grid:
        print(" ".join(map(str, row)))
    return grid