def get_calendar(cfg):
    if not cfg["calendar"]["enabled"]:
        return ["Kalender deaktiviert"]

    # iCloud CalDAV optional später aktivierbar
    return [
        "10:00 Termin",
        "14:00 Meeting",
        "18:00 Einkauf"
    ]