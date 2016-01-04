import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

file = open('christmas_2015.txt', 'r')
decklists = file.read()
main_decks = []

for i in range(1,8):
    main_deck = decklists.split("Side Deck:")[i].split("Main Deck:")[0]
    main_deck = main_deck.split("\n")
    for card in main_deck:
        main_decks.append(card)


main_decks_analysis = dict()
for card in main_decks:
    try:
        number_of_cards = int(card.split("x")[0])
        card_name = card.split("\n")[0]
        card_name = card_name[3:]
        if card_name in main_decks_analysis:
            main_decks_analysis[card_name] += number_of_cards
        else:
            main_decks_analysis[card_name] = number_of_cards
    except:
        continue

labels = sorted(main_decks_analysis, key=main_decks_analysis.__getitem__, reverse=True)
sizes = sorted(main_decks_analysis.values(), reverse=True)
print labels
print sizes
top_cards = 7
cs=cm.Set1(np.arange(top_cards)/20.)
gaben ,patches, texts = plt.pie(sizes[:top_cards], labels=labels[:top_cards], autopct=make_autopct(sizes[:top_cards]), colors=cs, startangle=90, shadow=True)
plt.title('Yu-Gi-Oh Christmas Tournament 2015\nMost played cards in Side Deck')
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()
plt.show()
