import matplotlib.pyplot as plt


class StockCharts:
    def __init__(self, df):
        self.df = df

    def plot_close_price(self):
        plt.figure(figsize=(12, 6))

        plt.plot(
            self.df["Date"],
            self.df["Close"],
            label="Close Price"
        )

        plt.plot(
            self.df["Date"],
            self.df["MA_20"],
            label="20-Day MA"
        )

        plt.plot(
            self.df["Date"],
            self.df["MA_50"],
            label="50-Day MA"
        )

        buy_signals = self.df[self.df["Signal"] == 1]

        plt.scatter(
            buy_signals["Date"],
            buy_signals["Close"],
            marker="^",
            s=120,
            color="green",
            label="Buy"
        )

        sell_signals = self.df[self.df["Signal"] == -1]

        plt.scatter(
            sell_signals["Date"],
            sell_signals["Close"],
            marker="v",
            s=120,
            color="red",
            label="Sell"
        )

        plt.title("Stock Price with Moving Averages")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend(loc="best")
        plt.grid(True)

       


    def plot_equity_curve(self, strategy_equity, buy_hold_equity):

        plt.figure(figsize=(12, 6))

        plt.plot(
            self.df["Date"],
            strategy_equity,
            label="Strategy",
            linewidth=2
        )

        plt.plot(
            self.df["Date"],
            buy_hold_equity,
            label="Buy & Hold",
            linewidth=2
        )

        plt.title("Strategy vs Buy & Hold")
        plt.xlabel("Date")
        plt.ylabel("Portfolio Value")

        plt.grid(True)
        plt.legend()

    