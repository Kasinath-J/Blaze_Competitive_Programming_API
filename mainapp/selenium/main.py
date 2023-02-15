
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service
    # from selenium.webdriver.chrome.options import Options
    # from selenium.webdriver.common.by import By
    # from time import sleep
    # import requests
    # from bs4 import BeautifulSoup
    # import chromedriver_binary

    # # from webdriver_manager.chrome import ChromeDriverManager

    # chrome_options = Options()
    # chrome_options.add_experimental_option("detach",True)
    # # chrome_options.add_argument("--headless")
    # # chrome_options.add_argument("--window-size=1920x1080")


    # serv_obj = Service("backend\selenium_test\chromedriver.exe")
    # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    # # driver = webdriver.Chrome(service=serv_obj,options=chrome_options)
    # driver = webdriver.Chrome(service=serv_obj)
    # sleep(5)
    # driver.get("https://www.linkedin.com/in/panchumarthi-abhinav/")
    # sleep(5)
    # cookies_dict = {}
    # for cookie in driver.get_cookies():
    #     cookies_dict[cookie['name']] = cookie['value']

    # driver.close()
    # sleep(5)

    # resp = requests.get("https://www.linkedin.com/in/panchumarthi-abhinav/?trk=public-profile-join-page",
    # cookies=cookies_dict,
    # headers={
    #     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    #     'accept':'application/vnd.linkedin.normalized+json+2.1',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'en-US,en;q=0.6',
    #     'upgrade-insecure-requests':'1',
    #     'scheme': 'https',
    # })

    # html_doc = resp.text
    # # soup = BeautifulSoup(html_doc, 'html.parser')
    # # print(soup.find_all('ul',class_="experience__list"))

    # page_fun = open("dele.html",'w',encoding='utf-8')
    # page_fun.write(html_doc)
    # page_fun.close()
    # # modal__dismiss = driver.find_elements(By.CLASS_NAME,"modal__dismiss")
    # # print(modal__dismiss)
    # # modal__dismiss[0].click()

    # # driver.close()


    # # import requests
    # # from time import sleep
    # # from selenium import webdriver
    # # # import chromedriver

    # # driver = webdriver.Chrome()
    # # sleep(5)
    # # driver.maximize_window()
    # # sleep(5)
    # # driver.get("www.linkedin.com/")
    # # sleep(5)

