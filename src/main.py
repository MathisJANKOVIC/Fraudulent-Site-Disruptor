from playwright.sync_api import sync_playwright
from pages import login, info, payment

while(True):
    try:
        exec_count = int(input("Enter the number of form to fill with fake data: "))
        assert exec_count > 0
    except:
        print("The number has to be a positive integer")
    else:
        break

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)

    exec_progress = 0
    succes_count = 0
    failure_count = 0

    for _ in range(exec_count):
        page = browser.new_page()
        page.set_default_timeout(12000)

        exec_progress += 1
        print(f"{int((exec_progress - 1) / exec_count * 100)}% Loading... ({exec_progress}/{exec_count}) {succes_count} succes, {failure_count} failure(s)")

        try:
            page.goto("https://reglements-factures.com")

            login.process(page)

            pay_button = page.get_by_role("button", name="PAYER")
            pay_button.click()

            info.process(page)
            payment.process(page)

            page.close()
            succes_count += 1
        except:
            failure_count += 1
            
    browser.close()

    succes_percent = succes_count / exec_count * 100
    print(f"Complete with {round(succes_percent, 2)}% of succes")
