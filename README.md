# Stock Analyzer

A simple Python project for analyzing historical stock price data and evaluating a simple moving average crossover strategy.

This project was built to strengthen my understanding of quantitative finance concepts

The project fetches historical market data using `yfinance`, calculates common performance metrics, generates trading positions based on moving averages, and compares the strategy against a Buy & Hold approach.

## Features

- Fetch historical stock price data using `yfinance`
- Calculate daily returns
- Calculate cumulative returns
- Calculate annualized volatility
- Calculate the Sharpe Ratio
- Calculate maximum drawdown
- Compute 20-day and 50-day moving averages
- Implement a moving average crossover strategy
- Compare strategy performance with a Buy & Hold strategy
- Visualize stock prices and moving averages using Matplotlib

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance

## How It Works

1. Enter a stock ticker and a date range.
2. Historical stock data is fetched using `yfinance`.
3. Performance metrics are calculated.
4. 20-day and 50-day moving averages are generated.
5. A moving average crossover strategy determines whether the strategy should be invested or remain in cash.
6. Strategy performance is compared with a Buy & Hold approach.
7. The results and price chart are displayed.
