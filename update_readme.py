import whale_calculator

def write_readme(markdown):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(markdown)

wc = whale_calculator.whalecalculator()
data = wc.get_row_data()

# float update
for key, value in data.items():
    if isinstance(value, dict) and "spend" in value:
        data[key]["spend"] = float(value["spend"])

data["total_spend"] = float(data["total_spend"])

markdown = f"""# Genshin Impact - Whale Calculator
This is a Calculator what is a maximu for GI whale spend on game with worst luck. 

## Total Spend
all C6 characters   {data["Characters"]["spend"]:.2f} usd

all R5 weapons      {data["Weapons"]["spend"]:.2f} usd

Welkin Moon         {data["Welkin_Moon"]["spend"]:.2f} usd

Battle Pass         {data["BP"]["spend"]:.2f} usd

Battle Pass levl up {data["BP_LV_UP"]["spend"]:.2f} usd

Refil Resin         {data["resin_refill"]["spend"]:.2f} usd

---

total               {data["total_spend"]:.2f} usd
"""

write_readme(markdown)