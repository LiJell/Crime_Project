카카오맵 서울시 편의점 크롤링

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

def kakao_searching(word):
    url = 'https://map.kakao.com/?from=total&nil_suggest=btn&tab=place&q='+ word
    return url

url = kakao_searching('서울시 편의점')
driver.get(url)


html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')


addr = soup.select("div.addr")


next_page = driver.find_element(By.CSS_SELECTOR,"#info\.search\.page\.no2")
next_page.click()
next_btn = driver.find_element(By.CSS_SELECTOR, '#info\.search\.page\.next')
next_btn.click()
```

