from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MailHandler:
    def __init__(self, url):  # , url, sender, email_sender
        self.url = url
        self.sender = None  # sender
        self.email_sender = None  # email_sender
        self.logged = False
        self.browser = webdriver.Chrome(executable_path="chromedriver.exe")
        self.wait = WebDriverWait(self.browser, 500)

    def shutdown(self):
        self.browser.close()

    def login_in(self, login, password):
        self.browser.get(self.url)
        self.wait.until(EC.element_to_be_clickable((By.ID, "identifierId")))
        email = self.browser.find_element_by_id('identifierId')
        email.send_keys(login)
        button_next = self.browser.find_element_by_id('identifierNext')
        button_next.click()
        loggin_trigger = True
        i = 0
        while len(self.browser.find_elements_by_xpath("//div[@class='KTeGk']")) == 0:
            time.sleep(1)
            if i > 10:
                loggin_trigger = False
                break
            i += 1

        if loggin_trigger:
            self.wait.until(EC.element_to_be_clickable((By.NAME, "password")))
            passwd = self.browser.find_element_by_name('password')
            passwd.send_keys(password)
            button_next = self.browser.find_element_by_id('passwordNext')
            button_next.click()
            i = 0
            self.logged = True
            while len(self.browser.find_elements_by_xpath("//div[@class='T-I T-I-KE L3']")) == 0:
                time.sleep(1)
                if i > 10:
                    self.logged = False
                    break
                i += 1
        return self.logged

    def check_new_mails(self):
        if self.logged and len(self.browser.find_elements_by_xpath("//tr[@class='zA zE']")) > 0:
            # zA zE
            new_mail_list = self.browser.find_elements_by_xpath("//tr[@class='zA zE']")
            for new_mail in new_mail_list:
                print('mail ', new_mail.text)
        return new_mail_list

    def find_sender(self, sender, new_mails=True):
        if new_mails:
            pass
        else:
            pass

    def __get_email(self):
        emails = self.browser.find_elements_by_css_selector('.UI table > tbody > tr')
        i = 0
        for mail in emails:
            if self.sender.lower() in str(mail.text).lower():
                i += 1
        return i

    def send_mail(self, reciever, text):
        button_email_create = self.browser.find_element_by_xpath("//div[@class='T-I T-I-KE L3']")
        button_email_create.click()
        time.sleep(3)
        email_field = self.browser.find_element_by_xpath("//textarea[@name='to']")
        email_field.send_keys(self.email_sender)
        time.sleep(1)
        email_theme = self.browser.find_element_by_xpath("//input[@name='subjectbox']")
        email_theme.send_keys("Тестовое задание. Митрохин")
        time.sleep(1)
        email_body = self.browser.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']")
        email_body.send_keys(f'Добрый день! В моем почтовом ящике имеется письма от Вас в количестве '
                             f'{self.__get_email()} штук')
        time.sleep(1)
        button_send_email = self.browser.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
        button_send_email.click()
