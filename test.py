from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def find_element_by_text(driver, text, elem="button", root="//"):
    return driver.find_element_by_xpath(f'{root}{elem}[text()="{text}"]')


def pizza_hut_login(driver, username, password):
    login_btn = find_element_by_text(driver, "Log in")
    login_btn.click()

    time.sleep(10)

    email_txt = driver.find_element_by_name('email')
    email_txt.clear()
    email_txt.send_keys(username)

    passwd_txt = driver.find_element_by_name("password")
    passwd_txt.clear()
    passwd_txt.send_keys(password)
    passwd_txt.send_keys(Keys.RETURN)

    time.sleep(10)
   

def find_pizza_hut_location(driver, address):
    address_txt = driver.find_element_by_id("search-input")
    address_txt.send_keys(address)

    time.sleep(5)

    address_txt.send_keys(Keys.RETURN)
    
    time.sleep(10)

    begin_order_btn = find_element_by_text(driver, "Begin your order")
    begin_order_btn.click()

    time.sleep(10)


def ignore_extended_delivery_time_popup(driver):
    try:
        save_btn = find_element_by_text(driver, "Save")
        save_btn.click()
        time.sleep(10)
    except:
        print("Extended delivery time popup not found")


def ignore_closed_restaurant_popup(driver):
    try:
        ill_order_btn = find_element_by_text(driver, "I'll order")
        driver.execute_script("arguments[0].click();", ill_order_btn)
        time.sleep(10)
    except Exception as e:
        print("Closed restaurant popup not found")
        print(e)


def navigate_to_pizza_menu(driver):
    pizza_tab = driver.find_element_by_xpath('//li[.//span[text()="PIZZA"]]')
    pizza_tab.click()
    time.sleep(10)


def add_pizza_to_cart(driver, pizza_name):
    pizza_menu = driver.find_element_by_id("pizzas")
    pizza_title = find_element_by_text(pizza_menu, pizza_name, "span")
    pizza = pizza_title.find_element_by_xpath('..')
    add_btn = pizza.find_element_by_tag_name("button")

    driver.execute_script('arguments[0].scrollIntoView(true);', add_btn)
    driver.execute_script("arguments[0].click();", add_btn)
    time.sleep(10)

    add_to_cart_btn = find_element_by_text(driver, "Add to cart") 
    add_to_cart_btn.click()
    time.sleep(10)


def order_current_cart(driver):
    order_btn = find_element_by_text(driver, "Order")
    driver.execute_script("arguments[0].click();", order_btn)
    time.sleep(10)


def ignore_limited_time_offer_popup(driver):
    try:
        no_thanks = find_element_by_text(driver, "No, thanks")
        no_thanks.click()
        time.sleep(10)
    except:
        print("No limited offer popup found.")


def fill_in_order_details(driver, name, email, phone, flat_nr):
    name_txt = driver.find_element_by_name("firstName")
    name_txt.clear()
    name_txt.send_keys(name)

    email_txt = driver.find_element_by_name("email")
    email_txt.clear()
    email_txt.send_keys(email)

    phone_txt = driver.find_element_by_name("phone")
    phone_txt.clear()
    phone_txt.send_keys(phone)

    flat_nr_txt = driver.find_element_by_name("apartNumber")
    flat_nr_txt.clear()
    flat_nr_txt.send_keys(flat_nr)

    credit_card_opt = find_element_by_text(driver, "Credit card", elem="span")
    driver.execute_script("arguments[0].click();", credit_card_opt)
    time.sleep(10)

    order_and_pay_btn = find_element_by_text(driver, "Order and pay", elem="div")
    driver.execute_script("arguments[0].click();", order_and_pay_btn)
    time.sleep(10)


def make_payment(driver, card_nr, card_date, card_cvv, card_name):
    card_nr_txt = driver.find_element_by_id("card-number")
    card_nr_txt.clear()
    card_nr_txt.send_keys(card_nr)

    card_date_txt = driver.find_element_by_id("card-date")
    card_date_txt.clear()
    card_date_txt.send_keys(card_date)

    card_cvv_txt = driver.find_element_by_id("card-cvv")
    card_cvv_txt.clear()
    card_cvv_txt.send_keys(card_cvv)

    name_txt = driver.find_element_by_id("card-name")
    name_txt.clear()
    name_txt.send_keys(card_name)

    #Make sure everything works and you're ready for testing before uncommenting submit.
    #driver.find_element_by_xpath('//input[type="submit"]').submit()


def main(driver):    
    from config import *
    try:
        pizza_hut_login(driver, *CREDENTIALS)
        find_pizza_hut_location(driver, ADDRESS[0])
        ignore_extended_delivery_time_popup(driver)
        ignore_closed_restaurant_popup(driver)
        navigate_to_pizza_menu(driver)
        add_pizza_to_cart(driver, PIZZA_NAME)
        order_current_cart(driver)
        ignore_limited_time_offer_popup(driver)
        fill_in_order_details(driver, FIRST_NAME, EMAIL, PHONE, ADDRESS[1])
        make_payment(driver, CARD_NUMBER, CARD_DATE, CARD_CVV, CARD_FULL_NAME)
    except:
        driver.save_screenshot("error.png")
        raise


if __name__ == '__main__':
    with webdriver.Chrome() as driver:
        driver.get("https://pizzahut.pl/en")
        assert "Pizza Hut" in driver.title
        time.sleep(10)
        main(driver)

