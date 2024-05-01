from playwright.sync_api import Page
from datetime import date, timedelta
import random
import fakerlocale

def process(page: Page) -> None:
    input_lastname = page.locator(".inp:nth-child(1) > #inp")
    input_lastname.click()
    input_lastname.fill(fakerlocale.random.last_name())

    input_firstname = page.locator(".inp:nth-child(3) > #inp")
    input_firstname.click()
    input_firstname.fill(fakerlocale.fr.first_name())

    older_date = date.today() - timedelta(days=365*100)
    newer_date = date.today() - timedelta(days=365*18)
    random_date = older_date + timedelta(days=random.randint(0, (newer_date - older_date).days))

    input_date = page.locator(".inp:nth-child(5) > #inp")
    input_date.click()
    input_date.fill(str(random_date))

    input_postcode = page.locator(".inp:nth-child(7) > #inp")
    input_postcode.click()
    input_postcode.fill(fakerlocale.fr.postcode())

    submit_button = page.get_by_role("button", name="Rechercher")
    submit_button.click()