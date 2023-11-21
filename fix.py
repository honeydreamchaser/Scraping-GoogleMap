import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

chromedriver_path = './'
driver = webdriver.Chrome()

url = "https://www.google.com/maps/place/Coppice+Gate+-+Retirement+Living+-+McCarthy+Stone/@50.8522267,-1.4182785,17z/data=!3m1!4b1!4m6!3m5!1s0x487477422e7f89f1:0xc41eef697b284b6c!8m2!3d50.8522233!4d-1.4157036!16s%2Fg%2F11b7tqkcz5?entry=ttu"
# driver.maximize_window()
driver.get(url)
name_list = []
with open('test_fix.txt', 'r') as result_file:
    addr_list = result_file.readlines()
result_fix_file = open('result_fix.txt', 'w')

search_box = driver.find_element(by=By.ID, value='searchboxinput')
search_button = driver.find_element(by=By.ID, value='searchbox-searchbutton')
action = ActionChains(driver)

for i in range(3, len(addr_list), 2):
    fixed_name = ''

    if addr_list[i] == '\n':
        fixed_name = addr_list[i-1]
    elif addr_list[i] == addr_list[i-2]:
        fixed_name = addr_list[i-1]
    
    if fixed_name != '':
        search_box.clear()
        time.sleep(1)
        search_box.send_keys(fixed_name)
        time.sleep(10)

        try:
            search_results = driver.find_element(by=By.CLASS_NAME, value='hfpxzc')
        except NoSuchElementException:
            print("NoSuchElementException")
        else:
            try:
                search_results = driver.find_element(by=By.CLASS_NAME, value='hfpxzc')
            except StaleElementReferenceException:
                print("StaleElementReferenceException")
            else:
                print(search_results)
                time.sleep(1)
                search_results.click()
                time.sleep(10)
        
        address_data = []
        try:
            address_data = driver.find_elements(by=By.CLASS_NAME, value='Io6YTe')
        except NoSuchElementException:
            print("NoSuchElementException")
        else:
            try:
                address_data = driver.find_elements(by=By.CLASS_NAME, value='Io6YTe')
            except StaleElementReferenceException:
                print("StaleElementReferenceException")
            else:
                time.sleep(1)
                addr_data = ''
                j = 0
                for j in range(len(address_data)-1):
                    addr_data += ('\t' + address_data[j].text)
                addr_list[i] = addr_data + '\n'
                print(addr_list[i-1] + ' fixed:' + addr_list[i])
    result_fix_file.write(addr_list[i-1] + addr_list[i])

result_fix_file.close()
time.sleep(5)

driver.quit()