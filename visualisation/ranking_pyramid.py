import sys
import os
import matplotlib.pyplot as plt
import numpy as np

# Ensure the project root is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.sheets_client import get_sheet  # Import Google Sheets connection


def fetch_players_from_sheets():
    """Fetch player names sorted by rank from Google Sheets."""
    sheet = get_sheet("TRanking", "Players")
    data = sheet.get_all_records()
    players = sorted(data, key=lambda x: x["Rank"])  # Sort players by rank
    return [player["Player Name"] for player in players]  # Extract names


def calculate_pyramid_levels(num_players):
    """Determine the minimum number of levels needed to fit all players."""
    level = 0
    while (level * (level + 1)) // 2 < num_players:  # Sum of triangular numbers
        level += 1
    level += 3
    return level


def plot_ranking_pyramid(players):
    """Plots a dynamically sized ranking pyramid."""
    num_players = len(players)
    levels = calculate_pyramid_levels(num_players)  # Get required levels

    fig, ax = plt.subplots(figsize=(15, 6 + levels * 0.5))  # Adjust height dynamically
    ax.set_xlim(-levels, levels)
    ax.set_ylim(0, levels + 1)
    ax.axis("off")  # Hide axes

    index = 0
    for row in range(levels):
        y = levels - row  
        x_start = -row * 0.75  # Center properly
        for col in range(row + 1):
            if index >= num_players:
                break  # Stop if we placed all players
            
            x = x_start + col * 1.5  # Space out names evenly
            player_name = players[index]

            ax.text(x, y, player_name, fontsize=12, ha="center", va="center",
                    bbox=dict(facecolor="lightblue", edgecolor="black", boxstyle="round,pad=0.4"))

            index += 1

    # **Ensure remaining players (if any) are placed at the bottom**
    remaining_players = num_players - index
    if remaining_players > 0:
        y = 0  # Bottom row
        x_start = -remaining_players / 2  # Center the last row
        for col in range(remaining_players):
            x = x_start + col * 1.5
            player_name = players[index]
            ax.text(x, y, player_name, fontsize=12, ha="center", va="center",
                    bbox=dict(facecolor="lightblue", edgecolor="black", boxstyle="round,pad=0.4"))
            index += 1

    plt.title("Tennis Ranking Pyramid", fontsize=16, fontweight="bold")
    plt.show()


# Fetch data from Google Sheets & plot pyramid
if __name__ == "__main__":
    players = fetch_players_from_sheets()
    print(f"Total Players: {len(players)}")
    sys.stdout.flush()
    # Debugging output
    plot_ranking_pyramid(players)
