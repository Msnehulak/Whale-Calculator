from datetime import date
import requests

class whalecalculator:
    def __init__(self):
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
        self.versin_released = self.days_from_releas // (7 * 6) 

        self.characters()
        self.weapons()
        self.welkin_moon()
        self.battle_pass()
        self.battle_pass_levl_up()
        self.daly_resin_refill()
        self.skins()

    def characters(self):
        self.char_standard5_list = ["Jean", "Diluc", "Qiqi", "Mona", "Keqing", "Tighnari", "Dehya", "Mizuki"]
        self.char_standard5_count = len(self.char_standard5_list) 
        self.char_limited5char_list = self.get_limited_character_count()
        self.char_limited5_count = len(self.char_limited5char_list)

        self.char_pulls_one_copy = 180
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
        self.BP_owned = self.versin_released
        self.BP_spend = self.BP_owned * self.prices["battle_pass"]
        
        self.total_spend += self.BP_spend

    def battle_pass_levl_up(self):
        self.BP_LV_UP_levels = 50
        self.BP_LV_UP_count = self.BP_owned * self.BP_LV_UP_levels
        self.BP_LV_UP_spend_primo = self.BP_LV_UP_count * self.primo["bplvup"]
        self.BP_LV_UP_spend = self.primo_to_usd(self.BP_LV_UP_spend_primo)

        self.total_spend += self.BP_LV_UP_spend 

    def daly_resin_refill(self):
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
        url = "https://genshin-db-api.vercel.app/api/characters?query=5&matchCategories=true"
        response = requests.get(url)
        
        if response.status_code == 200:
            characters = list(response.json())
        else:
            print("error, API don't work, using hard code list")
            characters = ['Aether', 'Albedo', 'Alhaitham', 'Aloy', 'Arataki Itto', 'Arlecchino', 'Baizhu', 'Chasca', 'Chiori', 'Citlali', 'Clorinde', 'Columbina', 'Cyno', 'Dehya', 'Diluc', 'Durin', 'Emilie', 'Escoffier', 'Eula', 'Flins', 'Furina', 'Ganyu', 'Hu Tao', 'Ineffa', 'Jean', 'Kaedehara Kazuha', 'Kamisato Ayaka', 'Kamisato Ayato', 'Keqing', 'Kinich', 'Klee', 'Lauma', 'Linnea', 'Lumine', 'Lyney', 'Manekin', 'Manekina', 'Mavuika', 'Mona', 'Mualani', 'Nahida', 'Navia', 'Nefer', 'Neuvillette', 'Nilou', 'Qiqi', 'Raiden Shogun', 'Sangonomiya Kokomi', 'Shenhe', 'Sigewinne', 'Skirk', 'Tartaglia', 'Tighnari', 'Varesa', 'Varka', 'Venti', 'Wanderer', 'Wriothesley', 'Xianyun', 'Xiao', 'Xilonen', 'Yae Miko', 'Yelan', 'Yoimiya', 'Yumemizuki Mizuki', 'Zhongli', 'Zibai']
            
            # Filter standard 5*
        limited5char = []
        for char in characters:
            if char in self.char_standard5_list:
                pass
            else:
                limited5char.append(char)
        return limited5char

    def primo_to_usd(self, primo):
        """
        Take primo and transfer it in to usd base.
        I use avrige of all bundles becose i wont maximum acurate primo to usd.
        """
        bundles = self.prices["crystal"]

        costs_per_crystal = []
        for crys, price in bundles:
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