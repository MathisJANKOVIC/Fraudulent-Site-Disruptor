import random
import faker_utils

def run(page):
    phone_number = "0" + str(random.randint(6,7))
    for i in range(8):
        phone_number = phone_number + str(random.randint(0,9))

    input_phone_number = page.locator(".inp:nth-child(7) > #inp")
    input_phone_number.click()
    input_phone_number.fill(phone_number)

    input_address = page.locator(".inp:nth-child(9) > #inp")
    input_address.click()
    input_address.fill(faker_utils.fake_fr.street_address())

    input_city = page.locator(".inp:nth-child(11) > #inp")
    input_city.click()
    input_city.fill(faker_utils.fake_fr.city())

    continue_button = page.get_by_role("button", name="CONTINUER")
    continue_button.click()