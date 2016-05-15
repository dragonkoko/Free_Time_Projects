import time
import win32api, win32con
from pymouse import PyMouse

shrineFlag = 0
m = PyMouse()

def clickLeft(x,y):
    m.click(x, y, 1)
    time.sleep(.1)

def reconnect():
    time.sleep(.2)
    clickLeft(1035, 142)
    time.sleep(.2)
    clickLeft(685, 469)
    time.sleep(.3)
    clickLeft(685, 469)

def quickBattle():
    clickLeft(264, 70)
    time.sleep(.4)

def startGame():
    clickLeft(662, 372)
    time.sleep(.2)
    clickLeft(533, 487)
    time.sleep(.15)
    clickLeft(645, 574)
    time.sleep(.3)

def keepHand():
    clickLeft(811, 510)
    time.sleep(2)

def playShrine():
    global shrineFlag
    clickLeft(862, 693)
    time.sleep(.2)
    if(shrineFlag == 0):
        clickLeft(896, 651)
        shrineFlag = 1
    else:
        shrineFlag = 0
        clickLeft(918, 682)
    time.sleep(.2)
    clickLeft(602, 460)

def endTurn():
	time.sleep(.3)
	clickLeft(1329, 403)
	time.sleep(.3)
	clickLeft(1329, 403)

def closeReward():
    time.sleep(.3)
    clickLeft(685, 636)

def attack():
    time.sleep(.3)
    clickLeft(1292, 271)

def playCards():
    time.sleep(.3)
    for i in range(0, 11):
        clickLeft(490+(25*i), 670)

def fieldPress():
    time.sleep(.3)
    for i in range(0, 10):
        clickLeft(500+(35*i), 330)
    time.sleep(.1)
    clickLeft(680, 539)

def closeGraveyard():
    time.sleep(.2)
    clickLeft(680, 500)

def closeCreature():
    time.sleep(.2)
    clickLeft(684, 540)

def main():
    time.sleep(10)
    while(1):
        quickBattle()
        reconnect()
        startGame()
        keepHand()
        closeGraveyard()
        closeCreature()
        fieldPress()
        playShrine()
        playCards()
        attack()
        endTurn()
        closeReward()


if __name__ == '__main__':
    main()
