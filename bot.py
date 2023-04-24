from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from decouple import config 
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def fun(gmailID,password,content,driver, prog):
    driver.get('https://www.facebook.com/')
    user = driver.find_element_by_id('email')
    user.send_keys(gmailID)
    pass_enter = driver.find_element_by_id("pass")
    time.sleep(1)
    pass_enter.send_keys(password)
    pass_enter.send_keys(Keys.RETURN)
    time.sleep(5)
    fb_link = 'https://www.facebook.com/groups/'

    groups=[
        'writersnbloggers',
        '3007072836045135/?multi_permalinks=3756398127779265',
        '1416082568571443/?multi_permalinks=1755977424581954',
        'writersofmedium',
    ]
    
    prog_groups = [
        '821441531297615',
        'pypcom/',
        'includehelp/',
        'dsawidccplus/',
        '328341355260726/',
        '356919327808418/?hoisted_section_header_type=recently_seen&multi_permalinks=2069315549902112'
    ]

    if prog:
        groups+=prog_groups

    for group_id in groups:

        driver.get(fb_link+group_id)
        time.sleep(6)
        driver.execute_script("scrollBy(0,-800);")
        
        try:
            driver.find_element_by_xpath('//*[contains(text(),"Write something")]').click()
        except:
            driver.find_element_by_xpath('//*[contains(text(),"Create a public post")]').click()

            
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[role="dialog"] form[method="POST"]')))
        time.sleep(2)

        driver.switch_to.active_element.send_keys(content)
        time.sleep(4)
        driver.find_element_by_xpath("//*[@aria-label='Post']").click()
        time.sleep(6)
    
    driver.close()


if __name__=="__main__":
    
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-logging')
    options.add_argument("--disable-notifications");
    options.add_argument('--headless')
    prog=True
    link = 'https://github.com/The-Nightwing/fb-groupwall-poster-bot-Selenium-.git'
    driver = webdriver.Chrome(os.path.join(BASE_DIR,'chromedriver.exe'), options=options) 
    fun(config('userID',default=''),config('password',default=''),link+"\n"+'Drop your links too <3',driver, prog)


