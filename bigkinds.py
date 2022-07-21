from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# selenium
browser = webdriver.Chrome("D:/SLee/pythonProject/chromedriver")

browser.set_window_size(1800,1000)
url = "https://www.bigkinds.or.kr/"
browser.get(url)

# 로그인
browser.find_element_by_xpath("//*[@id='header']/div[1]/div/div/button[1]").click()
time.sleep(0.3)
browser.find_element_by_id("login-user-id").send_keys("아이디 입력")
browser.find_element_by_id("login-user-password").send_keys("비밀번호 입력")
browser.find_element_by_id("login-btn").click()
time.sleep(0.3)
browser.find_element_by_xpath("//*[@id='header']/div[2]/div[2]/div[1]/div/div[1]/div/ul/li[1]").click()
browser.find_element_by_xpath("//*[@id='header']/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/ul/li[1]/a").click()
# 전국일간지
# 1 경향신문 2 국민일보 3 내일신문 4 동아일보 5 문화일보 6 서울신문 7 세계일보 8 조선일보 9 중앙일보 10 한겨레 11 한국일보
browser.find_element_by_xpath("//*[@id='category_provider_list']/li[7]/span/label").click()

# year_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
year_list = ['2020']
# 분기 단위
date_list = {'1분기': ['01-01', '03-31'], '2분기': ['04-01', '06-30'], '3분기': ['07-01', '09-30'], '4분기': ['10-01', '12-31']}
# 두 달 단위
# date_list = {'1-2': ['01-01', '02-28'], '3-4': ['03-01', '04-30'], '5-6': ['05-01', '06-30'], '7-8': ['07-01', '08-31'], '9-10': ['09-01', '10-31'], '11-12': ['11-01', '12-31']}
# date_list = {'5-6': ['05-01', '06-30'], '7-8': ['07-01', '08-31'], '9-10': ['09-01', '10-31'], '11-12': ['11-01', '12-31']}
# 한 달 단위
# date_list = {'1월': ['01-01', '01-31'], '2월': ['02-01', '02-28'], '3월': ['03-01', '03-31'], '4월': ['04-01', '04-30'], '5월': ['05-01', '05-31'], '6월': ['06-01', '06-30'],
#              '7월': ['07-01', '07-31'], '8월': ['08-01', '08-31'], '9월': ['09-01', '09-30'], '10월': ['10-01', '10-31'], '11월': ['11-01', '11-30'], '12월': ['12-01', '12-31']}

browser.find_element_by_xpath("//*[@id='collapse-step-1-body']/div[3]/div/div[1]/div[1]/a").click()
time.sleep(0.1)

# 날짜 지정
for year in year_list:
    for date in date_list:
        begin = year + "-" + date_list[date][0]
        end = year + "-" + date_list[date][1]

        begin_date = browser.find_element_by_id("search-begin-date")
        begin_date.send_keys(Keys.CONTROL + "a")
        begin_date.send_keys(begin)
        end_date = browser.find_element_by_id("search-end-date")
        end_date.send_keys(Keys.CONTROL + "a")
        end_date.send_keys(end)
        browser.find_element_by_xpath("//*[@id='search-foot-div']/div[2]/button[2]").send_keys(Keys.ENTER)

        time.sleep(1)
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='news-results-tab']/div[2]/h3/span[6]")))
        # 페이지 확인
        soup = BeautifulSoup(browser.page_source, "lxml")
        output = soup.find("div", attrs={"class": "data-result-hd"})
        how_many_news = output.find("h3").find("span", attrs={"class": "total-news-cnt"})
        print(begin, " ", end, " ", how_many_news)

        # 엑셀 다운로드
        element = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "collapse-step-3")))
        browser.find_element_by_id("collapse-step-3").click()
        time.sleep(0.3)
        element = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='analytics-data-download']/div[3]/button")))
        browser.find_element_by_xpath("//*[@id='analytics-data-download']/div[3]/button").send_keys(Keys.ENTER)
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present())
            alert = browser.switch_to_alert()
            alert.accept()
        except:
            print("no alert")
        time.sleep(30)

        element = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "collapse-step-1")))
        browser.find_element_by_id("collapse-step-1").send_keys(Keys.ENTER)
        time.sleep(0.3)
