📄 README.md
markdown
Kopyala
Düzenle
# Instagram OSINT Tool

A powerful Python-based OSINT tool to gather publicly available intelligence from Instagram profiles.  
It retrieves and analyzes user data such as posts, followers, following, hashtags, and more.

> ⚠️ This tool works only on public profiles or private profiles accessible by a logged-in session.

---

## 🔍 Features

- Extracts and displays:
  - Username, full name, biography
  - Followers, following, and post count
  - Profile picture (downloaded)
- Downloads all available posts from the target profile
- Calculates:
  - Average likes and comments per post
  - Most frequently used hashtags
- Saves:
  - Followers and following lists into separate `.txt` files
  - Username-similar users into a third file for pattern analysis

---

## 🛠️ Installation

1. Make sure Python 3 is installed.
2. Install the required package:
```bash
pip install instaloader
🚀 Usage
bash
Kopyala
Düzenle
python insta_osint.py -u <username>
Example:

bash
Kopyala
Düzenle
python insta_osint.py -u natgeo
This will:

Print basic profile info

Download all posts into a folder named <username>_photos/

Save followers and followees into <username>_followers.txt and <username>_following.txt

Detect and save similar usernames into <username>_similar_users.txt

Show the 5 most used hashtags with frequency

Display average likes and comments per post

⚠️ Legal Notice
This script is for educational and ethical OSINT purposes only.
Scraping or automating access to Instagram data may violate their Terms of Service.
Use responsibly and only on profiles you have permission to analyze.

