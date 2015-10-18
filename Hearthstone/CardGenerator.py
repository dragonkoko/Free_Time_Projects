#-*-coding:utf8;-*-
import json
import random

class CardGenerator:
    attack = None
    health = None
    effect = None
    name = []
    highest_mana = 0
    number_of_minions = 0
    name_words = 0

    def __init__(self):
        with open("alljson.json") as json_file: json_cards = json.load(json_file)
        card_num = 0
        for set_name in ['Basic', 'Classic', 'Curse of Naxxramas', 'Blackrock Mountain', 'Goblins vs Gnomes', 'The Grand Tournament']:
            try:
                i = 0
                while(1):
                    if(json_cards[set_name][i]['type'] in ["Enchantment", "Hero Power", "Hero"]):
                        i += 1
                        continue
                    else:
                        try:
                            if(json_cards[set_name][i]['collectible'] == True):
                                mana = json_cards[set_name][i]['cost']
                                if(mana > self.highest_mana):
                                    self.highest_mana = mana
                                if(json_cards[set_name][i]['type'] == "Minion"):
                                    self.number_of_minions += 1
                                i += 1
                        except:
                            i += 1
            except:
                continue
        self.attack = []
        self.health = []
        self.effect = []
        for i in range(0,self.highest_mana+1):
            self.health.append([])
            self.effect.append([])
            self.attack.append([])
        for set_name in ['Basic', 'Classic', 'Curse of Naxxramas', 'Blackrock Mountain', 'Goblins vs Gnomes', 'The Grand Tournament']:
            try:
                i = 0
                while(1):
                    if(json_cards[set_name][i]['type'] in ["Enchantment", "Hero Power", "Hero"]):
                        i += 1
                        continue
                    else:
                        try:
                            if(json_cards[set_name][i]['collectible'] == True):
                                mana = json_cards[set_name][i]['cost']
                                if(json_cards[set_name][i]['type'] == "Minion"):
                                    self.attack[mana].append(json_cards[set_name][i]['attack'])
                                    self.health[mana].append(json_cards[set_name][i]['health'])
                                    self.effect[mana].append(json_cards[set_name][i]['text'])
                                    name_of_minion = json_cards[set_name][i]['name'].split(' ')
                                    for j in range(0, len(name_of_minion)):
                                        self.name.append(name_of_minion[j])
                                i += 1
                        except:
                            i += 1
            except:
                continue

    def generate(self, mana):
        name_length = random.randint(2,3)
        minion_name = ''
        for i in range(0, name_length):
            minion_name = minion_name + random.choice(self.name) + ' '
        print minion_name
        print "health: " + str(random.choice(self.health[mana]))
        print "attack: " + str(random.choice(self.attack[mana]))
        print "effect: " + random.choice(self.effect[mana])
