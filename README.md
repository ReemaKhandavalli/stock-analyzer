# Stock Analyzer

A simple Python project for analyzing historical stock price data and backtesting a simple moving average crossover strategy.

This project was built to strengthen my understanding of quantitative finance concepts

This project fetches historical market data, calculates common financial performance metrics, generates trading signals based on moving average crossovers, and compares the strategy against a buy-and-hold benchmark.

## Features

- Fetch historical stock price data using `yfinance`
- Calculate daily returns
- Calculate cumulative returns
- Calculate annualized volatility
- Calculate the Sharpe Ratio
- Calculate maximum drawdown
- Compute 20-day and 50-day moving averages
- Generate BUY and SELL signals using a moving average crossover strategy
- Backtest the strategy against a buy-and-hold benchmark
Visualize stock prices, moving averages, and trading signals using Matplotlib

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance

## How It Works

1. Enter a stock ticker and a date range.
2. Historical stock price data is fetched using yfinance.
3. Daily returns and financial performance metrics are calculated.
4. 20-day and 50-day moving averages are generated.
5. BUY and SELL signals are created when the moving averages cross.
6. Trading positions are generated from those signals.
7. The strategy is backtested and compared against a buy-and-hold approach.
8. Results are displayed in the terminal along with charts of the stock price, moving averages, and trading signals.
