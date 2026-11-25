"""Pemindai pola slop dan tanda baca terlarang pada teks.

Pemakaian:
  python3 scripts/pindai-slop.py berkas1.md berkas2.txt
  cat teks.txt | python3 scripts/pindai-slop.py -

Keluaran: daftar temuan bernomor baris. Temuan adalah peringatan, bukan vonis.
Kode keluar 0 bila bersih, 1 bila ada temuan.
"""
import re
import sys

TANDA = {
    "em dash": chr(8212),
    "en dash": chr(8211),
    "titik koma": chr(59),
    "tanda seru": chr(33),
    "elipsis": chr(8230),
    "titik koma Arab": chr(1563),
}

EMOJI = re.compile("[" + chr(0x1F300) + "-" + chr(0x1FAFF) + chr(0x2600) + "-" + chr(0x27BF) + chr(0x2B50) + chr(0x2705) + chr(0x274C) + "]")

POLA = [
    # Pembuka dan penutup seremonial
    (r"(^|[.?] )(tentu saja|tentu|baiklah|pertanyaan (yang )?(bagus|menarik))[ ,.]", "pembuka seremonial"),
    (r"\b(semoga (ini )?membantu|jangan ragu untuk|senang (bisa )?membantu|beri tahu saya jika)\b", "penutup basa-basi"),
    (r"\b(certainly|absolutely|great question|i hope this helps|feel free to|happy to help|let me know if)\b", "seremonial Inggris"),
    # Kata dan frasa pompa
    (r"\b(di era (digital|globalisasi|modern|revolusi)|di zaman (yang )?(serba|modern))\b", "pembuka klise"),
    (r"\b(tak|tidak) dapat dipungkiri\b", "frasa klise"),
    (r"\b(sangat|amat) (krusial|penting sekali|vital)\b", "penegas berlebihan"),
    (r"\b(memainkan|memegang) peran(an)? (yang )?(penting|krusial|vital|kunci)\b", "frasa klise"),
    (r"\b(lanskap|ekosistem|paradigma baru|menjembatani kesenjangan|membuka pintu)\b", "kata pompa"),
    (r"\b(mari kita (selami|bahas|jelajahi|telusuri)|perlu (dicatat|digarisbawahi|ditekankan) bahwa)\b", "pengantar pompa"),
    (r"\b(bukan (hanya|sekadar)[^.]{0,80}(tetapi|melainkan) (juga|pula))\b", "pola bukan hanya tetapi juga"),
    (r"\b(delve|tapestry|testament to|pivotal|landscape of|realm of|navigate the|foster|leverag(e|ing)|underscor(e|es|ing)|seamless(ly)?|robust|holistic|game[- ]changer|unlock(ing)? the)\b", "kosakata slop Inggris"),
    (r"\b(it(\x27|’)?s (important|worth) (to note|noting)|in today(\x27|’)?s (fast-paced|digital|modern)|in the realm of|at the end of the day)\b", "frasa slop Inggris"),
    (r"(في عصرنا الحالي|لا يخفى على أحد)", "klise Arab"),
]

def pindai(teks):
    temuan = []
    for no, baris in enumerate(teks.splitlines(), 1):
        for nama, ch in TANDA.items():
            if ch in baris:
                temuan.append((no, nama, ch))
        if EMOJI.search(baris):
            temuan.append((no, "emoji", EMOJI.search(baris).group(0)))
        for pola, label in POLA:
            m = re.search(pola, baris, re.IGNORECASE)
            if m:
                temuan.append((no, label, m.group(0)))
    # kalimat berpanjang seragam: bandingkan panjang kalimat pada satu paragraf
    for no, para in enumerate(teks.split("\n\n"), 1):
        kalimat = [k for k in re.split(r"(?<=[.?])\s+", para.strip()) if len(k.split()) > 2]
        if len(kalimat) >= 4:
            n = [len(k.split()) for k in kalimat]
            if min(n) >= 7 and max(n) - min(n) <= 3:
                temuan.append((no, "panjang kalimat seragam pada paragraf ke-" + str(no), str(n)))
    return temuan


def main(argv):
    sumber = argv[1:] or ["-"]
    ada = False
    for s in sumber:
        if s == "-":
            teks, nama = sys.stdin.read(), "(stdin)"
        else:
            with open(s, encoding="utf-8") as f:
                teks, nama = f.read(), s
        for no, label, cuplikan in pindai(teks):
            ada = True
            print(nama + ":" + str(no) + ": " + label + ": " + str(cuplikan))
    if not ada:
        print("Bersih.")
    return 1 if ada else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
