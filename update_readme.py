import whale_calculator
import matplotlib.pyplot as plt
import requests

SPEND_CHARD_NAME = "spend_chart.png"

def get_exchange_rate():
    try:
        response = requests.get("https://api.frankfurter.app/latest?from=USD&to=EUR")
        if response.status_code == 200:
            return response.json()["rates"]["EUR"]
    except:
        pass
    return 0.92

eur_rate = get_exchange_rate()

def format_row(name, usd_value, total_usd):
    percent = (usd_value / total_usd) * 100
    eur_value = usd_value * eur_rate
    return f"| {name} | {eur_value:.2f} EUR | {usd_value:.2f} USD | {percent:.1f}% |"

def generate_pie_chart(data):
    categories = ['Characters', 'Weapons', 'Resin Refill', 'Welkin', 'BattlePass', 'BP Levels', 'skins']
    values = [
        data["Characters"]["spend"],
        data["Weapons"]["spend"],
        data["resin_refill"]["spend"],
        data["Welkin_Moon"]["spend"],
        data["BP"]["spend"],
        data["BP_LV_UP"]["spend"],
        data["skin"]["spend"],
    ]

    total = sum(values)
    legend_labels = [f'{l}: {v/total*100:1.1f}%' for l, v in zip(categories, values)] 
                # char       # wnp        #resin      #welkin     # BP        # BP lvs      #skin    
    colors = ['#ff9999',"#ffd966","#99f1ff","#99acff","#ffc965","#eeff6b","#e597ff"]

    fig, ax = plt.subplots(figsize=(14, 8), facecolor='none')

    wedges, _ = ax.pie(
        values, 
        colors=colors, 
        startangle=140, 
        pctdistance=0.95,
        labeldistance=1.1
    )

    ax.legend(
        wedges, 
        legend_labels,
        title="Categories",
        title_fontsize=21,
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        
        fontsize=19,
        frameon=False,
    )

    ax.set_title('Genshin Impact Whale Spend Distribution', pad=15, size=24)

    plt.savefig('spend_chart.png', bbox_inches='tight', transparent=False, facecolor="white")
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



markdown = f"""
# Genshin Impact - Whale Calculator
This is a calculator that estimates how much a Genshin Impact whale can spend in the game.

To remove randomness and make the result deterministic, the calculator assumes worst-case luck:
- 180 pulls per 5★ character (guaranteed after losing the 50/50)
- 80 pulls per 5★ weapon

**Note:** 
For characters, losing the 50/50 is required to reach the deterministic cost.
For weapons, the model assumes a guaranteed limited 5★ weapon within the pity cycle and does not simulate additional losses.

**!!!** 
The result represents a theoretical maximum and deterministic cost, not an average or realistic outcome.

## Pie Spend Distribution

![Whale Chart]({SPEND_CHARD_NAME})

## Table Spend Distribution
| Type | Spend (EUR) | Spend (USD) | Share |
| :--- | :--- | :--- | :--- |
{format_row("All C6 characters", data["Characters"]["spend"], data["total_spend"])}
{format_row("All R5 weapons", data["Weapons"]["spend"], data["total_spend"])}
{format_row("Welkin Moon", data["Welkin_Moon"]["spend"], data["total_spend"])}
{format_row("Battle Pass", data["BP"]["spend"], data["total_spend"])}
{format_row("Battle Pass Level Up", data["BP_LV_UP"]["spend"], data["total_spend"])}
{format_row("Resin Refill", data["resin_refill"]["spend"], data["total_spend"])}
{format_row("All skins", data["skin"]["spend"], data["total_spend"])}
| |
| **Total** | **{data["total_spend"] * eur_rate:.2f} EUR** | **{data["total_spend"]:.2f} USD** | **100%** |
"""

write_readme(markdown)
