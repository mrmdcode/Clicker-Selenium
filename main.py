from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json
import time


driver = webdriver.Firefox()
driver.get("http://localhost:8000/login")

start_time = time.time()
f =open("data.json")
data = json.load(f)

for i in data:
    print(i)
    # input text
    if i["type"] == "start":
        driver = webdriver.Firefox()
        driver.get("http://localhost:8000/login")
    if i["type"] == "input_text":
        if i["NAME"] != "":
            element = driver.find_element(By.NAME, i["NAME"])
            element.send_keys(i["value"])
        elif i["XPATH"] != "":
            element = driver.find_element(By.XPATH, i["XPATH"])
            element.send_keys(i["value"])
        else:
            print("Id Is Empty")
    #         input prompt
    if i["type"] == "input_prompt":
        if i["NAME"] != "":
            element = driver.find_element(By.NAME, i["NAME"])
            element.send_keys(input("value : "))
        elif i["XPATH"] != "":
            element = driver.find_element(By.XPATH, i["XPATH"])
            element.send_keys(input("value : "))
        else:
            print("Id Is Empty")




    # input select
    if i["type"] == "input_select":
        if i["NAME"] != "":
            element = Select(driver.find_element(By.NAME, i["NAME"]))
            if i["index"] != "":
                print(i["index"])
                element.select_by_index(i["index"])
            elif i["value"] != "":
                element.select_by_visible_text(i["value"])
            else:
                print("value and index all Empty")
        elif i["XPATH"] != "":
            element = Select(driver.find_element(By.XPATH, i["XPATH"]))
            if i["index"] != "":
                element.select_by_index(i["index"])
            elif i["value"] != "":
                element.select_by_visible_text(i["value"])
            else:
                print("value and index all Empty")
        else:
            print("Id Is Empty")

    #         click
    if i["type"] == "click":
        if i["NAME"] != "":
            element = driver.find_element(By.NAME, i["NAME"])
            element.click()
        elif i["XPATH"] != "":
            element = driver.find_element(By.XPATH, i["XPATH"])
            element.click()
        else:
            print("Id Is Empty")
#     exit


end_time = time.time()
total_time = end_time - start_time
print("proccess time is : ", total_time)

