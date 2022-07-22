import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "")
    OWNER = os.environ.get("OWNER_ID", "")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", None)
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
Anda dapat Mengunduh hampir semua hal Dari Akun Instagram Anda.
<b>Apa yang Dapat Diunduh?:</b>


 1. Semua posting dari Profil apa pun.  (Baik Publik dan Pribadi, untuk profil pribadi Anda harus menjadi pengikut.)
 2. Semua Postingan dari feed Anda.
 3. Cerita dari profil apa pun (Baik Publik maupun Pribadi, untuk profil pribadi Anda harus menjadi pengikut.)
 4. DP profil apa saja (Tidak perlu difollow)
 5. Daftar Pengikut dan Pengikut dari Profil apa pun.
 6. Daftar pengikut yang mengikuti kembali nama pengguna yang diberikan.
 7. Daftar pengikut yang tidak mengikuti kembali nama pengguna yang diberikan.
 8. Kisah Pengikut Anda.
 9. Tagged posting dari profil apapun.
 10. Postingan Anda yang disimpan.
 11. video IGTV.
 12. Sorotan dari profil apa pun.
 13. Setiap Postingan Publik dari Tautan (Post/Reels/IGTV)

<b>Bagaimana cara mengunduh:</b>

Mudah!!

 Anda harus masuk ke akun Anda dengan /login.
Anda punya dua pilihan:

1. Dari Username:

Cukup kirimkan username instagram.

Sebagai Contoh:
<code>samantharuthprabhuoffl</code>
<code>subin_p_s_</code>
<code>_chill_manh_7</code>


2. Dari URL/Link instagram:

Anda juga dapat mengirim tautan posting untuk mengunduh posting atau video.

Sebagai Contoh:
<code>https://www.instagram.com/p/CL4QbUiLRNW/?utm_medium=copy_link</code>
<code>https://www.instagram.com/taylorswift/p/CWds7zapgHn/?utm_medium=copy_link</code>


<b>Perintah dan Penggunaan yang Tersedia</b>

/start - Periksa apakah bot hidup.
/restart - Mulai ulang bot (Jika Anda mengacaukan apa pun, gunakan /restart.)
/help - Tampilkan Menu Bantuan.
/login - Masuk ke akun Anda.
/logout - Keluar dari akun anda.
/account - Menunjukkan detail akun yang masuk.

/posts <username> - Unduh posting dari nama pengguna apa pun. Menggunakan /posts untuk mengunduh postingan sendiri atau <code> /posts <username> </code>untuk yang lain.
Contoh : <code>/posts samantharuthprabhuoffl</code>

/igtv <username> - Unduh video IGTV dari nama pengguna yang diberikan. Jika tidak ada nama pengguna yang diberikan, unduh IGTV Anda.

/feed <number of posts to download> - Mengunduh kiriman dari umpan Anda. Jika tidak ada nomor yang ditentukan, semua kiriman dari umpan akan diunduh.
Contoh: <code>/feed 10</code> to download latest 10 posts from feed.

/saved <number of posts to download> - Downloads your saved posts. If no number specified all saved posts will be downloaded.
Contoh: <code>/saved 10</code> to download latest 10 saved posts.

/followers <username> - Get a list of all followers of given username. If no username given, then your list will be retrieved.
Contoh: <code>/followers samantharuthprabhuoffl</code>

/followees <username> - Get a list of all followees of given username. If no username given, then your list will be retrieved.

/fans <username> - Get a list of of followees who follow back the given username. If no username given, your list will be retrieved.

/notfollowing <username> - Get a list of followees who is not following back the given username.

/tagged <username> - Downloads all posts in which given username is tagged. If nothing given your tagged posts will be downloaded.

/story <username> - Downloads all stories from given username. If nothing given your stories will be downloaded.

/stories - Unduh semua cerita dari semua pengikut Anda.

/highlights <username> - Unduh sorotan dari nama pengguna yang diberikan, Jika tidak ada sorotan Anda akan diunduh.


"""
    HOME_TEXT = """
<b>Hai, [{}](tg://user?id={})

Ini adalah bot [{}](www.instagram.com/{}) untuk mengelola akun Instagram. 
Saya hanya bisa bekerja untuk pemilik saya [{}](tg://user?id={}).
Tetapi Anda dapat Menyebarkan bot yang sama untuk Anda gunakan dari kode sumber di bawah ini.

Gunakan /help untuk mengetahui apa yang bisa saya lakukan?</b>
"""
    HOME_TEXT_OWNER = """
<b>Helo, [{}](tg://user?id={})
Saya asisten Anda untuk mengelola akun Instagram Anda.

Gunakan /help untuk mengetahui apa yang bisa saya lakukan untuk Anda.</b>
"""

