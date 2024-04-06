# Fraudulent-Website-Disruptor

Fraudulent Website Disruptor is an automated program that sends massive fake data to a phishing website to undermine its activity. Scammers will have thousands of fake identities and bank information to test, enough to waste plenty of their time and prevent a few people from being scammed.

Since the fraudulent website has been taken down, running the program will likely result in a 0% success rate.

## Installation
Python 3.6 or later is required to run this program.

```bash
# Clone the repository
git clone https://github.com/MathisJANKOVIC/Fraudulent-Website-Disruptor

# Enter the project directory
cd ./Fraudulent-Website-Disruptor

# Install the required packages
pip install -r requirements.txt

# Install the required playwright browser (only on Windows)
python -m playwright install chromium

# Run the program
python ./src/main.py
```

## Built With
<a href="https://www.python.org"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="50" height="50"/></a>
<a href="https://playwright.dev"><img src="https://playwright.dev/img/playwright-logo.svg" alt="playwright" width="50" height="50"/></a>
