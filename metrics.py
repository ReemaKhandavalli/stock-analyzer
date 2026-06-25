import numpy as np


class StockMetrics:

    def __init__(self, df):
        self.df = df

    def calculate_daily_returns(self):

        self.df["Daily Return"] = self.df["Close"].pct_change()

    def get_returns(self):

        return self.df["Daily Return"].dropna()

    def cumulative_return(self):

        returns = self.get_returns()

        cumulative = (1 + returns).cumprod()

        return cumulative.iloc[-1] - 1

    def volatility(self):

        returns = self.get_returns()

        return returns.std() * np.sqrt(252)

    def sharpe_ratio(self):

        returns = self.get_returns()

        return (returns.mean() / returns.std()) * np.sqrt(252)

    def max_drawdown(self):

        cumulative_returns = (1 + self.get_returns()).cumprod()

        running_max = cumulative_returns.cummax()

        drawdown = (cumulative_returns - running_max) / running_max

        return drawdown.min()
    
    def moving_average(self, window):
        self.df[f"MA_{window}"] = (
            self.df["Close"]
            .rolling(window=window)
            .mean()
        )
        