# Fraudulent-Website-Disruptor

Fraudulent Website Disruptor is an algorithm that sends massive fake data to a phishing website to undermine its activity. Scammers will have thousands of fake identities and bank information to try out, enough to waste plenty of their time and keep a few people from being scammed.

The scam consists of sending massive fraudulent messages to smartphones which tell users that they have to pay a contravention due to traffic violation and to click on the link. This link actually redirects to a fake website that emulate an official French website. Once a user has clicked on the link, he is taken to a page where he has to fill out forms with his personal identity and bank information. Once he get trapped, scammers attempt to make illegal transactions with his bank card.

Update : the website has been downed so if you run the script you will probably have 0% of succes rate

## Requirements
- Python 3

## Configuration
1. Download and extract the zip or clone the project
2. Open a terminal and install faker with command `pip install faker`
3. Install Playwright with command `pip install Playwright`
4. Navigate to `C:\User\AppData\Roaming\Python\PythonXX\site-packages\playwright\driver` (only for Windows)
5. Run the command `playwright.cmd install` (only for Windows)
6. Navigate into a terminal to the project directory
7. Run the command `python main.py` (requires python path in environement variables)