import time
import win32api, win32con
from pymouse import PyMouse

m = PyMouse()

def clickLeft(x,y):
    m.click(x, y, 1)
    time.sleep(.1)
	
def pickCasual():
	clickLeft(630, 500)
	time.sleep(.3)

def pickDeck():
	clickLeft(390, 505)
	time.sleep(.3)

def startGame():
	pickCasual()
	pickDeck()

def keepHand():
    clickLeft(680, 720)
    time.sleep(2)

def endTurn():
	clickLeft(1075, 370)
	time.sleep(.3)
	clickLeft(1055, 335)
	time.sleep(.3)

def closeReward():
	clickLeft(1140, 615)
	time.sleep(.3)

def playCards():
	for i in range(0, 8):
		clickLeft(645, 670)
		time.sleep(.1)

def main():
    time.sleep(10)
    while(1):
		startGame()
		keepHand()
		playCards()
		endTurn()
		closeReward()

if __name__ == '__main__':
    main()
