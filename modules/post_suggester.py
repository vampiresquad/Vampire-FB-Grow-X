# modules/post_suggester.py

POST_IDEAS = {
    "hacking": [
        "Did you know you can trace IPs using open source tools? 🔍",
        "Top 5 Linux tools every ethical hacker should know 💻",
        "Always remember: With great power comes great responsibility ⚡"
    ],
    "motivation": [
        "Winners never quit. Quitters never win! 💯",
        "Discipline is the bridge between goals and success 🔥",
        "Stay focused. Stay fearless. Your time is coming. 🚀"
    ],
    "coding": [
        "Learning Python? Here's your daily tip: use list comprehensions 🧠",
        "Debugging is twice as hard as writing the code in the first place 😅",
        "Code, sleep, repeat. The life of a developer 👨‍💻"
    ],
    "tech": [
        "AI isn't the future, it's the present 🤖",
        "5G vs WiFi 6: What's better for IoT?",
        "Quantum computing will break the internet 🔐 (or save it?)"
    ]
}

CTA_IDEAS = [
    "💬 Drop your thoughts below!",
    "📢 Tag a friend who should see this!",
    "✅ Follow me for more insights!",
    "❤️ Like & Share to help others learn too!",
    "🔁 Repost if you agree!"
]

def suggest_post(topic):
    topic = topic.lower()
    print("\n🧠 Viral Post Ideas:\n")
    if topic in POST_IDEAS:
        for idea in POST_IDEAS[topic]:
            print(f"• {idea}")
    else:
        print("⚠️ No ideas available for this topic yet.")

    print("\n📣 Suggested Call-To-Actions (CTA):")
    for cta in CTA_IDEAS:
        print(f"• {cta}")
    print()
