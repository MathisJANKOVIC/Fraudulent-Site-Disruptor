# Fraudulent-Website-Disruptor

Fraudulent Website Disruptor is a program that sends massive fake data to a phishing website to undermine its activity. Scammers will have thousands of fake identities and bank information to test, enough to waste plenty of their time and prevent a few people from being scammed.

Since the fraudulent website has been taken down, running the program will likely result in a 0% success rate.

## Installation
Python 3.6 or later is required to run this program.

```bash
# Clone the repository
git clone https://github.com/MathisJANKOVIC/Fraudulent-Website-Disruptor.git

# Enter the project directory
cd ./Fraudulent-Website-Disruptor

# Install the required modules
pip install -r requirements.txt

# On Windows
---------------------------------------------------------------------------------------
# Navigate to the Playwright driver directory (replace USER and VERSION accordingly)
cd 'C:\Users\USER\AppData\Roaming\Python\PythonVERSION\site-packages\playwright\driver'

# Install Playwright browser
./playwright.cmd install
---------------------------------------------------------------------------------------

# Go back to project directory and run it with python
python ./src/main.py
```