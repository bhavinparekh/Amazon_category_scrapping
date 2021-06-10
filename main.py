import re
import time

import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from fake_useragent import UserAgent
import csv

chromedriver_autoinstaller.install()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("user-agent=%s" % UserAgent().random)

#PROXY = "socks5://0.0.0.0:9050"
#chrome_options.add_argument('--proxy-server=%s' % PROXY)
df = pd.read_csv('keys.csv')

result = []
count = 5100
err = 0
for key in df['Terme de recherche'][5100:]:
    if err > 1000:
        break
    print('row=%s' % count)
    count += 1
    try:
        import random, time


        with webdriver.Chrome(executable_path="chromedriver", options=chrome_options) as driver:
            driver.implicitly_wait(100)
            number_list = ["https://www.amazon.fr/s?k=" + key,
                           "https://www.amazon.fr/s?k=" + key + '&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss',
                           "https://www.amazon.fr/s?k=" + key + '&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1',
                           "https://www.amazon.fr/s?k=" + key + '&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2',
                           "https://www.amazon.fr/s?k=" + key + '&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_3',
                           "https://www.amazon.fr/s?k=" + key + '&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_4', ]
            # random item from list
            driver.get(random.choice(number_list))

            product1 = driver.find_element(By.XPATH, "//div[@data-cel-widget='search_result_1']")
            soup = BeautifulSoup(driver.page_source, "html.parser")
            ul = soup.find('ul', attrs={"aria-labelledby": "n-title"})
            tmp = []
            counter = 0
            for li in ul.findAll('li', attrs={"id": re.compile('^n/')}):
                counter += 1
                if len(li.get('class')) == 1:
                    if len(tmp) != 0:
                        with open('searchResult.csv', 'a') as f:
                            writer = csv.writer(f)
                            writer.writerow([key, tmp[0]])
                            if len(tmp) > 1:
                                l1 = tmp[0]
                                for l2 in tmp[1:]:
                                    writer = csv.writer(f)
                                    writer.writerow([key, l1 + '|' + l2])
                                    print(key, 'L1:' + l1, ' L2:' + l2)

                        tmp.clear()
                    tmp.append(li.text.strip())
                else:
                    tmp.append(li.text.strip())
                if counter == 9:
                    break
    except Exception as e:
        err += 1
        print(e, '\nerr no:', err)
        with open('error_key.txt', 'a') as f:
            f.write(key + '\n')
        time.sleep(60 * 8)
