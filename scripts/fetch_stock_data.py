import json
import datetime
import urllib.request

today = datetime.date.today().isoformat()

# Danh sách mã đang hiển thị trong Dashboard V3
SYMBOLS = ["VNINDEX", "VCB", "VIC", "HPG"]

SOURCE_URL = "https://raw.githubusercontent.com/financedataorg/stock-data/main/vietnam.json"

with urllib.request.urlopen(SOURCE_URL) as response:
    raw = response.read().decode("utf-8")
    source_data = json.loads(raw)

stocks = []
for s in source_data:
    if s["symbol"] in SYMBOLS:
        stocks.append({
            "symbol": s["symbol"],
            "close": s["close"],
            "change": s.get("change", 0)
        })

data = {
    "updated_at": today,
    "stocks": stocks
}

with open("data/market_summary.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ Market summary updated:", today)
