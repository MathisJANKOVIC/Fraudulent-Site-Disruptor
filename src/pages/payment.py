from playwright.sync_api import Page
import random

import faker_country

def process(page: Page) -> None:
    credit_card_num = ""
    for _ in range(16):
        credit_card_num += str(random.randint(0,9))

    input_card_num = page.locator(".inp:nth-child(1) > #inp")
    input_card_num.click()
    input_card_num.fill(faker_country.fr.credit_card_number())

    input_expire_date = page.locator(".inp:nth-child(3) > #inp")
    input_expire_date.click()
    input_expire_date.fill(faker_country.fr.credit_card_expire())

    input_security_code = page.locator(".inp:nth-child(5) > #inp")
    input_security_code.click()
    input_security_code.fill(faker_country.fr.credit_card_security_code())

    pay_button = page.get_by_role("button", name="PAYER")
    pay_button.click()