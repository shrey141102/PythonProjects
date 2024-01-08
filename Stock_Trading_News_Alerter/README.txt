Stock Trading News Alerter

Description:
A Python-based tool designed to monitor stock prices of any company.
Initially demonstrated with Tesla (TSLA), now adaptable for any stock symbol.
Utilizes APIs from Alpha Vantage and NewsAPI for real-time financial and news data.
Sends SMS alerts for significant stock price changes via the Twilio API.

Features:
Monitors stock prices of user-specified companies.
Compares daily closing prices to identify significant percentage changes.
Fetches relevant news if stock price change exceeds a certain threshold.
Automated SMS updates for stock price changes and related news.

Pre-requisites:
Python installation.
Python modules: requests, twilio.
API keys from Alpha Vantage, NewsAPI, and Twilio.
Twilio account with a virtual number and a verified phone number.

Setup Instructions:
Install required Python modules.
Obtain API keys by signing up for Alpha Vantage, NewsAPI, and Twilio.
Clone the repository.
Input API keys and phone numbers in the script variables.

Usage:
Execute the script.
Input the desired stock symbol and company name when prompted.
Receive SMS alerts for selected stock's significant price changes and news.

Enhancements:
Adaptability to monitor any stock symbol as per user input.
Enhanced user interaction with prompts for stock symbol and company name.
