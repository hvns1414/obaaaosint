import instaloader
from optparse import OptionParser
import os
from collections import Counter
print("hnfxed@mrxhash")
def analyze_posts(profile):
    total_likes = 0
    total_comments = 0
    post_count = 0
    hashtags = []

    # Klasör oluştur
    folder_name = f"{profile.username}_photos"
    os.makedirs(folder_name, exist_ok=True)

    for post in profile.get_posts():
        total_likes += post.likes
        total_comments += post.comments
        post_count += 1
        hashtags.extend(post.caption_hashtags)

        # Gönderiyi klasöre indir
        instaloader.Instaloader().download_post(post, target=folder_name)

    if post_count > 0:
        avg_likes = total_likes / post_count
        avg_comments = total_comments / post_count
        print(f"Ortalama Beğeni: {avg_likes:.2f}, Ortalama Yorum: {avg_comments:.2f}")

        # Hashtag analizi
        hashtag_count = Counter(hashtags)
        most_common_hashtags = hashtag_count.most_common(5)  # En yaygın 5 hashtag
        print("En Çok Kullanılan Hashtagler:")
        for tag, count in most_common_hashtags:
            print(f"#{tag}: {count} kez kullanılmış")

def save_followers_and_following(profile, username):
    followers_file = f"{profile.username}_followers.txt"
    following_file = f"{profile.username}_following.txt"
    similar_users_file = f"{username}_similar_users.txt"

    similar_followers = []
    similar_following = []

    # Takipçileri ve takip edilenleri yazma
    with open(followers_file, "w") as f:
        f.write("Followers:\n")
        for follower in profile.get_followers():
            f.write(f"{follower.username}\n")
            # Eğer kullanıcı adı ile aynıysa, benzer takipçileri ekle
            if username.lower() in follower.username.lower():
                similar_followers.append(follower.username)

    with open(following_file, "w") as f:
        f.write("Following:\n")
        for followee in profile.get_followees():
            f.write(f"{followee.username}\n")
            # Eğer kullanıcı adı ile aynıysa, benzer takip edilenleri ekle
            if username.lower() in followee.username.lower():
                similar_following.append(followee.username)

    # Benzer kullanıcıları bir dosyaya yazma
    with open(similar_users_file, "w") as f:
        f.write("Benzer Kullanıcılar:\n")
        for similar_user in set(similar_followers + similar_following):
            f.write(f"{similar_user}\n")

    print(f"Takipçiler '{followers_file}' ve takip edilenler '{following_file}' dosyalarına yazıldı.")
    print(f"Benzer kullanıcılar '{similar_users_file}' dosyasına yazıldı.")

def get_instagram_profile_data(username):
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print(f"Username: {profile.username}")
        print(f"Full Name: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")

        # Profil fotoğrafını indir
        L.download_profilepic(profile)

        # Tüm gönderileri indir
        analyze_posts(profile)

        # Takipçi ve takip edilenleri kaydet
        save_followers_and_following(profile, username)

    except Exception as e:
        print(f"Hata: {e}")

def main():
    parser = OptionParser(usage="usage: %prog -u <username>")
    parser.add_option("-u", "--username", dest="username", help="Instagram kullanıcı adı", metavar="USERNAME")

    (options, args) = parser.parse_args()

    if not options.username:
        parser.error("Kullanıcı adını girmeniz gerekiyor.")

    username = options.username
    get_instagram_profile_data(username)

if __name__ == "__main__":
    main()
