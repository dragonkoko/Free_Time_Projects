import urllib2
from random import randint
import combo_counter

ydk = open("Regional_Rogue_3.ydk", "r")
ydk = ydk.read()
card_bar_code = ydk.split("\n")
print(card_bar_code)

combos = [i for i in range(150)]
consistency_check = combo_counter.combo_file("consistency_check.txt")
number_of_combos = combo_counter.count_combos(consistency_check)
combo_line = consistency_check.split("\n")
for i in range(0, number_of_combos):
    combos[i] = combo_line[i].split("$")
    print(combos[i])

deck = [i for i in range(80)]
i = 1
i2 = -1
flag = 0
while (flag == 0):
    try:
        i += 1
        i2 += 1
        leng = len(card_bar_code[i])
        while (leng < 8):
            card_bar_code[i] = ("0" + card_bar_code[i])
            leng = len(card_bar_code[i])
        if card_bar_code[i] == "#extra":
            flag = 1
        else:
            if card_bar_code[i] != "70368879":
                response = urllib2.urlopen("http://yugioh.wikia.com/wiki/%s" % card_bar_code[i])
                page_source = response.read()
                card_name_getting = page_source.split("cardtable-header", 1)
                card_name_getting = card_name_getting[0].split("</title>")
                card_name_getting = card_name_getting[0].split("<title>")
                card_name = card_name_getting[1].replace(" - Yu-Gi-Oh!", "")
                deck[i2] = card_name
    except:
        print("got an error")
        flag = 1

deck_copy = deck
deck_size = i2 - 1
combo_count = 0
combo_type = [i for i in range(100)]
for i in range(0, number_of_combos):
    combo_type[i] = 0;
    
hand = [i for i in range(5)]
for i3 in range(0,24):
    deck = list(deck_copy)
    print("\nhand %d\n" % i3)
    for i in range(0,5):
        while True:
            rand_card = randint(0,deck_size)
            if deck[rand_card] != "Gaben":
                print(deck[rand_card])
                hand[i] = deck[rand_card]
                deck[rand_card] = "Gaben"
                break
    combo = combo_counter.combo_check(hand, combos, number_of_combos)
    if combo > 0:
        combo_count += 1
        combo_type[combo] += 1
        print("Combo!")
        
        
print(combo_count)
for i in range(1, number_of_combos):
    print("Combo number: %d is drawn %d times" % (i, combo_type[i]))
