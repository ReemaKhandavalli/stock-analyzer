from matplotlib import pyplot as plt

from data import StockDataLoader
from metrics import StockMetrics
from charts import StockCharts
from strategies import MovingAverageStrategy
from backtester import Backtester


def main():

    ticker = input("Enter Stock Ticker: ")
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")

    loader = StockDataLoader(
        ticker=ticker,
        start_date=start_date,
        end_date=end_date
    )

    df = loader.load_data()

    # Performance Metrics
    metrics = StockMetrics(df)

    metrics.calculate_daily_returns()
    metrics.moving_average(20)
    metrics.moving_average(50)

    # Trading Strategy
    strategy = MovingAverageStrategy(df)
    
    strategy.generate_signals()
    strategy.generate_position()

    # Backtesting
    backtester = Backtester(df)

    backtester.strategy_returns()

    strategy_equity = backtester.strategy_equity_curve()
    buy_hold_equity = backtester.buy_and_hold_equity_curve()

    # Showing Results
    print("\n -----------PERFORMANCE METRICS---------- \n")

    print(f"Cumulative Return : {metrics.cumulative_return():.2%}")
    print(f"Annual Volatility : {metrics.volatility():.2%}")
    print(f"Sharpe Ratio      : {metrics.sharpe_ratio():.2f}")
    print(f"Maximum Drawdown  : {metrics.max_drawdown():.2%}")

    print()

    print(f"20-Day Moving Average : {df['MA_20'].iloc[-1]:.2f}")
    print(f"50-Day Moving Average : {df['MA_50'].iloc[-1]:.2f}")

    print()

    print("----------- BACKTEST RESULTS ----------- \n")

    print(f"Strategy Return   : {strategy_equity.iloc[-1] - 1:.2%}")
    print(f"Buy & Hold Return : {buy_hold_equity.iloc[-1] - 1:.2%}")

    # Charts
    charts = StockCharts(df)
    charts.plot_close_price()

    charts.plot_equity_curve(
    strategy_equity,
    buy_hold_equity)

    plt.show()

if __name__ == "__main__":
    main()