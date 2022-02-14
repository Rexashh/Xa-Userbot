# ReCode by @pikyus1
# FROM Rose-Userbot <https://github.com/SendiAp/Rose-Userbot>
# t.me/Rose_Userbot

import random
import redis

from userbot import CMD_HELP
from userbot.events import register

dare = [
    "Bertindak seperti monyet dan merekam video itu.",
    "Bersikaplah seolah-olah Anda tidak mengerti bahasa manusia sampai giliran Anda berikutnya (munculkan bahasa Anda sendiri).",
    "Bertindak seperti karakter Disney favorit Anda selama sisa permainan.",
    "Jadian Sama Owner @JustRex.",
    "Tutup mata Anda dan kirim pesan teks buta ke orang acak.",
    "Tulis puisi di tempat berdasarkan sesuatu yang dihasilkan oleh kelompok.",
    "Masuk Groups @rexaprivateroom.",
    "Semua yang Anda katakan selama 5 menit berikutnya harus berima.",
    "Semua yang Anda katakan selama 5 menit berikutnya tidak boleh mengandung kata-kata: 'tetapi', 'a', 'the', 'atau'",
    "Bilang i love you ke @JustRex.",
    "Buat lagu rap gaya bebas tentang setiap orang dalam grup",
    "Buatlah puisi dengan menggunakan kata 'oranye' dan 'rusa'.",
    "Buatlah puisi dengan menggunakan kata 'nanas' dan 'apel'.",
    "Buatlah puisi dengan menggunakan kata 'angsa' dan 'kacang tanah'.",
    "Buatlah puisi tentang warna biru.",
    "Buat cerita tentang orang acak dalam kelompok.",
    "Banting Hp Kalian , Tanpa Emosi.",
    "Posting 'Saya suka bahasa Inggris!' di sebuah media sosial.",
    "Rekam video Anda menari, tetapi tanpa musik.",
    "Rekam video Anda memainkan drum udara ke lagu pilihan Anda.",
    "Rekam video Anda bermain gitar udara ke lagu pilihan Anda.",
    "Rekam kesan selebriti favorit Anda.",
    "Rekam kesan hewan favorit Anda.",
    "Rekam tawa jahat terbaik Anda; sekeras yang Anda bisa.",
    "Catat kesan presiden terbaik Anda.",
    "Rekam diri Anda mengucapkan alfabet mundur.",
    "Rekam diri Anda menyanyikan Twinkle Twinkle, Little Star sambil mengalahkan tinju.",
    "Rekam diri Anda menyanyikan alfabet tanpa menggerakkan mulut Anda.",
    "Rekam diri Anda berbicara tentang makanan favorit Anda dalam aksen Rusia.",
    "Ucapkan ya dengar aku setelah semua yang Anda katakan selama 5 menit berikutnya.",
    "Ucapkan Anda tahu apa yang saya katakan setelah semua yang Anda katakan selama 5 menit berikutnya.",
    "Kirim pesan teks kepada seseorang yang menanyakan apakah mereka percaya pada alien, kirim tangkapan layar percakapan.",
    "Kirim email ke salah satu guru Anda, beri tahu mereka tentang bagaimana hari Anda berjalan dan ambil tangkapan layar.",
    "Kirim pesan teks yang tidak diminta ke salah satu teman Anda, beri tahu mereka tentang bagaimana hari Anda berjalan dan ambil tangkapan layar.",
    "Kirim foto terakhir yang Anda ambil dengan kamera ponsel Anda.",
    "Kirim tangkapan layar terakhir yang Anda ambil di ponsel Anda.",
    "Kirim foto paling memalukan di ponsel Anda.",
    "Kirim selfie tertua di ponsel Anda.",
    "Kirim tangkapan layar dari riwayat pencarian google terbaru Anda.",
    "Kirim selfie Anda membuat wajah lucu.",
    "Atur bahasa telepon Anda ke bahasa Cina selama 10 menit berikutnya.",
    "Tunjukkan tiga orang terakhir yang Anda kirimi SMS dan apa yang dikatakan pesan tersebut.",
    "Kirim pesan teks kepada orang yang Anda sukai dan beri tahu mereka betapa Anda menyukainya.",
    "Gunakan huruf nama pemain lain untuk mendeskripsikannya (mis. SAM : S = Konyol ; A = Menarik ; M = Merry)",
    "Ucapkan kata pertama yang muncul di benak Anda, dan rekamlah.",

]

