Project Title: Stock Trading News Alerter

Description:
- A Python-based tool to monitor a firm's stock prices.( Tesla taken here for example ) 
- Sends daily updates on stock price changes via SMS.
- Utilizes APIs from Alpha Vantage and NewsAPI for real-time financial and news data.

Structure:
- Retrieves stock data using Alpha Vantage API.
- Compares closing prices to calculate percentage changes.
- Fetches relevant news articles if the stock price change exceeds a certain threshold.
- Uses Twilio API to send updates as SMS messages.

Pre-requisites:
- Python Installation.
- Modules: `requests`, `twilio`.
- API keys for Alpha Vantage, NewsAPI, and Twilio.
- Twilio account setup with a virtual number and a verified phone number.

Setup Instructions:
1. Install required Python modules: `pip install requests twilio`.
2. Sign up for Alpha Vantage, NewsAPI, and Twilio to get respective API keys.
3. Enter the API keys and phone numbers in the provided variables.

Usage:
- Run the script to receive daily TSLA stock updates.
- Configure for other stocks by changing STOCK_NAME and COMPANY_NAME variables.
