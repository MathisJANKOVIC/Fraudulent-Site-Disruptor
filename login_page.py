from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime
import random
import faker_utils

def run(page):
    input_last_name = page.locator(".inp:nth-child(1) > #inp")
    input_last_name.click()
    input_last_name.fill(faker_utils.faker_random.last_name())

    input_first_name = page.locator(".inp:nth-child(3) > #inp")
    input_first_name.click()
    input_first_name.fill(faker_utils.fake_fr.first_name())

    start_date = datetime(1950, 1, 1).date()
    end_date = datetime.now().date() - relativedelta(years = 18)
    date = start_date + timedelta(days = random.randint(0,(end_date - start_date).days))

    input_date = page.locator(".inp:nth-child(5) > #inp")
    input_date.click()
    input_date.fill(str(date))

    input_postcode = page.locator(".inp:nth-child(7) > #inp")
    input_postcode.click()
    input_postcode.fill(faker_utils.fake_fr.postcode())

    submit_button = page.get_by_role("button", name="Rechercher")
    submit_button.click()