#!/usr/bin/env python3
"""The Passport Page of a Country That Isn't There — Republika Marisal.

Deterministic PIL render of an open passport spread (1024x1024 PNG).
Invented salt-pan harbour republic behind a tide wall. No network, no randomness.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = "/output/entry.png"

# ---------- fonts ----------
FONT_DIRS = ["/usr/share/fonts/truetype/liberation", "/usr/share/fonts/truetype/dejavu"]

def font(names, size):
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()

SERIF_B = lambda s: font(["LiberationSerif-Bold.ttf", "DejaVuSerif-Bold.ttf"], s)
SERIF   = lambda s: font(["LiberationSerif-Regular.ttf", "DejaVuSerif.ttf"], s)
SERIF_I = lambda s: font(["LiberationSerif-Italic.ttf", "DejaVuSerif.ttf"], s)
SANS_B  = lambda s: font(["LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf"], s)
SANS    = lambda s: font(["LiberationSans-Regular.ttf", "DejaVuSans.ttf"], s)
MONO    = lambda s: font(["LiberationMono-Regular.ttf", "DejaVuSansMono.ttf"], s)

# ---------- palette ----------
INK      = (38, 52, 84)      # deep harbour blue
INK_SOFT = (84, 98, 124)
PAPER    = (247, 242, 228)
PAPER_R  = (245, 240, 224)
RULE     = (150, 160, 178)
RED      = (146, 44, 48)
GREEN    = (44, 110, 84)
BLUE     = (52, 84, 150)
TEAL     = (38, 110, 108)
GREY_TXT = (96, 104, 118)

img = Image.new("RGB", (W, H), (18, 18, 20))
d = ImageDraw.Draw(img)

# pages
LX0, LX1 = 30, 502
RX0, RX1 = 522, 994
PY0, PY1 = 28, 996
d.rectangle([LX0, PY0, LX1, PY1], fill=PAPER)
d.rectangle([RX0, PY0, RX1, PY1], fill=PAPER_R)
# spine shadow
for i in range(10):
    shade = 232 - i * 6
    d.line([(502 + i, PY0), (502 + i, PY1)], fill=(shade, shade - 8, shade - 28))
    d.line([(522 - i, PY0), (522 - i, PY1)], fill=(shade, shade - 8, shade - 28))
d.rectangle([LX0, PY0, LX1, PY1], outline=(190, 184, 162), width=1)
d.rectangle([RX0, PY0, RX1, PY1], outline=(190, 184, 162), width=1)

def text(x, y, s, f, fill=INK, anchor="la", spacing=0):
    d.text((x, y), s, font=f, fill=fill, anchor=anchor, spacing=spacing)

def tw(s, f):
    b = d.textbbox((0, 0), s, font=f)
    return b[2] - b[0]

# ---------- left page header ----------
cx = (LX0 + LX1) // 2
# emblem: circle, salt crystal (diamond), waves
ex, ey, er = cx, 86, 30
d.ellipse([ex - er, ey - er, ex + er, ey + er], outline=INK, width=2)
d.ellipse([ex - er + 4, ey - er + 4, ex + er - 4, ey + er - 4], outline=INK, width=1)
d.polygon([(ex, ey - 16), (ex + 11, ey - 2), (ex, ey + 12), (ex - 11, ey - 2)], outline=INK, width=2)
d.line([(ex - 11, ey - 2), (ex + 11, ey - 2)], fill=INK, width=1)
for wy in (ey + 15, ey + 20):
    pts = []
    for t in range(-14, 15, 2):
        import math
        pts.append((ex + t, wy + (2 if (t // 4) % 2 == 0 else -1)))
    d.line(pts, fill=INK, width=1)

text(cx, 128, "REPUBLIKA MARISAL", SERIF_B(25), anchor="ma")
text(cx, 160, "REPUBLIC OF MARISAL", SANS(11), fill=INK_SOFT, anchor="ma")
# letter-spaced PASAPORT
pas = "P A S A P O R T"
text(cx, 180, pas, SANS_B(13), anchor="ma")
d.line([(LX0 + 26, 208), (LX1 - 26, 208)], fill=INK, width=2)

# ---------- portrait ----------
PX0, PYp0, PX1, PYp1 = LX0 + 28, 224, LX0 + 196, 430
d.rectangle([PX0, PYp0, PX1, PYp1], fill=(203, 211, 220), outline=INK, width=2)
# shoulders / shirt
d.polygon([(PX0 + 18, PYp1), (PX0 + 34, PYp1 - 52), (PX0 + 62, PYp1 - 62),
           (PX1 - 62, PYp1 - 62), (PX1 - 34, PYp1 - 52), (PX1 - 18, PYp1)], fill=(44, 62, 92))
# collar
d.polygon([(PX0 + 62, PYp1 - 62), ((PX0 + PX1) // 2, PYp1 - 40), (PX1 - 62, PYp1 - 62),
           ((PX0 + PX1) // 2, PYp1 - 56)], fill=(232, 234, 236))
# neck
ncx = (PX0 + PX1) // 2
d.rectangle([ncx - 13, PYp0 + 118, ncx + 13, PYp0 + 148], fill=(222, 178, 146))
# face
d.ellipse([ncx - 34, PYp0 + 34, ncx + 34, PYp0 + 128], fill=(232, 190, 158))
# hair (short, dark, side part) — rounded cap following the head
d.pieslice([ncx - 37, PYp0 + 24, ncx + 37, PYp0 + 100], start=175, end=365, fill=(52, 42, 36))
d.chord([ncx - 37, PYp0 + 24, ncx + 37, PYp0 + 100], start=175, end=365, fill=(52, 42, 36))
d.rectangle([ncx - 37, PYp0 + 56, ncx - 31, PYp0 + 80], fill=(52, 42, 36))
d.rectangle([ncx + 31, PYp0 + 56, ncx + 37, PYp0 + 80], fill=(52, 42, 36))
# side-part line
d.line([(ncx - 20, PYp0 + 40), (ncx + 14, PYp0 + 36)], fill=(84, 70, 60), width=2)
# ears
d.ellipse([ncx - 39, PYp0 + 78, ncx - 31, PYp0 + 96], fill=(228, 184, 150))
d.ellipse([ncx + 31, PYp0 + 78, ncx + 39, PYp0 + 96], fill=(228, 184, 150))
# brows, eyes, nose, mouth
d.line([(ncx - 22, PYp0 + 76), (ncx - 8, PYp0 + 74)], fill=(52, 42, 36), width=3)
d.line([(ncx + 8, PYp0 + 74), (ncx + 22, PYp0 + 76)], fill=(52, 42, 36), width=3)
d.ellipse([ncx - 18, PYp0 + 82, ncx - 10, PYp0 + 88], fill=(30, 30, 34))
d.ellipse([ncx + 10, PYp0 + 82, ncx + 18, PYp0 + 88], fill=(30, 30, 34))
d.line([(ncx, PYp0 + 88), (ncx - 3, PYp0 + 104), (ncx + 4, PYp0 + 106)], fill=(190, 140, 108), width=2)
d.line([(ncx - 10, PYp0 + 116), (ncx + 10, PYp0 + 116)], fill=(150, 96, 84), width=3)
text(PX0, PYp1 + 8, "FOTOGRAFIA / PHOTOGRAPH", SANS(8), fill=GREY_TXT)

# ---------- data fields ----------
FX = LX0 + 216
fields = [
    ("TIP / TYPE", "P"),
    ("KOD / CODE", "MSL"),
    ("PASAPORT NR / PASSPORT NO.", "MSL 007314"),
    ("PREZIME / SURNAME", "HAVEL"),
    ("IME / GIVEN NAMES", "TOMAS REN"),
    ("DRZAVLJANSTVO / NATIONALITY", "MARISALAN"),
    ("RODEN / DATE OF BIRTH", "09 OCT 1988"),
    ("MJESTO RODENJA / PLACE OF BIRTH", "PORT SALIN"),
    ("SPOL / SEX", "M"),
    ("IZDANO / DATE OF ISSUE", "22 JAN 2024"),
    ("VRIJEDI DO / DATE OF EXPIRY", "22 JAN 2034"),
    ("TIJELO / AUTHORITY", "SALT OFFICE, PORT SALIN"),
]
fy = 224
for label, val in fields:
    text(FX, fy, label, SANS(8), fill=GREY_TXT)
    text(FX, fy + 12, val, SANS_B(14), fill=INK)
    fy += 40
    if label.startswith("TIJELO"):
        fy -= 6

# signature (nudged down after first render so it clears the authority field)
sy = 732
text(LX0 + 30, sy, "Tomas Ren Havel", SERIF_I(24), fill=(30, 44, 92))
d.line([(LX0 + 30, sy + 34), (LX0 + 250, sy + 34)], fill=INK_SOFT, width=1)
text(LX0 + 30, sy + 40, "POTPIS / HOLDER'S SIGNATURE", SANS(8), fill=GREY_TXT)

# ---------- MRZ (ICAO 9303, weights 7-3-1) ----------
def cd(s):
    vals = {c: i for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    vals["<"] = 0
    w = [7, 3, 1]
    return str(sum(vals.get(c, 0) * w[i % 3] for i, c in enumerate(s)) % 10)

line1 = ("P<MSLHAVEL<<TOMAS<REN" + "<" * 44)[:44]
pno = "MSL007314"
dob, exp = "881009", "340122"
personal = "<" * 14
line2 = pno + cd(pno) + "MSL" + dob + cd(dob) + "M" + exp + cd(exp) + personal + cd(personal)
line2 += cd(line2[:10] + line2[13:20] + line2[21:43])
assert len(line1) == 44 and len(line2) == 44, (line1, line2)

MX0, MY0, MX1, MY1 = LX0 + 26, 812, LX1 - 26, 916
d.rectangle([MX0, MY0, MX1, MY1], fill=(240, 234, 216), outline=INK_SOFT, width=1)
text(MX0 + 14, MY0 + 18, line1, MONO(15), fill=(30, 34, 40))
text(MX0 + 14, MY0 + 52, line2, MONO(15), fill=(30, 34, 40))
text(LX0 + 28, 952, "2", SERIF(13), fill=GREY_TXT)

# faint watermark emblem, left page (kept clear of the data fields)
wx, wy = LX0 + 112, 560
d.ellipse([wx - 52, wy - 52, wx + 52, wy + 52], outline=(238, 232, 214), width=2)
d.polygon([(wx, wy - 26), (wx + 17, wy - 3), (wx, wy + 20), (wx - 17, wy - 3)], outline=(238, 232, 214), width=2)

# ---------- right page ----------
text(RX0 + 26, 52, "VIZE / VISAS", SERIF_B(24))
text(RX1 - 26, 58, "12", SERIF(13), fill=GREY_TXT, anchor="ra")
d.line([(RX0 + 26, 92), (RX1 - 26, 92)], fill=INK, width=2)
text(RX0 + 26, 102, "ENTRY AND EXIT STAMPS — TRAVEL HISTORY", SANS(9), fill=GREY_TXT)

stamps = [
    ("MARISAL", "DEPARTURE", "PORT SALIN", "03 MAR 2024", RED, -3, "rect"),
    ("BRANNOVIA", "ARRIVAL", "OST KAI", "05 MAR 2024", BLUE, 2, "rect"),
    ("BRANNOVIA", "DEPARTURE", "OST KAI", "19 MAR 2024", BLUE, -2, "rect"),
    ("MARISAL", "ARRIVAL", "PORT SALIN", "21 MAR 2024", RED, 3, "rect"),
    ("MARISAL", "DEPARTURE", "PORT SALIN", "08 SEP 2024", RED, 2, "oval"),
    ("KELDARA", "ARRIVAL", "LUMEN QUAY", "10 SEP 2024", TEAL, -3, "oval"),
    ("KELDARA", "DEPARTURE", "LUMEN QUAY", "24 SEP 2024", TEAL, 2, "oval"),
    ("MARISAL", "ARRIVAL", "PORT SALIN", "26 SEP 2024", RED, -2, "oval"),
]

def stamp(x, y, w, h, country, kind, port, date, color, angle, shape):
    s = Image.new("RGBA", (w + 8, h + 8), (0, 0, 0, 0))
    sd = ImageDraw.Draw(s)
    if shape == "oval":
        sd.ellipse([3, 3, w + 4, h + 4], outline=color + (255,), width=3)
        sd.ellipse([8, 8, w - 1, h - 1], outline=color + (255,), width=1)
    else:
        sd.rounded_rectangle([3, 3, w + 4, h + 4], radius=10, outline=color + (255,), width=3)
        sd.rounded_rectangle([8, 8, w - 1, h - 1], radius=7, outline=color + (255,), width=1)
    f1, f2, f3 = SANS_B(14), SANS(9), SANS_B(12)
    cxx = (w + 8) // 2
    sd.text((cxx, 16), country, font=f1, fill=color + (255,), anchor="ma")
    sd.text((cxx, 36), kind, font=f2, fill=color + (255,), anchor="ma")
    sd.text((cxx, 49), port, font=f2, fill=color + (255,), anchor="ma")
    sd.text((cxx, 64), date, font=f3, fill=color + (255,), anchor="ma")
    s = s.rotate(angle, expand=True, resample=Image.BICUBIC)
    img.paste(s, (x, y), s)

SW, SH = 196, 92
pos = [(RX0 + 30, 132), (RX0 + 244, 130), (RX0 + 30, 242), (RX0 + 244, 244),
       (RX0 + 30, 352), (RX0 + 244, 350), (RX0 + 30, 462), (RX0 + 244, 464)]
for (c, k, p, dt, col, ang, sh), (x, y) in zip(stamps, pos):
    stamp(x, y, SW, SH, c, k, p, dt, col, ang, sh)

# conditions box
BX0, BY0, BX1, BY1 = RX0 + 26, 592, RX1 - 26, 806
d.rectangle([BX0, BY0, BX1, BY0 + 32], fill=INK)
text(BX0 + 14, BY0 + 7, "CONDITIONS OF ISSUE", SANS_B(14), fill=(247, 242, 228))
d.rectangle([BX0, BY0, BX1, BY1], outline=INK, width=2)
lines = [
    "Valid for travel on salt barges and harbour ferries.",
    "The bearer must surrender this passport to the Salt",
    "Office during the spring brine harvest (April - May)",
    "for the seasonal stamp. Not valid for overland travel",
    "beyond the Tide Wall without a marsh permit.",
]
ly = BY0 + 46
for ln in lines:
    text(BX0 + 14, ly, ln, SERIF(13.5), fill=(52, 58, 72))
    ly += 21
text(BX0 + 14, ly + 6, "No. 007314  ·  Fee paid at issue", SANS(9), fill=GREY_TXT)

# fee stamp (circle, overlapping box corner)
fs = Image.new("RGBA", (150, 150), (0, 0, 0, 0))
fd = ImageDraw.Draw(fs)
fd.ellipse([4, 4, 146, 146], outline=RED + (255,), width=3)
fd.ellipse([12, 12, 138, 138], outline=RED + (255,), width=1)
fd.text((75, 42), "SALT TAX", font=SANS_B(15), fill=RED + (255,), anchor="ma")
fd.text((75, 64), "PAID", font=SANS_B(17), fill=RED + (255,), anchor="ma")
fd.text((75, 90), "9 MAR", font=SANS_B(15), fill=RED + (255,), anchor="ma")
fs = fs.rotate(-12, expand=True, resample=Image.BICUBIC)
img.paste(fs, (BX1 - 138, BY1 - 92), fs)

text(RX0 + 26, 838, "This passport remains the property of the Republic of Marisal.", SERIF_I(12), fill=GREY_TXT)
text(RX0 + 26, 858, "If found, please return to any Marisalan consulate or salt office.", SERIF_I(12), fill=GREY_TXT)

os.makedirs("/output", exist_ok=True)
img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT}: {os.path.getsize(OUT)} bytes, {img.size}")
