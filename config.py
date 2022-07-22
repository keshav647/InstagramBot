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

/feed <jumlah postingan yang diunduh> - Mengunduh kiriman dari umpan Anda. Jika tidak ada nomor yang ditentukan, semua kiriman dari umpan akan diunduh.
Contoh: <code>/feed 10</code> untuk mengunduh 10 posting tersimpan terbaru.

/saved <jumlah postingan yang diunduh> - Mendownload posting Anda yang disimpan. Jika tidak ada nomor yang ditentukan, semua posting yang disimpan akan diunduh.
Contoh: <code>/saved 10</code> untuk mengunduh 10 posting tersimpan terbaru.

/followers <username> - Dapatkan daftar semua pengikut dari nama pengguna yang diberikan. Jika tidak ada nama pengguna yang diberikan, maka daftar Anda akan diambil.
Contoh: <code>/followers samantharuthprabhuoffl</code>

/followees <username> - Dapatkan daftar semua pengikut dari nama pengguna yang diberikan. Jika tidak ada nama pengguna yang diberikan, maka daftar Anda akan diambil.

/fans <username> - Dapatkan daftar semua pengikut dari nama pengguna yang diberikan. Jika tidak ada nama pengguna yang diberikan, maka daftar Anda akan diambil.

/notfollowing <username> -  Dapatkan daftar pengikut yang tidak mengikuti kembali nama pengguna yang diberikan.

/tagged <username> - Mengunduh semua posting di mana nama pengguna yang diberikan ditandai. Jika tidak ada postingan yang diberi tag Anda akan diunduh.

/story <username> - Mengunduh semua cerita dari nama pengguna yang diberikan. Jika tidak ada yang diberikan, cerita Anda akan diunduh..

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

