#!/usr/bin/env python3

import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Import all modules
from modules import (
    profile_optimizer,
    hashtag_generator,
    post_suggester,
    group_finder,
    follower_tracker
)

# ----------------------
# Display Banner
# ----------------------
def banner(user, lang):
    os.system('clear')
    print(Fore.RED + Style.BRIGHT + """
██╗   ██╗ █████╗ ███╗   ███╗██████╗ ██╗██████╗ ███████╗
██║   ██║██╔══██╗████╗ ████║██╔══██╗██║██╔══██╗██╔════╝
██║   ██║███████║██╔████╔██║██████╔╝██║██████╔╝█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║██╔═══╝ ██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║██║     ██║██║     ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝
""" + Fore.CYAN + f"\n🧛‍♂️ Welcome {user} | Vampire-FB-Grow-X")
    print(Fore.YELLOW + "🌍 Language: " + ("বাংলা" if lang == "bn" else "English") + "\n")

# ----------------------
# First-Time Setup
# ----------------------
def setup():
    os.system('clear')
    print(Fore.MAGENTA + "🔧 First-time Setup for Vampire-FB-Grow-X\n")
    name = input("🧑 Enter your name: ")
    print("\n🌐 Choose language:")
    print("1. English\n2. বাংলা")
    lang = input("🔢 Option (1/2): ")
    return name.strip(), "bn" if lang.strip() == "2" else "en"

# ----------------------
# Main Menu
# ----------------------
def main_menu(user, lang):
    banner(user, lang)
    if lang == "bn":
        print(Fore.GREEN + """
[1] প্রোফাইল অপ্টিমাইজার
[2] ভাইরাল পোস্ট সাজেশন
[3] হ্যাশট্যাগ জেনারেটর
[4] গ্রুপ খোঁজা
[5] ফলোয়ার ট্র্যাকার
[0] টুল বন্ধ করুন
""")
    else:
        print(Fore.GREEN + """
[1] Profile Optimizer
[2] Viral Post Suggester
[3] Hashtag Generator
[4] Group Finder
[5] Follower Tracker
[0] Exit Tool
""")

    choice = input(Fore.CYAN + "📲 Enter your choice: ")
    return choice.strip()

# ----------------------
# Main Program Loop
# ----------------------
if __name__ == "__main__":
    try:
        user, lang = setup()
        while True:
            opt = main_menu(user, lang)
            if opt == "0":
                print(Fore.RED + "👋 Goodbye, stay ethical!")
                break

            elif opt == "1":
                dummy_data = {
                    "name": user,
                    "bio": "Learning ethical hacking and growing my profile!",
                    "url": "https://facebook.com/vampire.shourov",
                    "profile_pic": True,
                    "cover_photo": False
                }
                profile_optimizer.optimize_profile(dummy_data)

            elif opt == "2":
                topic = input("📌 Enter your topic (e.g., hacking, coding, tech): ")
                post_suggester.suggest_post(topic)

            elif opt == "3":
                topic = input("🎯 Enter your post topic (e.g., motivation, coding): ")
                hashtag_generator.suggest_hashtags(topic)

            elif opt == "4":
                topic = input("🔎 Enter your interest/topic (e.g., hacking, gaming): ")
                group_finder.find_groups(topic)

            elif opt == "5":
                print("\n📍 [1] Add Today’s Follower Count")
                print("📍 [2] Show Growth Summary")
                sub = input("🔢 Choose option (1/2): ")
                if sub == "1":
                    count = input("🔢 Enter current follower count: ")
                    if count.isdigit():
                        follower_tracker.add_entry(int(count))
                    else:
                        print("❌ Invalid input. Must be a number.")
                elif sub == "2":
                    follower_tracker.show_progress()
                else:
                    print("❌ Invalid option.")

            else:
                print(Fore.RED + "❌ Invalid choice. Try again.")

            input(Fore.CYAN + "\n🔁 Press Enter to return to menu...")

    except KeyboardInterrupt:
        print(Fore.RED + "\n❌ Interrupted. Exiting gracefully.")
