# modules/follower_tracker.py

import json
import os
from datetime import datetime

DATA_FILE = "data/followers_log.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_entry(count):
    data = load_data()
    date = datetime.now().strftime("%Y-%m-%d")
    data[date] = count
    save_data(data)
    print(f"✅ Follower count saved for {date}.")

def show_progress():
    data = load_data()
    if not data:
        print("❌ No data available. Add at least one entry first.")
        return
    print("\n📊 Follower Growth Summary:\n")
    dates = list(data.keys())
    counts = list(data.values())
    for i in range(len(dates)):
        print(f"{dates[i]} ➜ {counts[i]} followers")
    print("\n🔚 End of log.\n")
