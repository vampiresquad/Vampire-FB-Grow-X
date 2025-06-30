# modules/group_finder.py

GROUP_SUGGESTIONS = {
    "hacking": [
        "Ethical Hacking Community",
        "Cyber Security Bangladesh",
        "Bug Bounty Hunters [Global]",
        "Termux & Linux Hackers Hub"
    ],
    "tech": [
        "Tech News & Updates",
        "AI | Robotics | IoT",
        "Technology Talk Bangladesh"
    ],
    "coding": [
        "Python Programmers",
        "Learn Coding With Fun",
        "Bangladesh Developer Community"
    ],
    "gaming": [
        "Mobile Legends Bangla",
        "Gamers of Bangladesh",
        "PC/Console Gaming Zone"
    ]
}

TIPS = [
    "📢 Join groups with >50K members.",
    "💬 Be active: comment, react, post.",
    "🧠 Share tips to gain followers.",
    "🔗 Always link back to your profile smartly."
]

def find_groups(topic):
    topic = topic.lower()
    print("\n🧩 Suggested Groups:\n")
    if topic in GROUP_SUGGESTIONS:
        for group in GROUP_SUGGESTIONS[topic]:
            print(f"• {group}")
    else:
        print("⚠️ No group suggestions found for this topic.")
    
    print("\n🧠 Group Growth Tips:")
    for tip in TIPS:
        print(tip)
    print()
