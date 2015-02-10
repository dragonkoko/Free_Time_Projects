import Tkinter
from Tkinter import*
from random import randint
import Image, ImageTk

top = Tkinter.Tk()
top.title("Yu-Gi-Oh Hand Tester")
top.wm_iconbitmap('tester.ico')
top.resizable(width=FALSE, height=FALSE)
top.geometry('{}x{}'.format(900, 300))

def randomHand():
   rand_ints = [999, 999, 999, 999, 999]
   x = 0
   y = 40
   deck_size
   for i in range (0, 5):
      flag = 0
      while flag != 1:
         rand_card = randint(0, deck_size)
         if rand_card in rand_ints:
            flag = 0
         else:
            flag = 1
            rand_ints[i] = rand_card
            label = Label(image=deck[rand_card])
            label.place(x=x, y=y)
            x += 180

def newDeck():
   deck_name = e.get()
   ydk = open("deck/%s.ydk" % deck_name, "r")
   ydk = ydk.read()
   card_bar_code = ydk.split("\n")
   i = 1
   i2 = -1
   flag = 0
   global deck_size
   while (flag == 0):
       try:
           i += 1
           i2 += 1
           leng = len(card_bar_code[i])
           if card_bar_code[i] == "#extra\n":
               flag = 1
           else:
               if card_bar_code[i] != "70368879":
                 image = Image.open('pics/%s.jpg' % card_bar_code[i])
                 deck[i2] = ImageTk.PhotoImage(image)
               else:
                  i2 -= 1
                  
       except:
           flag = 1
   deck_size = i2 - 1
   
e = Entry(top)
e.place(x=20, y=8)
e.delete(0, END)
e.insert(20, "name of the deck")
deck = [i for i in range(80)]
deck_size = 0
NewHand = Tkinter.Button(top, text ="New Hand", command = randomHand, bg="grey")
NewHand.place(x=420, y=8)
UpdateDeck = Tkinter.Button(top, text ="Update Deck", command = newDeck, bg="grey")
UpdateDeck.place(x=150, y=5)
top.mainloop()
