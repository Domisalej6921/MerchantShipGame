from setup_game import *

def get_user_direction():

    global direction

    direction = input('Which way would you like your merchant ship to head?  N/E/S/W:     ').upper()

    # return the direction the user entered:
    return direction #Doesnt return the direction as a usable variable to be imported into the __main__.py

def get_new_player_position(player_position, direction, grid):

    #Grid Size
    grid_size = len(grid)

    #Extracting current player's position
    old_row, old_col = player_position

    # Initialize new player position
    new_row, new_col = old_row, old_col

    # If statements to act depending on the chosen direction
    if direction == "N":
        new_row = (old_row - 1) % grid_size
    elif direction == "E":
        new_col = (old_col + 1) % grid_size
    elif direction == "S":                                  # Needs to be worked on ---- delete comment after
        new_row = (old_row + 1) % grid_size
    elif direction == "W":
        new_col = (old_col - 1) % grid_size
    else:
        print("That is not a valid direction. Please choose again.")
        return None

    global updated_player_position

    updated_player_position = (new_row, new_col)
    return updated_player_position # Will not return the correct newly updated position of the player after they choose which direction they want to travel in

direction = get_user_direction()

new_player_position = get_new_player_position(player_position, direction, grid)

def move_player(grid, old_player_position, new_player_position):

    # Extracting old player position
    old_row, old_col = old_player_position

    # Extracting new player position
    new_row, new_col = new_player_position

    # Removing player from old position
    grid[old_row][old_col] = '.'

    # Placing player in new position
    grid[new_row][new_col] = 'M'

    # Print the updated grid
    print('Player moved:')
    print_grid(grid)

    return grid


def kill_player(grid, old_player_position, new_player_position):
    """
    This function should 'kill' the player; it's actually very similar to
    moving the player: it can be done simply by removing "M" from the old
    position and putting "X" in the new position.

    The function doesn't need to return anything, as the grid can be updated
    "in place", but you can return the grid or anything else you need if
    you like.

    :param grid: The 2D gameboard
    :type grid: list
    :param old_player_position: the player's current position
    :type old_player_position: tuple
    :param new_player_position: the new player position
    :return:
    """

    # your code to kill the player here
