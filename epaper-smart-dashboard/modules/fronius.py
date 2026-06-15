import requests

def get_fronius(ip):
    try:
        url = f"http://{ip}/solar_api/v1/GetPowerFlowRealtimeData.fcgi"
        r = requests.get(url, timeout=5)
        d = r.json()["Body"]["Data"]["Site"]

        return {
            "pv": round(d.get("P_PV", 0)),
            "load": round(d.get("P_Load", 0)),
            "grid": round(d.get("P_Grid", 0)),
            "autonomy": d.get("rel_Autonomy", 0)
        }

    except Exception as e:
        return {"error": str(e)}