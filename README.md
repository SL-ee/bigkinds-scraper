# bigkinds-scraper
빅카인즈(https://www.bigkinds.or.kr/)를 긁는 Python 코드입니다.

<br/>

### 준비
+ selenium을 설치해야 사용할 수 있습니다.
```python
!pip install selenium
```

+ Chrome 버전에 맞는 Chromedriver가 필요합니다.   
<a href="chrome://settings/help">Chrome 버전 확인</a>: chrome://settings/help       
<a href="https://chromedriver.chromium.org/downloads">Chromedriver 설치</a>       

<br/>

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

+ 언론사 선택   
파일을 다운 받을 때 파일명에 언론사가 포함되지 않아서 언론사별로 돌릴 수 있게 코드에서 직접 입력하게 만들었습니다.
```python
# 전국일간지
# 1 경향신문 2 국민일보 3 내일신문 4 동아일보 5 문화일보 6 서울신문 7 세계일보 8 조선일보 9 중앙일보 10 한겨레 11 한국일보
browser.find_element_by_xpath("//*[@id='category_provider_list']/li[7]/span/label").click()
```   

+ 날짜 단위 선택   
두 달 단위, 한 달 단위를 이용할 경우 2월은 윤년 확인이 필요합니다.
```python
# 분기 단위
date_list = {'1분기': ['01-01', '03-31'], '2분기': ['04-01', '06-30'], '3분기': ['07-01', '09-30'], '4분기': ['10-01', '12-31']}
# 두 달 단위
date_list = {'1-2': ['01-01', '02-28'], '3-4': ['03-01', '04-30'], '5-6': ['05-01', '06-30'], '7-8': ['07-01', '08-31'], '9-10': ['09-01', '10-31'], '11-12': ['11-01', '12-31']}
# 한 달 단위
date_list = {'1월': ['01-01', '01-31'], '2월': ['02-01', '02-28'], '3월': ['03-01', '03-31'], '4월': ['04-01', '04-30'], '5월': ['05-01', '05-31'], '6월': ['06-01', '06-30'], '7월': ['07-01', '07-31'], '8월': ['08-01', '08-31'], '9월': ['09-01', '09-30'], '10월': ['10-01', '10-31'], '11월': ['11-01', '11-30'], '12월': ['12-01', '12-31']}
```   

<br/>
### 주의사항   
데이터 행이 20,000건이 넘어가면 20,000건까지만 다운받아집니다.   
이로 인한 데이터 누락을 방지하기 위해 검색 수를 출력하고 있으니 확인하고 날짜 단위를 변경하는 등의 방법을 이용해 20,000건 이하로 조절해주세요.
