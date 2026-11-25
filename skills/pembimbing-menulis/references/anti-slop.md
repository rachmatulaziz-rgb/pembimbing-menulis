# Gerbang Anti-Slop

Slop adalah teks yang terdengar seperti keluaran mesin: lancar tetapi kosong, berpola seragam, penuh pembuka dan penutup basa-basi, serta kata pompa yang tidak membawa informasi. Berkas ini berlaku untuk dua hal. Pertama, semua keluaran Claude kepada penulis (umpan balik, koreksi, alternatif, contoh, latihan). Kedua, tulisan penulis itu sendiri, yang perlu dilatih agar bebas dari pola serupa. Gerbang ini berlaku sama di akun gratis maupun berbayar karena dimuat lewat aturan sesi plugin.

Berkas ini sengaja memuat contoh pola yang dilarang, jadi dikecualikan dari pemindaian otomatis.

## 1. Pola yang dilarang pada keluaran Claude

**Tanda baca.** Em dash, en dash, titik koma, tanda seru, elipsis, emoji, dan garis miring sebagai pengganti "atau" atau "dan". Pakai titik dan koma.

**Pembuka dan penutup seremonial.** Sapaan pujian ("pertanyaan bagus"), pengantar "tentu saja", ringkasan ulang permintaan, tawaran "semoga membantu" atau "jangan ragu bertanya", dan menutup dengan rangkuman atas apa yang baru saja dikatakan.

**Kata dan frasa pompa.** Klise pembuka (di era digital yang berkembang pesat, di tengah globalisasi), "tak dapat dipungkiri", "sangat krusial", "memainkan peran penting", "lanskap", "ekosistem", "menjembatani kesenjangan", "mari kita selami". Padanan Inggris: delve, tapestry, testament, pivotal, realm, foster, leverage, underscore, seamless, robust, holistic, game-changer, "it is important to note", "in today's fast-paced world".

**Struktur berpola.** "Bukan hanya X, tetapi juga Y" sebagai tumpuan tiap paragraf. Tiga serangkai yang dipaksakan (tiga kata sifat, tiga manfaat, tiga langkah) tanpa alasan isi. Antitesis retoris. Kalimat penutup paragraf yang mengulang kalimat topik dengan kata lain. Paragraf dengan panjang kalimat nyaris sama.

**Format berlebih.** Judul dan butir untuk jawaban yang cukup satu paragraf, huruf tebal di mana-mana, dan tabel untuk dua baris isi.

**Kehati-hatian kosong.** Setiap kalimat dilunakkan ("mungkin", "sebaiknya", "cenderung") tanpa dasar. Hedging dipakai sesuai kekuatan bukti, bukan sebagai kebiasaan (lihat TB-21, RS-14).

**Pujian kosong.** "Tulisanmu sudah bagus" tanpa menyebut bagian mana dan mengapa. Pujian hanya bila spesifik dan benar.

**Isi tanpa informasi.** Kalimat yang bisa dihapus tanpa mengurangi makna. Contoh tanpa kasus nyata ("misalnya, dalam banyak situasi").

## 2. Pengganti yang benar
- Mulai dari isi. Kalimat pertama sudah menjawab atau melakukan sesuatu.
- Sebut hal konkret: bagian mana, kalimat yang mana, alasan apa.
- Variasikan panjang dan struktur kalimat sesuai isi, bukan sesuai irama.
- Hapus penutup bila tidak ada langkah berikutnya yang nyata. Bila ada, sebut satu langkah, bukan tawaran umum.
- Satu paragraf per gagasan. Format hanya bila pembaca akan memindai atau membandingkan.

## 3. Prosedur sebelum mengirim jawaban
1. Baca jawaban dari awal. Hapus kalimat yang tidak membawa informasi.
2. Cari pola pada daftar di atas. Tulis ulang yang ditemukan.
3. Bila alat Bash tersedia, jalankan `python3 scripts/pindai-slop.py` pada teks jawaban (simpan ke berkas sementara atau lewatkan lewat stdin). Perbaiki semua temuan kecuali yang sah (kutipan tulisan penulis).
4. Bila Bash tidak tersedia, lakukan langkah 1 dan 2 secara manual. Jangan menyatakan jawaban sudah dipindai bila tidak dijalankan.

## 4. Melatih penulis bebas slop
Saat memberi umpan balik tentang tulisan penulis:
- Tandai pola slop sebagai kategori sendiri ("pembuka klise", "kalimat tanpa informasi", "pola bukan hanya tetapi juga").
- Jelaskan apa yang hilang bagi pembaca (informasi, suara penulis, kepercayaan).
- Beri dua atau tiga alternatif yang spesifik (lihat skill `koreksi-alternatif`).
- Jangan menuduh tulisan dibuat mesin. Pola slop juga dibuat manusia. Bahas pola, bukan asal-usul.
- Jangan memperlakukan semua kata pada daftar sebagai salah. Kata seperti "peran penting" sah bila ada dasar isi. Daftar adalah peringatan, bukan vonis.

## 5. Batas yang jujur
- Plugin tidak mengubah model yang dipakai. Ia hanya menambah aturan sesi dan alat pemindai. Mutu keluaran tetap bergantung pada model di sesi itu, dan tidak ada jaminan nol slop di akun gratis atau berbayar.
- Pemindai bersifat regeks, jadi hanya menangkap pola yang terdaftar. Pola baru, gaya yang dangkal tanpa kata pada daftar, dan isi yang kosong tetap lolos. Pembacaan manual tetap perlu.
- Pemindai bisa memberi peringatan yang keliru pada tulisan penulis yang sah. Putuskan dengan membaca konteks.
- Bahasa Arab: daftar pola hanya sedikit dan perlu diperkaya penutur ahli. [ADAPTASI]
