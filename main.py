from playwright.sync_api import sync_playwright

import login_page
import info_page
import payment_page

execution_number = input("Number of form to fill with fake data : ")
while(not execution_number.isnumeric()):
    print("\033[31mExecution number must be an integer \033[0m")
    execution_number = input("Number of form to fill with fake data : ")

execution_number = int(execution_number)

with sync_playwright() as playwright :
    browser = playwright.chromium.launch(headless = True)
    execution_progress = succes_number = failure_number = 0

    for i in range(execution_number) :
        page = browser.new_page()
        page.set_default_timeout(15_000)

        execution_progress = execution_progress + 1
        print(f"{int((execution_progress - 1)/execution_number * 100)}% Loading... ({execution_progress}/{execution_number}) {succes_number} succes, {failure_number} failure(s)")

        try:
            page.goto("https://reglements-factures.com")

            login_page.main(page)

            pay_button = page.get_by_role("button", name="PAYER")
            pay_button.click()

            info_page.main(page)
            payment_page.main(page)

            page.close()
            succes_number += 1

        except Exception:
            failure_number += 1

    browser.close()

    succes_percent = succes_number/execution_number * 100
    print(f"Complete with {round(succes_percent, 2)}% of succes")