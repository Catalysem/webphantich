import json
import datetime
import yfinance as yf

today = datetime.date.today().isoformat()

data = {
    "updated_at": today,
    "stocks": {
        "VNINDEX": []
    }
}

df = yf.download("^VNINDEX", period="10d")
df.reset_index(inplace=True)

for _, row in df.iterrows():
    data["stocks"]["VNINDEX"].append({
        "date": row["Date"].strftime("%Y-%m-%d"),
        "close": round(float(row["Close"]), 2)
    })

with open("data/stock_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Updated:", today)
