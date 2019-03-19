#!/usr/bin/python

import sys
sys.path.append('./')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

verbose_mode = False
grouped_mode = False

names = []

specified = False
limited = False
region = "na"
mode = "Flex 5:5 Rank"
printable_mode = "Ranked Flex"
limitnum = 10
for opts in range(len(sys.argv)):
    if sys.argv[opts] == "--verbose":
        verbose_mode = True
    if sys.argv[opts] == "--grouped":
        grouped_mode = True
    if sys.argv[opts] == "-u":
        specified = True
        stringified = sys.argv[opts + 1]
        names.append(stringified.replace('_', ' '))
    if sys.argv[opts] == "-m":
        choice = sys.argv[opts + 1]
        if "flex" in choice.lower():
            mode = "Flex 5:5 Game"
            printable_mode = "Ranked Flex"
        elif "solo" in choice.lower():
            mode = "Ranked Solo"
            printable_mode = "Ranked Solo"
        elif "norm" in choice.lower():
            mode = "Normal"
            printable_mode = "Normal"
        elif "rank" in choice.lower():
            mode = "Rank"
            printable_mode = "Ranked"
    if sys.argv[opts] == "-r":
        region = sys.argv[opts + 1]
        if region == "kr":
            region = ""
    if sys.argv[opts] == "-l":
        limited = True
        limitnum = int(sys.argv[opts + 1])

if not specified:
    names = ["MAN OF INTELLECT", "Commandments", "LazerSquirrel", "MunichMonster", "Shmaul Cat"]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
path_to_extension = './3.41.0_0'
chrome_options.add_argument('load-extension=' + path_to_extension)
# chrome_options.binary_location = './google-chrome'

print('')
print('')

for j in range(len(names)):
   driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = './chromedriver')
   if verbose_mode:
        print("Loading information for user: " + names[j])
   driver.get('https://' + region + '.op.gg/summoner/userName=' + names[j])

   time.sleep(3)
    
   if verbose_mode:
        print("Page loaded.")
        print("Collecting games...") 

   goodbool = True
   while goodbool:
        try:
            getmaxgames = driver.find_element_by_class_name('GameMoreButton').find_element_by_tag_name('a')
            actions = webdriver.ActionChains(driver)
            actions.move_to_element(getmaxgames).click().perform()
        except:
            goodbool = False

        time.sleep(2)

   buttons = driver.find_elements_by_class_name('MatchDetail')
   yote = driver.find_elements_by_class_name('GameType')
   result_detail = driver.find_elements_by_class_name('GameResult')
   realstuff = driver.find_element_by_class_name('RealContent')
   if verbose_mode:
        print("Found " + str(len(yote)) + " games in total")
   total = 0
   totalscore = 0
   runningtotal = 0
   for i in range(len(yote)):
      yeet = yote[i].get_attribute('innerHTML')
      resultinfo = result_detail[i].get_attribute('innerHTML')
      bol = (mode in yeet) and (not ("Remake"  in resultinfo))
      if bol:
         actions = webdriver.ActionChains(driver)
         actions.move_to_element(buttons[i]).click().perform()
         time.sleep(1.5)
         getName = realstuff.find_elements_by_css_selector('td.SummonerName.Cell')
         getScores = driver.find_elements_by_css_selector('div.OPScore.Text')
         namestuff = []
         for hi in range(10):
            namestuff.append(getName[runningtotal * 10 + hi].find_element_by_tag_name('a').get_attribute('innerHTML'))
         namesG = [x.lower() for x in namestuff]
         othernames = [x.lower() for x in names]
         goodtogo = True
         if grouped_mode:
            if not set(othernames).issubset(namesG):
                goodtogo = False
         if goodtogo:
             if verbose_mode:
                print(printable_mode + " game " + str(total + 1) + ":")
             for h in range(10):
                username = getName[runningtotal*10 + h].find_element_by_tag_name('a').get_attribute('innerHTML')
                if verbose_mode:
                    print(username + " " + getScores[runningtotal*10 + h].get_attribute('innerHTML'))
                if names[j].lower() in username.lower():
                    names[j] = username
                    totalscore = totalscore + float(getScores[runningtotal*10 + h].get_attribute('innerHTML'))
             total = total + 1
             if verbose_mode:
                print("")
             if limited and limitnum == total:
                break;
         runningtotal = runningtotal + 1

   print(names[j] + " aggregate OP.GG score over " + str(total) + " " + printable_mode + " games: " + str(totalscore / total))
   if verbose_mode:
        print("")
        print("")

   driver.close()