truth = [
    "Apakah Anda seorang siswa yang pekerja keras?",
    "Apakah Anda menyukai olahraga apa pun?",
    "Apakah Anda takut pada binatang apa pun?",
    "Apakah Anda takut mati? Mengapa?",
    "Apakah Anda takut hantu?",
    "Apakah kamu masih perawan?",
    "Bisakah Anda menjilat siku Anda?",
    "Bisakah Anda melihat diri Anda menikah dengan anak paling menyeramkan di sekolah Anda suatu hari nanti?",
    "Bisakah Anda berbicara bahasa yang berbeda?",
    "Bisakah Anda menyentuhkan lidah ke hidung?",
    "Bisa pakai tongkat pogo?",
    "Bisakah Anda pergi seminggu tanpa junk food?",
    "Bisakah Anda pergi dua bulan tanpa berbicara dengan teman-teman Anda?",
    "Jelaskan mimpi teraneh yang pernah kamu alami?",
    "Jelaskan mimpi teraneh yang pernah kamu alami?",
    "Jelaskan mimpi terbaru Anda yang Anda ingat?",
    "Jelaskan pertemuan romantis terbaru Anda?",
    "Jelaskan ciuman terburuk Anda?",
    "Apakah Anda percaya pada cinta sama sekali?",
    "Apakah Anda percaya pada cinta pada pandangan pertama?",
    "Apakah Anda pernah berbicara dengan diri sendiri di cermin?",
    "Apakah Anda memiliki bakat terpendam? Apa itu?",
    "Apakah kamu punya pekerjaan? Jika demikian, apa hal favorit Anda tentang itu?",
    "Apakah kamu punya teman khayalan?",
    "Apakah Anda memiliki fobia?",
    "Apakah Anda memiliki bakat yang tidak biasa?",
    "Apakah kamu tahu cara memasak?",
    "Apakah Anda tahu cara menari?",
    "Apakah Anda suka mengerjakan tugas?",
    "Apakah Anda suka berolahraga?",
    "Apakah Anda mengirim pesan kepada orang-orang selama kelas Anda?",
    "Lebih suka apple atau android?",
    "Apakah Anda bernyanyi di kamar mandi? Lagu apa yang kamu nyanyikan terakhir kali?",
    "Apakah Anda pikir Anda akan menikahi bf/gf Anda? Jika tidak, mengapa tidak?",
    "Jelaskan kepada orang yang paling tidak Anda sukai di grup ini mengapa Anda paling tidak menyukainya?",
    "Apakah kamu pernah berantem selama di sekolah?",
    "Udah pernah ciuman belum? Jika demikian, siapa ciuman terbaik Anda?",
    "Apakah Anda pernah menggigit kuku kaki?",
    "Pernahkah Anda menyalahkan kentut pada binatang?",
    "Pernahkah Anda menyalahkan sesuatu yang telah Anda lakukan pada salah satu saudara Anda?",
    "Pernahkah kamu menyontek saat ujian?",
    "Apakah Anda pernah ditipu atau ditipu?",
    "Pernahkah kamu memanjat pohon?",
    "Apakah Anda pernah mengotori celana Anda sejak Anda masih kecil?",
    "Pernahkah Anda makan makanan yang Anda jatuhkan ke tanah? Jika ya, berapa lama di tanah?",
    "Pernahkah kamu tertidur saat pelajaran berlangsung?",
    "Apakah Anda pernah naksir seorang guru?",
    "Pernahkah Anda naksir seseorang yang sahabat Anda kencani?"
    "Pernahkah Anda memiliki seseorang yang menulis tugas atau pekerjaan untuk Anda?",
    "Pernahkah Anda mencium binatang?",
    "Pernahkah Anda membiarkan seseorang disalahkan atas sesuatu yang Anda lakukan?",
    "Pernahkah kamu berbohong kepada sahabatmu sendiri?",
    "Pernahkah Anda berbohong kepada orang tua Anda tentang apakah Anda berada di kelas atau tidak?",
    "Pernahkah Anda berbohong kepada orang tua Anda tentang apa yang Anda lakukan sepulang sekolah?",
    "Pernahkah Anda buang air kecil di kolam renang?",
    "Pernahkah Anda mengupil di depan umum?",
    "Pernahkah Anda memposting sesuatu di internet/media sosial yang Anda sesali?",
    "Pernahkah Anda mengerjai salah satu guru Anda?",
    "Pernahkah Anda menerima surat cinta?",
    "Pernahkah Anda naik bus tanpa membayar ongkosnya?",
    "Pernahkah Anda mencuri sesuatu yang bernilai lebih dari $10?",
    "Apakah Anda pernah mencuri sesuatu?",
    "Pernahkah Anda mengambil uang dari teman sekamar Anda?",
    "Pernahkah Anda mengambil uang yang bukan milik Anda?",
    "Pernahkah Anda mengadakan pesta di rumah Anda?",
    "Pernahkah Anda berbohong saat bermain Truth or Dare? Apa itu dan mengapa?",
    "Pernahkah Anda menceritakan salah satu rahasia sahabat Anda, bahkan jika Anda mengatakan tidak akan melakukannya?",
    "Pernahkah Anda menggunakan kata sandi orang lain?",
    "Pernahkah Anda menonton film dewasa tanpa sepengetahuan orang tua Anda?",
    "Pernahkah Anda mengenakan pakaian yang sama selama lebih dari tiga hari?",
    "Bagaimana perasaan Anda tentang potongan akhir sepotong roti?",
    "Bagaimana perasaan Anda tentang media sosial?",
    "Seberapa jauh Anda akan pergi untuk mendapatkan pria atau wanita impian Anda?",
    "Berapa banyak pacar (atau pacar) yang Anda miliki?",
    "Berapa hari Anda bisa pergi tanpa pasangan Anda?",
    "Berapa banyak anak yang ingin Anda miliki?",
    "Berapa banyak saudara yang Anda miliki?",
    "Berapa kali Anda melewatkan kelas tanpa alasan?",
    "Berapa umur Anda ketika orang tua Anda mendudukkan Anda untuk berbicara dan apa yang mereka katakan (atau tidak katakan) tentang burung dan lebah?",
    "Seberapa cepat Anda menyadari bahwa Anda jatuh cinta dengan pasangan Anda?",
    "Seberapa cepat Anda ingin memulai sebuah keluarga?",
    "Bagaimana ciuman pertamamu?",
    "Jika tidak ada yang namanya uang, apa yang akan Anda lakukan dengan hidup Anda?",
    "Jika Anda bisa menjadi pahlawan super; apa kekuatanmu?",
    "Jika kamu bisa menjadi hewan apa saja, kamu ingin menjadi binatang apa?",
    "Jika Anda bisa menjadi dinosaurus apa pun; yang mana?",
    "Jika Anda bisa menjadi penjahat super; siapa kamu?",
    "Jika Anda dapat mengubah satu hal di tubuh Anda, apakah itu?",
    "Jika Anda bisa mewarnai rambut Anda dengan warna apa pun, warna apa yang akan Anda pilih?",
    "Jika Anda bisa menghapus satu pengalaman masa lalu, apakah itu?",
    "Jika Anda bisa pergi ke mana saja di dunia, ke mana Anda akan pergi?",
    "Jika Anda dapat membuat satu permintaan saat ini juga, apakah itu?",
    "Jika Anda hanya bisa mendengar satu lagu selama sisa hidup Anda, apakah itu?",
    "Jika Anda dapat memiliki bisnis sendiri suatu hari nanti, apakah itu?",
    "Jika Anda bisa memiliki bisnis Anda sendiri suatu hari nanti; apa yang akan terjadi?",
    "Jika Anda dapat bertukar kehidupan dengan selebritas mana pun selama sehari, siapakah itu?",
    "Jika Anda dapat mengambil satu hal buruk di dunia, apakah itu?",
    "Jika Anda bisa, apa yang akan Anda ubah dalam hidup Anda?",
    "Jika Anda belum pernah bertemu pasangan Anda, menurut Anda di mana Anda akan berada?",
    "Jika Anda memiliki pilihan untuk hidup sendiri sekarang, apakah Anda akan melakukannya?",
    "Kalau pernah selingkuh, kenapa dilakuin?",
    "Jika Anda tiba-tiba memiliki satu juta dolar; apa yang akan kamu lakukan dengan semua uangmu?",
    "Jika Anda seorang miliarder, apa yang akan Anda habiskan untuk lakukan?",
    "Jika Anda menyelamatkan semua orang di sini dari gedung yang terbakar, tetapi Anda harus meninggalkan satu, siapa itu?",
    "Jika Anda terjebak di pulau terpencil, teman mana yang Anda inginkan bersama Anda?",
    "Jika kamu terjebak di sebuah pulau selama 3 hari, apa yang akan kamu bawa?",
]


