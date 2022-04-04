from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver, xpath):
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    wait = WebDriverWait(driver, 120, ignored_exceptions=ignored_exceptions)
    element = wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
    # element = driver.find_element(By.XPATH, xpath)
    return element


def find_elements(driver, xpath):
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    wait = WebDriverWait(driver, 120, ignored_exceptions=ignored_exceptions)
    elements = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
    # elements = driver.find_elements(By.XPATH, xpath)
    return elements


def fill_element(driver, element, value):
    element.send_keys(value)


def click_element(driver, element):
    element.click()


def get_value(driver, element):
    value = element.text
    return value


def move_to_element(driver, element):
    element.send_keys(Keys.END)
