from sheets_client import get_sheet, get_all_data, authorize_gsheets
from rank import update_ranking 


def add_player_if_not_exists():
    players_sheet = get_sheet("TRanking", "Players")
    players = players_sheet.get_all_records()
    player_name = input("Enter new player name: ").strip()

    for player in players:      # Check if player already exists
        if player["Player Name"] == player_name:
            return  # Player already exists, no need to add

    new_rank = len(players) + 1     # If not found, add to the last rank
    players_sheet.append_row([new_rank, player_name, 0, 0])  # Rank, Name, Wins, Losses
    print(f"Added new player: {player_name} to rankings.")


def add_match_and_update_ranking():           #new_match = ["3", "Eva", "Felix", "Felix", "26.02.25", "6-4"]
    Match_sheet = get_sheet("TRanking", "Matches")
    ID = len(Match_sheet.get_all_values()) + 1 #gets first empty row
    players_sheet = get_sheet("TRanking", "Players")
    players = players_sheet.get_all_records()
    player_names = {player["Player Name"]: i + 2 for i, player in enumerate(players)}   #player_names = {player["Player Name"] for player in players}  # Set for fast lookup

    while True:
        Player1 = input("Challenger (has to have the lower Ranking): ").strip()
        Player2 = input("Challenged (has to have the higher Ranking): ").strip()
        if Player1 in player_names and Player2 in player_names:
            break  # Exit loop if both names exist
        print("\n❌ One or both player names are incorrect. Please try again!\n")

    Winner = input(f"Who won? ({Player1} / {Player2}): ").strip()
    while Winner not in {Player1, Player2}:  
        print("\n❌ Invalid winner name! Please enter exactly as shown.")
        Winner = input(f"Who won? ({Player1} / {Player2}): ").strip()

    Date = input("Date (format: 24.02.2025): ")
    Score = input("Score (format: 6-3 or 3-6)")
    new_match = [ID, Player1, Player2, Winner, Date, Score]
    Match_sheet.append_row(new_match)
    print("Match added successfully!")


    Loser = Player1 if Player2 == Winner else Player2

      # Get row numbers from dictionary
    winner_row = player_names[Winner]
    loser_row = player_names[Loser]

    # Update Wins and Losses **directly**
    winner_wins = int(players[winner_row - 2]["Wins"]) + 1
    loser_losses = int(players[loser_row - 2]["Losses"]) + 1

    players_sheet.update_cell(winner_row, 3, winner_wins)  # Update Wins column
    players_sheet.update_cell(loser_row, 4, loser_losses)  # Update Losses column

    # Call ranking update
    update_ranking(Player1, Player2, Winner)






    







