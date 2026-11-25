# pembimbing-menulis

Partner, tutor, dan pembimbing menulis dalam bahasa Indonesia, Inggris, dan Arab.

## Isi
| Komponen | Fungsi |
|---|---|
| Skill pembimbing-menulis | Pintu masuk. Mode Mulai, Kerangka, Tulis bersama, Umpan balik, Latihan, Riset dan catatan, Poles |
| Skill umpan-balik-tulisan | Umpan balik bertingkat pada draf, dari tujuan dan tesis sampai mekanik, dengan uji khas per jenis tulisan |
| Skill koreksi-alternatif | Koreksi kalimat dengan alasan, dua atau tiga alternatif bernuansa, dan rekomendasi beralasan, plus daftar pola penulis |
| Gerbang anti-slop | `anti-slop.md` dan `scripts/pindai-slop.py`: daftar pola yang dilarang, prosedur sebelum mengirim, dan pemindai otomatis |
| Skill latihan-menulis | Latihan bertarget dengan bank jenis latihan |
| Agen pembimbing | Sesi bimbingan panjang |
| Konteks aturan | Dimuat tiap sesi lewat hook SessionStart |

## Rujukan
Semua rujukan ada di `skills/pembimbing-menulis/references/`.

| Berkas | Isi |
|---|---|
| metode-bimbingan.md | Cara membimbing, tahap penulis, pertanyaan pemandu |
| ketentuan-final-draft.md | FD-01 sampai FD-52, parafrase ketentuan paragraf, esai, bukti, nada, dan kohesi, dalam tiga bahasa |
| panduan-per-jenis-tulisan.md | JT-01 sampai JT-15. Struktur, kalimat topik atau tesis, penanda bahasa, kesalahan khas, dan pertanyaan pemandu per jenis tulisan |
| tata-bahasa-untuk-menulis.md | TB-01 sampai TB-33. Butir tata bahasa dan mekanik, kesalahan khas, uji cepat |
| kaidah-bahasa-indonesia.md | ID-01 sampai ID-40. Ejaan (EYD Edisi V), tata bahasa, istilah, diksi, kolokasi, dan idiom bahasa Indonesia |
| kaidah-bahasa-inggris.md | EN-01 sampai EN-30. Register akademik, ejaan, istilah, diksi, kolokasi, preposisi, dan idiom bahasa Inggris |
| kaidah-bahasa-arab.md | AR-01 sampai AR-40. Nahwu, sharaf, istilah, diksi, kolokasi, dan ungkapan bahasa Arab (adaptasi, perlu konfirmasi ahli) |
| riset-sitasi-dan-integritas.md | RS-01 sampai RS-15. Mencari dan menilai sumber, mencatat, memparafrase, mengutip, sitasi, dan menghindari plagiat |

## Prinsip
Penulis memegang kendali. Diagnosis sebelum saran. Umpan balik jujur dan bisa ditindaklanjuti. Tidak ada karangan sumber atau data.

## Dasar ketentuan
Ketentuan berasal dari parafrase seri buku ajar Cambridge Final Draft 1 sampai 4 (Cambridge University Press, 2016). Buku itu untuk pembelajar bahasa Inggris, jadi sebagian aturan adalah konvensi gaya dan penyederhanaan untuk belajar. Bagian Arab adalah adaptasi dan perlu dikonfirmasi penutur ahli.

## Cakupan bacaan
- Dibaca dan dirangkum: seluruh kalimat berisi aturan dan seluruh blok instruksional unit pada keempat buku.
- Tidak ditelaah baris demi baris: latihan, teks bacaan, model tulisan mahasiswa, ucapan terima kasih, dan daftar pustaka buku.
- Teks buku ketiga hasil pemindaian dan banyak yang rusak, sehingga sebagian bagian tidak terbaca utuh.
- Contoh dalam plugin ini buatan sendiri. Teks buku tidak disalin.

## Batas
- Gerbang anti-slop berlaku lewat aturan sesi dan pemindai regeks. Plugin tidak mengubah model, jadi tidak ada jaminan nol slop di akun gratis atau berbayar. Pemindai hanya menangkap pola yang terdaftar.
- Plugin ini menyediakan umpan balik berulang dengan alternatif dan alasan untuk melatih kepekaan. Ia tidak menjamin penulisnya menulis seperti penutur asli. Itu bergantung pada banyaknya membaca, menulis, dan umpan balik.
- Bukan pengganti dosen pembimbing atau pedoman jurnal. Pedoman resmi mengalahkan plugin ini.
- Skor rubrik adalah alat bimbingan, bukan nilai resmi.
- Pustaka teori pedagogi dalam metode-bimbingan.md adalah pengetahuan umum yang perlu diverifikasi sebelum dikutip.
- Kaidah Indonesia merujuk EYD Edisi V (SK Kepala Badan Bahasa Nomor 0424/I/BS.00.01/2022). Kaidah Arab dan daftar idiom adalah ringkasan penyusun yang perlu dicek ke kamus dan penutur ahli.
- Gaya sitasi buku (MLA edisi lama) tidak diadopsi. Ikuti gaya yang diminta dosen atau jurnal.

## Versi
0.5.0. Menambah gerbang anti-slop (aturan sesi, anti-slop.md, pemindai pindai-slop.py).
0.4.0. Menambah skill koreksi-alternatif (format koreksi, alternatif, alasan, dan daftar pola penulis).
0.3.0. Menambah catatan kaidah per bahasa (Indonesia, Inggris, Arab) untuk tata bahasa, istilah, diksi, dan idiom.
0.2.0. Menambah panduan per jenis tulisan, tata bahasa, riset dan sitasi, peta uji per jenis, dan bank latihan yang diperluas.
0.1.0. Rilis awal.
