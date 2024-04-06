from playwright.sync_api import Page, Locator
from datetime import date, timedelta
import random

import faker_utils

def main(page: Page):
    input_lastname: Locator = page.locator(".inp:nth-child(1) > #inp")
    input_lastname.click()
    input_lastname.fill(faker_utils.random_country.last_name())

    input_firstname: Locator = page.locator(".inp:nth-child(3) > #inp")
    input_firstname.click()
    input_firstname.fill(faker_utils.fr.first_name())

    older_date = date.today() - timedelta(days=365*100)
    newer_date = date.today() - timedelta(days=365*18)
    random_date = older_date + timedelta(days=random.randint(0, (newer_date - older_date).days))

    input_date: Locator = page.locator(".inp:nth-child(5) > #inp")
    input_date.click()
    input_date.fill(str(random_date))

    input_postcode: Locator = page.locator(".inp:nth-child(7) > #inp")
    input_postcode.click()
    input_postcode.fill(faker_utils.fr.postcode())

    submit_button: Locator = page.get_by_role("button", name="Rechercher")
    submit_button.click()