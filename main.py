
'''
Made by github.com/sfmth

'''

import pyautogui, sys
import cv2
import numpy as np
from PIL import Image
import PIL.ImageOps
import pytesseract

def main():
    try:
        tx_l = []
        while(True):
            try:
                image = pyautogui.screenshot()
                # image.show()
                # print("cropping")
                cropped = image.crop((820, 410, 1090, 620))
                # print("inverting color")
                inv = PIL.ImageOps.invert(cropped)
                # print("showing image")
                # inv.show()
                # print("recognizing text")
                custom_config3 = r'--oem 3 --psm 6'
                # txt0 = pytesseract.image_to_string(inv, config=custom_config1)
                # print(txt0 + "\n------")
                # txt1 = pytesseract.image_to_string(inv, config=custom_config2)
                # print(txt1 + "\n------")
                txt2 = pytesseract.image_to_string(inv, config=custom_config3)
                # print(txt2 + "\n------")
                tx = txt2.strip()
                # print(tx)
                tx = tx.replace(" ", "")
                if tx == "":
                    pyautogui.click(x=971, y=971)
                tx = tx.replace("(", "1")
                tx = tx.replace("[", "1")
                tx = tx.replace("]", "1")
                tx = tx.replace(")", "1")
                tx = tx.replace("l", "1")
                tx = tx.replace("|", "1")
                tx = tx.replace("%"+"x", "x")
                tx_l.append(tx)
                tx = tx.split("\n")
                tx[1] = tx[1].replace("-", "=")
                if tx[0][0] == 0:
                    tx[0] = "1"+tx[0]
                if tx[1] == "=":
                    tx[1] = tx[1]+"1"
                # print(tx)
                if "-" in tx[0]:
                    eq = tx[0].split("-")
                    ans = int(eq[0]) - int(eq[1])
                elif "/" in tx[0]:
                    eq = tx[0].split("/")
                    ans = int(eq[0]) / int(eq[1])
                elif "+" in tx[0]:
                    eq = tx[0].split("+")
                    ans = int(eq[0]) + int(eq[1])
                elif "x" in tx[0]:
                    eq = tx[0].split("x")
                    ans = int(eq[0]) * int(eq[1])
                elif "x" in tx[0]:
                    eq = tx[0].split("x")
                    ans = int(eq[0]) * int(eq[1])
                elif "%" in tx[0]:
                    eq = tx[0].split("%")
                    ans = int(eq[0]) * int(eq[1])
                else:
                    print("unrecognized char:" + tx[0])
                if ans == int(tx[1].replace("=","")):
                    # print("\ntrue")
                    pyautogui.click(x=879, y=966)
                else:
                    # print("\nfalse")
                    pyautogui.click(x=1039, y=967)
                
            except Exception:
                pass
            pyautogui.click(x=1039, y=850)
            now = len(tx_l)
            if tx_l[now-1] == tx_l[now-2]:
                print("\n......\nloop detected\n......\n")
                pyautogui.click(x=879, y=966)
    except KeyboardInterrupt:
        print('\n')






# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

if __name__ == '__main__':
    main()
    
    
