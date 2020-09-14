import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
from selenium.webdriver.support import expected_conditions as EC
import read_image
from selenium.common.exceptions import NoSuchElementException
import time
import image_handling.no_data as no
import image_handling.match_test2 as match2

answers = []

# Funktionen ska köras då användaren kommit in i portalen
def question_loop(question_arr, departments, driver, wait):
    for question in question_arr:
        gender = ["Kvinna", "Man"]

        driver.find_element_by_xpath('//a[text()="Alla frågor"]').click()

        # Placerar markören i inputfältet för val av fråga
        input_element = driver.find_element_by_class_name("radPreventDecorate")
        input_element.click()
        input_element.send_keys(question)
        input_element.send_keys(Keys.ENTER)
        # wait.until(lambda driver: driver.find_element_by_class_name("QuestionRepeaterWrap"))

        time.sleep(2)

        driver.find_element_by_class_name("resetFilters").click

        time.sleep(1)

        elements = driver.find_elements_by_xpath('//div[contains(@class, "ExpandableFilterList") and ' +
            'contains(@class, "collapsed")]/div/h1')

        if elements:
            element = elements[0].click()

        time.sleep(2)

        """         # Klickar ut tjänstebenämning
        elements = driver.find_elements_by_xpath('//li[(@class="question_334746 ")]/h2')

        time.sleep(1)

        elements[0].click()

        time.sleep(1)

        # Undesöker om checkboxen för doktorand är iklickad
        doc_elements = driver.find_elements_by_xpath('//li[(@id="FilterInputButton5573397")]/i[contains(@class, "icons-checked")]')


        # Klickar i rutan för doktorand om den ej är iklickad

        if not doc_elements:
            elements = driver.find_elements_by_xpath('//li[(@id="FilterInputButton5573397")]/i')

            elements[0].click()

        time.sleep(1) """

        for index, curr_gend in enumerate(gender):

            driver.implicitly_wait(3)

            elements = driver.find_elements_by_xpath('//div[contains(@class, "ExpandableFilterList") and ' +
                'contains(@class, "collapsed")]/div/h1')

            if elements:
                element = elements[0].click()

            # Klickar ut fliken "kön" om den är kollapsad
            elements = driver.find_elements_by_xpath('//li[(@class="question_275954 ")]/h2')

            if elements:
                time.sleep(2)
                elements[0].click()

            # Klickar ut könfliken om bara ett val är synligt
            elements = driver.find_elements_by_xpath('//li[contains' +
                '(@class, "question_275954")]/ul/li')

            if len(elements) == 1:
                elements[0].click()

            time.sleep(1)
            # Avmarkerar alla val av kön
            wait = WebDriverWait(driver, 0.5) # timeout after 0.5 seconds
            driver.implicitly_wait(0.5)

            elements = driver.find_elements_by_xpath('//li[(@id="FilterInputButton4484538") and contains(@class, "On")]')

            if elements:
                elements[0].click()

            elements = driver.find_elements_by_xpath('//li[(@id="FilterInputButton4484539") and contains(@class, "On")]')

            if elements:
                elements[0].click()

            elements = driver.find_elements_by_xpath('//span[contains(text(), "Markera alla")]' +
                '/preceding-sibling::i')


            if elements:
                try:
                    elements[0].click()
                except Exception as e:
                    print(e)

            time.sleep(2)
            elements = driver.find_elements_by_xpath('//span[contains(text(), "Avmarkera alla")]' +
                '/preceding-sibling::i')


            if elements:
                try:
                    elements[0].click()
                except Exception as e:
                    print(e)

            wait = WebDriverWait(driver, 10) # timeout after 10 seconds
            driver.implicitly_wait(10)

            time.sleep(2)

            element = driver.find_element_by_xpath('//li[.//span[contains(text(),"' + curr_gend + '")]]/i')

            element.click()

            department_loop(departments, question, curr_gend, driver, wait)


def department_loop(departments, question, gender, driver, wait):
    for index, department in enumerate(departments, 1):
        # Expanderar fliken med chalmers organisation om den är kollapsad
        wait = WebDriverWait(driver, 0.5) # timeout after 0.5 seconds

        driver.implicitly_wait(3)

        time.sleep(2)
        elements = driver.find_elements_by_xpath('//div[contains(@id, "HierarchyFilterSubmenu") ' +
            'and contains(@class, "collapsed")]')

        if elements:
            elements[0].click()

        wait = WebDriverWait(driver, 10) # timeout after 10 seconds
        driver.implicitly_wait(10)

        time.sleep(2)
        # Rensar alla checkboxarna i organisationsträdet
        driver.find_element_by_id('clearButton').click()

        time.sleep(3)
        # Väljer avdelning
        input_element = driver.find_element_by_xpath('//span[text()="' +
            department  + '"]/preceding-sibling::input').click()
        x_locator = "//span[text()='" + department + "']/preceding-sibling::input[(@checked='checked')]"
        wait.until(EC.visibility_of_element_located((By.XPATH, x_locator)))
        driver.find_element_by_id('updateButton').click()

        time.sleep(2)
        #wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="Loader" and contains(@style, "top:")]')))

        element = driver.find_element_by_css_selector(".QuestionRepeaterWrap img")

        filename = "temp_qs_" + question + "_" + department + "_" + gender + "_d" + str(index) + ".png"
        url = element.get_attribute("src")

        urlretrieve(url, filename)

        this_ans = [department, question, gender]

        ans_data = [0, 0, 0, 0, 0, 0, 0, 0]

        if not no.check_none(filename):
            ans_data = read_image.get_data(filename)

        print("ans_data", ans_data)

        this_ans.append(ans_data)

        answers.append(this_ans)


def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True