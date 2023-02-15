
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup
# import chromedriver_binary

# from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")


serv_obj = Service("mainapp\selenium\chromedriver.exe")

def linkedin_scratch(profile):

    connectionCount=0
    
    try:
        # driver = webdriver.Chrome(service=serv_obj)
        driver = webdriver.Chrome(service=serv_obj,options=chrome_options)
        driver.get("https://www.linkedin.com/company/linkedin/")
        sleep(5)
        cookies_dict = {}
        for cookie in driver.get_cookies():
            cookies_dict[cookie['name']] = cookie['value']

        driver.close()
        resp = requests.get("https://www.linkedin.com/in/{}/?trk=public-profile-join-page".format(profile),
        cookies=cookies_dict,
        headers={
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
            'accept':'application/vnd.linkedin.normalized+json+2.1',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.6',
            'upgrade-insecure-requests':'1',
            'scheme': 'https',
        })

        html_doc = resp.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        connectionCount = int(soup.find_all('span',class_="top-card__subline-item")[-1].text.split(" ")[0])
        # print(connectionCount)

    except:
        pass

    ret = {}
    ret['img_url'] = None
    ret['aboutus'] = None	
    ret['headline'] = None
    ret['geoLocationName'] = None
    ret['experience'] = []
    ret['education'] = []
    ret['certifications'] = []
    ret['projects'] = []
    ret['honors'] = []
    ret['publications'] = []
    ret['skills'] = []
    ret['connectionsCount'] = connectionCount

    return ret

# print(linkedin_scratch("raj-kumar-837b151ba"))