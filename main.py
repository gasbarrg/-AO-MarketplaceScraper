import sys
import pytesseract
import pyscreenshot
import pyautogui
import time
import pandas as pd
import keyboard

path = "C:\\Users\\Gasba\\Documents\\@Personal Files\\AlbionMarketBot\\res"  # TODO Fix
pathFolder = "C:\\Users\\Gasba\\Documents\\@Personal Files\\AlbionMarketBot"
col1 = "Item"
col2 = "Avg Price FS: "
col3 = "Cheapest: "


# Globals
cycle=True
i=0
actualPrices = []
cheapestPrices = []

# Possible menu Selections
menus=["1", "2", "3", "4", "5", "6", "9"]
menuList=["1 - Hammers", "2 - Holy Staff", "3 - Cloth Armor", "4 - Spears", "5 - Plate Helmets", "6 - ALL"]

# "Adept's", "Expert's", " Master's", "Grandmaster's", "Elder's"

items = ["empty"],\
        ["Adept's Ancient Hammer Head", "Expert's Ancient Hammer Head", "Master's Ancient Hammer Head",
         "Grandmaster's Ancient Hammer Head", "Elder's Ancient Hammer Head",
         "Adept's Hellish Hammer Heads ", "Expert's Hellish Hammer Heads ", " Master's Hellish Hammer Heads ",
         "Grandmaster's Hellish Hammer Heads ", "Elder's Hellish Hammer Heads ",
         "Adept's Massive Metallic Hand", "Expert's Massive Metallic Hand", " Master's Massive Metallic Hand",
         "Grandmaster's Massive Metallic Hand", "Elder's Massive Metallic Hand",
         "Adept's Engraved Log", "Expert's Engraved Log", " Master's Engraved Log",
         "Grandmaster's Engraved Log", "Elder's Engraved Log"],\
         ["Adept's Messianic Curio", "Expert's Messianic Curio", " Master's Messianic Curio",
         "Grandmaster's Messianic Curio", "Elder's Messianic Curio",
         "Adept's Ghastly Scroll ", "Expert's Ghastly Scroll ", " Master's Ghastly Scroll ",
         "Grandmaster's Ghastly Scroll ", "Elder's Ghastly Scroll ",
         "Adept's Infernal Scroll", "Expert's Infernal Scroll", " Master's Infernal Scroll",
         "Grandmaster's Infernal Scroll", "Elder's Infernal Scroll",
         "Adept's Possessed Scroll", "Expert's Possessed Scroll", " Master's Possessed Scroll",
         "Grandmaster's Possessed Scroll", "Elder's Possessed Scroll"],\
         ["Adept's Alluring Amulet", "Expert's Alluring Amulet", " Master's Alluring Amulet",
         "Grandmaster's Alluring Amulet", "Elder's Alluring Amulet",
         "Adept's Druidic Feathers", "Expert's Druidic Feathers", " Master's Druidic Feathers",
         "Grandmaster's Druidic Feathers", "Elder's Druidic Feathers",
         "Adept's Infernal Cloth Folds", "Expert's Infernal Cloth Folds", " Master's Infernal Cloth Folds",
         "Grandmaster's Infernal Cloth Folds", "Elder's Infernal Cloth Folds",
         "Adept's Sanctified Belt", "Expert's Sanctified Belt", " Master's Sanctified Belt",
         "Grandmaster's Sanctified Belt", "Elder's Sanctified Belt"],\
         ["Adept's Keeper Spearhead", "Expert's Keeper Spearhead", " Master's Keeper Spearhead",
         "Grandmaster's Keeper Spearhead", "Elder's Keeper Spearhead",
         "Adept's Ruined Ancestral Vamplate", "Expert's Ruined Ancestral Vamplate", " Master's Ruined Ancestral Vamplate",
         "Grandmaster's Ruined Ancestral Vamplate", "Elder's Ruined Ancestral Vamplate",
         "Adept's Infernal Harpoon Tip", "Expert's Infernal Harpoon Tip", " Master's Infernal Harpoon Tip",
         "Grandmaster's Infernal Harpoon Tip", "Elder's Infernal Harpoon Tip",
         "Adept's Cursed Barbs", "Expert's Cursed Barbs", " Master's Cursed Barbs",
         "Grandmaster's Cursed Barbs", "Elder's Cursed Barbs"]\

prices = []
pricesCheapest = []
currPrice = 0

