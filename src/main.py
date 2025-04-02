import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from update_matches import add_match_and_update_ranking, add_player_if_not_exists
from visualisation.ranking_pyramid import fetch_players_from_sheets, plot_ranking_pyramid

def menu():
    while True:
        try:
            my_decision = int(input("New Player: Press 1, New Match: Press 2, To create pyramid: Press 3, Exit: Press 4: "))

            if my_decision == 1:
                add_player_if_not_exists()

            elif my_decision == 2:
                add_match_and_update_ranking()

            elif my_decision == 3:
                plot_ranking_pyramid(fetch_players_from_sheets())

            elif my_decision == 4:
                print("Exiting program.")
                break

            else:
                print("Invalid input, please enter 1, 2, 3 or 4.")

        except ValueError:
            print("Invalid input, please enter a number.")


if __name__ == "__main__":
    menu()
