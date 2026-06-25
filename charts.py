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

        plt.title("Stock Price with Moving Averages")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)

        plt.show()