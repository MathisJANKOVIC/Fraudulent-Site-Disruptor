from playwright.sync_api import sync_playwright
from pages import login, info, payment

while(True):
    try:
        execution_count = int(input("Enter the number of form to fill with fake data : "))
        assert execution_count > 0
    except:
        print("\033[31mExecution number must be a positive integer \033[0m")
    else:
        break

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)

    execution_progress = 0
    succes_number = 0
    failure_number = 0

    for i in range(execution_count):
        page = browser.new_page()
        page.set_default_timeout(12_000)

        execution_progress += 1
        print(f"{int((execution_progress - 1)/execution_count * 100)}% Loading... ({execution_progress}/{execution_count}) {succes_number} succes, {failure_number} failure(s)")

        try:
            page.goto("https://reglements-factures.com")

            login.process(page)
            pay_button = page.get_by_role("button", name="PAYER")
            pay_button.click()

            info.process(page)
            payment.process(page)

            page.close()
            succes_number += 1

        except Exception:
            failure_number += 1

    browser.close()

    succes_percent = succes_number/execution_count * 100
    print(f"Complete with {round(succes_percent, 2)}% of succes")