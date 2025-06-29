#!/usr/bin/env python3

import os
import time
from colorama import Fore, Style, init
from modules import profile_optimizer
from modules import hashtag_generator
from modules import post_suggester
from modules import group_finder
from modules import follower_tracker
if opt == "3":
    topic = input("🎯 Enter your post topic (e.g., hacking, motivation, coding): ")
    hashtag_generator.suggest_hashtags(topic)
    input("🔁 Press Enter to return to menu...")
elif opt == "2":
    topic = input("📌 Enter your topic (e.g., hacking, coding, tech): ")
    post_suggester.suggest_post(topic)
    input("🔁 Press Enter to return to menu...")


elif opt == "4":
    topic = input("🔎 Enter your interest/topic (e.g., hacking, coding, gaming): ")
    group_finder.find_groups(topic)
    input("🔁 Press Enter to return to menu...")

def banner(user, lang):
    os.system('clear')
    print(Fore.RED + Style.BRIGHT + """
██╗   ██╗ █████╗ ███╗   ███╗██████╗ ██╗██████╗ ███████╗
██║   ██║██╔══██╗████╗ ████║██╔══██╗██║██╔══██╗██╔════╝
██║   ██║███████║██╔████╔██║██████╔╝██║██████╔╝█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║██╔═══╝ ██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║██║     ██║██║     ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝
            """ + Fore.CYAN + f"\n🧛‍♂️ Welcome {user}! | Vampire-FB-Grow-X")
    print(Fore.YELLOW + "🌍 Language: " + ("বাংলা" if lang == "bn" else "English"))
    print(Style.RESET_ALL)

def setup():
    os.system('clear')
    print(Fore.MAGENTA + "🔧 First-time Setup for Vampire-FB-Grow-X\n")
    name = input("🧑 Enter your name: ")
    print("\n🌐 Choose language:")
    print("1. English\n2. বাংলা")
    lang = input("🔢 Option (1/2): ")
    return name, "bn" if lang == "2" else "en"

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
    return choice

if __name__ == "__main__":
    try:
        user, lang = setup()
        while True:
            opt = main_menu(user, lang)
            if opt == "0":
                print(Fore.RED + "👋 Goodbye!")
                break
            elif opt == "1":
                dummy_data = {
                    "name": "Shourov",
                    "bio": "Learning hacking and building tools!",
                    "url": "https://facebook.com/vampire.shourov",
                    "profile_pic": True,
                    "cover_photo": False
                }
                profile_optimizer.optimize_profile(dummy_data)
                input("🔁 Press Enter to return to menu...")
            else:
                print(Fore.YELLOW + "🛠️ Module under construction...")
                input("🔁 Press Enter to return to menu...")
    except KeyboardInterrupt:
        print("\n❌ Interrupted. Exiting.")
