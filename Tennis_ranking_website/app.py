import sys
import os
import matplotlib.pyplot as plt
import numpy as np

# Ensure the project root is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.sheets_client import get_sheet  # Import Google Sheets connection

from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

# Ensure static folder exists
STATIC_FOLDER = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(STATIC_FOLDER, exist_ok=True)

def fetch_players_from_sheets():
    """Fetch player rankings from Google Sheets."""
    sheet = get_sheet("TRanking", "Players")  
    data = sheet.get_all_records()    
    players = sorted(data, key=lambda x: x["Rank"])  
    return [player["Player Name"] for player in players]

def plot_ranking_pyramid(players):
    """Generate a ranking pyramid image and save it."""
    num_players = len(players)
    levels = int((np.sqrt(8 * num_players + 1) - 1) / 2)  

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(-levels * 1.2, levels * 1.2)
    ax.set_ylim(0, levels + 1)
    ax.axis("off")

    index = 0
    for row in range(levels):
        y = levels - row  
        x_start = -row / 2  
        for col in range(row + 1):
            if index >= num_players:
                break
            x = x_start + col * 1.4
            player_name = players[index]

            ax.text(x, y, player_name, fontsize=12, ha="center", va="center",
                    bbox=dict(facecolor="lightblue", edgecolor="black", boxstyle="round,pad=0.4"))
            index += 1

    plt.title("Tennis Ranking Pyramid", fontsize=16, fontweight="bold")

    # Save image in the static folder
    pyramid_path = os.path.join(STATIC_FOLDER, "ranking_pyramid.png")
    plt.savefig(pyramid_path)
    plt.close()

@app.route("/")
def home():
    players = fetch_players_from_sheets()
    plot_ranking_pyramid(players)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
