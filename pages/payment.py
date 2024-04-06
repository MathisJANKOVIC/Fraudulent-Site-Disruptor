from playwright.sync_api import Page, Locator
import random

import faker_utils

def main(page: Page):
    credit_card_num = ""
    for _ in range(16):
        credit_card_num += str(random.randint(0,9))

    input_card_num: Locator = page.locator(".inp:nth-child(1) > #inp")
    input_card_num.click()
    input_card_num.fill(faker_utils.fr.credit_card_number())

    input_expire_date: Locator = page.locator(".inp:nth-child(3) > #inp")
    input_expire_date.click()
    input_expire_date.fill(faker_utils.fr.credit_card_expire())

    input_security_code: Locator = page.locator(".inp:nth-child(5) > #inp")
    input_security_code.click()
    input_security_code.fill(faker_utils.fr.credit_card_security_code())

    pay_button: Locator = page.get_by_role("button", name="PAYER")
    pay_button.click()