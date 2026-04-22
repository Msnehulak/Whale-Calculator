import whale_calculator
import matplotlib.pyplot as plt

SPEND_CHARD_NAME = "spend_chart.png"

def generate_pie_chart(data):
    categories = ['Characters', 'Weapons', 'Welkin', 'BattlePass', 'BP Levels', 'Resin Refill']
    values = [
        data["Characters"]["spend"],
        data["Weapons"]["spend"],
        data["Welkin_Moon"]["spend"],
        data["BP"]["spend"],
        data["BP_LV_UP"]["spend"],
        data["resin_refill"]["spend"]
    ]

    total = sum(values)
    legend_labels = [f'{l}: {v/total*100:1.1f}%' for l, v in zip(categories, values)]

    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

    fig, ax = plt.subplots(figsize=(14, 8), facecolor='none')

    wedges, _ = ax.pie(
        values, 
        colors=colors, 
        startangle=140, 
        pctdistance=0.85,
        labeldistance=1.1
    )

    ax.legend(
        wedges, 
        legend_labels,
        title="Spending Categories",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=12,
        frameon=True,
    )

    ax.set_title('Genshin Impact Whale Spend Distribution', pad=20, size=16, color='white')

    plt.savefig('spend_chart.png', transparent=True, bbox_inches='tight')
    plt.close()

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

# pie charct gen
generate_pie_chart(data)



markdown = f"""# Genshin Impact - Whale Calculator
This is a Calculator what is a maximu for GI whale spend on game with worst luck. 

## Spend Distribution

![Whale Chart]({SPEND_CHARD_NAME})

"""

"""

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