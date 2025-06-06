import os

import  pytest
from selene import browser, have
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


@pytest.fixture(scope = 'function')
def driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    yield
    browser.quit()

def test_open_sait(driver):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type('Иван').press_enter()
    browser.element('[id="lastName"]').type('Иванов').press_enter()
    browser.element('[id="userEmail"]').type('ivanov@.mail.ru').press_enter()
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type('9998887766').click()

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('option[value="1998"]').click()
    browser.element('.react-datepicker__month-select').element('option[value="5"]').click()
    browser.element('[aria-label="Choose Wednesday, July 8th, 1998"]').click()

    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()

    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('kalendar-2025.jpg'))

    browser.element('#currentAddress').type('проспект Мира дом 1')
    browser.element('#react-select-3-input').type('raja').press_enter()
    browser.element('#react-select-4-input').type('jaip').press_enter()

    browser.element('#submit').click()


    browser.element('tbody').should(have.text('Student Name Иван Иванов'))
    browser.element('tbody').should(have.text('Student Email ivanov@.mail.ru'))
    browser.element('tbody').should(have.text('Gender Male'))
    browser.element('tbody').should(have.text('Mobile 999888776'))
    browser.element('tbody').should(have.text('Date of Birth 08 July,1998'))
    browser.element('tbody').should(have.text('Subjects Maths'))
    browser.element('tbody').should(have.text('Picture kalendar-2025.jpg'))
    browser.element('tbody').should(have.text('Address проспект Мира дом 1'))
    browser.element('tbody').should(have.text('State and City Rajasthan Jaipur'))