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
bigkinds.py를 이용하세요.   
+ 빅카인즈 아이디, 비밀번호 입력
```python
# 로그인
browser.find_element_by_xpath("//*[@id='header']/div[1]/div/div/button[1]").click()
time.sleep(0.3)
browser.find_element_by_id("login-user-id").send_keys("아이디 ")
browser.find_element_by_id("login-user-password").send_keys("비밀번호 입력")
browser.find_element_by_id("login-btn").click()
```