def getScreenshot():
    sc = pyscreenshot.grab(bbox=(1839, 745, 1909, 782,))
    sc.save(path + r'\data1.png')

def getScreenshotCheapest():
    sc = pyscreenshot.grab(bbox=(1411, 379, 1579, 420,))
    sc.save(path + r'\data1.png')

def getData():
    img = cv2.imread('res\\data1.png')
    text = pytesseract.image_to_string(img)
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.strip("\n")
    # Add price to list
    if text == '':
        text = "ERROR"
    if text.__contains__("k"):
        text=text.replace("k", "000")
    if text.__contains__("m"):
        text=text.replace("m", "000000")
    if text.__contains__("average"):
        text = "NO AVG"
    if text != "ERROR" and text != "NO AVG":
        try:
            text = int(text)
        except ValueError:
            text = "VALUE ERROR!"

    print(text)
    return text




def searchItem():
    i = 0
    j = 1
    while j < len(items):
        while i < len(items[j]):
            # Move to search bar and click
            pyautogui.moveTo(860, 200)
            pyautogui.mouseDown(); time.sleep(.05)
            pyautogui.mouseUp(); time.sleep(.05)
            # Search Item
            pyautogui.write(items[j][i]); time.sleep(.35)
            # Get cheapest item:
            getScreenshotCheapest()
            pricesCheapest.append(getData())
            # Select first tiem
            pyautogui.moveTo(1664,402)
            pyautogui.click(); time.sleep(.05)
            # Get price
            getScreenshot()
            prices.append(getData())
            # Move to "X" and click to exit buy menu
            pyautogui.moveTo(1243, 252);
            pyautogui.mouseDown(); time.sleep(.05)
            pyautogui.mouseUp(); time.sleep(.05)
            i += 1
        j += 1
        i = 0
    global cycle
    cycle = False


def searchCheapest(set, item):
    # Move to search bar and click
    pyautogui.moveTo(860, 200);
    pyautogui.mouseDown(); time.sleep(.05)
    pyautogui.mouseUp(); time.sleep(.05)
    # Search Item
    pyautogui.write(items[set][item]); time.sleep(.35)
    # Move to "X" and click to exit buy menu
    pyautogui.moveTo(1243, 252)
    pyautogui.mouseDown()
    time.sleep(.05)
    pyautogui.mouseUp()
    time.sleep(.05)


def cycleMenu():
    # Initialize Globals
    global cycle, i
    # Wait for menu select
    print("Please Select a Menu 1 - 6")
    for string in menuList:
        print("\t" + string)
    select=keyboard.read_key()

    # Set loop
    cycle=True;
    i=0
    while not (select in menus):
        select=keyboard.read_key()  # Wait for correct menu select
    # Print Menu:
    if select in menus:
        print("Selected Menu " + str(select) + ":")
        cycleItems(int(select))


def cycleItems(menu):
    global cycle, i
    j=1
    while cycle:
        if menu == 6:
            if i >= len(items[j]):
                j+=1
                i=0
            if j == len(items):
                cycle=False
                return

            keyboard.wait("-")  # Wait for user
            print(items[j][i] + ":\t\t\tACTUAL = " + str(actualPrices[(j - 1) * 20+ i]) +
                  ":\tCHEAPEST = " + str(cheapestPrices[(j - 1) * 20+ i]))
            searchCheapest(j, i)
            i += 1

        elif menu == 9:
            # SAVE ALL ITEMS
            searchItem()
            data=pd.DataFrame({col2: prices, col3: pricesCheapest})
            data.to_excel('Output.xlsx', sheet_name='sheet1', index=False)


        else:
            if i >= len(items[menu]):
                cycle=False  # Break from list when end of array
                return
            keyboard.wait("-")  # Wait for user
            print(items[menu][i] + ":\t\t\tACTUAL = " + str(actualPrices[(menu - 1) * 20 + i]) +
                  ":\t\tCHEAPEST = " + str(cheapestPrices[(menu - 1) * 20 + i]))
            searchCheapest(menu, i)
            i+=1



def readFileData():
    global actualPrices, cheapestPrices
    data = pd.read_excel(pathFolder + '\\Output.xlsx')
    df1 = pd.DataFrame(data, columns=[col2]).to_numpy()
    df2 = pd.DataFrame(data, columns=[col3]).to_numpy()
    actualPrices = df1
    cheapestPrices = df2

    # TODO: Return price for specific item.

if __name__ == '__main__':
    readFileData()
    while True:
        cycleMenu()
