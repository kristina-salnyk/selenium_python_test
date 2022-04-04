from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import string_methods
import webdriver_actions


class Test:

    def __init__(self, params):
        service = Service(params['webdriver'])
        options = webdriver.ChromeOptions()
        options.add_argument(params['lang'])

        self.driver = webdriver.Chrome(service=service, options=options)
        self.login = params['login']
        self.password = params['password']

    def __del__(self):
        self.driver.quit()

    def open_page(self, page_url):
        self.driver.get(page_url)

    def auth(self):
        login_field = webdriver_actions.find_element(self.driver, '//input[@name="identifier"]')
        webdriver_actions.fill_element(self.driver, login_field, self.login)

        next_btn = webdriver_actions.find_element(self.driver, '//button[@jsname="LgbsSe"]')
        webdriver_actions.click_element(self.driver, next_btn)
        time.sleep(1)

        password_field = webdriver_actions.find_element(self.driver, '//input[@name="password"]')
        webdriver_actions.fill_element(self.driver, password_field, self.password)

        next_btn = webdriver_actions.find_element(self.driver, '//button[@jsname="LgbsSe"]')
        webdriver_actions.click_element(self.driver, next_btn)
        time.sleep(1)

    def send_email(self, count):
        index = 0
        while index < count:
            theme = string_methods.generate_random_string(10)
            body = string_methods.generate_random_string(10)

            new_email_btn = webdriver_actions.find_element(self.driver, '//div[@role="button"and@gh="cm"]')
            webdriver_actions.click_element(self.driver, new_email_btn)

            time.sleep(1)

            recipient_field = webdriver_actions.find_element(self.driver, '//div[@role="dialog"]//textarea[@name="to"]')
            webdriver_actions.fill_element(self.driver, recipient_field, self.login)

            theme_field = webdriver_actions.find_element(self.driver,
                                                         '//div[@role="dialog"]//input[@name="subjectbox"]')
            webdriver_actions.fill_element(self.driver, theme_field, theme)

            body_field = webdriver_actions.find_element(self.driver,
                                                        '//div[@role="dialog"]//div[@role="textbox"]')
            webdriver_actions.fill_element(self.driver, body_field, body)

            send_btn = webdriver_actions.find_element(self.driver,
                                                      '(//table[@role="group"]//div[@role="button"])[1]')
            webdriver_actions.click_element(self.driver, send_btn)

            time.sleep(1)

            self.check_email(theme, body)
            index += 1

    def check_email(self, theme, body):
        xpath = '//tr[@role="row" and descendant::span[@email="' + self.login + '"] and descendant::span[' \
                                                                                'normalize-space()="' + theme + '"]]'
        element = webdriver_actions.find_element(self.driver, xpath)
        webdriver_actions.click_element(self.driver, element)

        time.sleep(1)

        body_field = webdriver_actions.find_element(self.driver, '//div[@role="listitem"]//div[@dir="ltr"]')

        assert body == webdriver_actions.get_value(self, body_field)

        back_btn = webdriver_actions.find_element(self.driver, '(//div[@gh="mtb"]//div[@role="button"])[1]')
        webdriver_actions.click_element(self.driver, back_btn)

    def read_email(self, email_count):
        email_data = dict()

        xpath = '//tr[@role="row" and descendant::span[@email="' + self.login + '"]]/td[5]'
        elements = webdriver_actions.find_elements(self.driver, xpath)
        email_count_found = len(elements)

        index = 0
        while index < email_count_found:
            xpath = '(//tr[@role="row" and descendant::span[@email="' + self.login + '"]]/td[5])[' + str(
                index + 1) + ']'
            element = webdriver_actions.find_element(self.driver, xpath)
            webdriver_actions.click_element(self.driver, element)

            time.sleep(1)

            theme_field = webdriver_actions.find_element(self.driver, '//table[@role="presentation"]//h2')
            theme = webdriver_actions.get_value(self, theme_field)

            body_field = webdriver_actions.find_element(self.driver, '//div[@role="listitem"]//div[@dir="ltr"]')
            body = webdriver_actions.get_value(self, body_field)

            back_btn = webdriver_actions.find_element(self.driver, '(//div[@gh="mtb"]//div[@role="button"])[1]')
            webdriver_actions.click_element(self.driver, back_btn)

            if len(theme) == 10 and len(body) == 10:
                email_data[theme] = body

            if len(email_data) == email_count:
                return email_data

            index += 1

        return email_data

    def send_report(self, email_data):
        for key in email_data:
            chars_data = string_methods.chars_count(email_data[key])
            letter_count = chars_data['letters']
            number_count = chars_data['numbers']
            body = 'Received mail on theme ' + key + ' with message: ' + email_data[
                key] + '. It contains ' + str(letter_count) + ' letters and ' + str(number_count) + ' numbers.'

            new_email_btn = webdriver_actions.find_element(self.driver, '//div[@role="button"and@gh="cm"]')
            webdriver_actions.click_element(self.driver, new_email_btn)

            recipient_field = webdriver_actions.find_element(self.driver, '//div[@role="dialog"]//textarea[@name="to"]')
            webdriver_actions.fill_element(self.driver, recipient_field, self.login)

            theme_field = webdriver_actions.find_element(self.driver,
                                                         '//div[@role="dialog"]//input[@name="subjectbox"]')
            webdriver_actions.fill_element(self.driver, theme_field, 'Sent data')

            body_field = webdriver_actions.find_element(self.driver,
                                                        '//div[@role="dialog"]//div[@role="textbox"]')
            webdriver_actions.fill_element(self.driver, body_field, body)

            send_btn = webdriver_actions.find_element(self.driver,
                                                      '(//table[@role="group"]//div[@role="button"])[1]')
            webdriver_actions.click_element(self.driver, send_btn)

            time.sleep(2)

    def delete_email(self, email_data):
        for key in email_data:
            xpath = '//tr[@role="row" and descendant::span[@email="' + self.login + '"] and descendant::span[' \
                                                                                    'normalize-space()="' + key + \
                    '"]]//div[@role="checkbox"] '
            element = webdriver_actions.find_element(self.driver, xpath)
            webdriver_actions.move_to_element(self.driver, element)
            webdriver_actions.click_element(self.driver, element)

        time.sleep(1)

        btn_delete = webdriver_actions.find_element(self.driver, '(//div[@gh="mtb"]//div[@role="button"])[4]')
        webdriver_actions.click_element(self.driver, btn_delete)

        time.sleep(4)
