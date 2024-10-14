import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import random
import string
import undetected_chromedriver as uc
import os
import pyperclip
import time
from selenium.webdriver.common.keys import Keys
import pyautogui


# Function to open, refresh and copy tempmail
def tempmail_copy_email(user_agent):

    uc_options = webdriver.ChromeOptions()
    uc_options.add_argument(f'user-agent={user_agent}')
    uc_options.add_argument('--disable-blink-features=AutomationControlled')
    uc_options.add_argument('--disable-popup-blocking')
    uc_options.add_argument('--start-maximized')
    uc_options.add_argument('--disable-extensions')
    uc_options.add_argument('--no-sandbox')
    uc_options.add_argument('--disable-dev-shm-usage')

    uc_driver = uc.Chrome(headless = False, use_subprocess = False, options = uc_options, executable_path = r"F:\Projects\tempmail_new\chromedriver.exe")

    uc_driver.get('https://temp-mail.org/en/')

    wait_1 = WebDriverWait(uc_driver, 20)
    delete_button = wait_1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="click-to-delete"]')))
    delete_button.click()

    wait_2 = WebDriverWait(uc_driver, 20)  
    copy_button = wait_2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tm-body"]/div[1]/div/div/div[2]/div[1]/form/div[2]/button')))
    copy_button.click()

    return pyperclip.paste(), uc_driver

# Function that takes email as input and signs up into rivalIQ
def sign_up_rivaliq(email):

    url = 'https://www.rivaliq.com/social-media-competitive-analysis/'
    # url = "https://www.rivaliq.com/signup"

    driver_rival = webdriver.Firefox(options=tor_options)
    driver_rival.find_element(By.XPATH,'//*[@id="connectButton"]').click()
    time.sleep(20)

    try:
        driver_rival.get(url)

        email_id_wait = WebDriverWait(driver_rival, 30).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/article/div/div/div[1]/div[1]/div[1]/a[1]"))
        )

        driver_rival.find_element(By.XPATH, "/html/body/div[2]/div/article/div/div/div[1]/div[1]/div[1]/a[1]").click()
        
        email_id_wait = WebDriverWait(driver_rival, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/article/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/form/div[1]/div/input'))
        )

        email_id = driver_rival.find_element(By.XPATH, '/html/body/div[1]/div/article/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/form/div[1]/div/input')
        email_id.send_keys(email)

        
        length = random.randint(2, 9)

        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

        first_name = driver_rival.find_element(By.XPATH, '//*[@id="signup-form"]/div/div/div/form/div[2]/div/div[1]/div[1]/div/div/input')
        first_name.send_keys(random_string)

        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

        last_name = driver_rival.find_element(By.XPATH, '//*[@id="signup-form"]/div/div/div/form/div[2]/div/div[1]/div[2]/div/div/input')
        last_name.send_keys(random_string)

        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
        company_name = driver_rival.find_element(By.XPATH, '//*[@id="signup-form"]/div/div/div/form/div[2]/div/div[2]/div[1]/div/div/input')
        company_name.send_keys(random_string)

        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

        company_name = driver_rival.find_element(By.XPATH, '//*[@id="signup-form"]/div/div/div/form/div[2]/div/div[2]/div[2]/div/div/input')
        company_name.send_keys(random_string)

        brand_agency_wait = WebDriverWait(driver_rival, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/article/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/form/div[2]/div/div[3]/div/select'))
        )
        brand_agency = driver_rival.find_element(By.XPATH, '//html/body/div[1]/div/article/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/form/div[2]/div/div[3]/div/select/option[2]').click()

        check_box = driver_rival.find_element(By.XPATH, '//*[@id="signup-form"]/div/div/div/form/div[2]/div/div[4]/div/div[1]/label/input')
        check_box.click()

        get_account_wait = WebDriverWait(driver_rival, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/article/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/form/div[1]/div/input'))
        )

        get_account = driver_rival.find_element(By.CSS_SELECTOR, '.btn')
        get_account.click()

        wait = WebDriverWait(driver_rival, 100)
        wait.until(EC.url_to_be("https://app.rivaliq.com/signupSuccess"))
        
    except Exception as e:
        driver_rival.quit()
        sign_up_rivaliq(email)

    finally:
        time.sleep(5)
        driver_rival.quit()

# Function to copy confirmation link address from tempmail
def copy_conf_link(driver):
    wait = WebDriverWait(driver, 10)
    enter_email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a')))
    enter_email.click()

    wait = WebDriverWait(driver, 10)
    link_address_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@style="color: rgb(255, 255, 255); text-decoration: none; font-size: 16px; line-height: 22px;"]')))

    link_address = link_address_button.get_attribute('href')
    driver.quit()
    return link_address

# Set password and continue 
def account_creation(confirmation_link):

    user_agent = random.choice(user_agents)
    try:
        tor_options.add_argument(f'user-agent={user_agent}')
        tor_driver = webdriver.Firefox(options=tor_options)

        tor_driver.find_element(By.XPATH,'//*[@id="connectButton"]').click()
        time.sleep(20)
        
        tor_driver.get(confirmation_link)

        wait = WebDriverWait(tor_driver, 30)
        password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="registration"]/div/div/div/section/div/div/div/form/div[3]/input')))
        actions = ActionChains(tor_driver)
        actions.click(password).send_keys("Ipac@123")

        confirm_password = tor_driver.find_element(By.XPATH, '//*[@id="registration"]/div/div/div/section/div/div/div/form/div[4]/input[1]')
        actions.click(confirm_password).send_keys("Ipac@123")

        actions.perform()

        continue_page = tor_driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/section/div/div/div/form/a')
        continue_page.click()

    except:
        tor_driver.quit()
        account_creation(confirmation_link)
        
    return tor_driver

