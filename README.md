# bigkinds-scraper
빅카인즈(https://www.bigkinds.or.kr/)를 긁는 Python 코드입니다.

### 준비
+ selenium을 설치해야 사용할 수 있습니다.
```python
!pip install selenium
```

+ Chrome 버전에 맞는 Chromedriver가 필요합니다.   
<a href="chrome://settings/help">Chrome 버전 확인</a>: chrome://settings/help       
<a href="https://chromedriver.chromium.org/downloads">Chromedriver 설치</a>       

### 코드 사용
전체 코드는 bigkinds.py를 확인해주세요.   
+ 빅카인즈 아이디, 비밀번호 입력
```python
# 로그인
browser.find_element_by_xpath("//*[@id='header']/div[1]/div/div/button[1]").click()
time.sleep(0.3)
browser.find_element_by_id("login-user-id").send_keys("아이디 ")
browser.find_element_by_id("login-user-password").send_keys("비밀번호 입력")
browser.find_element_by_id("login-btn").click()
```

+ 날짜 단위 선택
```python
# 로그인
# 분기 단위
date_list = {'1분기': ['01-01', '03-31'], '2분기': ['04-01', '06-30'], '3분기': ['07-01', '09-30'], '4분기': ['10-01', '12-31']}
# 두 달 단위
# date_list = {'1-2': ['01-01', '02-28'], '3-4': ['03-01', '04-30'], '5-6': ['05-01', '06-30'], '7-8': ['07-01', '08-31'], '9-10': ['09-01', '10-31'], '11-12': ['11-01', '12-31']}
# date_list = {'5-6': ['05-01', '06-30'], '7-8': ['07-01', '08-31'], '9-10': ['09-01', '10-31'], '11-12': ['11-01', '12-31']}
# 한 달 단위
# date_list = {'1월': ['01-01', '01-31'], '2월': ['02-01', '02-28'], '3월': ['03-01', '03-31'], '4월': ['04-01', '04-30'], '5월': ['05-01', '05-31'], '6월': ['06-01', '06-30'],
#              '7월': ['07-01', '07-31'], '8월': ['08-01', '08-31'], '9월': ['09-01', '09-30'], '10월': ['10-01', '10-31'], '11월': ['11-01', '11-30'], '12월': ['12-01', '12-31']}
```
