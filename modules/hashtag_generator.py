# modules/hashtag_generator.py

import json
import os

DATA_PATH = os.path.join("data", "hashtags.json")

def load_hashtags():
    try:
        with open(DATA_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Error: Hashtag data not found.")
        return {}

def suggest_hashtags(topic):
    tags = load_hashtags()
    topic = topic.lower()
    if topic in tags:
        print(f"\n📢 Suggested hashtags for '{topic}':\n")
        for tag in tags[topic]:
            print(f"#{tag}", end='  ')
        print("\n")
    else:
        print(f"\n⚠️ No hashtags found for '{topic}'. Try another topic or update database.\n")
