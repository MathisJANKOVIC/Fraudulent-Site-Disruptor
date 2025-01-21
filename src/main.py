from playwright.sync_api import sync_playwright

import forms

WEBSITE_DOMAIN = "reglements-factures.com"
WEBSITE_URL = f"https://{WEBSITE_DOMAIN}"

TIMEOUT = 12_000

while True:
    try:
        execution_count = int(input(
            f"Enter the number of time to flood the website '{WEBSITE_DOMAIN}' with fake data: "
        ))
        assert execution_count > 0
    except:
        print("The input must be be a positive integer.\n")
    else:
        break

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)

    execution_progress = 0
    succes_count = 0
    failure_count = 0

    for _ in range(execution_count):
        page = browser.new_page()
        page.set_default_timeout(TIMEOUT)

        execution_progress += 1

        progress_percent = (execution_progress - 1) / execution_count * 100

        print(f"{round(progress_percent)}% Loading...", end="")
        print(f"({execution_progress}/{execution_count}) {succes_count} success, {failure_count} failure(s)")

        try:
            page.goto(WEBSITE_URL)

            forms.login.fill_out(page)

            pay_button = page.get_by_role("button", name="PAYER")
            pay_button.click()

            forms.info.fill_out(page)
            forms.payment.fill_out(page)

            page.close()
            succes_count += 1
        except:
            failure_count += 1

    browser.close()

    succes_percent = succes_count / execution_count * 100
    print(f"Complete with {round(succes_percent, 2)}% of success")
