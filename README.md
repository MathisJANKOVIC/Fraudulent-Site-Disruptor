# Fraudulent-Website-Disruptor

Fraudulent Website Disruptor is a Python algorithm on console that use Playwright librairy to automate web process. The use of the algorithm is to send mass fake information to a phishing website to undermine their activity. Scammers will have thousands of fake identity and bank information to try out.

I got that idea after I received severals fraudulent messages on my smartphone which say that I have to pay a contravention due to traffic violation and to click on the link. That link actually redirect to a fake website that emulate an official French website. Once you've clicked on the link you're taken to a page where you have to fill out forms with your personal identity and bank information. Once you get trapped, the scammer will try to do some illegal transactions with your bank card.

Update : the website has been down so if you run the script you will probably have 0% of succes rate

## Requirements
- Git (optionnal)
- Python

## Configuration
    1. Download and extract the zip or clone the project
    2. Open a terminal
    3. Install faker with command `pip install faker`
    4. Install Playwright with command `pip install Playwright`
    5. Navigate to `AppData\Roaming\Python\Python310\site-packages\playwright\driver`
    6. Run the command `playwright.cmd install`
    7. Navigate into a terminal to the project directory
    8. Run the command `python main.py` (requires python path in environement variables)
