# Fraudulent-Website-Disruptor

Fraudulent Website Disruptor is an algorithm that sends massive fake data to a phishing website to undermine its activity. Scammers will have thousands of fake identities and bank information to try out, enough to waste plenty of their time and keep a few people from being scammed.

The scam consists of sending massive fraudulent messages to smartphones which tell users that they have to pay a contravention due to traffic violation and to click on the link. This link actually redirects to a fake website that emulate an official French website. Once a user has clicked on the link, he is taken to a page where he has to fill out forms with his personal identity and bank information. Once he get trapped, scammers attempt to make illegal transactions with his bank card.

Update : the website has been downed so if you run the script you will probably have 0% of succes rate

## Installation
Python 3 is required to run this program.

```bash
# Clone the repository
git clone https://github.com/MathisJANKOVIC/Fraudulent-Website-Disruptor.git

# Install the required modules
pip install faker
pip install playwright

# On Windows navigate to the playwright driver dir (XX stands for your python version)
cd 'C:\User\AppData\Roaming\Python\PythonXX\site-packages\playwright\driver'

# Install playwright browsers (only on Windows)
playwright.cmd install

# Go to the project directory and run it with python
python main.py
```