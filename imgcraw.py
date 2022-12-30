from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request

options = webdriver.ChromeOptions()   
options.add_experimental_option("excludeSwitches", ["enable-logging"])   #오류대비 설정
driver = webdriver.Chrome(options=options)

word = str(input("검색어: "))#검색어 입력
driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")#구글(이미지) 검색 사이트
driver.maximize_window()#웹브라우저 창 화면 최대화
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input.gLFyf").send_keys(word) #키워드 입력
driver.find_element(By.CSS_SELECTOR, "input.gLFyf").send_keys(Keys.RETURN)

list = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")#이미지를 리스트로 불러옴

i = 0

address = "(주소 입력)" #파일을 저장할 주소
for img in list:
    i += 1
    try:

        imgurl = img.get_attribute("src") #img src 태그 탐색
        time.sleep(1)
        urllib.request.urlretrieve(imgurl,address+"/"+str(word)+str(i)+".jpg") # 폴더에 이미지 저장 urlretrieve(이미지 링크, 저장할 폴더 위치 & 이름)

        if i > 9:
            break #10개까지 제한

    except: #예외처리 : 저장불가 -> 패스
        print("저장 불가로 인해 다음으로 넘어감")
        pass
