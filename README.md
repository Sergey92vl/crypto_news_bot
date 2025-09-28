# crypto_news_bot
crypto_news_bot - This is your personal guide to the world of cryptocurrency and crypto projects.You no longer need to collect information on the Internet, just enter the name of the project you are interested in, and it will collect all the available information in one place.

Installing dependencies and running

1. Make sure you have Python 3.6+. installed. Download it from python.org if it's not already installed.
2. Install the required requests library. Open the command line (CMD) in the project folder and run:
pip install requests
3. In the config.py file, replace "your_actual_api_key_here" with your actual NewsAPI key. (Go to https://newsapi.org and register and get your free API key. We will need it later)


Launching:

Method 1 (Double-click): Just double-click on the bot.bat file. The bot will ask you a question.

Method 2 (From the command line): Open CMD in the project folder and run:
bash
bot.bat "Solana"
or

bash
bot.bat "Latest Ethereum news"