# truth
@register(outgoing=True, pattern="^.truth$")
async def redis(pong):
    await pong.reply(random.choice(truth))


@register(outgoing=True, pattern="^.t$")
async def redis(pong):
    await pong.reply(random.choice(truth))


@register(outgoing=True, pattern="^t$")
async def redis(pong):
    await pong.reply(random.choice(truth))


@register(outgoing=True, pattern="^T$")
async def redis(pong):
    await pong.reply(random.choice(truth))

# dare


@register(outgoing=True, pattern="^.dare$")
async def redis(pong):
    await pong.reply(random.choice(dare))


@register(outgoing=True, pattern="^.d$")
async def redis(pong):
    await pong.reply(random.choice(dare))


@register(outgoing=True, pattern="^d$")
async def redis(pong):
    await pong.reply(random.choice(dare))


@register(outgoing=True, pattern="^D$")
async def redis(pong):
    await pong.reply(random.choice(dare))

CMD_HELP.update(
    {
        "truth": "**✘ Plugin** `truth` | `.t` | `t` |\
        \n\n  •  **Perintah :** `.truth` \
        \n  •  **Fungsi :** Mengirimkan Sebuah Pertanyaan Random.\
        \n\n  •  **Perintah :** `.dare` | `.d` | `d` |\
        \n  •  **Fungsi :** Mengirimkan Sebuah Tantangan Random.\
    "
    }
)
