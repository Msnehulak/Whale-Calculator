from datetime import date
import requests
import math

AVRIGE_FOR_LIMITED_5 = 93
USE_AIP = False

class whalecalculator:
    def __init__(self):
        self.char_limited5_list = ['aether', 'albedo', 'alhaitham', 'aloy', 'arataki itto', 'arlecchino', 'baizhu', 'chasca', 'chiori', 'citlali', 'clorinde', 'columbina', 'cyno', 'dehya', 'diluc', 'durin', 'emilie', 'escoffier', 'eula', 'flins', 'furina', 'ganyu', 'hu tao', 'ineffa', 'jean', 'kaedehara kazuha', 'kamisato ayaka', 'kamisato ayato', 'keqing', 'kinich', 'klee', 'lauma', 'linnea', 'lumine', 'lyney', 'manekin', 'manekina', 'mavuika', 'mona', 'mualani', 'nahida', 'navia', 'nefer', 'neuvillette', 'nilou', 'qiqi', 'raiden shogun', 'sangonomiya kokomi', 'shenhe', 'sigewinne', 'skirk', 'tartaglia', 'tighnari', 'varesa', 'varka', 'venti', 'wanderer', 'wriothesley', 'xianyun', 'xiao', 'xilonen', 'yae miko', 'yelan', 'yoimiya', 'yumemizuki mizuki', 'zhongli', 'zibai']
        self.char_standard5_list = ["Jean", "Diluc", "Qiqi", "Mona", "Keqing", "Tighnari", "Dehya", "Mizuki"]
        self.prices = {
            "welkin": 4.99,
            "battle_pass": 9.99,
            "crystal": [
                [60, 0.99],
                [300, 4.99],
                [980, 14.99],
                [1980, 29.99],
                [3280, 49.99],
                [6480, 99.99]
            ]
        }
        self.primo = {
            "bplvup": 150,
            "refil_resin": [50, 100, 100, 150, 200, 200],
            "pull": 160
        }
        self.total_spend = 0

        self.release_date = date(2020, 9, 28)
        self.today_date = date.today()
        self.days_from_releas = self.today_date - self.release_date
        self.days_from_releas = self.days_from_releas.days
        self.version_released = self.days_from_releas // (7 * 6) 

        self.characters()
        self.weapons()
        self.welkin_moon()
        self.battle_pass()
        self.battle_pass_level_up()
        self.daily_resin_refill()
        self.skins()

    def characters(self):
        
        self.char_standard5_count = len(self.char_standard5_list) 
        self.char_limited5char_list = self.get_limited_character_count()
        self.char_limited5_count = len(self.char_limited5char_list)

        self.char_pulls_one_copy = AVRIGE_FOR_LIMITED_5
        self.char_pulls_C6 = self.char_pulls_one_copy * 7
        self.char_total_pulls = self.char_pulls_C6 * self.char_limited5_count
        self.char_total_primo = self.char_total_pulls * self.primo["pull"]
        self.char_spend = self.primo_to_usd(self.char_total_primo)

        self.total_spend += self.char_spend
   
           

    def weapons(self):
        self.wpn_count = self.char_limited5_count
        self.wpn_pulls_one_copy = 80
        self.wpn_pulls_R5 = self.wpn_pulls_one_copy * 5
        self.wpn_total_pulls = self.wpn_pulls_R5 * self.wpn_count
        self.wpn_total_primo = self.wpn_total_pulls * self.primo["pull"]
        self.wpn_spend = self.primo_to_usd(self.wpn_total_primo)

        self.total_spend += self.wpn_spend

    def welkin_moon(self):
        self.welkin_moon_owned = self.days_from_releas // 30 
        self.welkin_moon_spend = self.welkin_moon_owned * self.prices["welkin"]
        
        self.total_spend += self.welkin_moon_spend

    def battle_pass(self):
        self.BP_owned = self.version_released
        self.BP_spend = self.BP_owned * self.prices["battle_pass"]
        
        self.total_spend += self.BP_spend

    def battle_pass_level_up(self):
        self.BP_LV_UP_levels = 50
        self.BP_LV_UP_count = self.BP_owned * self.BP_LV_UP_levels
        self.BP_LV_UP_spend_primo = self.BP_LV_UP_count * self.primo["bplvup"]
        self.BP_LV_UP_spend = self.primo_to_usd(self.BP_LV_UP_spend_primo)

        self.total_spend += self.BP_LV_UP_spend 

    def daily_resin_refill(self):
        self.resin_refill_dayli_refil = sum(self.primo["refil_resin"])
        self.resin_refil_spend_primo = self.resin_refill_dayli_refil * self.days_from_releas
        self.resin_refil_spend = self.primo_to_usd(self.resin_refil_spend_primo)

        self.total_spend += self.resin_refil_spend

    def skins(self):
        self.skin_list = [
            1680, # Sea Breeze Dandelion - Jean
            1680, # Summertime Sparkle - Barbara
            1680, # Opulent Splendor - Keqing
            1680, # Orchid's Evening Gown - Ningguang
            2480, # Red Dead of Night - Diluc
            1680, # Ein Immernachtstraum - Fischl
            1680, # Springbloom Missive - Ayaka
            1680, # A Sobriquet Under Shade - Lisa
            1680, # Blossoming Starlight - Klee
            1680, # Sailwind Shadow - Kaeya
            1680, # Frostflower Dew - Ganyu
            1680, # Twilight Blossom - Shenhe
            1680, # Bamboo Rain - Xingqiu
            1680, # Breeze of Sabaa - Nilou
            1680, # Phantom in Boots - Kirara
        ]
        self.skin_total_primo = sum(self.skin_list)
        self.skin_spend = self.primo_to_usd(self.skin_total_primo)

        self.total_spend += self.skin_spend

    def get_limited_character_count(self):
            # requests
        if USE_AIP:
            url = "https://genshin-db-api.vercel.app/api/characters?query=5&matchCategories=true"
            response = requests.get(url)
        

            if response.status_code == 200:
                characters = list(response.json())
            else:
                print("error, API don't work, using hard code list")
                characters = self.char_standard5_list
        else:
            characters = self.char_limited5_list

            # Filter standard 5*
        limited5char = []
        for char in characters:
            if char in self.char_standard5_list:
                pass
            else:
                limited5char.append(char)
        return limited5char
    
    def primo_to_usd(self, primo, use_largest_bundle_only=True):
        """
        Convert primogems to USD.
        use_largest_bundle_only = True  → whale buys only 6480 packs
        use_largest_bundle_only = False → uses average across all packs
        """
        if use_largest_bundle_only:
            crys, price = self.prices["crystal"][5]
            return math.ceil(primo / crys) * price
        else:
            costs_per_crystal = []
                
            for crys, price in self.prices["crystal"]:
                costs_per_crystal.append(price / crys)
            
            average_cost_per_crystal = sum(costs_per_crystal) / len(costs_per_crystal)

            return round(primo * average_cost_per_crystal, 2)
            

    def get_row_data(self):
        return {
            "Characters": {
                "spend": self.char_spend
            },
            "Weapons": {
                "spend": self.wpn_spend
            },
            "Welkin_Moon": {
                "spend": self.welkin_moon_spend
            },
            "BP": {
                "spend": self.BP_spend
            },
            "BP_LV_UP": {
                "spend": self.BP_LV_UP_spend
            },
            "resin_refill": {
                "spend": self.resin_refil_spend   
            },
            "skin": {
                "spend": self.skin_spend
            },
            "total_spend": self.total_spend
        }

    def main(self):
        print(f"""
{"="*40}
            Total Spend
all C6 characters   {self.char_spend:.2f} usd
all R5 weapons      {self.wpn_spend:.2f} usd 
Welkin Moon         {self.welkin_moon_spend:.2f} usd
Battle Pass         {self.BP_spend:.2f} usd
Battle Pass levl up {self.BP_LV_UP_spend:.2f} usd
Refil Resin         {self.resin_refil_spend:.2f} usd
Skins               {self.skin_spend:.2f} usd

total               {self.total_spend:.2f} usd
{"="*40}
""")


if __name__ == "__main__":    
    wc = whalecalculator()
    wc.main()