# Function to fill profile to corresponding slot
def profile_filler(driver, profile_id, index):
    
    time.sleep(6)
    # wait = WebDriverWait(driver, 30)

    # if index == 0:
        # profile = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/form/div[1]/div[1]/input')))                                            
        # profile.send_keys(profile_id)
        # profile.send_keys(Keys.RETURN)   

    # else:
        # profile = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[{index}]/form/div[1]/div[1]/input')))
        # profile.send_keys(profile_id)
        # profile.send_keys(Keys.RETURN)   

    pyautogui.write(profile_id, interval=0.1)
    pyautogui.press('enter')
    
    time.sleep(6)

    # if profile.get_attribute('value') =='':
    #     print('Invalid', profile_id)    

    #     return False
    
    return True        

# Function to completely fill all slots in registration rage 
def profile_filler_page(driver, profile_list_index, profile_list, invalid_profiles, temp_mail, tempmail_account_mapping):
    profile_count = 0
    while profile_count < 4 and profile_list_index < len(profile_list):
        if profile_filler(driver, profile_list[profile_list_index], profile_count):
            profile_list_index += 1
            profile_count += 1
            tempmail_account_mapping[profile_list[profile_list_index]] = temp_mail
        else:
            profile_list_index += 1
            invalid_profiles.append(profile_list[profile_list_index])

    # continue_wait = WebDriverWait(driver, 10)
    # continue_wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div/div/div[3]/button'))).click()

    # get_started_wait = WebDriverWait(driver, 10)
    # get_started_wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/div/button'))).click()

    time.sleep(5)
    pyautogui.moveTo(945, 855, duration = 1)  
    pyautogui.click()

    pyautogui.moveTo(945, 880, duration = 1)  
    pyautogui.click()
    
    pyautogui.moveTo(945, 905, duration = 1)  
    pyautogui.click()

    time.sleep(10)
    pyautogui.moveTo(1010, 770, duration = 1)  
    pyautogui.click()

    return profile_list_index, tempmail_account_mapping

# Function to download CSV from RivalIQ. Note: Set Xpath of date range 
def rival_iq_download(platform, driver, x_coordinate = 1850, y_coordinate = 620):
    platform_ID = platform + '-link'

    wait_1 = WebDriverWait(driver, 100)
    wait_1.until(EC.visibility_of_element_located((By.ID, platform_ID)))

    time.sleep(5)
    platfrom_link = driver.find_element(By.ID, platform_ID)
    platfrom_link.click()

    wait_2 = WebDriverWait(driver, 100)
    wait_2.until(EC.visibility_of_element_located((By.LINK_TEXT, "Post Tags")))

    time.sleep(5)
    post_tags = driver.find_element(By.LINK_TEXT, "Post Tags")
    post_tags.click()

    pyautogui.moveTo(x_coordinate, y_coordinate, duration = 2)
    pyautogui.click()

    try:
        ad_popup = driver.find_element(By.XPATH, '/html/body/div/div/span/div/div/div/span')
        ad_popup.click()

    except:
        pass

    try:
        wait_popup_2 = WebDriverWait(driver, 10)
        wait_popup_2.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default.x-big-end[data-role='end']")))

        pop_up_2 = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.x-big-end[data-role='end']")
        pop_up_2.click()

    except:
        pass

    wait_4 = WebDriverWait(driver, 100)
    wait_4.until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-tags"]/div[2]/div/div[2]/div/div/div/div/div/div[1]/ul/li[4]/div/div/button')))

    wait_a = WebDriverWait(driver, 100)
    wait_a.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[1]/div/div[2]/div[3]/div/div/button')))
    date_range = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/div[2]/div[3]/div/div/button')
    date_range.click()

    wait_a = WebDriverWait(driver, 100)
    wait_a.until(EC.presence_of_element_located((By.CLASS_NAME, "period-selector")))

    select_range = driver.find_element(By.CLASS_NAME, "period-selector")
    date_range_options = Select(select_range)
    
    option_value = "2"      # for 30 days
    date_range_options.select_by_value(option_value)

    # day = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div[1]/div[4]/div/div[3]/table/tbody/tr[1]/td[4]/button')
    # day.click()

    apply = driver.find_element(By.CLASS_NAME, "x-save")
    apply.click()

    try:
        wait_popup = WebDriverWait(driver, 10)
        wait_popup.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-role='end']"))).click()

    except:
        pass

    try:
        wait_popup_2 = WebDriverWait(driver, 10)
        wait_popup_2.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default.x-big-end[data-role='end']"))).click()
    except:
        pass

    try:
        wait_popup_2 = WebDriverWait(driver, 10)
        wait_popup_2.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[3]/div[2]/button[2]"))).click()

    except:
        pass

    wait_3 = WebDriverWait(driver, 10)
    wait_3.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-tags"]/div[2]/div/div[2]/div/div/div/div/div/div[1]/ul/li[4]/div/div/button'))).click()
    
    wait_4 = WebDriverWait(driver, 10)
    wait_4.until(EC.element_to_be_clickable((By.LINK_TEXT, "Download a CSV"))).click()

    time.sleep(10)
    pyautogui.press("enter")

    driver.quit()