from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import email, password, send_to, message_to_send


class HangoutsBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):

        # Go to website
        self.driver.get('https://hangouts.google.com')
        self.driver.maximize_window()

        #Click Sign In
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gb_70"]')))
        signin_btn = self.driver.find_element_by_xpath('//*[@id="gb_70"]')
        signin_btn.click()

        #Enter Email
        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(email)

        email_next = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
        email_next.click()

        #Enter Password
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        password_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password_in.send_keys(password)

        password_next = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
        password_next.click()

        #Click Message
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[4]/div/div/ul/li[3]/div[1]')))
        new_conv_btn = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[4]/div[4]/div/div/ul/li[3]/div[1]')
        new_conv_btn.click()

        #Input email to send message to
        sleep(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(bot.driver.find_elements_by_tag_name('iframe')[1])
        email_send = self.driver.find_element_by_xpath('//*[@id=":4.vw"]/div/div[1]/div/div[2]/div/div[4]/div[1]/div/input')
        email_send.send_keys(send_to)

        #Select Contact
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=":4.vw"]/div/div[2]/div/div/div/div[3]/div/div/div[7]/div[2]/ul/li')))
        select_contact_btn = self.driver.find_element_by_xpath('//*[@id=":4.vw"]/div/div[2]/div/div/div/div[3]/div/div/div[7]/div[2]/ul/li')
        select_contact_btn.click()

        #Send Message
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('iframe')[6])
        message = self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/div/div[3]/div/div/div[4]/div[2]/div[3]/div/div[2]')
        message.send_keys(message_to_send)

        #Send Message
        message.send_keys(Keys.ENTER)

bot = HangoutsBot()
bot.login()

