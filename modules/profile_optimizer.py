# modules/profile_optimizer.py

import re

def check_name(name):
    if len(name.split()) < 2:
        return "❌ Your name looks too short. Use full name to increase trust."
    return "✅ Name looks good!"

def check_bio(bio):
    if len(bio) < 10:
        return "❌ Bio is too short. Add something interesting!"
    elif "follow" not in bio.lower():
        return "⚠️ Add a call to action like 'Follow me for more updates!'"
    return "✅ Bio looks great!"

def check_url(url):
    if not url:
        return "❌ You didn't add any custom Facebook URL!"
    elif not re.match(r'^https:\/\/facebook\.com\/[a-zA-Z0-9_.]+$', url):
        return "❌ Invalid URL format. Use: https://facebook.com/your.username"
    return "✅ Custom URL looks good!"

def check_profile_pic(status):
    return "✅ Profile picture set!" if status else "❌ No profile picture found!"

def check_banner(status):
    return "✅ You have a cover photo!" if status else "⚠️ Add a cover photo for better appearance."

def optimize_profile(data):
    print("\n🔍 Checking your profile...\n")
    print(check_name(data.get("name", "")))
    print(check_bio(data.get("bio", "")))
    print(check_url(data.get("url", "")))
    print(check_profile_pic(data.get("profile_pic", False)))
    print(check_banner(data.get("cover_photo", False)))
    print("\n🎯 Profile optimization complete.\n")
