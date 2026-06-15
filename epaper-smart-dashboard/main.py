import yaml
from modules.fronius import get_fronius
from modules.weather import get_weather
from modules.calendar import get_calendar
from modules.display import render_display

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    cfg = load_config()

    fronius = get_fronius(cfg["fronius"]["ip"])
    weather = get_weather(cfg["location"]["lat"], cfg["location"]["lon"], cfg)
    calendar = get_calendar(cfg)

    img = render_display(cfg, fronius, weather, calendar)

    img.save("debug.png")

    # === ePaper Output ===
    # from waveshare_epd import epd10in85
    # epd = epd10in85.EPD()
    # epd.init()
    # epd.display(epd.getbuffer(img))
    # epd.sleep()

if __name__ == "__main__":
    main()