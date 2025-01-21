from playwright.sync_api import Page

from fakerlocale import fr_locale

def fill_out(page: Page) -> None:
    input_card_num = page.locator(".inp:nth-child(1) > #inp")
    input_card_num.click()
    input_card_num.fill(fr_locale.credit_card_number())

    input_expire_date = page.locator(".inp:nth-child(3) > #inp")
    input_expire_date.click()
    input_expire_date.fill(fr_locale.credit_card_expire())

    input_security_code = page.locator(".inp:nth-child(5) > #inp")
    input_security_code.click()
    input_security_code.fill(fr_locale.credit_card_security_code())

    pay_button = page.get_by_role("button", name="PAYER")
    pay_button.click()