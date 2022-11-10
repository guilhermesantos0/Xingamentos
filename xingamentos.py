import time
import pyautogui as pg

words = []
sentMessages = 0

with open('palavras.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        words.append(i)

time.sleep(3)   

for i in words:
    pg.write(f"{i}")
    pg.press("enter")
    sentMessages += 1