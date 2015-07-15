import requests

def get_price(card_name, quantity):
    try:
        url = "http://www.mtgotraders.com/store/advanced-search.php?name=" + card_name + "&minprice=&maxprice=&instock=on&sortby=price&sorting=asc&x=70&y=13&artist=&text=&cost=&type=&cardname=&powtgh=&setname="
        scraped_page = requests.get(url).text
        take_price = scraped_page.split("Card Results")[1].split(card_name)[1].split("<td class=\"price\">$")[1].split("</td>")[0]
        price_all = float(take_price)*quantity
        return price_all
    except:
        try:
            take_price = scraped_page.split("Card Results")[1].split(card_name)[5].split("<td class=\"price\">$")[1].split("</td>")[0]
            price_all = float(take_price)*quantity
            return price_all
        except:
            print card_name+" failed to check price!"
            return 0.00

def get_deck(file_name):
    deck_file = open(file_name, "r")
    deck_file = deck_file.read()
    cards = deck_file.split("\n")
    return cards

def main():
    print "gaben"
    cards = get_deck("rancor.txt")
    print cards
    cost = 0.00
    exclude_list = ["Creature (", "Instant (", "Artifact (", "Land (", " Cards", "Enchantment (", "Sorcery (", "Planeswalker ("]
    for card in cards:
        if not any(s in card for s in exclude_list):
            card_name = card[2:]
            card_quantity = card[0]
            print card_name+" quantity: "+card_quantity
            price = get_price(card_name, int(card_quantity))
            print price
            cost += price
    print cost

if __name__ == "__main__":
    main()
