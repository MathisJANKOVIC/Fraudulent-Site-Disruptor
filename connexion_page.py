from playwright.sync_api import sync_playwright
from dateutil.relativedelta import relativedelta
from faker import Faker
from datetime import datetime, timedelta
import random

execution_number = input("Number of form to fill with fake data : ")
while(not execution_number.isnumeric()):
    print("Error : execution number must be an integer ")
    execution_number = input("Number of form to fill with fake data : ")

execution_number = int(execution_number)

with sync_playwright() as playwright :
    browser = playwright.chromium.launch(headless=True)
    fake_fr = Faker(locale="fr_FR")
    faker_countries = ["fr_FR","fr_BE","fr_BE","fr_CA","es_ES","hr_HR","it_IT","ru_RU","en_US","en_GB"]
    fake_random = Faker(locale=faker_countries[random.randint(0,len(faker_countries)-1)])

    start_date = datetime(1950, 1, 1).date()
    end_date = datetime.now().date() - relativedelta(years=18)

    execution_progress = 1
    succes_number = failure_number = 0

    for i in range(execution_number) :
        print(f"{int((execution_progress-1)/execution_number * 100)}% Loading... {succes_number} succes, {failure_number} failure(s)")
        page = browser.new_page()
        page.set_default_timeout(10000)
        page.set_viewport_size({"width": 500, "height": 700})

        try:
            page.goto("https://reglements-factures.com")

            input_last_name = page.locator(".inp:nth-child(1) > #inp")
            input_last_name.click()
            input_last_name.fill(fake_random.last_name())

            input_first_name = page.locator(".inp:nth-child(3) > #inp")
            input_first_name.click()
            input_first_name.fill(fake_fr.first_name())

            date = start_date + timedelta(days=random.randint(0,(end_date - start_date).days))
            input_date = page.locator(".inp:nth-child(5) > #inp")
            input_date.click()
            input_date.fill(str(date))

            input_postcode = page.locator(".inp:nth-child(7) > #inp")
            input_postcode.click()
            input_postcode.fill(fake_fr.postcode())

            submit_button = page.get_by_role("button", name="Rechercher")
            submit_button.click()

            pay_button = page.get_by_role("button", name="PAYER")
            pay_button.click()

            phone_number = "0" + str(random.randint(6,7))
            for i in range(8):
                phone_number = phone_number + str(random.randint(0,9))

            input_num_tel = page.locator(".inp:nth-child(7) > #inp")
            input_num_tel.click()
            input_num_tel.fill(phone_number)

            input_address = page.locator(".inp:nth-child(9) > #inp")
            input_address.click()
            input_address.fill(fake_fr.street_address())

            input_city = page.locator(".inp:nth-child(11) > #inp")
            input_city.click()
            input_city.fill(fake_fr.city())

            continue_button = page.get_by_role("button", name="CONTINUER")
            continue_button.click()

            credit_card_num = ""
            for i in range(16):
                credit_card_num = credit_card_num + str(random.randint(0,9))

            input_card_num = page.locator(".inp:nth-child(1) > #inp")
            input_card_num.click()
            input_card_num.fill(fake_fr.credit_card_number())

            input_expire_date = page.locator(".inp:nth-child(3) > #inp")
            input_expire_date.click()
            input_expire_date.fill(fake_fr.credit_card_expire())

            input_security_code = page.locator(".inp:nth-child(5) > #inp")
            input_security_code.click()
            input_security_code.fill(fake_fr.credit_card_security_code())

            pay_button = page.get_by_role("button", name="PAYER")
            pay_button.click()
            page.close()
            succes_number += 1

        except:
            failure_number += 1

        execution_progress = execution_progress + 1

    print(f"Finished with {succes_number/execution_number * 100}% of succes")
