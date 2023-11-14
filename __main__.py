from setup_game import *
from player_actions import *
import setup_game
import player_actions

if __name__ == "__main__":
    setup_game.create_grid(size)
    setup_game.add_rocks(grid, difficulty)
    setup_game.place_player(grid)
    setup_game.place_enemy(grid)
    setup_game.print_grid(grid)
    player_actions.get_user_direction()
    player_actions.get_new_player_position(player_position, direction, grid)
    player_actions.move_player(grid, old_player_position, new_player_position)
    setup_game.print_grid(grid)
    print("PIRATES!")