import pyautogui as pyA
import time
import re
import cv2
from twilio.rest import Client

#make sure all programs are minimized and that valorant is in a small window, not full screen ON EVERY SINGLE ACCOUNT
#use gui automation to take 3 screenshots of skins on rotation

def logIn(username, password):
    print("starting in 5 seconds")
    time.sleep(5)
    pic3 = pyA.locateOnScreen('Images/valicon.PNG', confidence = 0.85)
    if pic3 != None:
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        #time.sleep(1)
        pyA.moveTo(pic3X, pic3Y)
        #time.sleep(1)
        pyA.click(pic3X, pic3Y)
        pyA.click(pic3X, pic3Y)
    else:
        print("send text: valicon not found, exiting program.")
        return
    
    time.sleep(10)
    pic3 = pyA.locateOnScreen('Images/confirmedOpen.PNG', confidence = 0.95)
    if pic3 == None:
        print("send text: val did not open up after icon clicked")
        return

    
    pyA.typewrite(username)
    time.sleep(3)
    pyA.hotkey("tab")
    pyA.typewrite(password)
    pyA.hotkey("enter")

    time.sleep(3)
    pic3 = pyA.locateOnScreen('Images/bigPlay.PNG', confidence = 0.95)
    if pic3 != None:
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        #time.sleep(1)
        pyA.moveTo(pic3X, pic3Y)
        #time.sleep(1)
        pyA.click(pic3X, pic3Y)

        


def checkSkins():
    time.sleep(30) #20
    #pyA.hotkey('alt', 'enter')
    time.sleep(5)
    pic3 = pyA.locateOnScreen('Images/iUnderstand.PNG', confidence = 0.55) #might be too low
    if pic3 != None:
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        time.sleep(1)
        pyA.moveTo(pic3X, pic3Y)
        time.sleep(1)
        pyA.click(pic3X, pic3Y)
        print("i understand found and clicked")
        time.sleep(1)
        pyA.moveTo(0,0)
        time.sleep(1)
        pyA.moveTo(pic3X, pic3Y)
        time.sleep(1)
        pyA.click(pic3X, pic3Y)
     

    time.sleep(2)
    pic3 = pyA.locateOnScreen('Images/store.PNG', confidence = 0.95)
    if pic3 != None:
        pic3 = pyA.center(pic3)
        pic3X, pic3Y = pic3
        #time.sleep(1)
        pyA.moveTo(pic3X, pic3Y)
        #time.sleep(1)
        pyA.click(pic3X, pic3Y)
    
    time.sleep(2)
    pyA.hotkey("win", "prtsc")
    time.sleep(2)
    pyA.hotkey("alt", "f4")



logIn("EddieTGH12", "sexyboi123321123")
checkSkins()
time.sleep(5)
logIn("flawlessduettt", "edgoo1212")
checkSkins()
time.sleep(5)
logIn("cypherismydaddy", "edgoo1212")
checkSkins()
time.sleep(5)