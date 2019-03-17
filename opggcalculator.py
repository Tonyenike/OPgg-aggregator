import sys
sys.path.append('./')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

verbose_mode = False

names = []

specified = False
limited = False
region = "na"
limitnum = 10
for opts in range(len(sys.argv)):
    if sys.argv[opts] == "--verbose":
        verbose_mode = True
    if sys.argv[opts] == "-u":
        specified = True
        names.append(sys.argv[opts + 1])
    if sys.argv[opts] == "-r":
        region = sys.argv[opts + 1]
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



for j in range(len(names)):
   driver = webdriver.Chrome(chrome_options=chrome_options, executable_path = './chromedriver')
   print("Loading information for user: " + names[j])
   driver.get('https://" + region + ".op.gg/summoner/userName=' + names[j])

   time.sleep(5)
    
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

        time.sleep(3)

   buttons = driver.find_elements_by_class_name('MatchDetail')
   yote = driver.find_elements_by_class_name('GameType')
   realstuff = driver.find_element_by_class_name('RealContent')
   if verbose_mode:
        print("Found " + str(len(yote)) + " games in total")
   total = 0
   totalscore = 0
   for i in range(len(yote)):
      yeet = yote[i].get_attribute('innerHTML')
      bol = "Flex 5:5 Rank" in yeet
      if bol:
         if verbose_mode:
                print("Ranked Flex 5v5 game " + str(total + 1) + ":")
         actions = webdriver.ActionChains(driver)
         time.sleep(1)
         actions.move_to_element(buttons[i]).click().perform()
         time.sleep(1)
         getName = realstuff.find_elements_by_css_selector('td.SummonerName.Cell')
         getScores = driver.find_elements_by_css_selector('div.OPScore.Text')
         for h in range(10):
            username = getName[total*10 + h].find_element_by_tag_name('a').get_attribute('innerHTML')
            if verbose_mode:
                print(username + " " + getScores[total*10 + h].get_attribute('innerHTML'))
            if names[j] in username:
                 totalscore = totalscore + float(getScores[total*10 + h].get_attribute('innerHTML'))
         total = total + 1
         if verbose_mode:
            print("")
         if limited and limitnum == total:
            break;

   print("Found " + str(total) + " Flex 5:5 games")
   print("Aggregate OP.GG score: " + str(totalscore / total))
   print("")
   print("")

   driver.close()
