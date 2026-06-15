from PIL import Image, ImageDraw, ImageFont
import datetime

W = 1360
H = 480

def render_display(cfg, f, w, c):

    img = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(img)

    col = W // 3

    # ================= LEFT =================
    d.text((20, 10), "⚡ ENERGIE", fill=0)

    if "error" not in f:
        d.text((20, 60), f"PV: {f['pv']} W", fill=0)
        d.text((20, 100), f"Load: {f['load']} W", fill=0)
        d.text((20, 140), f"Grid: {f['grid']} W", fill=0)
        d.text((20, 180), f"Autarkie: {f['autonomy']}%", fill=0)

    # ================= MIDDLE =================
    now = datetime.datetime.now()

    d.text((col + 20, 10), "🕒 ZEIT", fill=0)
    d.text((col + 20, 60), now.strftime("%H:%M"), fill=0)
    d.text((col + 20, 100), now.strftime("%A %d.%m.%Y"), fill=0)

    d.text((col + 20, 160), "📅 HEUTE", fill=0)

    y = 200
    for e in c[:5]:
        d.text((col + 20, y), e, fill=0)
        y += 30

    # ================= RIGHT =================
    x = col * 2 + 20

    d.text((x, 10), "🌤 WETTER", fill=0)

    if "error" not in w:
        d.text((x, 60), f"{w['temp']}°C", fill=0)
        d.text((x, 100), w["desc"], fill=0)

        d.text((x, 150), "4H FORECAST", fill=0)

        y = 190
        for fcast in w["forecast"]:
            d.text((x, y), f"{fcast['time']} {fcast['temp']}°", fill=0)
            y += 25

    # GRID LINES
    d.line((col, 0, col, H), fill=0)
    d.line((col*2, 0, col*2, H), fill=0)

    return img