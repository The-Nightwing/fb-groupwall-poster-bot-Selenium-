# Facebook Group Poster

A Python script that uses Selenium to automate the process of logging into Facebook and posting a message to the groups mentioned in bot.py 

## Requirements

- Python 3.2 or later
- Selenium
- ChromeDriver

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/facebook-group-poster.git
```
2. Install the required packages
```bash
pip install -r requirements.txt
```

3. Download ChromeDriver from the official website and add it to your PATH.

4. Add your Facebook username and password to the .env file
```bash
userID=yourusername
password=yourpassword
```

## Usage
1. Run the Script.
```bash
python bot.py
```
2. Enter the message you want to post to the group. 
3. The script will automatically log in to Facebook and post the message to the group(s) specified in the code.

## Note
- Make sure that the ChromeDriver executable is in the PATH, e.g., place it in the same directory as the script.

- The script is set up to post to specific group(s) by default, you can edit the code to change the group(s) you want to post to.

This version of the README includes instructions for installing ChromeDriver, which is to download it from the official website and add it to the PATH, it also includes a link to the official website.
