from playwright.sync_api import Page
import random

import faker_utils

def process(page: Page) -> None:
    # French phone numbers start with 06 or 07
    phone_num = "0" + str(random.randint(6,7))
    for _ in range(8):
        phone_num += str(random.randint(0,9))

    input_phone_num = page.locator(".inp:nth-child(7) > #inp")
    input_phone_num.click()
    input_phone_num.fill(phone_num)

    input_address = page.locator(".inp:nth-child(9) > #inp")
    input_address.click()
    input_address.fill(faker_utils.fr.street_address())

    input_city = page.locator(".inp:nth-child(11) > #inp")
    input_city.click()
    input_city.fill(faker_utils.fr.city())

    continue_button = page.get_by_role("button", name="CONTINUER")
    continue_button.click()