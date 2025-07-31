import pandas as pd
import os

# Create output directory
output_dir = "outputs/2025_su_tables_full"
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------
# Record Summary
record_data = {
    "Category": ["ALL GAMES", "CONFERENCE", "NON-CONFERENCE"],
    "Overall": ["10-9", "5-4", "5-5"],
    "Home": ["5-4", "3-2", "2-2"],
    "Away": ["4-4", "2-2", "2-2"],
    "Neutral": ["1-1", "0-0", "1-1"]
}
pd.DataFrame(record_data).to_csv(f"{output_dir}/record_summary.csv", index=False)

# -------------------------------------
# Game Schedule
schedule_data = [
    ["Feb 07", "UALBANY", "W 21-9", "2127"],
    ["Feb 15", "at #7 Maryland", "W 15-9", "758"],
    ["Feb 18", "CORNELL", "W 18-10", "2214"],
    ["Feb 22", "at #2 North Carolina", "L 8-16", "1088"],
    ["Feb 25", "#3 NORTHWESTERN", "L 8-12", "2080"],
    ["Mar 01", "#14 CLEMSON", "L 8-9", "2899"],
    ["Mar 07", "#7 STANFORD", "Wo2 14-13", "2165"],
    ["Mar 10", "#10 JOHNS HOPKINS", "L ot 13-14", "2049"],
    ["Mar 15", "at Pitt", "W 17-11", "600"],
    ["Mar 19", "at #17 Loyola", "W 14-12", "432"],
    ["Mar 23", "#20 NOTRE DAME", "W 12-11", "3622"],
    ["Mar 29", "#11 VIRGINIA", "W 13-12", "2736"],
    ["Apr 02", "at #13 Yale Bulldogs", "L 10-13", "653"],
    ["Apr 05", "at California", "W 18-6", "250"],
    ["Apr 12", "at Virginia Tech", "L 11-14", "157"],
    ["Apr 17", "#2 BOSTON COLLEGE", "L 2-17", "1645"],
    ["Apr 22", "vs #13 Stanford", "L 10-15", "0"],
    ["May 09", "vs Brown Bears", "W 15-9", "583"],
    ["May 11", "at #5 Yale Bulldogs", "L 8-9", "608"]
]
pd.DataFrame(schedule_data, columns=["Date", "Opponent", "Score", "Attendance"]).to_csv(f"{output_dir}/game_schedule.csv", index=False)

# -------------------------------------
# Goals by Period
goals_data = {
    "Team": ["Syracuse", "Opponents"],
    "1st": [74, 64],
    "2nd": [65, 52],
    "3rd": [48, 45],
    "4th": [47, 59],
    "OT": [0, 1],
    "OT2": [1, 0],
    "Total": [235, 221]
}
pd.DataFrame(goals_data).set_index("Team").to_csv(f"{output_dir}/goals_by_period.csv")

# -------------------------------------
# Saves by Period
saves_data = {
    "Team": ["Syracuse", "Opponents"],
    "1st": [43, 39],
    "2nd": [42, 48],
    "3rd": [37, 40],
    "4th": [39, 39],
    "OT": [1, 2],
    "OT2": [0, 0],
    "Total": [162, 168]
}
pd.DataFrame(saves_data).set_index("Team").to_csv(f"{output_dir}/saves_by_period.csv")

# -------------------------------------
# Shots by Period
shots_data = {
    "Team": ["Syracuse", "Opponents"],
    "1st": [145, 154],
    "2nd": [147, 143],
    "3rd": [129, 115],
    "4th": [114, 138],
    "OT": [2, 2],
    "OT2": [1, 0],
    "Total": [538, 552]
}
pd.DataFrame(shots_data).set_index("Team").to_csv(f"{output_dir}/shots_by_period.csv")

# -------------------------------------
# Shots on Goal by Period
sog_data = {
    "Team": ["Syracuse", "Opponents"],
    "1st": [113, 107],
    "2nd": [113, 94],
    "3rd": [88, 82],
    "4th": [86, 98],
    "OT": [2, 2],
    "OT2": [1, 0],
    "Total": [403, 383]
}
pd.DataFrame(sog_data).set_index("Team").to_csv(f"{output_dir}/shots_on_goal.csv")

# -------------------------------------
# Team Statistics
team_stats = {
    "Statistic": [
        "SHOTS", "GOALS", "ASSISTS", "FREE POSITION GOALS", "FREE POSITION ATTEMPTS",
        "SHOOTING PERCENTAGE", "SOG", "SOG %", "MAN-UP GOALS", "MAN-UP OPPORTUNITIES",
        "MAN-DOWN GOALS", "MAN-DOWN OPPORTUNITIES", "GROUND BALLS", "TURNOVERS",
        "CAUSED TURNOVERS", "DRAW CONTROLS", "FACE-OFFS WON", "CLEARING ATTEMPTS",
        "CLEARS SUCCESSFUL", "CLEAR %", "YELLOW CARDS", "RED CARDS", "GOALS ALLOWED",
        "GOALS AGAINST AVG"
    ],
    "Syracuse": [
        538, 235, 91, 46, 123, ".437", 403, ".749", 6, 33, 0, 13,
        269, 303, 151, 260, 15, 296, 263, ".889", 22, 0, 221, "11.63"
    ],
    "Opponents": [
        552, 221, 88, 35, 84, ".400", 383, ".694", 3, 12, 2, 25,
        295, 306, 161, 277, 11, 290, 258, ".890", 17, 1, 235, "12.37"
    ]
}
pd.DataFrame(team_stats).to_csv(f"{output_dir}/team_statistics.csv", index=False)

# -------------------------------------
# Player Statistics (Sample Rows)
player_stats = [
    [1, "Meaghan Tyrrell", 19, 50, 35, 85, 109, 78, 28, 2, 2, 6, 3, 0, 0],
    [2, "Emma Ward", 19, 43, 24, 67, 111, 73, 9, 2, 0, 0, 7, 0, 0],
    [3, "Olivia Adamson", 19, 34, 10, 44, 88, 52, 4, 1, 1, 4, 16, 0, 0],
    [4, "Delaney Radin", 19, 19, 4, 23, 39, 30, 2, 0, 0, 3, 1, 0, 0],
    [5, "Kaitlyn Tarpey", 19, 15, 2, 17, 23, 20, 1, 0, 0, 0, 0, 0, 0]
]
columns = [
    "Jersey", "Player", "GP", "G", "A", "Pts", "Sh", "SOG",
    "GB", "TO", "CT", "DC", "YC", "RC", "MAN-UP"
]
pd.DataFrame(player_stats, columns=columns).to_csv(f"{output_dir}/player_statistics.csv", index=False)

print(f"✅ All 8 tables saved to: {output_dir}")
