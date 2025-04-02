from sheets_client import get_sheet

def update_ranking(challenger_name, challenged_name, winner_name):      #Updates the ranking based on match results

    player_sheet = get_sheet("TRanking", "Players")
    players = player_sheet.get_all_records()    
    rankings = {player["Player Name"]: player["Rank"] for player in players}    # Convert player data to a dictionary: {player_name: rank}
    challenger_rank = rankings[challenger_name]
    challenged_rank = rankings[challenged_name]



    if winner_name == challenger_name and challenger_rank > challenged_rank:    # Only update if the challenger wins and is ranked lower (higher number)
        print(f"{challenger_name} won! Updating rankings...")

        for player in players:          # Move challenger up to the challenged's position
            if challenged_rank <= player["Rank"] < challenger_rank:
                player["Rank"] += 1     # Push players down

        for player in players:          # Update challenger’s rank
            if player["Player Name"] == challenger_name:
                player["Rank"] = challenged_rank

        players.sort(key=lambda x: x["Rank"])   # Sort players by updated rank

        for i, player in enumerate(players):
            row_data = [player["Rank"], player["Player Name"], player["Wins"], player["Losses"]]  
            player_sheet.update(f"A{i+2}:D{i+2}", [row_data])  # Update the whole row


        print("Ranking updated successfully!")
    else:
        print("No ranking changes.")





